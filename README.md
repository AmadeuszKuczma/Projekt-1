# Wykrywanie płuci po głosie

Program uczący się ze zbioru testowego plików .wav z nagraniami próbek głosów z informacją czy właścicielem głosu jest mężczyzna czy kobieta oraz potrafiący na podstawie wyuczonych wartości rozpoznawać płeć na plikach testowych.

### Zastosowany algorytm
Dostępne w internecie inforamcje na temat wykresów amplitudy fal dziękowych w zależności od częstotliwości pozwala stwierdzić, że aby rozpoznać czy osoba mówiąca jest kobieta czy mężczyzna należy sprawdzić która z sum wartości pewnych przedziałów tych wykresów jest większa. Skrypt poszukuje najbardziej optymalnych przedziałów dla obu płci na plikach treningowych. Zapamiętane wartości wykorzystuje na plikach testowych.

### Wymagane środowisko i biblioteki
 - Python 3.6 (najlepiej Anaconda)
 - numpy
 - scipy
 - copy
 - warnings
 - sys
 - soundfile
 
### Korzystanie

Skrypty umieszczone muszą być w folderze razem z folderem zawierającym pliki treningowe.

Aby rozpocząć trenowanie należy wywołać w folderze zawierającym:
```sh
python training.py
```

Aby rozpocząć testowanie należy wywowałać w folderze zawierającym:
```sh
python predict.py ścieżka do pliku z rozszerzeniem
```
