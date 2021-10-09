"""
Medical file Module hold the Patient medical information
"""
from enum import Enum
from datetime import datetime
from typing import List, Optional
from .patient import Patient
from .visit import Visit


class Medication:
    pass


class Sensetivity:
    pass


class MedicalFile:
    id: str
    patient: Patient
    current_visit: Optional[Visit]
    pats_visits: List[Visit]
    medications: List[Medication]
    sensetivities: List[Sensetivity]
