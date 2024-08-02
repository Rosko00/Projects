class Clovek:
    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek

    @property
    def jmeno(self):
        """Getter pre jmeno."""
        return self._jmeno

    @property
    def vek(self):
        """Getter pre vek."""
        return self._vek

    @vek.setter
    def vek(self, novy_vek):
        """Setter pre vek."""
        if novy_vek > 0:
            self._vek = novy_vek
        else:
            raise ValueError("Vek musí byť kladné číslo")

# Vytvorenie inštancie
clovek = Clovek("Jozef", 30)

# Prístup k jmenu (iba čítanie)
print(clovek.jmeno)  # Výpis: Jozef

# Prístup k veku (čítanie a zápis)
print(clovek.vek)  # Výpis: 30

# Nastavenie nového veku
clovek.vek = 35
print(clovek.vek)  # Výpis: 35


