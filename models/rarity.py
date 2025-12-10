"""
Module définissant l'énumération des raretés de cartes.
"""
from enum import Enum


class Rarity(Enum):
    """Énumération des raretés de cartes."""
    MORTEL = ("Mortel", 50, 5, "⚪")  # (nom, % apparition, valeur, emoji)
    ASCENDANT = ("Ascendant", 30, 25, "🟢")
    ELITE = ("Élite", 15, 150, "🟣")
    TRANSCENDATEUR = ("Transcendateur", 5, 1000, "🟡")

    @property
    def display_name(self) -> str:
        """Retourne le nom d'affichage de la rareté."""
        return self.value[0]

    @property
    def drop_rate(self) -> int:
        """Retourne le taux de drop en pourcentage."""
        return self.value[1]

    @property
    def sell_value(self) -> int:
        """Retourne la valeur de vente en pièces sacrées."""
        return self.value[2]

    @property
    def emoji(self) -> str:
        """Retourne l'emoji associé à la rareté."""
        return self.value[3]
