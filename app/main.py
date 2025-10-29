class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    """
        Create a list of Person objects
        and link them as husband/wife if names match.
        Clears Person.people at the start to avoid residual state.
    """
    Person.people = {}
    person_list = []

    for item in people:
        person = Person(item["name"], item["age"])
        person_list.append(person)

    for item in people:
        current = Person.people[item["name"]]

        if item.get("wife") and item["wife"] in Person.people:
            current.wife = Person.people[item["wife"]]

        if item.get("husband") and item["husband"] in Person.people:
            current.husband = Person.people[item["husband"]]

    return person_list
