"""
Package cards - Contient toutes les cartes du jeu organisées par mythologie.

Répartition des raretés :
- MORTEL (50%) : 48 cartes - 5 pièces
- ASCENDANT (30%) : 24 cartes - 25 pièces  
- ÉLITE (15%) : 20 cartes - 150 pièces
- TRANSCENDATEUR (5%) : 10 cartes - 1000 pièces

Total : 102 cartes
"""
from models.cards.grecque import GREEK_CARDS
from models.cards.egyptienne import EGYPTIAN_CARDS
from models.cards.nordique import NORSE_CARDS
from models.cards.japonaise import JAPANESE_CARDS
from models.cards.amerique_europe import AZTEC_MAYA_CARDS, CELTIC_CARDS, ARTHURIAN_CARDS
from models.cards.asie_slave import HINDU_CARDS, CHINESE_CARDS, SLAVIC_CARDS

# Base de données complète
CARDS_DATABASE = (
    GREEK_CARDS + 
    EGYPTIAN_CARDS + 
    NORSE_CARDS + 
    JAPANESE_CARDS + 
    AZTEC_MAYA_CARDS + 
    CELTIC_CARDS + 
    ARTHURIAN_CARDS +
    HINDU_CARDS + 
    CHINESE_CARDS + 
    SLAVIC_CARDS
)

# Listes par rareté (pour compatibilité)
from models.rarity import Rarity

MORTEL_CARDS = [c for c in CARDS_DATABASE if c.rarity == Rarity.MORTEL]
ASCENDANT_CARDS = [c for c in CARDS_DATABASE if c.rarity == Rarity.ASCENDANT]
ELITE_CARDS = [c for c in CARDS_DATABASE if c.rarity == Rarity.ELITE]
TRANSCENDATEUR_CARDS = [c for c in CARDS_DATABASE if c.rarity == Rarity.TRANSCENDATEUR]

__all__ = [
    "CARDS_DATABASE",
    "MORTEL_CARDS",
    "ASCENDANT_CARDS", 
    "ELITE_CARDS",
    "TRANSCENDATEUR_CARDS",
]
