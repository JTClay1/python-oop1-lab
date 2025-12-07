#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title  # normal attribute, no rules needed

        # using internal var so the property can control assignment
        self._page_count = None

        # setting through the property — triggers validation
        self.page_count = page_count

    # ------ PAGE COUNT PROPERTY (getter) ------
    @property
    def page_count(self):
        # when code asks for book.page_count, return the internal value
        return self._page_count

    # ------ PROPERTY SETTER (validation happens here) ------
    @page_count.setter
    def page_count(self, value):
        # tests expect ONLY integers for page_count
        if not isinstance(value, int):
            print("page_count must be an integer")
            return

        # if valid, store internally
        self._page_count = value

    # ------ METHODS ------
    def turn_page(self):
        # again, this exact string matters for pytest
        print("Flipping the page...wow, you read fast!")
