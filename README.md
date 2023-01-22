# Traveling Salesman

## Algorithmus

Zuerst werden alle mögliche Kombinationen der eingegebenen Städte generiert. Danach iteriert man mit einem For-Loop
durch alle Kombinationen.
"distance" wird auf 0 gesetzt und "combination" wird mit der Start-Stadt ergänzt.
Mit einem verschachtelten For-Loop wird auf "distance", die Fluglinie von zwei Städten,
addiert. Wenn der innere For-Loop durch ist, dann wird geschaut, ob "distance" kleiner ist als "min_distance", wenn das
der Fall ist, dann wird die jetzige distance min_distance und der min_path wird mit der jetzigen combination gesetzt.

Hiermit wird die Kombination mit der kleinsten Distanz berechnet.

## Libraries
Um die Kombinationen zu generieren, verwenden wir permutations von itertools.

## Daten
Die Städte sind in einem JSON-File gespeichert. Jede Stadt hat eine id, name, x- und y-Koordinate.
