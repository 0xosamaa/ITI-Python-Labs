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

def user_inputs():
    inputs = []
    for i in range(5):
        inputs.append(input(f"Enter element number {i+1}:\n"))
    inputs.sort(reverse=True)
    print(inputs)

user_inputs()