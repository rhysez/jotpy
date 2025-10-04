from enum import Enum
from typing import Self

class Process(Enum):
    CREATE = "1"
    VIEW = "2"
    UPDATE = "3"
    DELETE = "4"