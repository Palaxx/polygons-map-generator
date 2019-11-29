# Generatore di 'mappe' 

## Introduzione

Il progetto nasce al solo scopo didattico, l'idea alla base era quella di sviluppare un generatore di mappe poligonali, seguendo questa
[guida](https://www.redblobgames.com/)

Questo progetto doveva servire anche a farmi esplorare il linguaggio python, all'epoca questa era
uno delle mie prime applicazioni del linguaggio. 

## Descrizione

Il software genera due noise map, la prima viene utilizzata come identificativo delle altezza
delle celle, mentre la seconda identifica il livello di idratazione. 

La combinazione dei due valori identifica che tipo di terreno presente sulla cella. 

La mappa dei terreni viene poi data in pasto ad una classe che associa ogni terreno ad un colore e crea
un file di output.

## Parametri dell'applicativo

Lo script può essere personalizzato tramite l'immissione di alcuni parametri.

- **--size**: Indica la dimensione in larghezza e altezza della mappa generata
- **--seed**: Serve a configurare gli algoritmi di rumore, un valore di seed genererà sempre la stessa mappa
- **--octaves**: Questo numero indica il numero di differenti frequenze di rumore applicate
- **--noise**: Indica il tipo di rumore da applicare perlin o simplex
- **--tile_size**: Fattore scala su ogni singola tile

## Eseguire il comando 
```
python main.py --size 100 --seed 8 --octaves 10
```
