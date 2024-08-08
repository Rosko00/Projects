class Clovek:
    def __init__(self, meno, vek):
        self._meno = meno
        self._vek = vek

    # Getter pre meno
    @property
    def meno(self):
        return self._meno
    
    # Getter pre vek
    @property
    def vek(self):
        return self._vek
    
    # Setter pre vek
    @vek.setter
    def vek(self, novy_vek):
        if novy_vek > 0:
            self._vek = novy_vek
        else:
            raise ValueError("Vek musí byť kladné číslo")
    
    def pozdrav(self, pozdrav="Ahoj"):
        print(f"{pozdrav}, som {self.meno}")

# Získanie vstupu od používateľa
meno = input("Zadajte meno: ")
vek = int(input("Zadajte vek: "))

# Vytvorenie inštancie s používateľským vstupom
clovek = Clovek(meno, vek)

# Zobrazenie údajov
print(f"Meno: {clovek.meno}")
print(f"Vek: {clovek.vek}")

novy_vek = int(input("Zadajte nový vek: "))
try:
    clovek.vek = novy_vek
    print(f"Nový vek: {clovek.vek}")
except ValueError as e:
    print(e)

# Pozdrav
clovek.pozdrav()