#############
Services
#############

In order to support high performance and simplicity Clinicult 2.0 will be developed as micro-services architecture. 
each service will has his own purpose and his own data.

******************
Outlet
******************

User Service
==================
This service will store all the information on the User that use the system.the information will include also the user permissions. 
in addiiton to the user permissions (Role / Group), this services will store all the personal information. for example phone or mail.

The service will not store his login credentials. 
all the tokens or credentials will be stored in the :ref:`Authentication Service`


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
This Services will serve the admin web client. same as the :ref:`Clinic WEB Service`.


Admin Managment Services
====================================
This server will host all the API and queries that the admin clinet needs. the main idea is that this server will not hold data at all, and will just proxy the requests to other services.


Visits Service
==================
This service will hold the historic Visits. The issue here is that the data of this service will increament over the time, so to keep our performance fast and robust, we will keep here only the historic and not the **current** visit.
this services will also give an enhanced API to query on the historic visits.

there is an option to accelerate the queries is to use some Cache to hole the most visited enteries.
example for implementation is `LRU cache <https://www.geeksforgeeks.org/lru-cache-implementation/>`_  on Redis, to keep the visits per Patient.
in this case when Patient is in servies now, the historic visits will be served from the Cache instead of the DB.


Patient Service
==================
This Service will serve the Patient information. personal and mediacal.
for example, if we will need to create Mediacal file, Most of the data on the patient will be taken from this service.

In Addition, this service will hold the current visit of the patient. once the Patient finish his visit, the current visit will be reset and the current visist will be moved to the :ref:`Visits Service`.


API gateway
==================
API service that route all requests in the platform to his relevant service.
the main reason to hold this service is that the only way to get into out platform is only threw this service.
more information about it you can find in :doc:`security` chapter

******************
Architecture
******************


Communication
==================



data
==================