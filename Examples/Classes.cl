import * from System.Streams

class Person(name, age) -> Object {
    string() = "%s is %d years old" << (name, age)
    can_go_clubbing() =
        if age > 18 do
            true
        false
}

class Child(name, age) -> Person {
    super(name, age)

    in_school() = age >= 7 && age < 14
}

people = [] -> Person
people[] = init Person("John", 34)
people[] = init Child("Jimmy", 13)

string(people[1].in_school()) >> stdout
people[0] >> stdout