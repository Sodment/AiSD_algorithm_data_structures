import sys
import time
import itertools

sys.setrecursionlimit(10 ** 9)

# FUNCTIONS

class Backpack:
    # UTILITY
    def __init__(self, cargo_space):
        self.cargo_space = cargo_space
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    # BRUTE FORCE

    def brute_force(self):
        fmax = 0
        answer = None
        for X in range(1, 1 << len(self.items)):
            binary = bin(X).replace("0b", '')
            string = "0" * (len(self.items) - len(binary))
            string += binary
            current_subset = self.bruteforce_util(string)
            if current_subset[2] > self.cargo_space:
                continue
            if current_subset[1] > fmax:
                fmax = current_subset[1]
                answer = current_subset

        # PRINTING OUT ANSWER

        print("Przedmioty w plecaku (Algorytm wyczerpujacy):")
        if answer:
            for i in range(len(answer[0])):
                print(answer[0][i][2], end=', ')
            print("\nIch wartosc:", answer[1])
            print("Ich waga:", answer[2])
        else:
            print("Plecak pusty")


    def bruteforce_util(self, string):
        curr_set = []
        weight = 0
        price = 0
        for i in range(len(string)):
            if string[i] == "1":
                curr_set.append(self.items[i])
        for i in range(len(curr_set)):
            weight += curr_set[i][1]
            price += curr_set[i][0]
        return curr_set, price, weight

    # GREEEEEEEEEEEEEDDDDDDDDDYYYYYY

    def greedy_knapsack(self):
        answer = [[], 0, 0]
        sorted_items = sorted(self.items, key=lambda x: x[0]/x[1], reverse=True)
        i = 0
        while i < len(sorted_items):
            if answer[2] + sorted_items[i][1] <= self.cargo_space:
                answer[0].append(sorted_items[i][2])
                answer[1] += sorted_items[i][0]
                answer[2] += sorted_items[i][1]
            i += 1

        # PRINTING OUT ANSWER

        print("Przedmioty w plecaku (Algorytm zachlanny):")
        if answer[0]:
            for i in range(len(answer[0])):
                print(answer[0][i], end=', ')
            print("\nIch wartosc:", answer[1])
            print("Ich waga:", answer[2])
        else:
            print("Plecak pusty")

    # DYNAMIC APPROACH

    def dynamic_knapsack(self):
        cargo = self.cargo_space + 1
        itemy = len(self.items) + 1
        matrix = [[0 for x in range(cargo)] for x in range(itemy)]
        answer = [[], 0, 0]
        for i in range(itemy):
            for j in range(cargo):
                if i == 0 or j == 0:
                    matrix[i][j] = 0
                elif self.items[i-1][1] > j:
                    matrix[i][j] = matrix[i-1][j]
                elif self.items[i-1][1] <= j:
                    matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j - self.items[i-1][1]] + self.items[i-1][0])
                else:
                    print("WTF")
        #for i in range(len(matrix)):
         #   print(matrix[i])
        max_ = matrix[itemy-1][cargo-1]
        w = self.cargo_space
        for i in range(len(self.items), 0, -1):
            if max_ <= 0:
                break
            if max_ == matrix[i-1][w]:
                continue
            else:
                answer[0].append(self.items[i-1][2])
                answer[1] += self.items[i-1][0]
                answer[2] += self.items[i-1][1]
                max_ -= self.items[i-1][0]
                w -= self.items[i-1][1]

        # PRINTING OUT ANSWER

        print("Przedmioty w plecaku (Programowanie dynamiczne):")
        if answer[0]:
            for i in range(len(answer[0])):
                print(answer[0][i], end=', ')
            print("\nIch wartosc:", answer[1])
            print("Ich waga:", answer[2])
        else:
            print("Plecak pusty")


def Read_From_Keyboard():
    global amount_of_items
    global cargo_space
    return_array = []
    i = 0
    print("Podawaj przedmioty w formie:  wartosc_przedmiotu waga_perdzmiotu")
    while i < amount_of_items:
        try:
            price, weight = input().split()
            price = int(price)
            weight = int(weight)
        except ValueError:
            print("Thats not how it works")
            break
        return_array.append((price, weight, "x"+str(i+1)))
        i += 1
    return return_array

# DRIVER CODE


amount_of_items = None
cargo_space = None
items = []
while True:
    print("Wybierz sposob odczytu:\n1.Klawiatura\n2.Item.txt")
    try:
        choice = int(input())
    except ValueError:
        print("Wpisano nieodpowiedni numer, sprobuj ponownie")
        continue
    if choice == 1:
        print("Podaj ilosc przedmiotow i pojemnosc plecaka ")
        try:
            amount_of_items, cargo_space = input().split()
            amount_of_items = int(amount_of_items)
            cargo_space = int(cargo_space)
            items = Read_From_Keyboard()
            break
        except ValueError:
            print("Wpisano nieodpowiednie dane")
            continue
    elif choice == 2:
        file = open("Items.txt", "r")
        file = file.read()
        file = file.split()
        try:
            file = [int(x) for x in file]
        except ValueError:
            print("Zly format zapisu danych")
            continue
        amount_of_items = int(file[0])
        if amount_of_items <= 0:
            print("Not gonna happen")
            break
        cargo_space = int(file[1])
        if cargo_space <= 0:
            print("Not gonna happen")
            break
        file = file[2:]
        try:
            for i in range(2, 2 * (amount_of_items + 1), 2):
                x = (file[i - 2], file[i - 1], "x"+str(i//2))
                if x[0] <= 0 or x[1] <= 0:
                    print("Im afraid that item has to be dropped")
                    print("Item dropped: ", x[0], x[1] , x[2])
                else:
                    items.append(x)
        except IndexError:
            print("We are short of items!\nWe will work on", len(items), "items from now on")
        break
    else:
        print("Ops something wen wrong, please try again")
        continue

knapsack = Backpack(cargo_space)
for i in range(len(items)):
    knapsack.add_item(items[i])
#print("W plecaku jest:", knapsack.items)
while True:
    print("Wybierz co chcesz zrobic:\n1.Rozwiazanie metoda brute force\n2.Rozwiazanie metoda zachlanna\n3.Rozwiazanie metoda programowania dynamicznego\n4.Wyjscie z programu")
    try:
        ch = int(input())
    except ValueError:
        print("Nie ta liczba!")
    if ch == 1:
        start_time1 = time.perf_counter()
        knapsack.brute_force()
        print("Działam:", time.perf_counter() - start_time1, "s")
    elif ch == 2:
        start_time2 = time.perf_counter()
        knapsack.greedy_knapsack()
        print("Działam:", time.perf_counter() - start_time2, "s")
    elif ch == 3:
        start_time3 = time.perf_counter()
        knapsack.dynamic_knapsack()
        print("Działam:", time.perf_counter() - start_time3, "s")
    elif ch == 4:
        print("Bye bye")
        break;
        print("duap)")
    else:
        print("Nie ta liczba!")
