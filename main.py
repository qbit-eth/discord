import raffle


def first_raffle():
    raffle_list = [entry for entry in raffle.WINNERS[10:]]
    sage_raffle_list = [entry for entry in raffle.WINNERS[:10] if entry[1] == 1]
    already_sage = [entry for entry in raffle.WINNERS[:10] if entry[1] == 2]

    print("\nRIDDLE #2 SOLVER RAFFLE")
    winners = raffle.Raffle.choose_winner(25, raffle_list, True)

    for winner in winners:
        if winner[1] == 1:
            sage_raffle_list.append(winner)
        elif winner[1] == 2:
            already_sage.append(winner)

    print("\nRAFFLE FOR SAGE")
    sage_winner = raffle.Raffle.choose_winner(1, sage_raffle_list)
    print(" - The lucky winner for Sage role is {}!".format(sage_winner[0][0]))

    print("\nWINNERS THAT ARE ALREADY SAGES")
    for i, winner in enumerate(already_sage):
        print(" {}. {}".format(i + 1, winner[0]))


def second_raffle():
    print("\nRIDDLE #2 SOLVER RAFFLE FOR 3/6 SOLVERS")
    raffle.Raffle.choose_winner(11, raffle.MARCH_SIXTH_WINNERS, True)


def riddle_three_raffle():
    ip_winners = []
    sage_winners = []
    for name, raffle_list in [('ICHIRO', raffle.ICHIRO_WINNERS),
                                ('JIRO', raffle.JIRO_WINNERS),
                                ('SABURO', raffle.SABURO_WINNERS),
                                ('DRAWER', raffle.DRAWER_WINNERS)]:

        print('\nRIDDLE #3 SOLVER RAFFLE FOR {}'.format(name))

        winners = raffle.Raffle.choose_winner(7, raffle_list, True)

        already_sage = []
        sage_raffle_list = []

        for winner in winners:
            if winner[1] == 0:
                if winner[0] in ip_winners:
                    if winner[0] in sage_winners:
                        already_sage.append(winner)
                    else:
                        sage_raffle_list.append(winner)
                else:
                    ip_winners.append(winner[0])
            if winner[1] == 1:
                if winner[0] in sage_winners:
                    already_sage.append(winner)
                else:
                    sage_raffle_list.append(winner)
            elif winner[1] == 2:
                already_sage.append(winner)

        if len(sage_raffle_list) > 0:
            print('\nRAFFLE FOR SAGE')
            sage_winner = raffle.Raffle.choose_winner(1, sage_raffle_list)
            print(' - The lucky winner for Sage role is {}!'.format(sage_winner[0][0]))
            sage_winners.append(sage_winner[0])
        if len(already_sage) > 0:
            print('\nWINNERS THAT ARE ALREADY SAGES')
            for i, winner in enumerate(already_sage):
                print(" {}. {}".format(i + 1, winner[0]))


if __name__ == '__main__':
    riddle_three_raffle()
