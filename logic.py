def _is_win(tab):
    row1 = tab[1] == tab[2] == tab[3] != 0
    row2 = tab[4] == tab[5] == tab[6] != 0
    row3 = tab[7] == tab[8] == tab[9] != 0

    col1 = tab[1] == tab[4] == tab[7] != 0
    col2 = tab[2] == tab[5] == tab[8] != 0
    col3 = tab[3] == tab[6] == tab[9] != 0

    slash = tab[3] == tab[5] == tab[7] != 0
    backslash = tab[1] == tab[5] == tab[9] != 0

    return row1 or row2 or row3 or col1 or col2 or col3 or slash or backslash


def _is_draw(tab):
    set_row1 = {tab[1], tab[2], tab[3]} - {0}
    set_row2 = {tab[4], tab[5], tab[6]} - {0}
    set_row3 = {tab[7], tab[8], tab[9]} - {0}

    set_col1 = {tab[1], tab[4], tab[7]} - {0}
    set_col2 = {tab[2], tab[5], tab[8]} - {0}
    set_col3 = {tab[3], tab[6], tab[9]} - {0}

    set_slash = {tab[3], tab[5], tab[7]} - {0}
    set_backslash = {tab[1], tab[5], tab[9]} - {0}

    set_list = [set_row1, set_row2, set_row3, set_col1, set_col2, set_col3, set_slash, set_backslash]

    length_list = list(map(len, set_list))

    return not (0 in length_list or 1 in length_list)


def end_game(tab, flag):
    if _is_win(tab):
        print(f'Победил игрок {flag}!')
    if _is_draw(tab):
        print("Победила дружба!")
    return _is_draw(tab) or _is_win(tab)