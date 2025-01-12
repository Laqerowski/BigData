
# Hurtownia Danych Bibliotecznych

## 1. Wstęp / Opis projektu

**Library Management System** to aplikacja do zarządzania biblioteką, umożliwiająca administrowanie książkami, czytelnikami oraz wypożyczeniami za pomocą bazy danych MongoDB. Kluczowe funkcjonalności aplikacji obejmują:

- Zarządzanie książkami: dodawanie, edycja, wyświetlanie i usuwanie.
- Zarządzanie czytelnikami: dodawanie, edycja, wyświetlanie i usuwanie.
- Zarządzanie wypożyczeniami: rejestrowanie, aktualizacja dat zwrotu i przeglądanie wypożyczeń.
- Eksport i import danych w formacie JSON.

Aplikacja jest przeznaczona do środowiska terminalowego i napisana w Pythonie.

## 2. Cel projektu

Celem projektu jest stworzenie narzędzia do kompleksowego zarządzania biblioteką, w tym:

- Automatyzacja procesów zarządzania książkami i czytelnikami.
- Śledzenie aktywnych wypożyczeń i zarządzanie terminami zwrotów.
- Łatwe przenoszenie danych dzięki obsłudze formatu JSON.

Projekt wspiera małe i średnie biblioteki, minimalizując pracę manualną i ryzyko błędów.

## 3. Technologie użyte w projekcie

- **Język programowania:** Python
- **Baza danych:** MongoDB
- **Biblioteka:** `pymongo`
- **Format wymiany danych:** JSON
- **Środowisko:** terminal

## 4. Wymagania systemowe

### Sprzętowe
- Procesor: min. 1 GHz
- RAM: min. 512 MB
- Dysk: ok. 100 MB
- Połączenie internetowe (dla MongoDB Atlas)

### Programowe
- System operacyjny: Windows, macOS, Linux
- Python: wersja 3.6 lub nowsza
- Biblioteki Python: `pymongo`, `datetime`, `json`, `os`
- Baza danych: MongoDB Atlas lub lokalna instancja MongoDB

## 5. Instalacja

1. Pobierz projekt (plik .zip) i rozpakuj.
2. Upewnij się, że Python jest zainstalowany (zaznacz opcję "Add Python to PATH").
3. W terminalu przejdź do folderu projektu:
   ```bash
   cd /ścieżka/do/folderu
   ```
4. Zainstaluj wymagane biblioteki:
   ```bash
   pip install pymongo pandas matplotlib seaborn
   ```
5. Skonfiguruj bazę danych MongoDB (Atlas lub lokalną instancję).
6. Uruchom projekt:
   ```bash
   python main.py
   ```

## 6. Funkcjonalności

### Zarządzanie książkami
- Dodawanie, edycja, wyświetlanie, usuwanie książek.
- Wyświetlanie ostatnich 10 dodanych książek.

### Zarządzanie czytelnikami
- Dodawanie, edycja, wyświetlanie, usuwanie czytelników.
- Wyświetlanie ostatnich 10 dodanych czytelników.

### Zarządzanie wypożyczeniami
- Dodawanie nowych wypożyczeń.
- Śledzenie aktywnych wypożyczeń.
- Automatyczne generowanie terminów zwrotów.

### Eksport i import danych
- Eksport i import danych z/do plików JSON.

## 7. Przykłady użycia

### Dodanie książki
1. Wybierz opcję **Enter Data → Book**.
2. Podaj tytuł, autorów, kategorię, rok wydania, ocenę i liczbę stron.

### Dodanie czytelnika
1. Wybierz opcję **Enter Data → Reader**.
2. Podaj imię, nazwisko, e-mail, płeć i rok urodzenia.

### Wyświetlanie książek
1. Wybierz opcję **Display Data → All Books**.

## 8. Testy

System został przetestowany pod kątem poprawności działania kluczowych funkcji, takich jak:
- Dodawanie, edytowanie, usuwanie danych.
- Eksport i import danych.

## 9. Autorzy

- **Jan Rasiak**
- **Brajan Kostecki**
- **Jakub Mądrowski**

---

**Uwaga:** Projekt jest dostosowany do małych i średnich bibliotek. Zachęcamy do testowania i zgłaszania uwag!
