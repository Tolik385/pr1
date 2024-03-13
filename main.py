import pickle
from multipledispatch import dispatch
from typing import NamedTuple
from dataclasses import dataclass


class MyPharmacy:
    """Pharmacy on Voronina Street"""

    def __init__(self, healer, buyer, seller, recipe, sale):
        self.healer = healer
        self.buyer = buyer
        self.seller = seller
        self.recipe = recipe
        self.sale = sale

    def __add__(self, purchase):
        return self.recipe + self.buyer

    def get_info(self):
        return self.healer, self.buyer, self.seller, self.recipe, self.sale


class Healerr:
    """Tablets/syrups/dispensers sold by prescription"""

    def __init__(self, name, tip, vid, zena):
        self.name = name
        self.tip = tip
        self.vid = vid
        self.zena = zena

    def add(self, product_price):
        return self.name + product_price

    def get_info(self):
        return self.name, self.tip, self.vid, self.zena


"""Lab 3 lambda"""

# Создание Counter
from collections import Counter

my_healer = ['parazetomol30', 'parazetomol30', 'parazetomol30', 'parazetomol15', 'parazetomol15']
my_counter = Counter(my_healer)

print(my_counter)
print(my_counter['parazetomol30'])
print(my_counter['parazetomol15'])

# Создание deque
from collections import deque
my_deque = deque()
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

print(my_deque.Healerr())
print(my_deque)

class HealerDB:
    def __init__(self, name, tip, vid, zena):
        self.name = name
        self.tip = tip
        self.vid = vid
        self.zena = zena

    def add_name(self, name):
        if len(self.name) < 3:
            new_name = {'цена препарата - ': len(self.name) + 1, 'имя препарата - ': name}
            self.name.append(new_name)
        else:
            print("Вы не можете добавить более 3 препаратов")

    def delete_zena(self, zena):
        if self.name:
            self.name = [name for name in self.name if name['цена препарата - '] != zena]
        else:
            print("Препараты отсутствуют")

    def change_tip(self, zena, tip):
        for name in self.name:
            if name['цена препарата - '] == zena:
                name['тип препарата - '] = tip
                break
        else:
            print("Препарат с указанной ценой не найден")

class Healer0:
    def __init__(self):
        self.heller_database = HealerDB()
        self.heller_database.add_name('Тетрабонат')

    def printDB(self):
        if self.heller_database.name:
            for name in self.heller_database.name:
                print(f'имя препарата - {name["имя препарата - "]}\nимя препарата - {name["имя препарата - "]}\n')
        else:
            print("Список препаратов пуст")

    def run(self):
        choice = 0
        choices = {
            1: lambda: self.printDB(),
            2: lambda: self.heller_database.delete_zena(input('цена препарата - ')),
            3: lambda: self.heller_database.add_name(int(input('название препарата - '))),
            4: lambda: self.heller_database.change_tip(int(input('тип препарата - ')),
                                                       input('новое имя препарата - ')),
            5: lambda: None
        }

        while choice != 5:
            print("-------------------------------------------------")
            print('1. показать список препаратов')
            print('2. добавить препарат')
            print('3. удалить препарат')
            print('4. поменять имя препарата')
            print('5. выход из программы')
            print("-------------------------------------------------")
            choice = int(input("Выбор: "))

            if choice in choices:
                choices[choice]()


class Buyer:
    """The buyer comes with a recipe"""

    def __init__(self, familia, name2, otchestvo, adres, xorod, telefon):
        self.familia = familia
        self.name2 = name2
        self.otchestvo = otchestvo
        self.adres = adres
        self.xorod = xorod
        self.telefon = telefon

    def __add__(self, full_name):
        return self.familia + self.name2 + self.otchestvo

    def get_info(self):
        return self.familia, self.name2, self.otchestvo, self.adres, self.xorod, self.telefon


class Seller:
    """The seller fills all the medications"""

    def __init__(self, familia2, name3, otchestvo, postyp, dr, obrazov):
        self.familia2 = familia2
        self.name3 = name3
        self.otchestvo = otchestvo
        self.postyp = postyp
        self.dr = dr
        self.obrazov = obrazov

    def __add__(self, full_name2):
        return self.familia2 + self.name3 + self.otchestvo

    def get_info(self):
        return self.familia2, self.name3, self.otchestvo, self.postyp, self.dr, self.obrazov


class Recipe:
    """Recipe provided by customer"""

    def __init__(self, nomer, dvidachi, fiobolnogo, fiovracha, diagnoz):
        self.nomer = nomer
        self.dvidachi = dvidachi
        self.fiobolnogo = fiobolnogo
        self.fiovracha = fiovracha
        self.diagnoz = diagnoz

    def __add__(self, buyer_full_name):
        return self.nomer + self.fiobolnogo

    def get_info(self):
        return self.nomer, self.dvidachi, self.fiobolnogo, self.fiovracha, self.diagnoz


class Sale:
    """Purchases are made upon presentation of a prescription"""

    def __init__(self, data, lekarstvo, koliches, rezept1, prodav1):
        self.data = data
        self.lekarstvo = lekarstvo
        self.koliches = koliches
        self.rezept1 = rezept1
        self.prodav1 = prodav1

    def __add__(self, date_medicine):
        return self.data + self.lekarstvo

    # декаратор
    def data(my_func):
        def wrapper(self, *args, **kwargs):
            my_func(self, *args, **kwargs)
            global counter
            counter += 1
            print('Дата выдачи', self.data)
            print(f'Количество запросов: {counter}')

        return wrapper

    # Создание defaultdict
    from collections import defaultdict
    my_sale = defaultdict(list)
    my_sale["sale1"].append(1)
    my_sale["sale2"].append(2)
    print(my_sale["sale1"])
    print(my_sale["sale2"])
    print(my_sale["sale3"])

    @data
    def ff(self):
        pass

        def get_info(self):
            return self.data, self.lekarstvo, self.koliches, self.rezept1, self.prodav1

    def get_info(self):
        return self.data, self.lekarstvo, self.koliches, self.rezept1, self.prodav1


