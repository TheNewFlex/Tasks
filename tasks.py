class Task:
    def __init__(self, feladatNev, feladatLeiras):
        self.feladatNev = feladatNev
        self.feladatLeiras = feladatLeiras

    def __str__(self):
        return f"{self.feladatNev} {self.feladatLeiras}"

feladatDict = {}
i = 0
while i != 1:
    i = int(input("1 - Kilépés\n2 - Feladat hozzáadása\n\t"))
    if i == 1:
        print("Kilépés")
    elif i == 2:
        feladat = input("Feladat neve:\n\t")
        leiras = input("Feladat leírása:\n\t")
        Task(feladat, leiras)
        feladatDict[feladat] = leiras

for feladat in feladatDict:
    print(f"Feladat neve: {feladat}\nFeladat leírása: {feladatDict[feladat]}")