import json

import pydantic
from pydantic import BaseModel
from dataclasses import dataclass


class Person(BaseModel):
    name: str
    age: float


class Job(BaseModel):
    division: str
    employeeID: int


class Employee(Person):
    title: str
    yos: float
    job: Job


if __name__ == '__main__':
    # create object
    e1 = Employee(name="Bob", age=41, title="Mayor", yos=2.2, job=Job(division="Research", employeeID=2322))
    print(e1.json())

    # create object from json string
    new_emp = """{"name": "Captain Clownshoes", "age": 41.0, "title": "Manager", "yos": 2.2, "job": {"division": "Funny Stuff", "employeeID": 2322}}"""
    loaded_thing = json.loads(new_emp)
    e2 = Employee(**loaded_thing)
    print(e2.json())
