print("Program obliczajacy wartosc wielomianu trzeciego stopnia Algorytmem Hornera")

tablica = []
wynik = []

for i in range(4):
    tablica.append(int(input("Wprowadz zmienna: ")))
x = input("Wprowadz x: ")
x = int(x)
A = tablica[0]
B = A*x + tablica[1]
C = B*x + tablica[2]
D = C*x + tablica[3]

print("Na wyniku otrzymujemy liczby: \n",A,B,C,D)
print("Czyli rownanie: ",A,"x^2 + (",B,")x + (",C,") i reszta ",D)

close = input()

#BARTOSZ KACZOROWSKI