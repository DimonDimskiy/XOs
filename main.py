from bot import easy_bot
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
    is_bot = True
    is_player = False

    mode = str(input("Играть с ботом?(Y/N): "))
    match mode.lower():
        case "y":
            is_bot = True
            is_player = True
        case "n":
            is_bot = False
            is_player = True

    draw(test_tab)
    while True:
        print(flag)
        if is_bot:
            test_tab = easy_bot(test_tab, flag)
            #print(test_tab, type(test_tab))
            draw(test_tab)
            if end_game(test_tab, flag):
                if not is_player:
                    print("Боты играли без человека:)")
                break
            flag = change_flag(flag)
        if is_player:
            user_input(test_tab, flag)
            draw(test_tab)
            if end_game(test_tab, flag):
                break
            flag = change_flag(flag)
    # new_game = str(input("Еще партию?(Y): "))
    # if new_game.lower() == "y":
    #     game()


game()
