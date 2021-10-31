from obiekty.Osoba import Osoba
from obiekty.Przedmiot import Przedmiot


class Uczen(Osoba):
    """Klasa przechowujaca informacje o uczniach - ich przedmiotach i ocenach."""
    przedmioty = dict()

    def __init__(self, imie: str, nazwisko: str, pesel: str, wiek:int):
        super().__init__(imie, nazwisko,pesel, wiek)

    def dodajPrzedmiot(self, przedmiot: Przedmiot) -> None:
        """Dodawanie przedmiotu to listy ucznia"""
        self.przedmioty[przedmiot.nazwa]=przedmiot

    def usunPrzedmiot(self, przedmiot: str) -> None:
        """Usuwanie przedmiotu z listy ucznia"""
        self.przedmioty.pop(przedmiot,0)

    def postepy(self, przedmiot: str) -> float:
        """Zwraca ocene o postepach ucznia w nauce"""
        return self.przedmioty[przedmiot].srednia()

    def dodajOcene(self, przedmiot: str, ocena: int) -> None:
        """Dodaje ocene z przedmiotu."""
        self.przedmioty[przedmiot].dodajOcene(ocena)

    def pokazPrzedmiot(self,przedmiot: str) -> None:
        """Pokaz informacje o danym przedmiocie"""
        try:
            print(self.przedmioty[przedmiot])
        except KeyError:
            print("Nie ma takiego przedmiotu")

    def __str__(self):
        return f"{self.imie} {self.nazwisko} lat {self.wiek}"