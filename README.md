# Generator wypracowan

## Stack:
* Głównie python (wonż)
* Do generowania wypracowań używamy OpenAI (złodzieje) z wykorzystaniem text-davinci-003 (głupi model)

## Instalacja i uruchamianie:
* `pip install -r requirements.txt`
* `python3 server.py`
* `python3 client.py`

## Użycie:
Włączamy serwer oraz klienta. Używamy klienta do generowania wypracowań. Wpisujemy temat i chwili otrzymujemy wypracowanie.

## Historia i logowanie
Logujemy się podając unikalną parę login hasło. Po wygenerowaniu wypracowania dane są zapisywane w folderze `history`.
Aby pozyskac historię wygenerowanych wypracowań należy uruchomić `python3 history.py` i podać login i hasło.