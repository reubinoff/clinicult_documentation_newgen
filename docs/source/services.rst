#############
Services
#############

In order to support high performance and simplicity Clinicult 2.0 will be developed as micro-services architecture. 
each service will has his own purpose and his own data.

******************
Services
******************

User Service
==================
This service will store all the information on the User that use the system.the information will include also the user permissions. 
in addiiton to the user permissions (Role / Group), this services will store all the personal information. for example phone or mail.

The service will not store his login credentials. 
all the tokens or credentials will be stored in the :ref:`Authentication Services`



Authentication Service
==================
Authentication Methid will be implemented in this services. This service can be 3rd party service that can be integrated with out platform. 
for example: `Auth0 <https://auth0.com/>`_


Clinic WEB Service
==================
This service will hold the client static files with some web servies that serve those files. for example Nodejs with `Express <https://expressjs.com/>`_.


another option is to serve the Client site with `AWS Amplify <https://aws.amazon.com/amplify/>`_


Admin WEB Service
==================
This Services will serve the admin web client. same as the clinic web service.


Admin Managment Services
====================================
This server will host all the API and queries that the admin clinet needs. the main idea is that this server will not hold data at all, and will just proxy the requests to other services.


Visits Service
==================
history services


Patient Service
==================
patient + current visit


******************
Architecture
******************


Communication
==================

.. _data:
data
==================