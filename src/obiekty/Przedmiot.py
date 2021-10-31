from typing import List
from dataclasses import dataclass,field

@dataclass
class Przedmiot:
    nazwa: str
    oceny: List[int] = field(init=False)
    cena: int

    def __post_init__(self):
        """Tworzenie pustej listy ocen"""
        self.oceny = list()

    def getNazwa(self) -> str:
        """Zwracanie nazwy przedmiotu"""
        return self.nazwa

    def __str__(self):
        return f"Przedmiot: {self.nazwa}, cena za godzinę: {self.cena} zł" \
               f", oceny z przedmiotu: {self.oceny if len(self.oceny)>0 else 'Brak ocen'}"

    def dodajOcene(self, ocena: int) -> None:
        """Dodawanie nowej oceny z przedmiotu"""
        self.oceny.append(ocena)

    def usunOcene(self,ocena:int) -> None:
        self.oceny.remove(ocena)

    def srednia(self) -> float:
        suma=0
        for i in self.oceny:
            suma+=i
        return suma/len(self.oceny)