#        Task 2
# Library
# Write a class structure that implements a library. Classes:
#
# 1) Library - name, books = [], authors = []
# 2) Book - name, year, author (author must be an instance of Author class)
# 3) Author - name, country, birthday, books = []
#
# Library class
# Methods:
# - new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.
# - group_by_author(author: Author) - returns a list of all books grouped by the specified author
# - group_by_year(year: int) - returns a list of all the books grouped by the specified year
#
# All 3 classes must have a readable __repr__ and __str__ methods.
#
# Also, the book class should have a class variable which holds the amount of all existing books

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        return

    def __str__(self):
        return f"В библиотеке {self.name} есть книги {self.books}."


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return f'Книга {self.name} написана в {self.year} году, её автор {self.author}.'


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.book = []

    def __str__(self):
        return f'{self.name} родился в {self.country} d {self.year} году.'

mihail_bulgakov_books = ['Мастер и Маргарита', 'Собачье сердце', 'Записки юного врача']