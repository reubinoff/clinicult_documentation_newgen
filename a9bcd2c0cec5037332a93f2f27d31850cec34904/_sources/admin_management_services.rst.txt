#############
Admin Management Services 
#############


******************
Clinic Onboarding
******************
Clinics On-boarding will is interactive procedure in the system. this procedure may be invoke only by platform admin (aka root).
the procedure will create new clinic in Clinicult platform. 
The on-boarding procedure can create a clinic on target choosen deployment environment. 

in the Admin Web UI, will be an option to create new Clinic. once clicked, the admin will specify the Clinic name and the target deployment environment.
for example Clinic ``CT-Arad`` on environment ``Production``.

The Flow will run the following steps:

#. Create new EVS cluster
#. Create new databases for the clinic
#. open security-group and ports
#. mount Load-balancer to the relevant services
#. Create new User (admin) for the clinic in the User-service
#. Create sub-domain for the clinic. 
******************
Users Management
******************


******************
Settings
******************