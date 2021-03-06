import math
import numpy as np
import random
import datetime


#################################################################################
def get_input(msg=None, n=None):
    if n == None:
        print(msg)
    elif msg == None:
        print(n)
    else:
        print(msg, " ", n)
    return int(input())


#################################################################################
"""
    Read string value from user and return\n")
"""


def string_replace():
    str1 = "Hello <<UserName>>, How are you?"
    name = input("Enter your name : ")
    str1 = str1.replace("<<UserName>>", name)
    print(str1)


#################################################################################
"""
    Get one param, as n
    calculate the value n time and check the condition 
    and print percentage
"""


def flip_coin(n):
    for i in range(n):
        rand = random.random()
    if rand < 0.5:
        print("Percentage of Head : ", int(rand * 100))
    else:
        print("Percentage of Tail : ", int(rand * 100))


#################################################################################
"""
    check year is leap year or not and then return boolean value 
    param Getting year as int type 
"""


def is_leap_year(year):
    if (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


#################################################################################
"""
    Give the table of power of 2 when number will less than 31 
    param Getting number as int type
"""


def power_of_two(power):
    for i in range(power + 1):
        if power <= 31:
            print(i, " is power of 2 is : ", int(math.pow(2, i)))
        else:
            print("Range exceeded")


#################################################################################
"""
     Return the harmonic value as float 
     param Getting number n as int type
"""


def harmonic_value(n):
    value = 0
    for i in range(1, n + 1):
        value = value + 1 / n
    return value


#################################################################################
"""
    Get one param as n and then check is prime or not
    and return boolean value 
"""


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


#################################################################################
"""
     Print Prime factor of n
     param Getting number n as int type
"""


def prime_factor(n):
    print("Prime factor is : ")
    for i in range(2, n):
        if is_prime(i):
            if n % i == 0:
                print(i, " ")


#################################################################################
"""
    Get one param, array n
    print sum of three equal to zero
"""


def sum_of_three(n):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                if (n[i] + n[j] + n[k]) == 0:
                    print(n[i], " + ", n[j], " + ", n[k], " = 0")


#################################################################################
"""
    Get two param, one is x axis and second is y axis
"""


def euclidean_distance(x, y):
    return math.sqrt(math.pow(x, x) + math.pow(y, y))


#################################################################################
"""
    get three param a, b and c
    Give the roots of x for a*x*x + b*x + c.
"""


def root_of_x(a, b, c):
    delta = b * b - 4 * a * c
    x1 = (b + math.sqrt(abs(delta))) / (2 * a)
    x2 = (-b - math.sqrt(abs(delta))) / (2 * a)
    return x1, x2


#################################################################################
"""
    param it will get temperature and wind speed value as double
    Return weather value
"""


def weather(t, v):
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * math.pow(v, 0.16)
    return w


#################################################################################
"""
    Get two param for row and column
    Getting value from user and return two D array 
"""


def get_two_d_arr(r, c):
    print("Enter a list : ")
    arr = np.zeros((r, c))
    for i in range(r):
        for j in range(c):
            arr[i][j] = int(input())
    return arr


#################################################################################
"""
    Print two D array on console
"""


def display_two_d_arr(arr):
    print(arr)


#################################################################################
"""
    init to play tic-tac-toe game 
"""


def tic_tac_toe():
    arr = np.zeros((3, 3))
    player = int(input("If you want to play first then enter 1 else 2. "))
    cnt = 0
    while cnt < 9:
        if player == 1:
            show_game(arr)
            player_call(arr)
            cnt += 1
            player = 2
            if win_check(arr, 'X') == -1:
                player = -1
        elif player == 2:
            computer(arr)
            cnt += 1
            player = 1
            if win_check(arr, 'O') == -1:
                player = -1
        else:
            show_game(arr)
            break


#################################################################################
"""
    Show the tic-tac-toe game 
"""


def show_game(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if int(arr[i][j]) != 0:
                print(chr(int(arr[i][j])), end="  ")
            else:
                print("-", end="  ")
        print()


#################################################################################
"""
    This method for user player to play tic-tac-toe
    First will get position from player to marked X 
"""


def player_call(arr):
    print("Enter position with x and y co-ordinate")
    posX, posY = int(input()), int(input())
    # while True:
    if arr[posX][posY] == 0:
        arr[posX][posY] = ord('X')
        # break
    else:
        print("This position already marked.")
        show_game(arr)
        player_call(arr)


#################################################################################
"""
    This method for computer player
    Generate position and then marked O 
"""


def computer(arr):
    while True:
        posX = random.randrange(0, 3, 1)
        posY = random.randrange(0, 3, 1)
        if arr[posX][posY] == 0:
            arr[posX][posY] = ord('O')
            break


#################################################################################
"""
    Check to who won the tic-tac-toe game 
"""


def win_check(arr, ch):
    c = ord(ch)
    if (arr[0][0] == c and arr[0][1] == c and arr[0][2] == c) \
            or (arr[1][0] == c and arr[1][1] == c and arr[1][2] == c) \
            or (arr[2][0] == c and arr[2][1] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][0] == c and arr[2][0] == c) \
            or (arr[0][1] == c and arr[1][1] == c and arr[2][1] == c) \
            or (arr[0][2] == c and arr[1][2] == c and arr[2][2] == c) \
            or (arr[0][0] == c and arr[1][1] == c and arr[2][2] == c) \
            or (arr[0][2] == c and arr[1][1] == c and arr[2][0] == c):
        if ch == 'X':
            print("Player won")
            return -1
        else:
            print("Computer won")
            return -1


#################################################################################
"""
    Getting current time and return it
"""


def start_watch():
    start = datetime.datetime.now().microsecond
    return start


#################################################################################
"""
    Return elapse time 
"""


def stop_watch(start):
    stop = datetime.datetime.now().microsecond
    return stop - start


#################################################################################
"""
    Get three param, one is string, second is low index and third is end index
    swap the element and return string 
"""


def swap(str, l, r):
    str = list(str)
    str[l], str[r] = str[r], str[l]
    return ''.join(str)


#################################################################################
"""
    Get three param, one is string, second is low index and third is end index
"""


def permutation(str, l, r):
    if l == r:
        print(str)
    else:
        for i in range(l, r):
            str = swap(str, l, i)
            permutation(str, l + 1, r)
            str = swap(str, l, i)


#################################################################################
"""
    Get one param, as n
    return array of unique n number 
"""


def coupon_generator(n):
    li = [None] * n
    c = random.randrange(100, 500, 5)
    li[0] = int(c)
    j = 0
    while j < n:
        c = random.randrange(100, 500, 5)
        for i in range(j):
            if li[i] == c:
                c = random.randrange(100, 500, 5)
        li[j] = int(c)
        j += 1
    return li


#################################################################################
"""
    Gambler
"""


def gambler(goal):
    doller = 1
    win, loss = 0, 0
    while True:
        n = int(input("You guess some number between 1 to 2 :"))
        g = random.randrange(1, 3, 1)
        if n == g:
            doller += 1
            win += 1
            print("You won this bet.")
        else:
            print("You loss this bet.")
            doller -= 1
            loss += 1
        if doller == 0:
            print("You loss your all doller.")
            break
        elif doller == goal:
            print("You achived your goal.")
            break
    print("Tatal match : ", (win + loss))
    print("Percentage of win : ", ((win * 100) / (win + loss)))
    print("Percentage of loss : ", ((loss * 100) / (win + loss)))


#################################################################################
# 
# Algorithm
#
#################################################################################
"""
    param it will get two string 
    check it is anagram or not then return boolean value
"""


def is_anagram(str1, str2):
    if len(str1) == len(str2):
        arr = np.full((len(str2)), False)
        cnt = 0
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j] and arr[j] == False:
                    arr[j] = True
                    cnt += 1
                    break
    else:
        return False
    if cnt == len(str1):
        return True


