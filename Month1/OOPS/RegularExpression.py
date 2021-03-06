"""
Overview : Regular Expression Demonstration
purpose : Regular expression creation
class name : RegularExpression
author : Akash Khandare
date : 04/03/2019

"""

from re import search


class RegularExpression:
    def __init__(self, string):
        self.string = string

    def regular_expression(self):
        """
        Creating regular expression and find pattern in string and
        then replace that string with input string

        """
        patt1 = search("<+.{4}>+", self.string)
        patt2 = search("<+.{9}>+", self.string)
        patt3 = search("x{10}", self.string)
        patt4 = search("xx\Wxx\Wx{4}", self.string)

        try:
            name = input("Enter name : ").strip()
            full_name = input("Enter full name : ").strip()
            mobile_number = input("Enter mobile number : ").strip()
            date = input("Enter date : ").strip()

            if not name.isalpha() or not mobile_number.isnumeric():
                raise ValueError
        except ValueError:
            print("You have enter wrong data.")
            self.regular_expression()
        else:
            self.replace_string(patt1.group(), name)
            self.replace_string(patt2.group(), full_name)
            self.replace_string(patt3.group(), mobile_number)
            self.replace_string(patt4.group(), date)
        print(self.string)

    def replace_string(self, patt, word):
        """
        replace word with patt
        :param patt: pattern in string
        :param word: word which want to place on patt
        """
        self.string = self.string.replace(patt, word)


# Main method
if __name__ == '__main__':
    string = "Hello <<name>>, We have your full" \
             + " name as <<full name>> in our system. your contact number is 91­xxxxxxxxxx." \
             + " Please,let us know in case of any clarification Thank you BridgeLabz xx/xx/xxxx."
    regular_exp = RegularExpression(string)
    regular_exp.regular_expression()
