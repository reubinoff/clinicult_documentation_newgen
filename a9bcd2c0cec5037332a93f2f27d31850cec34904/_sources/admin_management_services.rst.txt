#############
Admin Management Services 
#############


******************
Clinic Management
******************

Onboarding
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



Clinic Actions
==================
In the Admin Management services will be a dashboard to manage all the running clinics on AWS platform.
the view will contains a table with all the clinics, and the status of the clinic. there will be three statues:

#. **Active** - all services are up and running and the hostname route requests to the hosts.
#. **Disable** - Services are Down/removed and the data are still exists. the dome will not route requests to hosts.
#. **Deleted** - All active resources will be deleted but the data will be archived. the domain will be released

in the dashboard, will be an option to update the clinic state.

Furthermore, there will be an option to update the clinic settings. More information about the settings you can find in :ref:`settings` chapter.

Another Option will be to update the users for each clinic. more about users you can find in :ref:`Users Management` section


Users Management
==================
Each Clinic has Users lists that have permission to access the clinic. Each User has his own role. the roles in the clinic are:

#. ``Admin`` - manage the clinic
#. ``Nurse`` - handle the states for Nurse
#. ``Doctor`` - handle the state for doctor
#. ``Office`` - manage the other states

the admin will have an option to Create/Update/Delete users in the clinic. update Role of user or Deleting a user will be take place only in those conditions:

#. User has logged out and logged back in
#. expiration time perioed has expired

Those conditions are due to token management mechanisim. 


.. note::

    We can enforce attention list per service on modified users. but its not a must for phase 1



Clinic Labeling
==================
Each Clinic can customize the view of the clinic's UI. for example `clinic Logo`. 
there will be a view in the clinic to upload or remove files that add client modification.

If not file has added, there will be some defaults to use them in the clients.



Clinic Modules
==================
Each clinic will have some Modules that may be use. for example:

#. Calendar
#. Family care
#. etc.

Each module will have an option to enable or disable from the clinic view.


******************
Settings
******************
Global settings
==================
Here will be All the configuration for the platform. there will be 3 kinds of configurations:

#. Global Admin configuration - for example admin mail for SMS notifications
#. Default Clinic configuration - default values for each config field
#. Clinic configuration - config per clinic for example clinic Language

The Clinic will use all the default configuration after the on-boarding phase. the platform Admin will have the option to updat this default values in the clinic view.

.. note::

    The clinic configuration will be in the Clinic view and the other configuration will have dofferent global view on the admin management service client.



Data Lists
==================
s

.. note::

    There will be an option to import Data lists from CSV file.
 


Languages
==================
sd


Notifications
==================
SNS

******************
Reports
******************

******************
Windows Servers
******************
