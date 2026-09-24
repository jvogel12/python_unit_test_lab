"""
Practice using

 assertTrue
 assertFalse
 assertIsNone
 assertIsNotNone
 assertIn
 assertNotIn

"""

from studentlists import ClassList, StudentError
from unittest import TestCase

class TestStudentLists(TestCase):

    def test_add_student_check_student_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        self.assertIn('Test Student', test_class.class_list)

        test_class.add_student('Another Test Student')
        self.assertIn('Test Student', test_class.class_list)
        self.assertIn('Another Test Student', test_class.class_list)


    def test_add_student_already_in_list(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        with self.assertRaises(StudentError):
            test_class.add_student('Test Student')


    ## TODO write a test that adds and removes a student, 
    # and asserts the student is removed. Use assertNotIn
    def test_add_remove_student_ensure_removed(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')
        test_class.remove_student('Test Student')
        self.assertNotIn('Test Student', test_class.class_list)


    ## TODO write a test that adds some example students, 
    # then removes a student not in the list, and asserts a StudentError is raised
    def test_remove_student_not_in_list_raises_student_error(self):
        test_class = ClassList(2)
        test_class.add_student('Test Student')

        with self.assertRaises(StudentError):
            test_class.remove_student('Student Not Enrolled')


    ## TODO write a test that removes a student from an 
    # empty list, and asserts a StudentError is raised
    def test_remove_student_from_empty_list_raises_student_error(self):
        test_class = ClassList(2)

        with self.assertRaises(StudentError):
            test_class.remove_student('Test Student')



    def test_is_enrolled_when_student_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')
        test_class.add_student('Martha Stewart')
        self.assertTrue(test_class.is_enrolled('Snoop Dogg'))
        self.assertTrue(test_class.is_enrolled('Martha Stewart'))


    def test_is_enrolled_empty_class_list(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_enrolled('Snoop Dogg'))


    ## TODO write a test that adds some example students to a test class,
    ## then, call is_enrolled for a student who is not enrolled. 
    # Use assertFalse to verify is_enrolled returns False.
    def test_is_enrolled_when_student_not_present(self):
        test_class = ClassList(2)
        test_class.add_student('Snoop Dogg')

        self.assertFalse(test_class.is_enrolled('Martha Stewart'))


    def test_string_with_students_enrolled(self):
        test_class = ClassList(2)
        test_class.add_student('Taylor Swift')
        test_class.add_student('Kanye West')
        self.assertEqual('Taylor Swift, Kanye West', str(test_class))


    def test_string_empty_class(self):
        test_class = ClassList(2)
        self.assertEqual('', str(test_class))


    def test_index_of_student_student_present(self):
        test_class = ClassList(3)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')
        test_class.add_student('Ron')

        self.assertEqual(1, test_class.index_of_student('Harry'))
        self.assertEqual(2, test_class.index_of_student('Hermione'))
        self.assertEqual(3, test_class.index_of_student('Ron'))

        # This assert passes, but it's redundant - the first assert statement will fail if
        # the method call returns None
        self.assertIsNotNone(test_class.index_of_student('Harry'))


  
    ## TODO write a test for index_of_student when the class_list list is empty.  
    # Assert index_of_student returns None for a student if the list is empty. 
    # use assertIsNone.
    def test_index_of_student_empty_class_returns_none(self):
        test_class = ClassList(2)

        self.assertIsNone(test_class.index_of_student('Harry'))
 
 
    ## TODO write another test for index_of_student. In the case when the 
    # class_list is not empty but has some students.
    # assert that searching for a student name that is not in the list, returns None.
    def test_index_of_student_missing_student_returns_none(self):
        test_class = ClassList(2)
        test_class.add_student('Harry')

        self.assertIsNone(test_class.index_of_student('Hermione'))

   
    ## TODO write a test for your new is_class_full method when the class is full. 
    # use assertTrue.
    def test_is_class_full_when_class_is_full(self):
        test_class = ClassList(2)
        test_class.add_student('Harry')
        test_class.add_student('Hermione')

        self.assertTrue(test_class.is_class_full())
    
    ## TODO write a test for your new is_class_full method for when is empty, 
    # and when it is not full. Use assertFalse.
    def test_is_class_full_when_empty_or_not_full(self):
        test_class = ClassList(2)
        self.assertFalse(test_class.is_class_full())

        test_class.add_student('Harry')
        self.assertFalse(test_class.is_class_full())
