# sensor.py

from random import *

class Sensor:
    """Base sensor class"""

    def __init__(self, normal_chance=0.95):
        self.normal_chance = normal_chance

    def get_unit(self): pass
    def generate_value(self): pass
    
class NIBP(Sensor):
    """Noninvasive blood pressure"""

    def __init__(self, normal_chance=0.95):
        super().__init__(normal_chance)

    def get_unit(self): return "mmHg"

    def generate_value(self):
        if (random() <= self.normal_chance):
            return (f"{randint(90, 119)}/{randint(60, 79)}", "Normal")
        category = choice([
            "Elevated",
            "Stage 1 high blood pressure",
            "Stage 2 high blood pressure",
            "Hypertensive crisis"
        ])
        if (category == "Elevated"):
            return (f"{randint(120, 129)}/{randint(60, 79)}", category)
        if (category == "Stage 1 high blood pressure"):
            return (f"{randint(130, 139)}/{randint(80, 89)}", category)
        if (category == "Stage 2 high blood pressure"):
            return (f"{randint(140, 179)}/{randint(90, 119)}", category)
        else:
            return (f"{randint(180, 200)}/{randint(120, 140)}", category)
        
class PulseOximeterSpO2(Sensor):
    """Pulse oximeter SpO2"""

    def __init__(self, normal_chance=0.95):
        super().__init__(normal_chance)

    def get_unit(self): return "%"

    def generate_value(self):
        if (random() <= self.normal_chance):
            return (randint(95, 100), "Normal")
        category = choice([
            "Hypoxemia",
            "Severe hypoxemia"
        ])
        if (category == "Hypoxemia"):
            return (randint(91, 94), category)
        else:
            return (randint(80, 90), category)
        
class RespiratoryRate(Sensor):
    """Respiratory rate"""

    def __init__(self, normal_chance=0.95):
        super().__init__(normal_chance)

    def get_unit(self): return "bpm"

    def generate_value(self):
        if (random() <= self.normal_chance):
            return (randint(8, 12), "Normal")
        category = choice([
            "Low breathing rate",
            "High breathing rate"
        ])
        if (category == "Low breathing rate"):
            return (randint(4, 7), category)
        else:
            return (randint(13, 18), category)
        
class Temperature(Sensor):
    """Body temperature"""

    def __init__(self, normal_chance=0.95):
        super().__init__(normal_chance)

    def get_unit(self): return "°C"

    def generate_value(self):
        if (random() <= self.normal_chance):
            return (randint(367, 371) / 10, "Normal")
        category = choice([
            "Hypothermia",
            "Hyperthermia"
        ])
        if (category == "Hypothermia"):
            return (randint(355, 366) / 10, category)
        else:
            return (randint(372, 400) / 10, category)