#############
Infrastructure 
#############

Clinicult 2.0 Services will be deployed on AWS platform. The deployment will be on `Kubernetes <https://kubernetes.io/>`_.
in addition to the services Clinicult 2.0 will have some storage for files and historic data.

All platform Code will be managed by Git on `Github <https://github.com>`_.

Fully CI/CD will be part of the development cycle to ensure the platform Quality. the CI/CD engine will be `Github-Actions <https://github.com/features/actions>`_.



******************
Docker
******************
To Deploy our services on the cloud, we will use `Docker <https://www.docker.com/>`_ containers.
Each service in our platform will be build on seperate Docker image and will deployed and different Pod/Service on the Cluster.

As part of the :ref:`Continous Integration` the service will be build to and image and will be pushed to the Container registry for deployment.

The base image to build the service is depends on the service infrastructure. for example, if the service will be developed in python fastapi, the relevant base image is in `This Repository <https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi>`_.
The deployment of the image on the cluster will be part of the AWS infrastructure.

Each Image will have option to run as  debug or as production. the option will be set threw Environment variable.
in addition the image will have option to read alot of other values from Environment variable as well.

The Docker container will expose some port for listening to incoming requests.

Example of Dockerfile in fastapi infrastructure:

.. code-block:: python

    FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

    # Install Poetry
    RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | 
        POETRY_HOME=/opt/poetry python && \
        cd /usr/local/bin && \
        ln -s /opt/poetry/bin/poetry && \
        poetry config virtualenvs.create false

    # Copy using poetry.lock* in case it doesn't exist yet
    COPY ./app/pyproject.toml ./app/poetry.lock* /app/

    RUN poetry install --no-root --no-dev

    COPY ./app /app
 

For more information about the deployment you can find on :ref:`ECS` chapter


******************
AWS
******************


Terraform
==================
Aws services will be managed by `Terraform project <https://www.terraform.io/>`_.

In our Account we will have 3 seperated environments:

#. development - will be used during the development stage
#. staging - for latest test before upgrading the production, or to test Beta versions
#. production - production Environment

All the Environments will be **identical**!. 

The deployment will be with terraform scripts. that each change will be only can modified from terraform. the changes will be applied manually only. CI for terraform scripts will just check validation of the scripts.
Terraform will save his environment state on S3. 

In addition to the product environments, Terraform will also apllied usful lambda functions to help during the deployment stage. for example, Lambda function that update ECS clusters with new version uploaded.

Another imprtant example for lambda function is to deploy new cluster (aka new Clinic) on ECS.


S3
==================
Each service in the cluster will have the option to get access to S3.
Clinicult 2.0 will have S3 storage per cluster (aka Clinic) the path in the S3 will idetify the relevant service. 
For example, Service visits, will write his data to 

.. code-block:: console

    s3://<clinic_name>/visits



ECS
==================
Each Clinic in Clinicult 2.0 will A seperate cluster in ECS fargate. each service will be an ECS service in the cluster. 
for each Clinic will be a dedicated subnet in the environment VPC. this way, we will have 3 different VPCs, for development, staging and production. and each clinic will have seperate subnet in the VPC.

Amazon Api Gateway may be integrated with ECS. more information may be found in `this guide <https://aws.amazon.com/blogs/compute/using-amazon-api-gateway-with-microservices-deployed-on-amazon-ecs/>`_.

All the clusters (aka clinics) will be accessed from the Api gateway **only**, and will be secured with TLS certivficate.
In addition, the clusters will also have subscription channel to the :ref:`SQS`. this way the :ref:`Admin Management Services` can push config changes or other updates to the clinic.


ECR
==================
All Docker images will be managed in the Elastic container registry. Each service will have seperate repository and versioning.

The mechanisim to push images will be only from the CI phase. 

We will have 10 version retention in the registry.
In addition, every deploy environment (stage, dev, prod) will have different tag:

.. code-block:: console

    clinicult/<service_name>:<env_name>-X.Y.Z