#################################################################################
"""
    Param It will get number n as int type
    Check it is palindrome or not and then return boolean value
"""


def is_palindrome(n):
    new = n
    reverse = 0
    while new != 0:
        temp = int(new % 10)
        new = int(new / 10)
        reverse = (reverse * 10) + temp
    if n == reverse:
        return True
    else:
        return False


#################################################################################
"""
    param It will get number range as int type
    return the array of prime number between 2 to range
"""


def get_prime_number(rng):
    arr = []
    for i in range(2, rng + 1):
        if is_prime(i):
            arr.append(i)
    return arr


#################################################################################
"""
    Get one param, as array
    return array of palindrome number
"""


def get_palindrome(arr):
    newArr = []
    for i in arr:
        if is_palindrome(i):
            newArr.append(i)
    return newArr


#################################################################################
"""
    Get one param, array
    return array of anagram number
"""


def get_anagram(arr):
    newArr = []
    for i in range(len(arr) - 1):
        for j in range(1 + i, len(arr)):
            if is_anagram(str(arr[i]), str(arr[j])):
                newArr.append(arr[i])
                newArr.append(arr[j])
    return newArr


#################################################################################
"""
     Param It will get list, start index and end index
     Give array in sorted order by insertion sort algorithm
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        while j > -1:
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -= 1
    return arr


#################################################################################
"""
     Param It will get list, start index and end index
     Give array in sorted order by bubble sort algorithm
