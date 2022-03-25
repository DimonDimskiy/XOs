def draw(gtab):
    tab = gtab.copy()
    for i in tab:
        if tab[i] == 0:
            tab[i] = " "
        elif tab[i] == 1:
            tab[i] = "X"
        elif tab[i] == 2:
            tab[i] = "0"
        else:
            print("InvalidInput")
            return
    print('1    |2    |3    ')
    print(f'  {tab[1]}  |  {tab[2]}  |  {tab[3]}')
    print('_____|_____|_____')
    print('4    |5    |6    ')
    print(f'  {tab[4]}  |  {tab[5]}  |  {tab[6]}')
    print('_____|_____|_____')
    print('7    |8    |9    ')
    print(f'  {tab[7]}  |  {tab[8]}  |  {tab[9]}')
    print('     |     |     ')
