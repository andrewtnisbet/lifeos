from enum import Enum

class EnergyLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Responsibility(str, Enum):
    WORK = "Work"
    CAREER = "Career"
    HEALTH = "Health"
    FINANCE = "Finance"
    HOME = "Home"
    RELATIONSHIP = "Relationship"
    LEARNING = "Learning"
    PERSONAL = "Personal"