"""


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


#################################################################################
"""
    Param It will get String array, start index and end index
    Give array in sorted order by merge sort algorithm
"""


def merge_sort(arr, start, end):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


#################################################################################
"""
    param It will get list, start index,middle index and end index
    Give array in sorted order by merge sort algorithm
    This method call in mergeSort
"""


def merge(arr, start, mid, end):
    temp = start
    n1 = mid - start + 1
    n2 = end - mid
    lm = [0] * n1
    rm = [0] * n2

    for i in range(n1):
        lm[i] = arr[temp]
        temp += 1
    for i in range(n2):
        rm[i] = arr[mid + 1]
        mid += 1
    k = 0
    j = 0
    while k < n1 and j < n2:
        if lm[k] > rm[j]:
            arr[start] = rm[j]
            j += 1
        else:
            arr[start] = lm[k]
            k += 1
        start += 1
    while k < n1:
        arr[start] = lm[k]
        k += 1
        start += 1
    while j < n2:
        arr[start] = rm[j]
        j += 1
        start += 1


#################################################################################
"""
    Param It will get list, start index, end index and key
    Give index of key value of which will find in array
"""


def binary_search(arr, start, last, key):
    while start <= last:
        mid = int((start + last) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            start = mid + 1
        elif arr[mid] > key:
            last = mid - 1


#################################################################################
"""
    Get one param, as Rupees for change
    Print change
"""


def vending_machine(change):
    arr = (1000, 500, 100, 50, 10, 5, 2, 1)
    for i in arr:
        if change == 0:
            return 0
        elif change >= i:
            print(i)
            change = vending_machine(change - i)


#################################################################################
"""
    Get one param, as i value
    return week name
"""


def week(i):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(i)


#################################################################################
"""
    Get three param, one is day, second is month and third is year
    return value of day of week
"""


def day_of_week(d, m, y):
    y0 = y - (14 - m) / 12
    x = y0 + y0 / 4 - y0 / 100 + y0 / 400
    m0 = m + 12 * ((14 - m) / 12) - 2
    d0 = (d + x + 31 * m0 / 12) % 7
    return week(int(d0))


#################################################################################
"""
    Get one param, decimal value
    return binary number
"""


def to_binary(n):
    tm = np.zeros(8)
    res = np.zeros(8)
    i = 0
    while n != 0:
        temp = int(n % 2)
        n = int(n / 2)
        tm[i] = temp
        i += 1
    i = 8
    for j in tm:
        i -= 1
        res[i] = j
    return res


#################################################################################
"""
    Get one param, binary number
    and Convert binary number into decimal
"""


def to_decimal(binary):
    j = 7
    res = 0
    for i in binary:
        if i == 1:
            res = res + math.pow(2, j)
        j -= 1
    return int(res)


#################################################################################
"""
    Get one param, binary number
    swap the nibble of binary number and return new binary number
"""


def swap_nibbles(binary):
    j = 4
    for i in range(4):
        binary[i], binary[j] = binary[j], binary[i]
        j += 1
    return binary


#################################################################################
"""
    Read data from file and return sorted list
"""


def read_from_file():
    f = open("abc.txt", 'r')
    word = ""
    for i in f:
        word = word + i
    st = word.split("\n")
    sts = bubble_sort(list(st))
    return sts


#################################################################################
"""
    Get two param, one is key which is for finding and second is sorted list
"""


def word_list(key, sts):
    print(sts)
    mid = binary_search(sts, 0, len(sts) - 1, key)
    if mid is None:
        return False
    return True


#################################################################################
"""
    Get one param as fahrenheit for converting into celsius
"""


def celsius_to_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f


#################################################################################
"""
    Get one param as fahrenheit for converting into celsius
"""


def fahrenheit_to_celsius(f):
    c = (f - 32) * 5 / 9
    return c


#################################################################################
"""
    Get two param, one is start range and other is last range like 0 to 10
"""


def question_to_find_your_number(start, last):
    while start <= last:
        mid = int((start + last) / 2)
        if get_input("are you guess this number : ", mid) == 1:
            print("Number found.")
            break
        elif int(get_input("If your number will greater than then enter 1 else 0 : ", mid)) == 1:
            start = mid + 1
            continue
        elif int(get_input("If your number will less than then enter 1 else 0 : ", mid)) == 1:
            last = mid - 1
