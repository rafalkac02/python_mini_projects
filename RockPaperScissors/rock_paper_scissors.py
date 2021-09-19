import sys

player_1 = input("Player 1: ")
player_2 = input("Player 2: ")

def handsign(player):
    answers = ['r', 'p', 's']
    answer = input(f"{player}, do you want to show rock (R), paper (P) or scissors (S)? ").lower()
    if answer not in answers:
        print("ERROR. The only valid answers are: 'R', 'P' or 'S' (case-insensitive).")
        sys.exit()
    return answer

sign_1 = handsign(player_1)
sign_2 = handsign(player_2)

def play(sign_1, sign_2):
    def win(p):
        print(f"{p} won!")

    if sign_1 == sign_2:
        print("It is a tie!")

    elif sign_1 == 'r':
        if sign_2 == 'p':
            win(player_2)
        else:
            win(player_1)
    elif sign_1 == 'p':
        if sign_2 == 's':
            win(player_2)
        else:
            win(player_1)
    elif sign_1 == 's':
        if sign_2 == 'r':
            win(player_2)
        else:
            win(player_1)

play(sign_1, sign_2)