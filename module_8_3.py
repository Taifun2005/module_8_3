class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message



class IncorrectCarNumbers(Exception):
    def __init__(self):
        self.message = message


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin_number):
        # проверяет его на корректность.
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber("Некорректный тип vin номер", )
        if 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber("Неверный диапазон для vin номера")
        return True

    def __is_valid_numbers(self, numbers):
        # проверяет его на корректность
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        if len(numbers) != 6:
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")
        return True


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
