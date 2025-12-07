#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # using _size and _price internally so the property setters run first
        self._size = None
        self._price = None

        # these hit the setter logic instead of bypassing validation
        self.size = size
        self.price = price

    # ------ SIZE "PROPERTY" (Python version) ------
    @property
    def size(self):
        # whenever I read .size, this is what gets returned
        return self._size

    @size.setter
    def size(self, value):
        # allowed size options
        valid_sizes = ["Small", "Medium", "Large"]

        # if someone sets an invalid size, print the test’s exact message
        if value not in valid_sizes:
            print("size must be Small, Medium, or Large")
            return

        # store the real value internally
        self._size = value

    # ------ PRICE PROPERTY ------
    @property
    def price(self):
        # same idea as size — reading .price goes through here
        return self._price

    @price.setter
    def price(self, value):
        # validating that price is a number (int or float)
        if not isinstance(value, (int, float)):
            print("price must be a number")
            return

        # store it as a float for consistency
        self._price = float(value)

    # ------ METHODS ------
    def tip(self):
        # print exactly what the test expects
        print("This coffee is great, here’s a tip!")

        # increase price by 1 (test checks this!)
        self._price = self._price + 1
