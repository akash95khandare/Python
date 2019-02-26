import numpy

from com.bridgelab.util import Utility as u


class TwoDPrimeArray:
    def __init__(self):
        self.arr = numpy.zeros((10, 25))

    def two_d_prime_array(self, range):
        number = u.get_prime_number(range)
        k = j = 0
        block = 100
        for i in number:
            if i > block:
                k += 1
                j = 0
                block += 100
            self.arr[k][j] = i
            j += 1

        print(self.arr)


t = TwoDPrimeArray()
rng = int(input("Enter range : "))
t.two_d_prime_array(rng)