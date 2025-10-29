class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = []

    for item in people:
        person = Person(item["name"], item["age"])
        person_list.append(person)

    for item in people:
        current = Person.people[item["name"]]

        if item.get("wife") is not None:
            current.wife = Person.people[item["wife"]]

        if item.get("husband") is not None:
            current.husband = Person.people[item["husband"]]

    return person_list
