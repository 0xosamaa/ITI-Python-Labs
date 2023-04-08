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

def reverse(inputs):
    inputs.sort(reverse=True)
    return inputs

print(reverse())

def fizz_buzz(num):
    if not(num % 5):
        if not(num % 3):
            return "FizzBuzz"
        return "Buzz"
    
    if not(num % 3):
        if not(num % 5):
            return "FizzBuzz"
        return "Fizz"
    
    return None

print(fizz_buzz(15))

