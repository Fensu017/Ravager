"""
Module définissant la classe Player pour gérer les joueurs.
"""
from dataclasses import dataclass, field
from typing import Dict, List
from datetime import datetime, date
from models.card import Card, get_card_by_id


@dataclass
class Player:
    """Représente un joueur avec son inventaire et ses statistiques."""
    user_id: int
    username: str
    sacred_coins: int = 0  # Pièces sacrées
    daily_rifts_remaining: int = 5  # Failles gratuites restantes aujourd'hui
    last_daily_reset: str = ""  # Date du dernier reset des failles quotidiennes
    inventory: Dict[str, int] = field(default_factory=dict)  # {card_id: quantité}
    total_rifts_opened: int = 0  # Statistique: total de failles ouvertes
    total_cards_collected: int = 0  # Statistique: total de cartes obtenues

    def __post_init__(self):
        """Initialise la date du dernier reset si non définie."""
        if not self.last_daily_reset:
            self.last_daily_reset = date.today().isoformat()

    def check_daily_reset(self) -> bool:
        """
        Vérifie si les failles quotidiennes doivent être reset.
        Retourne True si un reset a été effectué.
        """
        today = date.today().isoformat()
        if self.last_daily_reset != today:
            self.daily_rifts_remaining = 5
            self.last_daily_reset = today
            return True
        return False

    def can_open_free_rift(self) -> bool:
        """Vérifie si le joueur peut ouvrir une faille gratuite."""
        self.check_daily_reset()
        return self.daily_rifts_remaining > 0

    def use_free_rift(self) -> bool:
        """
        Utilise une faille gratuite.
        Retourne True si réussi, False sinon.
        """
        self.check_daily_reset()
        if self.daily_rifts_remaining > 0:
            self.daily_rifts_remaining -= 1
            self.total_rifts_opened += 1
            return True
        return False

    def can_buy_rift(self, cost: int = 200) -> bool:
        """Vérifie si le joueur peut acheter une faille."""
        return self.sacred_coins >= cost

    def buy_rift(self, cost: int = 200) -> bool:
        """
        Achète une faille avec des pièces sacrées.
        Retourne True si réussi, False sinon.
        """
        if self.can_buy_rift(cost):
            self.sacred_coins -= cost
            self.total_rifts_opened += 1
            return True
        return False

    def add_card(self, card: Card) -> None:
        """Ajoute une carte à l'inventaire."""
        if card.id in self.inventory:
            self.inventory[card.id] += 1
        else:
            self.inventory[card.id] = 1
        self.total_cards_collected += 1

    def add_cards(self, cards: List[Card]) -> None:
        """Ajoute plusieurs cartes à l'inventaire."""
        for card in cards:
            self.add_card(card)

    def remove_card(self, card_id: str, quantity: int = 1) -> bool:
        """
        Retire une carte de l'inventaire.
        Retourne True si réussi, False sinon.
        """
        if card_id in self.inventory and self.inventory[card_id] >= quantity:
            self.inventory[card_id] -= quantity
            if self.inventory[card_id] == 0:
                del self.inventory[card_id]
            return True
        return False

    def sell_card(self, card_id: str, quantity: int = 1) -> int:
        """
        Vend une carte et retourne les pièces gagnées.
        Retourne 0 si la vente échoue.
        """
        card = get_card_by_id(card_id)
        if card and self.remove_card(card_id, quantity):
            coins_earned = card.value * quantity
            self.sacred_coins += coins_earned
            return coins_earned
        return 0

    def get_card_count(self, card_id: str) -> int:
        """Retourne le nombre d'exemplaires d'une carte."""
        return self.inventory.get(card_id, 0)

    def get_total_cards(self) -> int:
        """Retourne le nombre total de cartes dans l'inventaire."""
        return sum(self.inventory.values())

    def get_unique_cards(self) -> int:
        """Retourne le nombre de cartes uniques possédées."""
        return len(self.inventory)

    def add_coins(self, amount: int) -> None:
        """Ajoute des pièces sacrées."""
        self.sacred_coins += amount

    def to_dict(self) -> dict:
        """Convertit le joueur en dictionnaire pour la sauvegarde."""
        return {
            "user_id": self.user_id,
            "username": self.username,
            "sacred_coins": self.sacred_coins,
            "daily_rifts_remaining": self.daily_rifts_remaining,
            "last_daily_reset": self.last_daily_reset,
            "inventory": self.inventory,
            "total_rifts_opened": self.total_rifts_opened,
            "total_cards_collected": self.total_cards_collected
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Player":
        """Crée un joueur depuis un dictionnaire."""
        return cls(
            user_id=data["user_id"],
            username=data["username"],
            sacred_coins=data.get("sacred_coins", 0),
            daily_rifts_remaining=data.get("daily_rifts_remaining", 5),
            last_daily_reset=data.get("last_daily_reset", ""),
            inventory=data.get("inventory", {}),
            total_rifts_opened=data.get("total_rifts_opened", 0),
            total_cards_collected=data.get("total_cards_collected", 0)
        )
