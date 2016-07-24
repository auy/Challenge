# -*- coding: utf-8 -*-


class AddressBook(object):
    """Class representing the main address book

    Attributes:
        name (str): Name of the address book
        people (list): Peoples in the address book
        groups (dict): Groups in the address book
    """

    @property
    def all_people(self):
        return set(self.people + [person for sublist in self.groups.values()
                                  for person in sublist])

    def __init__(self, name):
        self.name = name
        self.people = []
        self.groups = {}

    def __str__(self):
        return '<{}>'.format(self.name)

    def add_person(self, person):
        """Adds new person to the address book

        Args:
            person (Person): Person to add
        """
        self.people.append(person)

    def add_group(self, name, members):
        """Adds new group to the address book

        Args:
            name (name): Name of the group
            members (list): list of group members
        """
        if not members:
            members = []

        if name not in self.groups:
            self.groups[name] = members
        else:
            raise KeyError('Group name: {} already defined in address book.')

    def get_people_by_group(self, group_name):
        """Finds all people within a group with given group name

        Args:
            group_name (str): Name of the group
        Returns (list): list of people in the group
        """
        return self.groups.get(group_name, [])

    def get_groups_by_person(self, person_name):
        """Finds all groups that contains a user with given name

        Args:
            person_name (str): First name, last name or full name
        Returns (str): names of matching groups
        """
        groups = []
        for name, members in self.groups.iteritems():
            for person in members:
                if AddressBook._name_check(person, person_name):
                    groups.append(name)
        return groups

    def get_people_by_name(self, name):
        """Finds all people who matches with given name filter

        Args:
            name (str): First name, last name or full name
        Returns (list): list of matching people
        """
        return [person for person in self.all_people
                if AddressBook._name_check(person, name)]

    def get_people_by_email(self, email):
        """Finds all people who matches with given email filter

        Args:
            email (str): Partial email
        Returns (list): list of matching people
        """
        return [person for person in self.all_people
                if AddressBook._email_check(person, email)]

    @staticmethod
    def _name_check(person, name):
        """Checks if given name matches with user's full name

        Args:
            person (Person): Given person instance
            name (str): First name, last name or full name
        Returns:
             (bool) True if name matches with users else False
        """
        if person.first_name == name or person.last_name == name or \
                (person.first_name in name and person.last_name in name):
            return True
        else:
            return False

    @staticmethod
    def _email_check(person, partial_email):
        """Checks if given email matches with user's email

        Args:
            person (Person): Given person instance
            partial_email (str): Partial email
        Returns:
             (bool) True if email matches with users else False
        """
        if not partial_email:
            return False

        for email_ in person.emails:
            if partial_email in email_:
                return True
        return False


class Person(object):
    """Class representing a person in address book

    Attributes:
        first_name (str): first name of the person
        last_name (str): last name of the person
        addresses (list): list of addresses that person has
        emails (list): list of emails that person has
        phone_numbers (list): list of phone numbers that person has
    """

    def __str__(self):
        return '<{}, {}>'.format(self.last_name, self.first_name)

    def __init__(self, first_name, last_name, addresses, emails, phone_numbers):
        self.first_name = first_name
        self.last_name = last_name
        self.addresses = addresses
        self.emails = emails
        self.phone_numbers = phone_numbers