class Buyer1:
    def __init__(self, familia, name2):
        self.familia = familia
        self.name2 = name2


class BuyerOperation(HealerDB):
    def __init__(self, name=None, tip=None, name2=None, familia=None):
        super(BuyerOperation, self).__init__(name, tip, 'vid', 'zena')
        self.buyer1 = Buyer1(familia, name2)
        self.name = name

    def __str__(self):
        return 'name: {0}, tip: {1}, name2: {2}, familia: {3}'.format(self.name, self.tip, self.buyer1.name2,
                                                                      self.buyer1.familia)


class Pharmacy:
    @dispatch(str, int)
    def add_medicine(self, name, quantity):
        print("is added {name} medicine; quantity - {quantity}")

    @dispatch(str, int, str, int)
    def add_medicine(self, name, quantity, instructions, production_date):
        print(
            'medicine added - {name} ; quantity - {quantity} ; instructions - {instructions} ; date of manufacture - {production_date}')

    @dispatch(str)
    def add_medicine(self, name):
        print('medicine taken - {name}')


# интерфейс
from abc import ABC, abstractmethod


class Change(ABC):
    def description(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Shifts(Change):
    def __init__(self, time, change_name, number_sales):
        self.time = time
        self.change_name = change_name
        self.number_sales = number_sales

    def description(self):
        print("Смена")

    def stop(self):
        print("Смена окончена")

    def get_info(self):
        return f'Начало смены в {self.time}, Число продаж - {self.number_sales}.'


scenes1 = Shifts('7:00', 'Ivan', 12)
print(scenes1.get_info())
scenes1.stop()


class SizeBox(NamedTuple):
    height: float
    width: float
    length: float


def get_sized() -> SizeBox:
    """Логика, позволяющая получить размеры ящиков для препаратов"""
    return SizeBox(10, 15, 15)


size_box = get_sized()
print(f"Высота: {size_box.height}")
print(f"Ширина: {size_box.width}")
print(f"Длина: {size_box.length}")


class SizeBox1(NamedTuple):
    height: float
    width: float
    length: float


s = SizeBox1(height=10, width=15, length=15)
print(s.length)


@dataclass
class SizeBoxDataclass:
    height: float
    width: float
    length: float

    def get_sized_dataclass(self):
        return SizeBoxDataclass(10, 15, 15)

    # Деструктор
    def __del__(self):
        print(f'Экземпляр класса был удален')

    # Сериализация
    def serialize(self, name):
        with open(name, 'wb') as f:
            pickle.dump(self, f)

    # Десериализация
    @staticmethod
    def deserialize(name):
        with open(name, 'rb') as f:
            return pickle.load(f)



class Boxes(HealerDB):
    def __init__(self, name, tip, vid, zena, quantity_boxes, box_number, seller_name):
        super().__init__(name, tip, vid, zena)
        self.quantity_boxes = quantity_boxes
        self.box_number = box_number
        self.seller_name = seller_name

    def Name_title(self):
        print(f'Имя упаковщика коробки: {self.seller_name}')

    def Vistup(self):
        y = (self.quantity_boxes * 2) - 1
        print(f'Количество ящиков: {self.quantity_boxes}')

    def Drugs(self):
        print(f'Всего препаратов: {self.quantity_boxes}')

    def Name_title(self):
        print(f'Имя упаковщика коробки: {self.seller_name}')

    def Vistup(self):
        y = (self.quantity_boxes * 2) - 1
        print(f'Количество ящиков: {self.quantity_boxes}')


if __name__ == '__main__':
    drug_2 = Boxes("Название препарата", "Тип препарата", "Вид препарата", 100, 10, 5, "Имя упаковщика")
    drug_2.Name_title()

if __name__ == '__main__':
    # Создаем экземпляр класса
    drug_1 = SizeBoxDataclass(5, 7, 9)

    # Сериализуем объект drug_1 в файл 'drug_1.pickle'
    drug_1.serialize('drug_1.pickle')

    # Десериализуем объект из файла 'drug_1.pickle' и выводим его атрибуты
    deserialized_drug_1 = SizeBoxDataclass.deserialize('drug_1.pickle')
    print(deserialized_drug_1)


if __name__ == '__main__':
    pharmacyK = MyPharmacy('parazetomol', 'Petr', 'Ivan', 'nomer 123', '12 aprela')
    print(pharmacyK.get_info())

    buyer1 = Buyer('Ivanov', 'Ivan', 'Ivanovich', 'address', 'xorod', 'telephone')
    print(buyer1.get_info())

    seller1 = Seller('Petrov', 'Petr', 'Petrovich', 'postyp', 'dr', 'obrazov')
    print(seller1.get_info())

    recipe1 = Recipe('nomer', 'dvidachi', 'fiobolnogo', 'fiovracha', 'diagnoz')
    print(recipe1.get_info())

    sale1 = Sale('data', 'lekarstvo', 'koliches', 'rezept1', 'prodav1')
    print(sale1.get_info())

    buyer_operation = BuyerOperation('name', 'tip', 'name2', 'familia')
    print(buyer_operation)

    pharmacy_operation = Pharmacy()
    pharmacy_operation.add_medicine('medicine')
    pharmacy_operation.add_medicine('medicine', 10)
    pharmacy_operation.add_medicine('medicine', 10, 'instructions', 2022)

    box = Boxes("Название", "Совет", "Вид", "Цена", 10, 5, "Продавец")
    box.Name_title()
    box.Vistup()

