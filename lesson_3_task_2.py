from smartphone import Smartphone

catalog = [Smartphone("iPhone", "17", "+79112223344"),
           Smartphone("Samsung", "S24", "+79223334455"),
           Smartphone("Nokia", "3310", "+79334445566")]

for smartphone in catalog:
    print(f"{smartphone.mark}, {smartphone.model}, {smartphone.number}")
