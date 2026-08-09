def verify_card_number(card_digits):
    all_digits = card_digits.replace(' ', '').replace('-', '')

    check_digit = all_digits[-1]
    digits = all_digits[:len(all_digits) - 1]

    digits = digits[::-1]

    digits_list = []
    digits_list.append(int(check_digit))

    for index in range(len(digits)):
        if index % 2 != 1:
            if int(digits[index]) * 2 > 9:
                digits_list.append((int(digits[index]) * 2) - 9)
            else:
                digits_list.append(int(digits[index])* 2)

        else:
            digits_list.append(int(digits[index]))

    if sum(digits_list) % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"