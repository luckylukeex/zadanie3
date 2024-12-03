import random

def zgadnij_liczbe():
    liczba = random.randint(1, 10000)
    proba = 0

    print("Zgadnij liczbę od 1 do 10000!")

    while True:
        odpowiedz = int(input("Podaj swoją liczbę: "))
        proba += 1

        if odpowiedz < liczba:
            print("Za mało!")
        elif odpowiedz > liczba:
            print("Za dużo!")
        else:
            print(f"Brawo! Zgadłeś za {proba} razem!")
            break

zgadnij_liczbe()
