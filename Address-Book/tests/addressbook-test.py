import unittest

from addressbook import AddressBook
from addressbook import Person


class AddressBookTest(unittest.TestCase):

    def setUp(self):
        self.address_book = AddressBook('My Address Book')

        self.person1 = Person('Charles', 'Babbage', ['London'],
                              ['charles.babbage@gmail.com'], ['+10000000'])
        self.person2 = Person('John', 'Backus', ['Philadelphia'],
                              ['john.backus@yahoo.com'], ['+10000000',
                                                          '+10000000'])
        self.person3 = Person('George', 'Boole', ['Lincoln'],
                              ['boole@gmail.com'], ['+10000000'])
        self.person4 = Person('Ada', 'Lovelace', ['London'],
                              ['ada@gmail.com', 'ada@lovelace.com'],
                              ['+10000000'])
        self.person5 = Person('Noam', 'Chomsky',
                              ['Philadelphia',
                               'Philadelphia, Pennsylvania, U.S.'],
                              ['nchomsky@gmail.com'], ['+10000000'])
        self.person6 = Person('Edgar F.', 'Codd', ['Isle of Portland'],
                              ['efc@gmail.com'], ['+10000000'])
        self.person7 = Person('Edsger', 'Dijkstra', ['Rotterdam'],
                              ['dijkstra@yahoo.com'], ['+10000000'])
        self.person8 = Person('John', 'McCarthy',
                              ['Boston, Massachusetts, U.S.'],
                              ['johnmcc@gmail.com'], ['+10000000'])
        self.person9 = Person('Donald', 'Knuth', ['Milwaukee, Wisconsin, US'],
                              ['knuth@gmail.com'], ['+10000000'])
        self.person10 = Person('Alan', 'Turing',
                               ['Maida Vale, London, England'],
                               ['alan.turing@gmail.com'], ['+10000000'])

        self.person11 = Person('Harry', 'Turing', ['Nowhere, Just for Test'],
                               ['turing.harry@gmail.com'], ['+10000000'])

        self.group1 = [self.person1, self.person2, self.person3, self.person4]
        self.group2 = [self.person5, self.person2, self.person4, self.person10]
        self.group3 = [self.person7, self.person8, self.person11]
        self.group4 = []

        self.all_users = [self.person1, self.person2, self.person3,
                          self.person4, self.person5, self.person6,
                          self.person7, self.person8, self.person9,
                          self.person10, self.person11]

        self.address_book.add_person(self.person6)
        self.address_book.add_person(self.person7)
        self.address_book.add_person(self.person8)
        self.address_book.add_person(self.person9)

        self.address_book.add_group('friends', self.group1)
        self.address_book.add_group('relatives', self.group2)
        self.address_book.add_group('colleagues', self.group3)
        self.address_book.add_group('future friends', self.group4)

    def tearDown(self):
        self.address_book = None

    def test_add_person(self):
        person1 = Person('John', 'Doe', ['London'],
                         ['jd@gmail.com'], ['+10000000'])
        person2 = Person('Jane', 'Doe', ['Amsterdam'],
                         ['jane@yahoo.com'], ['+10000000',
                                              '+10000001'])
        person3 = Person('Charlie', 'Brown', ['USA'], ['cbrown@gmail.com'],
                         ['+10000000'])

        self.address_book.add_person(person1)
        self.address_book.add_person(person2)

        self.assertIn(person1, self.address_book.people)
        self.assertIn(person2, self.address_book.people)
        self.assertNotIn(person3, self.address_book.people)

    def test_add_group(self):
        group1 = [self.person10]
        group2 = []

        self.address_book.add_group('Group 1', group1)
        self.address_book.add_group('Group 2', group2)

        self.assertIn('Group 1', self.address_book.groups.keys())
        self.assertItemsEqual(group1, self.address_book.groups['Group 1'])
        self.assertIn('Group 2', self.address_book.groups.keys())
        self.assertItemsEqual(group2, self.address_book.groups['Group 2'])

    def test_find_group_members(self):
        friends = self.address_book.get_people_by_group('friends')
        relatives = self.address_book.get_people_by_group('relatives')
        colleagues = self.address_book.get_people_by_group('colleagues')
        empty_list1 = self.address_book.get_people_by_group('')
        empty_list2 = self.address_book.get_people_by_group('old friends')
        empty_list3 = self.address_book.get_people_by_group('future friends')

        self.assertItemsEqual(friends, [self.person1, self.person2,
                                        self.person3, self.person4])
        self.assertItemsEqual(relatives, [self.person2, self.person4,
                                          self.person5, self.person10])
        self.assertItemsEqual(colleagues, [self.person7, self.person8,
                                           self.person11])
        self.assertEqual(empty_list1, [])
        self.assertEqual(empty_list2, [])
        self.assertEqual(empty_list3, [])

    def test_find_persons_groups(self):
        turing_groups = self.address_book.get_groups_by_person('Turing')
        john_groups = self.address_book.get_groups_by_person('John')
        empty_list1 = self.address_book.get_groups_by_person('')
        empty_list2 = self.address_book.get_groups_by_person('Jo')
        empty_list3 = self.address_book.get_groups_by_person('ing')

        self.assertItemsEqual(turing_groups, ['relatives', 'colleagues'])
        self.assertItemsEqual(john_groups, ['friends', 'relatives',
                                            'colleagues'])
        self.assertEqual(empty_list1, [])
        self.assertEqual(empty_list2, [])
        self.assertEqual(empty_list3, [])

    def test_find_person_by_name(self):
        donald_knuth1 = self.address_book.get_people_by_name('Donald Knuth')
        donald_knuth2 = self.address_book.get_people_by_name('Donald')
        donald_knuth3 = self.address_book.get_people_by_name('Knuth')
        empty_list1 = self.address_book.get_people_by_name('Knu')
        empty_list2 = self.address_book.get_people_by_name('Don')
        empty_list3 = self.address_book.get_people_by_name('')
        people_named_john = self.address_book.get_people_by_name('John')
        people_named_turing = self.address_book.get_people_by_name('Turing')

        self.assertEqual(donald_knuth1[0], self.person9)
        self.assertEqual(donald_knuth2[0], self.person9)
        self.assertEqual(donald_knuth3[0], self.person9)
        self.assertEqual(empty_list1, [])
        self.assertEqual(empty_list2, [])
        self.assertEqual(empty_list3, [])
        self.assertItemsEqual(people_named_john, [self.person2, self.person8])
        self.assertItemsEqual(people_named_turing, [self.person10,
                                                    self.person11])

    def test_find_person_by_email(self):
        edgar_f_codd = self.address_book.get_people_by_email('efc@gmail.com')
        yahoo_users = self.address_book.get_people_by_email('yahoo')
        empty_list = self.address_book.get_people_by_email('')
        ada_lovelace = self.address_book.get_people_by_email('ada@lovelace.com')
        edsger_dijkstra = self.address_book.get_people_by_email('kstra')
        all_users = self.address_book.get_people_by_email('.com')

        self.assertEqual(edgar_f_codd[0], self.person6)
        self.assertItemsEqual(yahoo_users, [self.person2, self.person7])
        self.assertEqual(empty_list, [])
        self.assertEqual(ada_lovelace[0], self.person4)
        self.assertEqual(edsger_dijkstra[0], self.person7)
        self.assertItemsEqual(all_users, self.all_users)
