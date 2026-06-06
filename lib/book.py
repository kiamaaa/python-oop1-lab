#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast")

title_input = input("Enter book's title: ")
pages_input = input("Enter page number: ")


try:
    page_count = int(pages_input)
    
    my_book = Book(title_input, page_count)
    
    my_book.turn_page()
except ValueError:
    print("page_count must be an integer")
        