
# BigData

**Autorzy**: Jakub Mądrowski, Brayan Kostecki, Jan Rasiak

## Opis projektu

Projekt **BigData** koncentruje się na przetwarzaniu i analizie dużych zbiorów danych.
Repozytorium zawiera skrypty oraz notatniki Jupyter Notebook, które demonstrują różnorodne techniki analizy danych, wizualizacji oraz przetwarzania informacji z plików CSV i JSON.

## Struktura repozytorium

- **`data.ipynb`**: Notatnik Jupyter zawierający kod generujący dane oraz analizę danych z plików CSV i Kaggle.
- **`visualisation.ipynb`**: Notatnik Jupyter prezentujący techniki wizualizacji danych.
- **`main.py`**: Główny skrypt Pythona wraz z API do zarządzania bazą danych MongoDB.
- **Pliki danych**:
  - **`books_data.json`**
  - **`books_ids.json`**
  - **`borrowing_data.json`**
  - **`borrowing_dates.json`**
  - **`data_readers1.csv`**
  - **`data_readers2.csv`**
  - **`data_readers3.csv`**
  - **`data_readers4.csv`**
  - **`data_readers5.csv`**
  - **`library_card_ids.json`**
  - **`readers_data.json`**

## Wymagania

Aby uruchomić skrypty i notatniki zawarte w repozytorium, należy zainstalować następujące pakiety Pythona:

```bash
pip install pandas matplotlib seaborn jupyter
```

## Uruchamianie

1. **Klonowanie repozytorium**:

   ```bash
   git clone https://github.com/Laqerowski/BigData.git
   ```

2. **Uruchomienie notatnika Jupyter**:

   ```bash
   jupyter notebook
   ```

   Następnie otwórz plik `data.ipynb` lub `visualisation.ipynb` w interfejsie Jupyter.

3. **Uruchomienie skryptu Python**:

   ```bash
   python main.py
   ```
## API

W pliku `main.py` znajduje się kod do API konsolowego.

## Dane

Repozytorium zawiera przykładowe dane w formatach CSV i JSON, które są wykorzystywane w analizach i wizualizacjach.
Dane te obejmują informacje o książkach, czytelnikach oraz wypożyczeniach.

## Wizualizacje

Notatnik `visualisation.ipynb` zawiera przykłady wizualizacji danych z wykorzystaniem bibliotek `matplotlib` oraz `seaborn`. Dane do wizualizacji pochodzą z bazy danych MongoDB.
Możesz dostosować te wizualizacje do własnych potrzeb, modyfikując kod w notatniku.
