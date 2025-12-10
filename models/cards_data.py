"""
Base de données des cartes légendaires.
Ce fichier sert de point d'entrée - les cartes sont organisées dans models/cards/

Répartition des raretés :
- MORTEL (50%) : ~48 cartes - 5 pièces
- ASCENDANT (30%) : ~24 cartes - 25 pièces  
- ÉLITE (15%) : ~20 cartes - 150 pièces
- TRANSCENDATEUR (5%) : ~10 cartes - 1000 pièces
"""
from models.cards import (
    CARDS_DATABASE,
    MORTEL_CARDS,
    ASCENDANT_CARDS,
    ELITE_CARDS,
    TRANSCENDATEUR_CARDS,
)

__all__ = [
    "CARDS_DATABASE",
    "MORTEL_CARDS",
    "ASCENDANT_CARDS",
    "ELITE_CARDS",
    "TRANSCENDATEUR_CARDS",
]
