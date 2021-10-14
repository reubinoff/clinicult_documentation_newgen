#############
Services
#############

In order to support high performance and simplicity Clinicult 2.0 will be developed as micro-services architecture. 
each service will have his own purpose and his own data.

******************
Outlet
******************

User Service
==================
This service will store all the information on the User that use the system. the information will include also the user permissions. 
in addition to the user permissions (Role / Group), these services will store all the personal information. for example, phone or mail.

The service will not store his login credentials. 
all the tokens or credentials will be stored in the :ref:`Authentication Service`

In Each Clinic there will be 4 Role to access the clinic:

#. ``Admin`` - manage the clinic
#. ``Nurse`` - handle the states for Nurse
#. ``Doctor`` - handle the state for doctor
#. ``Office`` - manage the other states


Authentication Service
==================
Authentication Methid will be implemented in these services. This service can be 3rd party service that can be integrated with out platform. 
for example: `Auth0 <https://auth0.com/>`_

.. note::
    The only entities that can talk with this service is the :ref:`User Service` to update the user Role/Group, and the Client itslef for authentication


Clinic WEB Service
==================
This service will hold the client static files with some web servies that serve those files. for example, Nodejs with `Express <https://expressjs.com/>`_.


another option is to serve the Client site with `AWS Amplify <https://aws.amazon.com/amplify/>`_


Admin WEB Service
==================
This Services will serve the admin web client. same as the :ref:`Clinic WEB Service`.


Admin Management Services
====================================
This server will host all the API and queries that the admin client needs.
the main idea is that this server will hold only the relevant data for admin **only**, and will just proxy the requests to other services for the additional data.

More information on :doc:`admin_management_services`


Visits Service
==================
This service will hold the historic Visits. The issue here is that the data of this service will increment over the time, so to keep our performance fast and robust, we will keep here only the historic and not the **current** visit.
this services will also give an enhanced API to query on the historic visits.

there is an option to accelerate the queries is to use some Cache to hole the most visited entries.
example for implementation is `LRU cache <https://www.geeksforgeeks.org/lru-cache-implementation/>`_  on Redis, to keep the visits per Patient.
in this case when Patient is in service now, the historic visits will be served from the Cache instead of the Database.


Patient Service
==================
This Service will serve the Patient information. personal and medical.
for example, if we will need to create medical file, Most of the data on the patient will be taken from this service.

In Addition, this service will hold the current visit of the patient. once the Patient finish his visit, the current visit will be reset and the current visist will be moved to the :ref:`Visits Service`.


Clinic Management Service
==================
Templates Management



API gateway
==================
API service that route all requests in the platform to his relevant service.
the main reason to hold this service is that the only way to get into out platform is only through this service.
more information about it you can find in :doc:`security` chapter.

One of the Options to implement this service is with `Amazon Api Gateway <https://aws.amazon.com/api-gateway/>`_.

FHIR API
-----------------
All the API calls (that contain medical data) meet FHIR standard.
The API is written in `FHIR V4 standard <https://www.hl7.org/fhir/http.html>`_.



******************
Architecture
******************


Communication
==================
In Clinicut 2.0 we will have couple of communication channels:

#. User client to the :ref:`API gateway`
#. Admin client to the :ref:`Admin Management Services`
#. Between the platform services
#. Pub-Sub between :ref:`Admin Management Services` to the clinic clusters

.. note::
    API client is not relevant at this stage


By Design all the requests between the services and/or between the client to the services, will be threw REST API.
All the calls between the Clients to the platform will be threw the :ref:`API gateway` with **https** (`TLS <https://datatracker.ietf.org/doc/html/rfc5246>`_).
the calls between the platform servies will be in **http** to the local dns name that the service will get from the process manager (`k8s <https://kubernetes.io/>`_).

more information about communication protocol in :doc:`security` chapter.



Database
==================
Each Service in Clinicult 2.0 will have his own database. we will use `MySql <https://www.mysql.com/>`_ in version `8.X <https://dev.mysql.com/doc/relnotes/mysql/8.0/en/news-8-0-26.html>`_ to store the service data.
All the databases can host on the same server, but will have separate schemas. for multi-Geo services, will be serve as multi-Geo redundancy.
the meaning of that each service has his own data, is if we need to have API that will return an Object that have data from multiple services, the response servies (that get the API request) will aggregate te the full data from all of the services, and will return full request to the client.


Cache
==================
Caching will be ready to serve the services. option for caches:

#. `Redis <https://redis.io/>`_
#. `AWS Elastic Cache <https://www.google.com/aclk?sa=L&ai=DChcSEwibgdTWyb3zAhVS53cKHRlUDlYYABAAGgJlZg&ae=2&sig=AOD64_3eWIyBu6dtM602se28yrqiAz9lgg&q&adurl&ved=2ahUKEwj_kcvWyb3zAhVLDewKHSKAB-kQ0Qx6BAgCEAE>`_

In both case the idea is to store only temporary data and not persistant. means that each data that stored in cache, can be clear and this will not impcat the system with data loss.
Example, the last patients' historic visits in the clinic. 

.. note::
    cache mechanisim is not needed for the first stage



******************
Schema
******************
.. image:: imgs/services.png
    :width: 400
    :alt: Services Outlet


******************
RBAC
******************
Clinicult platform will implement Role-based-access-control. means that each user that communicate with the servicess will have to identify with the system with token that he get after Login phase.
this Token will include his permissions in the system. 

Each service that read the Token will be able to read the permissions that the user have. 

Each service will map the API in the service to the relevant permissions. despite the ``Login`` and ``Logout``, **all the other Apis requires permissions**.

Role can be implemented as:

.. code-block:: json

    [
        'clinicult:visits:read',
        'clinicult:patient:write'
        'clinicult:user:*'
    ]

in this Example, this permissions says that:

#. User have *read* access to the visits data
#. User have *write* + *read* access to the patient data
#. User have full access (includes delete) to the user data

the Toekn is send in Bearer Http Header. 

the service parse this Token and check the permissions. example for parsing and check experiration data:

.. code-block:: python

    from jwt.exceptions import ExpiredSignatureError

    try:
        payload = jwt.decode(
            token,
            key='my_super_secret',
            algorithms=[header_data['alg'], ]
        )
    except ExpiredSignatureError as error:
        print(f'Unable to decode the token, error: {error}')




.. note::
    Token expiration will be 2 weeks

More information on the Token and security you can find in :ref:`Authentication` chapter


******************
Reports
******************
TBD