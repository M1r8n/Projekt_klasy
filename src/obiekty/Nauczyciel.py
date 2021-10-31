from obiekty.Osoba import Osoba
from typing import List
from obiekty.Harmonogram import Harmonogram


class Nauczyciel(Osoba):
    """Klasa, przechowujaca dane nauczyciela i jego grafik."""
    uczniowie: List[Osoba]
    tytul: str
    stawkaGodzinowa: float
    harmonogram: Harmonogram

    def __init__(self):
        self.harmonogram = Harmonogram()
        pass

    def dodajUcznia(self, parametry):
        """Dodaje ucznia do nauczyciela"""
        pass

    def usunUcznia(self, parametry):
        """Usuwa ucznia z lisy nauczyciela"""
        pass

    def dodajZajecia(self, prarametry):
        """Dodawanie zajec do grafiku nauczyciela"""
        pass
    def usunZajecia(self, parametry):
        """Usuwanie grafiku z zajec nauczyciela"""
        pass

    def najblizszeZajecia(self):
        """Zwraca informację o najbliższych zajęciach w formie daty i godziny od do."""
        pass

    def harmonogram(self):
        """Podaje caly grafik z podziałem na dni."""
        pass

    def wolneGodziny(self, dlugosc: int = 0 ):
        """POdaje wszystkie wolne terminy o dlugosci podanej do funkcji."""
        if dlugosc>0:
            pass
        else:
            pass
