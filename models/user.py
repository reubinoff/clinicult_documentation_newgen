"""
User Module hold the Patient information
"""
from enum import Enum
from datetime import datetime

class Gender(Enum):
    male = 1
    female = 2
    other = 3

class Clinic(Enum):
    clalit = 1
    maccabi = 2
    other = 3

class User:
    @property
    def id() -> str:
        """[summary]

        :return: Client personal id
        :rtype: str
        """

    id: str
    first_name: str
    last_name: str
    gender: Gender
    date_of_birth: datetime
    personal_clinic: Clinic
    cellphone: str
    mail: str

class s:
    """
    sdsd
    """ 
