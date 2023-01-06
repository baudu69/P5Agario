from enum import Enum

fps = 30

class Epidemie(Enum):
    dureeIncubation = 5 * fps
    dureeContagion = 5 * fps
    pourcentageContagion = 0.5
    dureeDeces = 5 * fps
    pourcentageDeces = 0.5
    distanceMiniContagion = 100
