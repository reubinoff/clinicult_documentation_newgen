#############
Security
#############

Clinicut patform has medical sensetive data, hence we need to nesure that all our data is safe and protected.
the protection has couple of security layers.


******************
Environment Isolation
******************
Each clinic in the platform will run on seperate :ref:`ECS` cluster. Each cluster will has seperate subnet in his VPC. there will be know open ports between clinic's subnets.

Each Clinic will have different database per service. All the databases can be on the same RDS server. the database name will be generated automaticlly during :ref:`Clinic Onboarding` time.
the access from the cluster to the database, will be from Security-group that will define access from the Cluster to the spsific database. each service will have his own security-group to access his own database.
hence, Only the relevant service can access the database.

We will have 3 kinds of environemnts:

#. Production
#. Staging
#. Development

Clinic with the same name can be exists on each environment, but those clusters should be isolated.

the clinics will share only those components:

#. Load balancer
#. Amplify Client

Once we will keep those ruls, the data will be isolated and secured. 



******************
VPN
******************
To open access to the internal ip within the cluster, we will need to create VPN access **per deployment environment**.

Each Environemnt will have different VPN server. we will use `OpenVPN <https://openvpn.net/>`_ to implement the server side.

the Only ports that will be open is the web server, and it will be open to the :ref:`API gateway` **Only**, and the API gateway will be open to the Load Balancer **Only**.
The Load balancer will be open to the internet for incomming connection from the *Amplify Client*.



******************
SSL
******************
All the Web services will serve in Https/TLS **Only**. the Certificates will be generated from AWS `Certificate manager <https://aws.amazon.com/certificate-manager/>`_.

The client Certificate will be generated from `AWS Amplify <https://aws.amazon.com/amplify/>`_.



******************
AWS
******************
