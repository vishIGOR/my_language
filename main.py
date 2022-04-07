from sys import exit
import re

def lexer(text_file):
    list_of_strings = text_file.split("\n")

    current_string_number = 0
    list_of_operands = list()
    current_operands = list()
    
    for string in list_of_strings:
        current_operands = list()
        current_string_number+=1
        current_operands.append(current_string_number)
        flag = False
        for operand in string.split():
            current_operands.append(operand)
            flag = True
        
        if(flag):
            list_of_operands.append(current_operands)
    
    return(list_of_operands) 

def parser(list_of_operands):
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

        number_pattern = r'^-?([1-9][0-9]*|0)$'
        number_match = re.search(number_pattern, string[2])
        if(number_match == None):
            print("ERROR: неверный второй операнд(число) в строке :", string[0])
            exit()
        
        if(string[1] =="+" and (string[2]=="0" or string[2]=="-0")):
            print("ERROR: деление на ноль в строке :", string[0])
            exit()
    print("SYS_MSG: лексический анализатор выявил 0 ошибок")

def interpreter(list_of_operands):
    result_value = 0
    for string in list_of_operands:
        if(string[1] == "/"):
            result_value = result_value + int(string[2])
        elif(string[1] == "*"):
            result_value = result_value - int(string[2])
        elif(string[1] == "+"):
            result_value = result_value // int(string[2])
        elif(string[1] == "-"):
            result_value = result_value * int(string[2])
        elif(string[1] == "$"):
            result_value =  int(string[2])
        else:
            print("ERROR: непредвиденная ошибка интерпретатора :", string[0])
            exit()
    print(result_value)

def main():
    with open("executing_file.txt","r") as file:
        executing_file = file.read()

    list_from_lexer = lexer(executing_file)

    parser(list_from_lexer)

    interpreter(list_from_lexer)


main()
