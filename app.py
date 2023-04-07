def vowels_count(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count += 1
    return count

print(vowels_count("The quick brown for jumps over the lazy dog."))