from sys import exit
import re

# if("-2147480" < "-2147482"):
#     print(True)
# else:
#     print(False)

# pattern = r'^-?[0-9]+$'
# some_string = "0"
# match = re.search(pattern, some_string)
# if (match == None):
#     print("not found")
# else:
#     print(match[0])

test_list = list()

test_row = list()
test_row.append(1)
test_row.append("+")
test_row.append("-2")
test_list.append(test_row)


def lexical_analyzer(list_of_operands):
    for string in list_of_operands:
        if(len(string) < 3):
            print(
                "ERROR: неверное количество операндов(меньше двух) в строке :", string[0])
            exit()
        if(len(string) > 3):
            print(
                "ERROR: неверное количество операндов(больше двух) в строке :", string[0])
            exit()

        operation_pattern = r'^[/*+$-]$'
        operation_match = re.search(operation_pattern, string[1])
        if(operation_match == None):
            print("ERROR: неверный первый операнд(действие) в строке :", string[0])
            exit()

        number_pattern = r'^-?[1-9][0-9]*$'
        number_match = re.search(number_pattern, string[2])
        if(number_match == None):
            print("ERROR: неверный второй операнд(число) в строке :", string[0])
            exit()


lexical_analyzer(test_list)

print("all is ok")