from src.masks import get_mask_account, get_mask_card_number

user_card_number = input("Введите номер карты")
user_account_number = input("Введите номер счета")


print(get_mask_card_number(user_card_number))
print(get_mask_account(user_account_number))
