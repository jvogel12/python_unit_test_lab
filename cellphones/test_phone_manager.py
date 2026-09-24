import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')
        assignment_manager = PhoneAssignments()

        assignment_manager.add_employee(employee1)
        assignment_manager.add_employee(employee2)

        self.assertCountEqual([employee1, employee2], assignment_manager.employees)


    def test_create_and_add_employee_with_duplicate_id(self):
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(1, 'Bill')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_employee(employee1)

        with self.assertRaises(PhoneError):
            assignment_manager.add_employee(employee2)


    def test_assign_phone_to_employee(self):
        phone = Phone(1, 'Apple', 'iPhone 6')
        employee = Employee(1, 'Alice')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone)
        assignment_manager.add_employee(employee)

        assignment_manager.assign(phone.id, employee)

        self.assertEqual(employee.id, phone.employee_id)


    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

        phone = Phone(1, 'Apple', 'iPhone 6')
        employee1 = Employee(1, 'Alice')
        employee2 = Employee(2, 'Bill')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone)
        assignment_manager.assign(phone.id, employee1)

        with self.assertRaises(PhoneError):
            assignment_manager.assign(phone.id, employee2)

        self.assertEqual(employee1.id, phone.employee_id)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        phone1 = Phone(1, 'Apple', 'iPhone 6')
        phone2 = Phone(2, 'Apple', 'iPhone 5')
        employee = Employee(1, 'Alice')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone1)
        assignment_manager.add_phone(phone2)
        assignment_manager.assign(phone1.id, employee)

        with self.assertRaises(PhoneError):
            assignment_manager.assign(phone2.id, employee)

        self.assertIsNone(phone2.employee_id)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.

        phone = Phone(1, 'Apple', 'iPhone 6')
        employee = Employee(1, 'Alice')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone)
        assignment_manager.assign(phone.id, employee)

        assignment_manager.assign(phone.id, employee)

        self.assertEqual(employee.id, phone.employee_id)


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        phone = Phone(1, 'Apple', 'iPhone 6')
        employee = Employee(1, 'Alice')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone)
        assignment_manager.assign(phone.id, employee)

        assignment_manager.un_assign(phone.id)

        self.assertIsNone(phone.employee_id)


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist

        phone = Phone(1, 'Apple', 'iPhone 6')
        employee_with_phone = Employee(1, 'Alice')
        employee_without_phone = Employee(2, 'Bill')
        unknown_employee = Employee(3, 'Ted')
        assignment_manager = PhoneAssignments()
        assignment_manager.add_phone(phone)
        assignment_manager.add_employee(employee_with_phone)
        assignment_manager.add_employee(employee_without_phone)
        assignment_manager.assign(phone.id, employee_with_phone)

        self.assertIs(phone, assignment_manager.phone_info(employee_with_phone))
        self.assertIsNone(assignment_manager.phone_info(employee_without_phone))
        with self.assertRaises(PhoneError):
            assignment_manager.phone_info(unknown_employee)
