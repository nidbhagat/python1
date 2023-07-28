def count_alphabet_frequency(word):
    # Initialize an empty dictionary
    frequency_dict = {}
  
    for char in word:
        if char.isalpha():
            char_lower = char.lower()
            # Update the frequency in the dictionary
            frequency_dict[char_lower] = frequency_dict.get(char_lower, 0) + 1

    return frequency_dict

word = "Hello, World!"
result = count_alphabet_frequency(word)
print(result)
