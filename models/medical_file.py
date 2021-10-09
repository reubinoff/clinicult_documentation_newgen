"""
Medical file Module hold the Patient medical information
"""
from enum import Enum
from datetime import datetime
from typing import List
from .patient import Patient
from .visit import Visit


class Medication:
    pass


class Sensetivity:
    pass


class MedicalFile:
    id: str
    patient: Patient
    visits: List[Visit]
    medications: List[Medication]
    sensetivities: List[Sensetivity]
