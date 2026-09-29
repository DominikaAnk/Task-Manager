# System zarządzania zadaniami ⏱️

Prosta aplikacja okienkowa stworzona w celu ułatwienia zarządzania czasem i zadaniami. 

## 📌 Funkcjonalności
* **Zarządzanie zadaniami:** Użytkownik może dodawać, wyświetlać i usuwać zadania.
* **Śledzenie statusów:** Możliwość przypisania statusów za pomocą listy rozwijanej:
  * 🔴 "Do zrobienia" (domyślny, kolor czerwony)
  * 🟠 "W trakcie" (kolor pomarańczowy)
  * 🟢 "Zrobione" (kolor zielony)
* **Niezależny Timer:**
* Po zmianie statusu na "W trakcie" aplikacja automatycznie zaczyna odliczać czas dla konkretnego
* zadania (timery działają niezależnie). Po zmianie na "Zrobione" aplikacja wskazuje całkowity czas wykonania.
* **Interfejs graficzny:** Zaprojektowany przy użyciu biblioteki PySide 6.

## 🛠️ Architektura i struktura danych
Projekt wykorzystuje podstawowe założenia programowania obiektowego (klasy, hermetyzacja). 
Struktura danych opiera się na listach oraz słownikach (m.in. do przechowywania przypisania kolorów do statusów).

## 💻 Wykorzystane technologie
* Python
* PySide 6

## 🚀 Jak uruchomić projekt?
1. Sklonuj repozytorium na swój dysk.
2. Zainstaluj wymagane biblioteki poleceniem: `pip install -r requirements.txt`
3. Uruchom plik główny: `python projekt.py`
