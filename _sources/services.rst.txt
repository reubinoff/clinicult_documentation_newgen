Services
=====

In order to support high performance and simplicity Clinicult 2.0 will be developed as micro-services architecture. 
each service will has his own purpose and his own data.

Services
______

User Service
########
This service will store all the information on the User that use the system.the information will include also the user permissions. 
in addiiton to the user permissions (Role / Group), this services will store all the personal information. for example phone or mail.

The service will not store his login credentials. all the tokens or credentials will be stored in the :ref:`Authentication Service`

see :ref:`Services`.

Authentication Service
########
Authentication Methid will be implemented in this services. This service can be 3rd party service that can be integrated with out platform. 
for example: `Auth0 <https://auth0.com/>`_

Clinic WEB Service
########
readthedocs

Admin WEB Service
########
readthedocs

Visits Service
########
history services

Patient Service
########
patient + current visit



Architecture
_____

Communication
########

data
########