#############
Scenarios
#############



here are some main user flows in clinicult system

******************
Client on-boarding
******************

This scenario describe the acceptance of new customer to the clinic. in this flow we have two options:
one case is that user already exists in clinic data, and the second one is the patient is new.

In both cases we will search for the Patient in the Search bar. if Patient exists, we can update his visit in the clinic. 
if Patient not exists in clinic data, we will have a form that add new Patient to our system, and after Patient added, we can update his visit.

******************
Clinet Mediacal File
******************
Each patient that visit the clinic, willl have medical file that will describe all his mediacal history and visits.
in every state of his visit, the medical pearson, may take have access to his file.

******************
Patient state update
******************
Once patient has start his visit in the clinic, he may see couple of medical entities. 
each entity has option to change the pearson who need to check the patient. changing the medicak entity is similar to change his visit state.
The patien can change his state couple of times, and can visit in the same state more then one time.
for example, at the begining, the patient will see the nurse. then he can move to the doctor care, and then come back to the nurse.

each state will be recorded and will update within his medical file.
in addition, all those update will be stored in his visit event, and may be query later.
Each medical update his medical file as mentioed before.

******************
Medical entity dashboard
******************
for each entity in the clinic, we will show list of patients that ready for relevant state, according to his permission. in addition the medical entity can search on history of visits.
Each entity can see only his relevant states according to his permission that the admin give on the admin site.