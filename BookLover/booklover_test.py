# Class: DS5100
# Assignment: HW09
# Author: Raymundo Mora
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    # test 1 
    def test_1_add_book(self):
        # Create Instance
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        # Call method
        booklover1.add_book("Watchmen",5)
        
        self.assertTrue("Watchmen" in list(booklover1.book_list.book_name),"Test value is not true.")
    # test 2 
    def test_2_add_book(self):
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        booklover1.add_book("Watchmen",5)
        booklover1.add_book("Watchmen",4)
        
        expected = 1 
        nWatchmen = list(booklover1.book_list.book_name).count("Watchmen")
        self.assertEqual(nWatchmen,expected)
    # test 3 
    def test_3_has_read(self):
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        booklover1.add_book("Watchmen",5)
        answer = booklover1.has_read("Watchmen")
        self.assertTrue(answer,"Test value is not true.")     
    # test 4 
    def test_4_has_read(self):
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        booklover1.add_book("Watchmen",5)
        answer = booklover1.has_read("Harry Potter")
        self.assertFalse(answer,"Test value is not False.")
    # test 5 
    def test_5_num_books_read(self):
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        booklover1.add_book("Watchmen",5)  
        booklover1.add_book("Thus Spoke Zarathustra",4)
        booklover1.add_book("Crime and Punishment",3) 
        expected = 3 
        self.assertEqual(booklover1.num_books,expected)       
    # test 6
    def test_6_fav_books(self):
        booklover1 = BookLover("Ray","email@email.com","non-fiction")
        booklover1.add_book("Watchmen",5)  
        booklover1.add_book("Thus Spoke Zarathustra",4)
        booklover1.add_book("Crime and Punishment",3) 
        assertion = min(booklover1.fav_books().book_rating) > 3
        self.assertTrue(assertion,"Test value is not true.")
if __name__ == '__main__':
    # Had to add the arguments below to tell  
    unittest.main(verbosity=3)
