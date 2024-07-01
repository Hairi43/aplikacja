# Instrukcja dla domokrążcy

## Korzystanie z programu Zapisz
### Podaj ID domokrazcy:
Po uruchomieniu programu zostaniesz poproszony o wprowadzenie identyfikatora domokrazcy. Wpisz odpowiednie ID i naciśnij Enter.

### Wprowadzanie danych:
Program poprosi o wprowadzenie następujących danych:
- Ulica
- Nr budynku
- Nr mieszkania (jeśli brak, naciśnij Enter, aby pozostawić puste)
- Kod pocztowy
- Miejscowość
- Zużycie

Wprowadź każdą z tych informacji, naciskając Enter po każdej z nich.

### Sprawdzanie istnienia rekordu:
Program sprawdzi, czy w bazie danych istnieje już rekord z podanym adresem:

Jeśli rekord istnieje, zostaniesz zapytany, czy chcesz zaktualizować istniejące zużycie (wpisz t dla tak lub n dla nie).
Jeśli rekord nie istnieje, dane zostaną dodane jako nowy rekord.
### Kontynuowanie lub zakończenie:
Po wprowadzeniu danych zostaniesz zapytany, czy chcesz zakończyć wprowadzanie (wpisz t dla tak lub naciśnij Enter, aby kontynuować wprowadzanie kolejnych danych).

### Zakończenie i eksport do CSV:
Po zakończeniu wprowadzania danych, wszystkie zapisane rekordy zostaną wyeksportowane do pliku zebrane_dane.csv. Program wyświetli również wszystkie rekordy na ekranie.

## Korzystanie z programu Wyslij

### Uruchamianie pliku
Uruchomienie pliku wyśle wszystkie rekordy do zdalnej bazy danych. Sprawdź czy nie wyskoczył ci błąd, który sugeruje, że źle wpisałeś adres.

# Instrukcja dla analityka

## Korzystanie z programu Raporty

### Uruchamianie pliku
Uruchomienie pliku spowoduje narysowanie wykresu, który obrazuje ilość spisanych liczników przez każdego domokrążce.

W przyszłości planujemy dodać więcej możliwości tworzenia wykresów.

# Instrukcja dla admina

## Korzystanie z programu 

### Użycie programu
Uruchom program.
Podaj imię i nazwisko klienta, którego dane chcesz wyszukać, gdy program o to poprosi.
Program wyświetli tabelę z danymi klienta, w tym informacje o adresie, zużyciu energii oraz historii licznika.  
