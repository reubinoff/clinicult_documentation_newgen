"""
Visit Module discribe the patient visits in the clinic
"""
from enum import Enum
from datetime import datetime

class Visit:
    id: str
    first_name: str
    last_name: str
    gender: Gender
    date_of_birth: datetime
    personal_clinic: Clinic
    cellphone: str
    mail: str
