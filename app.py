import math
import re


def vowels_count(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count


print(vowels_count("The quick brown for jumps over the lazy dog."))


def numbers_list(length, start):
    numbers = []
    for i in range(start, start + length):
        numbers.append(i)
    return numbers


print(numbers_list(10, 5))


inputs = []
for i in range(5):
    inputs.append(input(f"Enter element number {i+1}:\n"))


def reverse_list(inputs):
    inputs.sort(reverse=True)
    return inputs


print(reverse_list(inputs))


def fizz_buzz(num):
    if not (num % 5):
        if not (num % 3):
            return "FizzBuzz"
        return "Buzz"

    if not (num % 3):
        if not (num % 5):
            return "FizzBuzz"
        return "Fizz"

    return None


print(fizz_buzz(15))

text = input("Enter text:\n")


def reverse_string(text):
    char_list = list(text)
    reversed_char_list = []
    for char in char_list:
        reversed_char_list.insert(0, char)
    reversed_string = "".join(reversed_char_list)

    return reversed_string


print(reverse_string(text))


PI = math.pi


def area_circum(radius):
    return (round(PI*(radius**2), 3), round(2*PI*radius, 3))


area, circumference = area_circum(6)
print(f"Area: {area}")
print(f"Circumference: {circumference}")


def get_name_email():
    name = input("Enter your name: ")
    while not name:
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not email:
        email = input("Enter your email: ")
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    while not (re.match(pat, email)):
        email = input("Enter a valid email: ")
    return (name, email)


name, email = get_name_email()
print(f"Name: {name}")
print(f"Email: {email}")


def occ_count(word, occ):
    return word.lower().count(occ)

print(occ_count("Hello ITI Hi iti Welcome ITI Greetings iti", "iti"))


def max_ordered(text):
    curr_substring = []
    max_substring = []
    for i, char in enumerate(text):
        if i >= len(text)-1:
            if curr_substring == max_substring:
                max_substring.append(char)
            return "".join(max_substring)
        if char < text[i+1]:
            curr_substring.append(char)
        else:
            if curr_substring == max_substring:
                max_substring.append(char)
            curr_substring = []
        if len(max_substring) < len(curr_substring):
            max_substring = curr_substring


print(max_ordered("abcdabcdefababcabcdefgh"))
