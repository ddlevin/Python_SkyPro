from adress import Adress
from mailing import Mailing

to_address = Adress("123456", "Moscow", "Lenina", "15", "42")
from_address = Adress("654321", "St.Petersburg", "Nevskiy", "10", "7")

mailing = Mailing(to_address, from_address, 1350, "TRACK123456789")


print(
    f"Отправление {mailing.track} из {mailing.from_adress} в "
    f"{mailing.to_adress}. Стоимость {mailing.cost} рублей."
)
