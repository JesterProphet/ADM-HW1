input_string = input()

lowercase_characters = sorted([character for character in input_string if character.islower()])
uppercase_characters = sorted([character for character in input_string if character.isupper()])
numbers = "".join(filter(str.isdigit, input_string))
odd_numbers = sorted([number for number in numbers if int(number) % 2 == 1])
even_numbers = sorted([number for number in numbers if int(number) % 2 == 0])

output_string = "".join(lowercase_characters + uppercase_characters + odd_numbers + even_numbers)

print(output_string)
