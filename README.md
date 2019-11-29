# Generatore di 'mappe' 

## Introduzione

Il progetto nasce al solo scopo didattico, l'idea alla base era quella di sviluppare un generatore di mappe poligonali, seguendo questa
[guida](https://www.redblobgames.com/)

Questo progetto doveva servire anche a farmi esplorare il linguaggio python, all'epoca questa era
uno delle mie prime applicazioni del linguaggio. 

## Parametri dell'applicativo

Lo script può essere personalizzato tramite l'immissione di alcuni parametri.

- **--size**: Indica la dimensione in larghezza e altezza della mappa generata
- **--seed**: Serve a configurare gli algoritmi di rumore, un valore di seed genererà sempre la stessa mappa
- **--octaves**: Questo numero indica il numero di differenti frequenze di rumore applicate
- **--noise**: Indica il tipo di rumore da applicare perlin o simplex
- **--tile_size**: Fattore scala su ogni singola tile