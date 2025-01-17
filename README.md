
# Dokumentacja projektu

## Nazwa kursu
**Testowanie i Jakość Oprogramowania**

---

## Autor
Damian Maziarz

## Indeks
35219

---

## Temat projektu
Kino

---

## Opis projektu
"Kino" to aplikacja umożliwiająca zarządzanie filmami i rezerwacjami biletów. Aplikacja pozwala  na dodawanie nowych filmów, edytowanie, usuwanie oraz rezerwowanie biletów na wybrane seanse. Oferuje także możliwość przeglądania dostępnych filmów i rezerwacji biletów na wybrany film.

---

## Uruchomienie projektu

1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repozytorium/kino.git
   cd kino
   ```

2. Zainstaluj zależności:
   ```bash
   pip install -r requirements.txt
   ```

3. Uruchom aplikację:
   ```bash
   flask run
   ```

4. Otwórz aplikację w przeglądarce pod adresem:
   ```http://127.0.0.1:5000```

---

## Testy

### Testy jednostkowe
Testy jednostkowe sprawdzają poprawność funkcji w aplikacji takich jak dodawanie, edytowanie, usuwanie filmów oraz rezerwacji. Testy te są uruchamiane przez pytest

### Testy integracyjne
Testy integracyjne sprawdzają scenariusze takie jak rezerwacja biletów, usuwanie filmów, edytowanie danych oraz sprawdzanie, czy dane są poprawnie wyświetlane na stronie.

### Uruchomienie testów
Testy można uruchomić za pomocą polecenia:
```bash
pytest tests
```

---

## Dokumentacja API
Dokumentacja API jest dostępna w pliku `API.md` i zawiera szczegóły na temat dostępnych endpointów, metod HTTP oraz przykładów zapytań.

---

## Przykłady testów (TestCases)

### Test 1: Sprawdzenie dostępności strony głównej
- **Kroki**:
  - Otwórz stronę główną (`/`).
- **Oczekiwany wynik**:
  - Strona załadowana poprawnie.
  - Widoczność przycisków "Filmy", "Dodaj film", "Rezerwacje".

### Test 2: Przeglądanie listy filmów
- **Kroki**:
  - Otwórz stronę z listą filmów (`/movies`).
- **Oczekiwany wynik**:
  - Wyświetlona lista dostępnych filmów.

### Test 3: Dodanie nowego filmu
- **Kroki**:
  - Przejdź do strony dodawania filmu (`/add_movie`), wypełnij formularz i dodaj film.
- **Oczekiwany wynik**:
  - Film dodany do bazy i wyświetlony na liście filmów.

### Test 4: Edycja filmu
- **Kroki**:
  - Edytuj istniejący film na stronie `/edit_movie/<id>`.
- **Oczekiwany wynik**:
  - Szczegóły filmu zaktualizowane.

### Test 5: Usunięcie filmu
- **Kroki**:
  - Usuń film z listy filmów (`/delete_movie/<id>`).
- **Oczekiwany wynik**:
  - Film usunięty z listy.

### Test 6: Rezerwacja biletów
- **Kroki**:
  - Przejdź na stronę rezerwacji (`/booking/<id>`), wypełnij formularz i zarezerwuj bilety.
- **Oczekiwany wynik**:
  - Rezerwacja została dodana do bazy danych.

### Test 7: Wyświetlanie rezerwacji
- **Kroki**:
  - Przejdź na stronę rezerwacji (`/bookings`).
- **Oczekiwany wynik**:
  - Widoczność dokonanych rezerwacji.

### Test 8: Usunięcie rezerwacji
- **Kroki**:
  - Usuń rezerwację z listy (`/delete_booking/<id>`).
- **Oczekiwany wynik**:
  - Rezerwacja usunięta.

### Test 9: Obsługa błędu 404
- **Kroki**:
  - Przejdź na stronę, która nie istnieje (`/invalid`).
- **Oczekiwany wynik**:
  - Wyświetlona strona błędu 404.

### Test 10: Walidacja formularzy
- **Kroki**:
  - Spróbuj wysłać pusty formularz rezerwacji.
- **Oczekiwany wynik**:
  - Pojawi się komunikat o błędzie walidacji.

---

## Technologie użyte w projekcie
- **Backend**:
  - Flask 2.3+ (Python)
  - Flask-SQLAlchemy (do zarządzania bazą danych)

- **Frontend**:
  - HTML5, CSS3, JavaScript
  - Bootstrap 5.3+

- **Baza danych**:
  - SQLite (w trybie in-memory do testów)
