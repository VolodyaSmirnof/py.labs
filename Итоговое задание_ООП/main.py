if __name__ == "__main__":
    from typing import List


    class Животное:
        """
        Базовый класс, представляющий животное.

        Attributes:
            name (str): Имя животного.
            age (int): Возраст животного.
            _health (int): Защищенный атрибут, обозначающий здоровье животного (0-100).
                           Инкапсулирован, так как это критически важный параметр,
                           который должен изменяться только через специальные методы.
        """

        def __init__(self, name: str, age: int, health: int = 100) -> None:
            """
            Конструктор класса Животное.

            Args:
                name: Имя животного.
                age: Возраст животного.
                health: Здоровье животного (по умолчанию 100).
            """
            self.name = name
            self.age = age
            self._health = health

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта Животное.
            """
            return f"Животное: {self.name}, Возраст: {self.age}, Здоровье: {self._health}"

        def __repr__(self) -> str:
            """
            Возвращает строковое представление объекта Животное для отладки.
            """
            return f"Животное(name='{self.name}', age={self.age}, health={self._health})"

        def sound(self) -> str:
            """
            Возвращает звук, которое издает животное.
            """
            return "Общий звук животного"

        def eat(self, food: str) -> None:
            """
            Животное ест указанную еду.

            Args:
                food: Название еды.
            """
            print(f"{self.name} ест {food}.")

        def get_health(self) -> int:
            """
            Возвращает текущий уровень здоровья животного.
            """
            return self._health

        def set_health(self, new_health: int) -> None:
            """
            Устанавливает новый уровень здоровья животного.
            Обеспечивает контроль допустимого диапазона значений.

            Args:
                new_health: Новый уровень здоровья (0-100).
            """
            if 0 <= new_health <= 100:
                self._health = new_health
            else:
                print("Ошибка: Здоровье должно быть в диапазоне от 0 до 100.")


    class Собака(Животное):
        """
        Класс, представляющий собаку, наследник класса Животное.

        Attributes:
            breed (str): Порода собаки.
            tricks (List[str]): Список известных собаке трюков.
        """

        def __init__(self, name: str, age: int, breed: str, health: int = 100) -> None:
            """
            Конструктор класса Собака.  Расширяет конструктор базового класса Животное,
            добавляя атрибут породы.

            Args:
                name: Имя собаки.
                age: Возраст собаки.
                breed: Порода собаки.
                health: Здоровье собаки (по умолчанию 100).
            """
            super().__init__(name, age, health)  # Вызов конструктора базового класса
            self.breed = breed
            self.tricks: List[str] = []

        def __str__(self) -> str:
            """
            Перегруженный метод __str__.  Добавляет информацию о породе к строковому
            представлению собаки.
            """
            return f"Собака: {self.name}, Порода: {self.breed}, Возраст: {self.age}, Здоровье: {self._health}"

        def __repr__(self) -> str:
            """
            Перегруженный метод __repr__.  Добавляет информацию о породе к строковому
            представлению собаки для отладки.
            """
            return f"Собака(name='{self.name}', age={self.age}, breed='{self.breed}', health={self._health})"

        def sound(self) -> str:
            """
            Перегруженный метод sound.  Собака лает.
            Перегрузка: звук собаки специфичен и отличается от общего звука животного.
            """
            return "Гав!"

        def learn_trick(self, trick: str) -> None:
            """
            Обучает собаку новому трюку.

            Args:
                trick: Название трюка.
            """
            self.tricks.append(trick)
            print(f"{self.name} научилась трюку '{trick}'!")

        def display_tricks(self) -> None:
            """
            Отображает список известных собаке трюков.
            """
            if self.tricks:
                print(f"{self.name} знает следующие трюки: {', '.join(self.tricks)}")
            else:
                print(f"{self.name} пока не знает никаких трюков.")

        def fetch(self, item: str) -> None:
            """
            Собака приносит предмет.  Метод унаследован от базового класса.

            Args:
                item: Название предмета.
            """
            print(f"{self.name} (порода {self.breed}) приносит {item}!")


    # Пример использования
    animal = Животное("Общий питомец", 5)
    print(animal)  # Животное: Общий питомец, Возраст: 5, Здоровье: 100
    print(repr(animal))  # Животное(name='Общий питомец', age=5, health=100)
    print(animal.sound())  # Общий звук животного
    animal.eat("трава")  # Общий питомец ест трава.

    dog = Собака("Бобик", 3, "Дворняга")
    print(dog)  # Собака: Бобик, Порода: Дворняга, Возраст: 3, Здоровье: 100
    print(repr(dog))  # Собака(name='Бобик', age=3, breed='Дворняга', health=100)
    print(dog.sound())  # Гав!
    dog.eat("кость")  # Бобик ест кость.
    dog.learn_trick("сидеть")
    dog.learn_trick("лежать")
    dog.display_tricks()  # Бобик знает следующие трюки: сидеть, лежать
    dog.fetch("мячик")  # Бобик (порода Дворняга) приносит мячик!

    dog.set_health(50)
    print(dog.get_health())  # 50

    dog.set_health(150)  # Ошибка: Здоровье должно быть в диапазоне от 0 до 100.
    pass