for example:

.. code-block:: console

    clinicult/user_service:stage-1.0.32

In addition, Will be also *'latest'* tag for the latest production environment.




SNS
==================
SNS is a distributed publish-subscribe system. Messages are pushed to subscribers as and when they are sent by publishers to SNS.
Amazon SNS is a fast, flexible, fully managed push notification service that lets you send individual messages or to bulk messages to large numbers of recipients.

The :ref:`Admin Management Services` will have option to notify the clinics about configuration change or other notification with the SNS.
Each service in the clinic will option to subscribe on :ref:`Admin Management Services` notifications.
Each message will have different area of intrest (aka Topic). each service will subscribe to the relevant Topic.
For example:

.. code-block:: json

    {
    "Type" : "SubscriptionConfirmation",
    "MessageId" : "165545c9-2a5c-472c-8df2-7ff2be2b3b1b",
    "Token" : "2336412f37...",
    "TopicArn" : "arn:aws:sns:us-west-2:123456789012:MyTopic",
    "Message" : "You have chosen to subscribe to the topic arn:aws:sns:us-west-2:123456789012:MyTopic.\nTo confirm the subscription, visit the SubscribeURL included in this message.",
    "SubscribeURL" : "https://sns.us-west-2.amazonaws.com/?Action=ConfirmSubscription&TopicArn=arn:aws:sns:us-west-2:123456789012:MyTopic&Token=2336412f37...",
    "Timestamp" : "2012-04-26T20:45:04.751Z",
    "SignatureVersion" : "1",
    "Signature" : "EXAMPLEpH+DcEwjAPg8O9mY8dReBSwksfg2S7WKQcikcNKWLQjwu6A4VbeS0QHVCkhRS7fUQvi2egU3N858fiTDN6bkkOxYDVrY0Ad8L10Hs3zH81mtnPk5uvvolIC1CXGu43obcgFxeL3khZl8IKvO61GWB6jI9b5+gLPoBc1Q=",
    "SigningCertURL" : "https://sns.us-west-2.amazonaws.com/SimpleNotificationService-f3ecfb7224c7233fe7bb5f59f96de52f.pem"
    }

To subscribe to this topic, the Service will create an SQS and will subscribe to the topic with sqs endpoint.
for example:

.. code-block:: python

    try:
        subscription = topic.subscribe(
            Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)
        logger.info("Subscribed %s %s to topic %s.", protocol, endpoint, topic.arn)
    except ClientError:
        logger.exception(
            "Couldn't subscribe %s %s to topic %s.", protocol, endpoint, topic.arn)
        raise

More examples can be found in `Github <https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/python/example_code/sns/sns_basics.py>`_



Amplify
==================
For Clinicult Web Clients we will use `AWS Amplify <https://aws.amazon.com/amplify/>`_ infrastructure for serving and :ref:`Continous Integration`.

AWS Amplify is a set of purpose-built tools and services that makes it quick and easy for front-end web and mobile developers build full-stack applications on AWS, with the flexibility to leverage the breadth of AWS services to further customize applications. 




Schema
==================
.. image:: imgs/infra.png
    :width: 400
    :alt: Services Outlet



******************
Source Control
******************
All Code services will be managed by Source control. our code will be on `Github <https://github.com>`_.
the entire code will be in single repository for easy managment and development cycle.



******************
Continous Integration
******************
The entire Continous Integration will be implemented in `Github-Actions <https://github.com/features/actions>`_.

For each service the flow will be:

#. Run tests
#. Build :ref:`Docker` image
#. Upload image to :ref:`ECR`
#. Update :ref:`ECS` service with the new image

The flow can be change according to the code.

CI session will run only on the relevant code that changed. for example, if Service_a has changed, there is no need to run CI on service_b code.

The CI will run for each push to the relevant environemnts branches:

#. **main** - production
#. **develop** - staging
#. **development** - testing


the feature branches will exit from the development branch.





