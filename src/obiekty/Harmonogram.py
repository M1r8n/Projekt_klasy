from obiekty.Przedmiot import Przedmiot
from typing import List
dniTygodnia= ["Po","Wt", "Sr","Cz","Pt","So","Ni"]


class AlreadyReserved(Exception):
    """Wyjatek dla proby zajecia juz zarezerwowanych godzin."""

    def __init__(self, message: str):
        self.message = message


class Harmonogram:
    dnitygodnia = dict()

    def __init__(self):
        for dzien in dniTygodnia:
            self.dnitygodnia[dzien] = {}

    def dodajTermin(self,dzien: str, godzina: int, iloscgodzin: int, przedmiot: Przedmiot) -> None:
        """Dodaje termin do harmonogramu, sprawdzając czy juz nie jest on zajety"""
        for i in range(iloscgodzin):
            if godzina+i in self.dnitygodnia[dzien].keys():
                raise AlreadyReserved(f"Nie mozna zajac {iloscgodzin} od godziny {godzina} w dniu {dzien}")
        for i in range(iloscgodzin):
            self.dnitygodnia[dzien][godzina+i] = przedmiot.getNazwa()
        
    def usunTermin(self, dzien : str, godzina: int, iloscgodzin: int = 1):
        """Usuwa termin z harmonogramu"""
        for i in range(iloscgodzin):
            self.dnitygodnia[dzien].pop(godzina+i)

    def wolneGodziny(self, dnia:str) -> List[int]:
        """Zwraca wszystkie wolne godziny podanego dnia"""
        return [i for i in range(8,21) if i not in self.dnitygodnia[dnia].keys()]
    
    def __str__(self):
        """Wyswietlenie harmonogramu."""
        return self.dnitygodnia.__str__()


def main():
    obiekt=Harmonogram()
    przedmiot=Przedmiot("Matematyka", 30)
    obiekt.dodajTermin("Wt",12,2,przedmiot)
    obiekt.dodajTermin("Wt",14,2,przedmiot)
    obiekt.usunTermin("Wt", 13, 2)
    print(obiekt.wolneGodziny("Wt"))
    
if __name__=="__main__":
    main()