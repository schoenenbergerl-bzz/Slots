import random


def display_slots(slots):
    print("| " + " | ".join(slots) + " |")


def check_win(slots):
    if slots[0] == slots[1] == slots[2]:
        return True
    return False


def play_game(balance):
    while balance > 0:
        print(f"\nAktueller Kontostand: {balance} €")
        bet = int(input("Wie viel möchten Sie setzen? (0 zum Beenden): "))

        if bet == 0:
            break
        if bet > balance:
            print("Sie können nicht mehr setzen, als Sie haben!")
            continue

        slots = [random.choice(['🍒', '🍋', '🍉', '🍌', '🍆️']) for _ in range(3)]
        display_slots(slots)

        if check_win(slots):
            win_amount = bet * 10  # Der Gewinn ist das 10-fache des Einsatzes
            balance += win_amount
            print(f"Sie haben gewonnen! Sie erhalten {win_amount} €.")
        else:
            balance -= bet
            print(f"Sie haben verloren. Ihr Verlust beträgt {bet} €.")

        if balance <= 0:
            print("Sie haben kein Geld mehr. Das Spiel ist zu Ende.")
            break

    print(f"\nSpiel beendet. Ihr endgültiger Kontostand ist: {balance} €")


def main():
    balance = int(input("Wie viel Geld haben Sie insgesamt? "))
    play_game(balance)


if __name__ == "__main__":
    main()
