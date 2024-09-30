from src.masks import get_mask_account, get_mask_card_number

user_card = input("Введите номер карты/счета")
date_str = input("Введите дату")


def mask_accaunt_card(user_card: str) -> str:
    """Функция маскирующая счет/карту"""
    if "Счет" in user_card:
        mask_acc_number = f"{user_card[:4]} {get_mask_account(user_card[5:])}"
        return mask_acc_number
    else:
        mask_card_num = f"{user_card[:-15]} {get_mask_card_number(user_card[-16:])}"
        return mask_card_num

print(mask_accaunt_card(user_card))


def get_date(date_str: str) -> str:
    """Функция изменения формата даты"""
    date_slice = date_str[0:10].split("-")
    return ".".join(date_slice[::-1])

print(get_date(date_str))