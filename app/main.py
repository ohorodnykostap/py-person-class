class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people: list) -> list:
    person_list = []

    for p in people:
        person = Person(p['name'], p['age'])
        person_list.append(person)

    for p in people:
        current = Person.people[p['name']]

        if 'wife' in p and p['wife']:
            current.wife = Person.people[p['wife']]

        if 'husband' in p and p['husband']:
            current.husband = Person.people[p['husband']]

    return person_list
