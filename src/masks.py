user_card_number = input()
user_account_number = input()


def get_mask_card_number(user_card_number: str) -> str:
    """Функция, скрывающая номер карты"""
    return f"{user_card_number[:4]} {user_card_number[4:6]}** **** {user_card_number[12:]}"


def get_mask_account(user_account_number: str) -> str:
    """Фкнуция, скрывающая номер счета"""
    return f"*{user_account_number[-4:]}"


print(get_mask_card_number(user_card_number))
print(get_mask_account(user_account_number))
