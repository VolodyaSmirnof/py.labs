# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union
class Lamp:
    """
    Атрибуты:
        luminocity (int): Количество света, излучаемое лампой в еденицу времени
        temperature (int): цветовая температура
    """
    def _init_(self, luminocity: Union[int, float], temperature: Union[int, float]):
        if not isinstance(luminocity, (int, float)):
            raise TypeError("Этот параметр является числовым")
        if luminocity < 0:
            raise ValueError("Этот параметр может принимать только неотрицательные значения")
        self.luminocity = luminocity

        if not isinstance(temperature, (int, float)):
            raise TypeError("Этот параметр является числовым")
        if not temperature > 0:
            raise ValueError("Этот параметр может принимать только значения больше нуля")
        self.temperature = temperature
    def is_Lamp_on(self):
        ...
    """
    Функция, которая определяет, включена ли лампа исходя из значения luminocity
    :return Является ли лампа включенной
    
    Пример:
    >>>lamp = Lamp (0, 4000)
    >>>lamp.is_Lamp_on()
    """
    def Lamp_color(self):
        ...
    """
    Функця, которая определяет цвет лампы, теплый или холодный
    :return: Цвет лампы
    
    Пример:
    >>>lamp = Lamp (0, 4000)
    >>>lamp.Lamp_color()
    """



class Tree:
        """
        Класс "Дерево".
        Атрибуты:
            species (str): Вид дерева (например, "дуб", "клён").
            height (float): Высота дерева в метрах.
            age (int): Возраст дерева в годах.
        """

        def __init__(self, species: str, height: float, age: int):

            if height < 0:
                raise ValueError("Высота должна быть неотрицательным значением")
            if age < 0:
                raise ValueError("Возраст должен быть неотрицательным значением")

            self.species = species
            self.height = height
            self.age = age

        def grow(self, meters: float) -> None:
            """
            Моделирует рост дерева, увеличивая его высоту.
             Пример:
                 >>> t = Tree("сосна", 5.0, 10)
                 >>> t.grow(2)
                 Дерево выросло на 2,0 метра
             """
            if meters < 0:
                raise ValueError("Рост должен быть неотрицательным значением")

            self.height += meters
            print(f"Дерево выросло на {meters} метра")

        def get_age(self) -> int:
            """
             Возвращает возраст дерева.
             Пример:
                >>> t = Tree("берёза", 8.0, 25)
                >>> t.get_age()
                25
            """
            return self.age
    def display_tree_info(self) -> str:
        """
        Возвращает строку, описывающую дерево и его атрибуты.
        Example:
           >>> t = Tree("дуб", 12.3, 75)
           >>> t.display_tree_info()
           'Дерево - дуб, его высота 12.3 метра, возраст 75 лет.'
        """
        return f"Дерево - {self.species}, его высота {self.height} метров, возраст {self.age} лет."
class Pencil:
    def __init__(self, length: Union[int, float], sharpness: bool):
        """
        Класс: карандаш
        Атрибуты:
            length: длина карандаша в сантиметрах
            sharpness: заточен ли карандаш
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Этот параметр является числовым")
        if not length > 0:
            raise ValueError("Значение этого параметра должно быть больше нуля")

        if not isinstance(sharpness, bool)
            raise TypeError("Значение этого параметра может принимать только значения типа true и false")
        self.length = length
        self.sharpness = sharpness

    def Life_expect(self):
        ...
    """
    Исходя из длины карандаша, описывает, сколько страниц формата А4 можно будет исписать этим карандашом
    Пример: 
    >>> pencil = Pencil (10, True)
    >>> pencil.Life_expect("Этим карандашом можно будет исписать", page_expect, "страниц формата А4")
    """
    def Status(self):
        ...
    """
    Выводит на экран параметры выбранного карандаша
    Пример:
    >>>pencil = Pencil (10, True)
    >>>pencil.Status("Длина карандаша -", length, "Карандаш", Is_sharp)
    """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
