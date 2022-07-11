# Class: DS5100
# Assignment: HW09
# Author: Raymundo Mora
import pandas as pd

class BookLover:
    def __init__(self,
                name,
                email,
                fav_genre,
                num_books=0,
                book_list=pd.DataFrame({'book_name':[],
                                        'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    # Method 1 
    def add_book(self,book_name,rating):
        assert isinstance(book_name,str), "'book_name' must be of type str"
        assert isinstance(rating,int), "'rating' must be of type int"
        assert 0 <= rating <= 5 , "'rating' must be 0 to 5"
        if book_name not in list(self.book_list.book_name):
            new_book = pd.DataFrame({'book_name':[book_name],
                                    'book_rating':[rating]})
            self.book_list = pd.concat([self.book_list, new_book],
                                    ignore_index=True)
            self.num_books += 1
        else:
            print(f"You already have {book_name} in your list.")
    # Method 2 
    def has_read(self,book_name):
        assert isinstance(book_name,str), "'book_name' must be of type str"
        return book_name in list(self.book_list.book_name)
    # Method 3 
    def num_books_read(self):
        return(self.num_books)
    # Method 4 
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3] 
    
