# Przywitanie gracza

print('Kółko i Krzyżyk\n\n')
input('Witamy w grze kółko i krzyżyk. Aby rozpocząć naciśnij klawisz Enter.')


# Stworzenie planszy i wytlumaczenie zasad

print("""
            7 | 8 | 9
            ---------
            4 | 5 | 6
            ---------
            1 | 2 | 3
            
            """)
input('Oto plansza do gry. Poszczególne cyfry reprezentują miejsca w jakie wprowadzony zostanie symbol po ich naciśnięciu.\n'
      'Gracz pierwszy gra symbolem "X", a gracz drugi symbolem "O"\n'
      'Aby rozpocząć naciśnij dowolny klawisz.')


# Funkcja sprawdzania wygranych

def win_check(win):
    count = 0
    win_possibilities = [[7,4,1], [8,5,2], [9,6,3],
                         [1,2,3], [4,5,6], [7,8,9],
                         [7,5,3], [9,5,1]]
    for n in win_possibilities:
        for x in n:
            if x in win:
                count += 1
        if count == 3:
            return True
        else:
            count = 0
    return False


# Rdzeń gry

def game_start():
    nr = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}
    plansza = f"""
                  Plansza Główna                            Klawiszologia
    
                    {nr[7]} | {nr[8]} | {nr[9]}                                 7 | 8 | 9    
                    ---------                                 ---------
                    {nr[4]} | {nr[5]} | {nr[6]}                                 4 | 5 | 6
                    ---------                                 ---------
                    {nr[1]} | {nr[2]} | {nr[3]}                                 1 | 2 | 3   """
    print(plansza)
    game_on = True
    win = False
    count = 0
    used_numbers = []
    x_nr = []
    o_nr = []
    
    while game_on:

        # Gracz 1
        x = int(input('\nGracz 1: Wybierz miejsce postawienia swojego symbolu(numery od 1 do 9): '))
        while x not in range(1, 10):
            print('\nNiedozwolony znak. Wybierz numer od 1 do 9!')
            x = int(input('Gracz 1: Wybierz miejsce postawienia swojego symbolu(numery od 1 do 9): '))
        while x in used_numbers:
            print('\nMiejsce już zajęte. Wybierz inne pole!')
            x = int(input('\nGracz 1: Wybierz miejsce postawienia swojego symbolu(numery od 1 do 9): '))
        used_numbers.append(x)
        x_nr.append(x)

        nr[x] = 'X'
        plansza = f"""
                          Plansza Główna                            Klawiszologia

                            {nr[7]} | {nr[8]} | {nr[9]}                                 7 | 8 | 9    
                            ---------                                 ---------
                            {nr[4]} | {nr[5]} | {nr[6]}                                 4 | 5 | 6
                            ---------                                 ---------
                            {nr[1]} | {nr[2]} | {nr[3]}                                 1 | 2 | 3   """
        print(plansza)
        if win_check(win=x_nr):
            print('Gracz 1 WYGRYWA!!!!')
            win = True
            game_on = False
        count += 1

        if count == 9:
            game_on = False

        # Gracz 2
        if game_on == True:
            o = int(input('\nGracz 2: Wybierz miejsce postawienia swojego symbolu: '))
            while o not in range(1, 10):
                print('\nNiedozwolony znak. Wybierz numer od 1 do 9!')
                o = int(input('Gracz 1: Wybierz miejsce postawienia swojego symbolu(numery od 1 do 9): '))
            while o in used_numbers:
                print('\nMiejsce już zajęte. Wybierz inne pole!')
                o = int(input('Gracz 1: Wybierz miejsce postawienia swojego symbolu(numery od 1 do 9): '))
            used_numbers.append(o)
            o_nr.append(o)
            nr[o] = 'O'

            plansza = f"""
                              Plansza Główna                            Klawiszologia

                                {nr[7]} | {nr[8]} | {nr[9]}                                 7 | 8 | 9    
                                ---------                                 ---------
                                {nr[4]} | {nr[5]} | {nr[6]}                                 4 | 5 | 6
                                ---------                                 ---------
                                {nr[1]} | {nr[2]} | {nr[3]}                                 1 | 2 | 3   """
            print(plansza)
            if win_check(win=o_nr):
                print('Gracz 2 WYGRYWA!!')
                win = True
                game_on = False
                
            count += 1

        if count == 9:
            game_on = False

    if win == False:
        print('\nRemis!!')


# Czy gracz chce zagrać jeszcze raz
    try_again = True
    while try_again:
        repeat = input('\nCzy chcesz zagrać jeszcze raz? T/N?: ')
        if repeat.lower() == 't':
            game_start()
        elif repeat.lower() == 'n':
            return '\n\nDziękujemy za grę :))'
        else:
            print('\nBłędna komenda. Spróbuj jeszcze raz.')

game_start()

input('\n\nAby zakończyć program wciśnij dowolny klawisz.')




