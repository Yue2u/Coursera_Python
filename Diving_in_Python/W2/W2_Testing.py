from datetime import date


def extract_description(usr_str):
    return "Открытие чемпионата..."


def extract_date(usr_str):
    return date(2018, 6, 14)


class Event:
    def __init__(self, description, date_):
        self.description = description
        self.date = date_

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, usr_input):
        description_ = extract_description(usr_input)
        date_ = extract_date(usr_input)
        return cls(description_, date_)


class Human:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def _say(text):
        print(text)

    def say_name(self):
        self._say(f"Hello, I am {self.name}")

    def say_age(self):
        self._say(f"Hello, I am {self.age} yo")

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 130


class Planet:
    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        print(f"Welcome to {self.name}, {human.name}!")
        self.population.append(human)


class Robot:
    def __init__(self, power):
        self._power = power

    @property
    def power(self):
        return self._power


wall_e = Robot(100)
print(wall_e.power)

event = Event.from_string("о чемпионате....")
print(event)

mars = Planet("Mars")

bob = Human("Bob", 42)
bob.say_name()
bob.say_age()
print(Human.is_age_valid(42))

mars.add_human(bob)


# --------------------------------------------------------------------------
import json


class PetExport:
    def export(self, pet):
        pass


class ExportJSON(PetExport):
    def export(self, pet):
        return json.dumps({
            "name": pet.name,
            "breed": pet.breed
        })


class ExportXML(PetExport):
    def export(self, pet):
        return f
#<?xml version="1.0" encoding="utf-8"?>
#<dog>
#   <name>{pet.name}</name>
#    <breed>{pet.breed}</breed>
#</dog>


class Pet:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def get_info(self):
        return f"{self.breed} named {self.get_name()}"


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super().__init__(name, breed)
        self._exporter = exporter or ExportJSON()
        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad exporter", exporter)

    def exprot(self):
        return self._exporter.export(self)


dog = ExDog("Sharik", "Dvornyaga", exporter=ExportXML())
print(dog.exprot())
dog2 = ExDog("Tuzik", "Mops", exporter=ExportJSON())
print(dog2.exprot())

