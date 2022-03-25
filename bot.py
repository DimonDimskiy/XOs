import random


def easy_bot(tab, flag):
    tab = tab.copy()
    bot_step = random.choice(range(1, 10))
    if bot_step in tab and tab[bot_step] == 0:
        tab[bot_step] = flag
        return tab
    else:
        return easy_bot(tab, flag)
