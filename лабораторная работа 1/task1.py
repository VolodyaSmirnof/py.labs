numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers.remove(None)
numbers.insert(4, sum(numbers)/(1+len(numbers)))
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:", numbers)
