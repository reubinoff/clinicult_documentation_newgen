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


ECR
==================



******************
Source Control
******************



******************
Continous Integration
******************



******************
Continous Deployment
******************