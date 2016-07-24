# addressbook

## Classes

### AddressBook
Class representing the main address book

#### Attributes:
 * name (str): Name of the address book
 * people (list): Peoples in the address book
 * groups (dict): Groups in the address book

#### Instance variables
 * all_people
 * groups
 * name
 * people

#### Methods
```python
__init__(self, name)

add_group(self, name, members)
    Adds new group to the address book

    Args:
        name (name): Name of the group
        members (list): list of group members

add_person(self, person)
    Adds new person to the address book

    Args:
        person (Person): Person to add

get_groups_by_person(self, person_name)
    Finds all groups that contains a user with given name

    Args:
        person_name (str): First name, last name or full name
    Returns (str): names of matching groups

get_people_by_email(self, email)
    Finds all people who matches with given email filter

    Args:
        email (str): Partial email
    Returns (list): list of matching people

get_people_by_group(self, group_name)
    Finds all people within a group with given group name

    Args:
        group_name (str): Name of the group
    Returns (list): list of people in the group

get_people_by_name(self, name)
    Finds all people who matches with given name filter

    Args:
        name (str): First name, last name or full name
    Returns (list): list of matching people
```

### Person
Class representing a person in address book

#### Attributes:
 * first_name (str): first name of the person
 * last_name (str): last name of the person
 * addresses (list): list of addresses that person has
 * emails (list): list of emails that person has
 * phone_numbers (list): list of phone numbers that person has

#### Instance variables
 * addresses
 * emails
 * first_name
 * last_name
 * phone_numbers

#### Methods
```python
__init__(self, first_name, last_name, addresses, emails, phone_numbers)
```

### Sample Usage
```python
>>> from addressbook import Person
>>> from addressbook import AddressBook

>>> person = Person('Charlie', 'Brown', ['USA'], ['cbrown@test.com'], ['+10000000'])
>>> addressbook = AddressBook('My AddressBook')

>>> addressbook.add_person(person)
>>> addressbook.add_group('group-1', [person])

>>> addressbook.get_groups_by_person('Charlie')
['group-1']

>>> addressbook.get_people_by_email('own@tes')
[<Brown, Charlie>]

>>> addressbook.get_people_by_group('group-1')
[<Brown, Charlie>]

>>> addressbook.get_people_by_name('Brown')
[<Brown, Charlie>]
```
