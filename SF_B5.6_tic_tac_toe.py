import random
import re


def who_is_first(answer):
    '''Функция для определения кто ходит первым'''
    global priority
    global user_xo
    global pc_xo
    variants = ['орел', 'решка']
    if answer not in variants:
        print('Неверный ответ! необходимо ввести орел или решка!')
        print('Запустите программу заново.')
        return False
    else:
        coin = random.choice(variants)
        if answer == coin:
            priority = True
            user_xo = 'x'
            pc_xo = 'o'
            print('Вы ходите первым')
            return True
        else:
            user_xo = 'o'
            pc_xo = 'x'
            priority = False
            print('Я хожу первым, поехали!')
            return True


def field_creator(field):
    '''Функция отрисовки игрового поля'''
    print('  0 1 2', end='')
    for i in range(3):
        print()
        print(i, end=' ')
        for j in range(3):
            print(field.get((i, j)), end=' ')


def pc_move(field, pc_xo):
    '''Функция реализующая ход ПК'''
    free_cells = [key for key in field.keys() if field[key] == '-']
    move = random.choice(free_cells)
    field[move] = pc_xo


def winning_cheker(field):
    '''Функция проверки победы'''
    if field[(0, 0)] == field[(0, 1)] == field[(0, 2)] and field[(0, 0)] != '-':
        return True
    elif field[(1, 0)] == field[(1, 1)] == field[(1, 2)] and field[(1, 0)] != '-':
        return True
    elif field[(2, 0)] == field[(2, 1)] == field[(2, 2)] and field[(2, 0)] != '-':
        return True
    elif field[(0, 0)] == field[(1, 0)] == field[(2, 0)] and field[(0, 0)] != '-':
        return True
    elif field[(0, 1)] == field[(1, 1)] == field[(2, 1)] and field[(0, 1)] != '-':
        return True
    elif field[(0, 2)] == field[(1, 2)] == field[(2, 2)] and field[(0, 2)] != '-':
        return True
    elif field[(0, 0)] == field[(1, 1)] == field[(2, 2)] and field[(0, 0)] != '-':
        return True
    elif field[(0, 2)] == field[(1, 1)] == field[(2, 0)] and field[(0, 2)] != '-':
        return True
    else:
        return False


def user_input_checker(user_data):
    free_cells = [key for key in field.keys() if field[key] == '-']
    user_data = tuple(map(int, user_data.split()))
    if user_data in free_cells:
        return True
    else:
        return False


def user_move():
    '''Функция контролирующая ход пользователя'''

    user_data = input('\nВведите адрес поля для совершения хода: сначала номер столбца, пробел, затем номер строки: ')
    while not (re.match(r'\d\s\d', user_data) and len(user_data) == 3) or not user_input_checker(user_data):
        print('\nОшибка ввода или поле уже занято!')
        user_data = input(
            'Введите адрес поля для совершения хода: сначала номер столбца, пробел, затем номер строки: ')
    user_data = tuple(map(int, user_data.split()))
    if priority:
        field[user_data] = 'x'
    else:
        field[user_data] = 'o'


priority = None
user_xo = None
pc_xo = None
field = {(0, 0): '-', (0, 1): '-', (0, 2): '-',
         (1, 0): '-', (1, 1): '-', (1, 2): '-',
         (2, 0): '-', (2, 1): '-', (2, 2): '-'}
winner = None

print('Добро пожаловать в игру крестики-нолики.')
print('С начала решим кто ходит первый, орел или решка?')
answer = input('Введите свой ответ: ')
if who_is_first(answer):
    for _ in range(4):
        if priority:
            field_creator(field)
            user_move()
            if winning_cheker(field):
                winner = True
                print('Вы выиграли.')
                break
            pc_move(field, pc_xo)
            print('Я сделал ход.')
            if winning_cheker(field):
                winner = True
                print('Вы проиграли.')
                break
        else:
            pc_move(field, pc_xo)
            print('Я сделал ход.')
            if winning_cheker(field):
                winner = True
                print('Вы проиграли.')
                break
            field_creator(field)
            user_move()
            if winning_cheker(field):
                winner = True
                print('Вы выиграли.')
                break
    if not winner:
        free_cells = [key for key in field.keys() if field[key] == '-']
        field[free_cells[0]] = 'x'
        if winning_cheker(field) and user_xo == 'x':
            print('Вы выиграли.')
        elif winning_cheker(field) and user_xo != 'x':
            print('Вы проиграли.')
        else:
            print('\nНичья!')
field_creator(field)
print('\nИгра завершена')
