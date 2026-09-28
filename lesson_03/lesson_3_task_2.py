from smartphone import Smartphone

catalog = [Smartphone("iPhone", "17", "+79112223344"),
           Smartphone("Samsung", "S24", "+79223334455"),
           Smartphone("Nokia", "3310", "+79334445566"),
           Smartphone("Xiaomi", "20T", "+79445556677"),
           Smartphone("Honor", "15 Pro", "+79556667788")]

for smartphone in catalog:
    print(f"{smartphone.mark}, {smartphone.model}, {smartphone.number}")
