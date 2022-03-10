import quantumrandom


class Raffle:

    def __init__(self):
        pass

    @staticmethod
    def choose_winner(amount, raffle_list, print_bool=False):
        seen = set()
        win_ind = -1
        seen.add(win_ind)

        winners = []
        for i in range(amount):
            while win_ind in seen:
                win_ind = int(quantumrandom.randint(0, len(raffle_list)))
            seen.add(win_ind)
            winners.append(raffle_list[win_ind])
            if print_bool:
                Raffle.print_winner(i, raffle_list[win_ind])

        return winners

    @staticmethod
    def choose_ip_only(amount, raffle_list, print_bool=False):
        seen = set()
        win_ind = -1
        seen.add(win_ind)

        winners = []
        print_index = 0
        while amount > 0:
            while win_ind in seen:
                win_ind = int(quantumrandom.randint(0, len(raffle_list)))
            seen.add(win_ind)
            winner = raffle_list[win_ind]
            if winner[1] == 0:
                winners.append(winner)
                amount -= 1
                if print_bool:
                    Raffle.print_winner(print_index, raffle_list[win_ind])
                    print_index += 1

        return winners

    @staticmethod
    def print_winner(index, winner):
        if winner[1] == 0:
            print(" {}. {} has won IdentityPass role.".format(index + 1, winner[0]))
        elif winner[1] == 1:
            print(" {}. {} will be added to Sage role raffle.".format(index + 1, winner[0]))
        else:
            print(" {}. {} is already a Sage...".format(index + 1, winner[0]))


