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

S3
==================

ECS
==================

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