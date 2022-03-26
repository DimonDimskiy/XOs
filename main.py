from bot import easy_bot, normal_bot, hard_bot
from graphic import draw
from logic import end_game


def user_input(tab, flag):
    if flag == 1:
        char = 'X'
    else:
        char = '0'
    try:
        step = int(input(f'Игрок {flag} ({char}), введите номер свободной ячейки: '))
        if step in tab and tab[step] == 0:
            tab[step] = flag
        elif step not in tab:
            raise ValueError
        else:
            print(f'Ячейка {step} занята!')
            user_input(tab, flag)
    except ValueError:
        print('Такой ячейки нет на поле!')
        user_input(tab, flag)


def change_flag(flag):
    if flag == 1:
        return 2
    elif flag == 2:
        return 1


def game():
    test_tab = {i: 0 for i in range(1, 10)}
    flag = 1
    is_bot = False
    bot_mode = 3

    mode = str(input("Играть с ботом?(Y): "))
    match mode.lower():
        case "y":
            is_bot = True

    if is_bot:
        while True:
            try:
                bot_mode = int(input("Выберите уровень сложности:\n1.Низкий\n2.Нормальный\n3.Высокий\n: "))
                if 0 < bot_mode < 4:
                    print(f"Выбран уровень сложности {bot_mode}")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Введите уровень сложности, от 1 до 3:")

    draw(test_tab)
    while True:
        if is_bot:
            if bot_mode == 1:
                test_tab = easy_bot(test_tab, flag)
            elif bot_mode == 2:
                test_tab = normal_bot(test_tab, flag)
            else:
                test_tab = hard_bot(test_tab, flag)
            draw(test_tab)
            if end_game(test_tab, flag):
                break
            flag = change_flag(flag)

        user_input(test_tab, flag)
        draw(test_tab)
        if end_game(test_tab, flag):
            break
        flag = change_flag(flag)

    new_game = str(input("Еще партию?(Y): "))
    if new_game.lower() == "y":
        game()


game()
