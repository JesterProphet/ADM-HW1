import re


n = int(input())

for _ in range(0, n):

    card_number = input()

    valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
    check = "Invalid"

    if len(card_number) in [16, 19]:
        cleaned_card_number = "".join([number for number in card_number if number in valid_characters])
        if cleaned_card_number.startswith(("4", "5", "6")):
            if len(re.findall('[0-9]', cleaned_card_number)) == 16:
                if cleaned_card_number.count("-") == 3:
                    if len(cleaned_card_number.split("-")) == 4:
                        if len([number_seq for number_seq in cleaned_card_number.split("-") if len(number_seq) == 4]) == 4:
                            cleaned_card_number = cleaned_card_number.replace("-", "")
                            if not re.findall(r'(.)\1{3}', cleaned_card_number):
                                check = "Valid"
                else:
                    if not re.findall(r'(.)\1{3}', cleaned_card_number):
                        check = "Valid"

    print(check)

