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
Authentication
******************
Each Clinic will be protected with different authentication mechanisim. means that each clinic will have different users and different admin user.
All authentication flow will be managed by :ref:`user service`. the authentication identification will be implemented with `Auth0 <https://auth0.com/>`_. 
The :ref:`user service` will manage the Users in the clinic, and the :ref:`Authentication Service` will manage the access flow. this way all clinic tokens will be safe.

.. image:: imgs/auth.png
    :alt: Authentication


More information about Oauth2 flow, you can find in `This documentation <https://auth0.com/docs/authorization/flows/authorization-code-flow-with-proof-key-for-code-exchange-pkce>`_



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
Domains
******************
The Domain will be managed In Route53.
the base route will be for example ``clinicult2.com``

Each Clinic will have seperate domains with ssl Certificates. the domain production templates:

#. ``service_name.clinic_name.clinicult2.com``
#. ``app.clinic_name.clinicult2.com``

for the other deployment environemnts the domain templates:

#. ``service_name.clinic_name.<environment>.clinicult2.com``
#. ``app.clinic_name.<environment>.clinicult2.com``

for example: ``app.ct-arad.staging.clinicult2.com``


The load-balancer will route the requests to ``X.clinic_name.clinicult2.com`` to the relevant cluster


in addition the admin will have those domains:

#. ``app.admin.clinicult2.com`` - client
#. ``src.admin.clinicult2.com`` - server



******************
AWS
******************

IAM
==================
You use an access key (an access key ID and secret access key) to make programmatic requests to AWS. However, do not use your AWS account root user access key. The access key for your AWS account root user gives full access to all your resources for all AWS services, including your billing information. You cannot reduce the permissions associated with your AWS account root user access key.

Therefore, protect your root user access key like you would your credit card numbers or any other sensitive secret. Here are some ways to do that:

We strongly recommend that you do not use the root user for your everyday tasks, even the administrative ones. Instead, use your root user credentials only to `create your IAM admin <https://docs.aws.amazon.com/IAM/latest/UserGuide/getting-started_create-admin-group.html>`_ user. Then securely lock away the root user credentials and use them to perform only a few account and service management tasks. For everyday tasks, do not use your IAM admin user. Instead, `use roles to delegate permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#delegate-using-roles>`_.

If you do have an access key for your AWS account root user, delete it. If you must keep it, rotate (change) the access key regularly. To delete or rotate your root user access keys, go to the My Security Credentials page in the AWS Management Console and sign in with your account's email address and password. You can manage your access keys in the Access keys section. For more information about rotating access keys, see Rotating access keys.

Never share your AWS account root user password or access keys with anyone. The remaining sections of this document discuss various ways to avoid having to share your AWS account root user credentials with other users. They also explain how to avoid having to embed them in an application.

Use a strong password to help protect account-level access to the AWS Management Console.

Enable AWS multi-factor authentication (MFA) on your AWS account root user account. For more information, see Using multi-factor authentication (MFA) in `AWS <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html>`_.


Access keys
________________
Access keys provide programmatic access to AWS. Do not embed access keys within unencrypted code or share these security credentials between users in your AWS account. For applications that need access to AWS, configure the program to retrieve temporary security credentials using an IAM role. To allow your users individual programmatic access, create an IAM user with personal access keys.


Monitoring
________________
You can use logging features in AWS to determine the actions users have taken in your account and the resources that were used. The log files show the time and date of actions, the source IP for an action, which actions failed due to inadequate permissions, and more.

Logging features are available in the following AWS services:

`Amazon CloudFront <https://aws.amazon.com/cloudfront/>`_ – Logs user requests that CloudFront receives. For more information, see `Access Logs <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html>`_ in the Amazon CloudFront Developer Guide.

`AWS CloudTrail <https://aws.amazon.com/cloudtrail/>`_ – Logs AWS API calls and related events made by or on behalf of an AWS account. For more information, see the AWS CloudTrail User Guide.

`Amazon CloudWatch <https://aws.amazon.com/cloudwatch/>`_ – Monitors your AWS Cloud resources and the applications you run on AWS. You can set alarms in CloudWatch based on metrics that you define. For more information, see the Amazon `CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/>`_.

`AWS Config <https://aws.amazon.com/config/>`_ – Provides detailed historical information about the configuration of your AWS resources, including your IAM users, user groups, roles, and policies. For example, you can use AWS Config to determine the permissions that belonged to a user or user group at a specific time. For more information, see the `AWS Config Developer Guide <https://docs.aws.amazon.com/config/latest/developerguide/>`_.

`Amazon Simple Storage Service (Amazon S3) <https://aws.amazon.com/s3/>`_ – Logs access requests to your Amazon S3 buckets. For more information, see Server Access Logging in the Amazon Simple Storage Service User Guide.




Resources
==================
All Aws Resource will be created from Terraform. this means that Terraform will have an Account with AWS Access keys the grant him permissions to create resources in AWS account.

In addition, we will have option to create new environment in :ref:`Clinic Onboarding` session. this flow create new resources in AWS account. hence, the host that run this routine, will have permission to create those resource.
the grantted permissions will be from seperate account and will have only the required permissions **only**.

