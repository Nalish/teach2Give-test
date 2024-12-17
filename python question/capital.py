def capitalize_words(input_string):
    words = input_string.split()  
    capitalized_words = [word.capitalize() for word in words]
    result = " ".join(capitalized_words)
    return result

user_input = input("Enter a string: ")
result = capitalize_words(user_input)
print("Capitalized String:", result)
