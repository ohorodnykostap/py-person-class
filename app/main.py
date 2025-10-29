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

        if "wife" in item and item["wife"]:
            current.wife = Person.people[item["wife"]]

        if "husband" in item and item["husband"]:
            current.husband = Person.people[item["husband"]]

    return person_list
