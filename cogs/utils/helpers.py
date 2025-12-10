"""
Constantes et fonctions utilitaires pour le système de collection.
"""
import discord
from typing import List

from models.rarity import Rarity
from models.card import Card, get_card_by_id
from models.cards_data import CARDS_DATABASE


# === CONSTANTES DU JEU ===
CARDS_PER_RIFT = 10  # Nombre de cartes par faille
RIFT_COST = 200  # Coût d'une faille en pièces sacrées
DAILY_FREE_RIFTS = 5  # Nombre de failles gratuites par jour

# Ordre d'affichage des raretés (du plus rare au moins rare)
RARITY_ORDER = [Rarity.TRANSCENDATEUR, Rarity.ELITE, Rarity.ASCENDANT, Rarity.MORTEL]

# Couleurs d'embed selon la rareté
RARITY_COLORS = {
    Rarity.MORTEL: discord.Color.light_grey(),
    Rarity.ASCENDANT: discord.Color.green(),
    Rarity.ELITE: discord.Color.purple(),
    Rarity.TRANSCENDATEUR: discord.Color.gold()
}


# === FONCTIONS UTILITAIRES ===

def get_rarity_color(rarity: Rarity) -> discord.Color:
    """Retourne la couleur Discord associée à une rareté."""
    return RARITY_COLORS.get(rarity, discord.Color.blue())


def count_cards_by_rarity(cards: List[Card]) -> dict:
    """Compte les cartes par rareté dans une liste de cartes."""
    counts = {rarity: 0 for rarity in Rarity}
    for card in cards:
        counts[card.rarity] += 1
    return counts


def count_inventory_by_rarity(inventory: dict) -> dict:
    """Compte les cartes par rareté dans un inventaire {card_id: qty}."""
    counts = {rarity: 0 for rarity in Rarity}
    for card_id, qty in inventory.items():
        card = get_card_by_id(card_id)
        if card:
            counts[card.rarity] += qty
    return counts


def format_rarity_summary(rarity_counts: dict) -> str:
    """Formate un résumé des raretés pour affichage dans un embed."""
    lines = []
    for rarity in RARITY_ORDER:
        if rarity_counts[rarity] > 0:
            lines.append(f"{rarity.emoji} {rarity.display_name}: **{rarity_counts[rarity]}**")
    return "\n".join(lines)


def find_card_by_name_or_id(search: str, search_in: List[Card] = None) -> Card | None:
    """
    Recherche une carte par nom ou ID (insensible à la casse).
    
    Args:
        search: Le terme de recherche (nom ou ID).
        search_in: Liste de cartes à parcourir (défaut: CARDS_DATABASE).
    
    Returns:
        La carte trouvée ou None.
    """
    cards = search_in if search_in is not None else CARDS_DATABASE
    search_lower = search.lower()
    
    for card in cards:
        if card.id.lower() == search_lower or card.name.lower() == search_lower:
            return card
    return None


def create_card_embed(
    card: Card, 
    footer_text: str = None, 
    show_image: bool = False, 
    owned: int = None
) -> discord.Embed:
    """
    Crée un embed Discord standardisé pour afficher une carte.
    
    Args:
        card: La carte à afficher.
        footer_text: Texte optionnel pour le footer.
        show_image: Si True, affiche l'image en grand, sinon en miniature.
        owned: Nombre d'exemplaires possédés (optionnel).
    
    Returns:
        L'embed Discord formaté.
    """
    embed = discord.Embed(
        title=f"{card.rarity.emoji} {card.name}",
        description=card.description,
        color=get_rarity_color(card.rarity)
    )
    embed.add_field(name="🏛️ Mythologie", value=card.mythology, inline=True)
    embed.add_field(name="⭐ Rareté", value=card.rarity.display_name, inline=True)
    embed.add_field(name="💰 Valeur", value=f"{card.value} pièces sacrées", inline=True)
    
    if owned is not None:
        embed.add_field(name="📦 Possédées", value=f"{owned} exemplaire(s)", inline=True)
    
    if show_image:
        embed.set_image(url=card.image_url)
    else:
        embed.set_thumbnail(url=card.image_url)
    
    if footer_text:
        embed.set_footer(text=footer_text)
    
    return embed


async def check_user_ownership(
    interaction: discord.Interaction, 
    owner_id: int, 
    error_msg: str = "❌ Cette action ne vous appartient pas !"
) -> bool:
    """
    Vérifie si l'utilisateur est le propriétaire de l'action.
    Envoie un message d'erreur éphémère si non.
    
    Args:
        interaction: L'interaction Discord.
        owner_id: L'ID du propriétaire attendu.
        error_msg: Message d'erreur personnalisé.
    
    Returns:
        True si l'utilisateur est le propriétaire, False sinon.
    """
    if interaction.user.id != owner_id:
        await interaction.response.send_message(error_msg, ephemeral=True)
        return False
    return True
