"""
Visit Module discribe the patient visits in the clinic
"""
from enum import Enum
from datetime import date, datetime
from typing import Optional, List
from models.patient import Clinic


class VisitState(Enum):
    doctor = 1
    nurse = 2
    unknown = 100
    finish = 999


class Measurment:
    pass


class Visit:
    id: str
    visit_date: datetime
    state: VisitState
    cellphone: str
    measurements: Optional[List[Measurment]]
