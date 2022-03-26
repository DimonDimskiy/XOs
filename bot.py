import random


def easy_bot(etab, flag):
    tab = etab.copy()
    bot_step = random.choice(range(1, 10))
    if bot_step in tab and tab[bot_step] == 0:
        tab[bot_step] = flag
        return tab
    else:
        return easy_bot(tab, flag)


def normal_bot(ntab, flag):

    def switch_zero(*args):
        list_ = []
        for arg in args:
            if arg == 0:
                list_.append(flag)
            else:
                list_.append(arg)
        return list_

    flags = (flag, flag, flag)
    tab = ntab.copy()

    row1 = [tab[1], tab[2], tab[3]]
    row2 = [tab[4], tab[5], tab[6]]
    row3 = [tab[7], tab[8], tab[9]]

    col1 = [tab[1], tab[4], tab[7]]
    col2 = [tab[2], tab[5], tab[8]]
    col3 = [tab[3], tab[6], tab[9]]

    slash = [tab[3], tab[5], tab[7]]
    backslash = [tab[1], tab[5], tab[9]]

    if row1.count(flag) == 2 and row1.count(0) == 1:
        tab[1], tab[2], tab[3] = flags
        return tab
    elif row2.count(flag) == 2 and row2.count(0) == 1:
        tab[4], tab[5], tab[6] = flags
        return tab
    elif row3.count(flag) == 2 and row3.count(0) == 1:
        tab[7], tab[8], tab[9] = flags
        return tab
    elif col1.count(flag) == 2 and col1.count(0) == 1:
        tab[1], tab[4], tab[7] = flags
        return tab
    elif col2.count(flag) == 2 and col2.count(0) == 1:
        tab[2], tab[5], tab[8] = flags
        return tab
    elif col3.count(flag) == 2 and col3.count(0) == 1:
        tab[3], tab[6], tab[9] = flags
        return tab
    elif slash.count(flag) == 2 and slash.count(0) == 1:
        tab[3], tab[5], tab[7] = flags
        return tab
    elif backslash.count(flag) == 2 and backslash.count(0) == 1:
        tab[1], tab[5], tab[9] = flags
        return tab
    elif row1.count(3 - flag) == 2 and row1.count(0) == 1:
        tab[1], tab[2], tab[3] = switch_zero(tab[1], tab[2], tab[3])
        return tab
    elif row2.count(3 - flag) == 2 and row2.count(0) == 1:
        tab[4], tab[5], tab[6] = switch_zero(tab[4], tab[5], tab[6])
        return tab
    elif row3.count(3 - flag) == 2 and row3.count(0) == 1:
        tab[7], tab[8], tab[9] = switch_zero(tab[7], tab[8], tab[9])
        return tab
    elif col1.count(3 - flag) == 2 and col1.count(0) == 1:
        tab[1], tab[4], tab[7] = switch_zero(tab[1], tab[4], tab[7])
        return tab
    elif col2.count(3 - flag) == 2 and col2.count(0) == 1:
        tab[2], tab[5], tab[8] = switch_zero(tab[2], tab[5], tab[8])
        return tab
    elif col3.count(3 - flag) == 2 and col3.count(0) == 1:
        tab[3], tab[6], tab[9] = switch_zero(tab[3], tab[6], tab[9])
        return tab
    elif slash.count(3 - flag) == 2 and slash.count(0) == 1:
        tab[3], tab[5], tab[7] = switch_zero(tab[3], tab[5], tab[7])
        return tab
    elif backslash.count(3 - flag) == 2 and backslash.count(0) == 1:
        tab[1], tab[5], tab[9] = switch_zero(tab[1], tab[5], tab[9])
        return tab
    else:
        return easy_bot(tab, flag)


def hard_bot(itab, flag):
    tab = itab.copy()
    if tab[5] == 0:
        tab[5] = flag
        return tab
    else:
        return normal_bot(tab, flag)
