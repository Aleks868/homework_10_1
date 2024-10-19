import pytest

from src.widget import mask_accaunt_card, get_date

@pytest.mark.parametrize(
    "value, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет *4305"),
    ],
)


def test_mask_accaunt_card(value: str, expected_result: str) -> None:
    assert mask_accaunt_card(value) == expected_result


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"