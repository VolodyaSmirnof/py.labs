# TODO Напишите функцию find_common_participants
def find_common_participants (first_group, second_group, arg = ","):
    first_group = first_group.split(arg)
    second_group = second_group.split(arg)
    inter = list(set(first_group).intersection(second_group))
    inter.sort()
    return inter

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print (find_common_participants(participants_first_group, participants_second_group, '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
