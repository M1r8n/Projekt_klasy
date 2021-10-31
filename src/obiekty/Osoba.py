class Osoba:
    """Klasa glowna po ktorej dziedziczą nauczyciel i uczniowie."""
    imie: str
    nazwisko: str
    pesel: str
    wiek: int

    def __init__(self, imie: str, nazwisko: str, pesel: str, wiek: int):
        self.imie=imie
        self.nazwisko=nazwisko
        self.pesel=pesel
        self.wiek=wiek

    def podajDanePersonalne(self):
        """Zwraca dane personalne osoby"""
        pass
