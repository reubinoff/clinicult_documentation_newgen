#############
Admin Management Services 
#############


******************
Clinic Management
******************

Clinic Onboarding
==================
Clinics On-boarding will is interactive procedure in the system. this procedure may be invoke only by platform admin (aka root).
the procedure will create new clinic in Clinicult platform. 
The on-boarding procedure can create a clinic on target choosen deployment environment. 

in the Admin Web UI, will be an option to create new Clinic. once clicked, the admin will specify the Clinic name and the target deployment environment.

example: Clinic ``CT-Arad`` on environment ``Production``.

I addition to this information the admin will specify the clinic's admin phone and mail. and the end of the on-boarding procedure, the admin will get sms and mail with the environment information. the credentials details, will be temporary and **will requires update after his first login**.


.. note::

    Its important to enforce the password update in his first Login.


The Flow will run the following steps:

#. Create new EVS cluster
#. Create new databases for the clinic
#. open security-group and ports
#. mount Load-balancer to the relevant services
#. Create new User (admin) for the clinic in the User-service
#. Create sub-domain for the clinic. (more information in :ref:`Domains` section)
#. push configuration from admin
#. open Amplify for serving to the new environment with the new sub-domain

this flow will run with terraform script on `Lambda <https://aws.amazon.com/lambda/>`_ context with specific permissions for on-boarding role.

After creation, the platform admin will be able to see the clinic in the Admin page, and to manage this environment




Users Management
==================



Settings
==================


******************
Windows Servers
******************