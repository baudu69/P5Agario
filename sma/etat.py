from enum import Enum


class Etat(Enum):
    SAIN = 1
    MALADE = 2
    IMMUNISE = 3
    MORT = 4
    CONTACT = 5
    CONTAGIEUX = 6
    MALADE_RATIONNEL = 7