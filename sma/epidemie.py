from enum import Enum


class Epidemie(Enum):
    dureeIncubation = 5
    dureeContagion = 5
    pourcentageContagion = 0.5
    dureeDeces = 5
    pourcentageDeces = 0.5
    distanceMiniContagion = 10
