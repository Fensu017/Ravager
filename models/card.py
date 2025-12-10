"""
Module définissant la classe Card et les fonctions de tirage.
"""
from dataclasses import dataclass
from typing import List
import random

from models.rarity import Rarity


@dataclass
class Card:
    """Représente une carte légendaire."""
    id: str
    name: str
    description: str
    mythology: str
    rarity: Rarity
    image_url: str

    @property
    def value(self) -> int:
        """Retourne la valeur de vente de la carte."""
        return self.rarity.sell_value

    def to_dict(self) -> dict:
        """Convertit la carte en dictionnaire pour la sauvegarde."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "mythology": self.mythology,
            "rarity": self.rarity.name,
            "image_url": self.image_url
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Card":
        """Crée une carte depuis un dictionnaire."""
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            mythology=data["mythology"],
            rarity=Rarity[data["rarity"]],
            image_url=data["image_url"]
        )


def get_cards_by_rarity(rarity: Rarity) -> List["Card"]:
    """Retourne toutes les cartes d'une rareté donnée."""
    from models.cards_data import CARDS_DATABASE
    return [card for card in CARDS_DATABASE if card.rarity == rarity]


def draw_random_card() -> "Card":
    """
    Tire une carte aléatoire en respectant les probabilités de rareté.
    - Ascendant: 75%
    - Élite: 20%
    - Transcendateur: 5%
    """
    roll = random.randint(1, 100)
    
    if roll <= 5:  # 1-5 = 5%
        rarity = Rarity.TRANSCENDATEUR
    elif roll <= 25:  # 6-25 = 20%
        rarity = Rarity.ELITE
    else:  # 26-100 = 75%
        rarity = Rarity.ASCENDANT
    
    cards_of_rarity = get_cards_by_rarity(rarity)
    return random.choice(cards_of_rarity)


def draw_cards(amount: int = 10) -> List["Card"]:
    """Tire plusieurs cartes (par défaut 10 pour une faille)."""
    return [draw_random_card() for _ in range(amount)]


def get_card_by_id(card_id: str) -> "Card | None":
    """Retourne une carte par son ID."""
    from models.cards_data import CARDS_DATABASE
    for card in CARDS_DATABASE:
        if card.id == card_id:
            return card
    return None
