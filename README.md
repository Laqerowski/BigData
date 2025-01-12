# BigData

**Autorzy:** Jakub Mądrowski, Brayan Kostecki, Jan Rasiak

## Opis projektu

Projekt **BigData** jest poświęcony przetwarzaniu i analizie dużych zbiorów danych. W ramach tego projektu znajdują się skrypty i notatniki Jupyter Notebook, które demonstrują różne techniki analizy danych, wizualizacji oraz przetwarzania informacji z plików CSV i JSON.

## Struktura repozytorium

- `data.ipynb`: Notatnik Jupyter zawierający analizę danych z plików CSV.
- `wizualizacja.ipynb`: Notatnik Jupyter prezentujący techniki wizualizacji danych.
- `main.py`: Główny skrypt Pythona do przetwarzania danych.
- `MOCK_DATA.csv`, `MOCK_DATA (1).csv`, `MOCK_DATA (2).csv`, `MOCK_DATA (3).csv`, `MOCK_DATA (4).csv`: Przykładowe pliki CSV używane w analizie.
- `books_data.json`, `books_ids.json`, `borrowing_data.json`, `borrowing_dates.json`, `library_card_ids.json`, `readers_data.json`: Przykładowe pliki JSON zawierające dane do analizy.

## Wymagania

Aby uruchomić skrypty i notatniki, upewnij się, że masz zainstalowane następujące oprogramowanie:

- Python 3.x
- Jupyter Notebook
- Biblioteki Python: `pandas`, `numpy`, `matplotlib`, `seaborn`

Możesz zainstalować wymagane biblioteki za pomocą polecenia:

```bash
pip install pandas numpy matplotlib seaborn
```

## Uruchamianie notatników Jupyter

Aby uruchomić notatniki Jupyter:

1. Otwórz terminal lub wiersz poleceń.
2. Przejdź do katalogu z repozytorium `BigData`.
3. Uruchom Jupyter Notebook poleceniem:

   ```bash
   jupyter notebook
   ```

4. W przeglądarce otworzy się interfejs Jupyter, gdzie możesz wybrać i uruchomić `data.ipynb` lub `wizualizacja.ipynb`.

## Uruchamianie skryptu Python

Aby uruchomić skrypt `main.py`:

1. Otwórz terminal lub wiersz poleceń.
2. Przejdź do katalogu z repozytorium `BigData`.
3. Wykonaj polecenie:

   ```bash
   python main.py
   ```
