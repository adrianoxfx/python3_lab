
def player_choose():
    while True:
        player1 = input("Player 1, escolha X ou O: ")
        if player1 not in jogadas_possiveis:
            print ("essa jogada não existe")
            pass
        else:
            break
    if player1 == jogadas_possiveis[0]:
        player2 = jogadas_possiveis[1]
        print("player2 joga com O")
    else:
        player2 = jogadas_possiveis[0]
        print("player2 joga com X")
    return [player1, player2]


def print_board(dict_result):
    print("   1    2   3")
    print("a   %s | %s | %s " %(dict_result["a1"],dict_result["a2"],dict_result["a3"]))
    print("   -----------")
    print("b   %s | %s | %s " %(dict_result["b1"],dict_result["b2"],dict_result["b3"]))
    print("   -----------")
    print("c   %s | %s | %s " %(dict_result["c1"],dict_result["c2"],dict_result["c3"]))


def ask_user(player):
    while True:
        coordenada = input("Player %s, use coordenadas para dizer sua jogada EX: a1, c3:  " %(player))
        if coordenada not in dict_result.keys():
            print ("essa coordenada não existe")
            pass
        else:
            break
    return coordenada


dict_result = {'a1':' ','a2':' ','a3':' ','b1':' ','b2':' ','b3':' ','c1':' ','c2':' ','c3':' '}
jogadas_possiveis = ["X","O"]
players = {'player1':'','player2':''}

players['player1'],players['player2'] = player_choose()


# while True:
#     print_board(dict_result)

#     resp = ask_user(player_choose[0])

#     dict_result[resp[0]] = resp[1]
