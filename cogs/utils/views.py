"""
Vues Discord (boutons interactifs) pour le système de collection.
"""
import discord
from typing import List

from models.rarity import Rarity
from models.card import Card
from services.database import db
from cogs.utils.helpers import (
    RARITY_ORDER,
    create_card_embed,
    check_user_ownership
)


class RiftResultView(discord.ui.View):
    """Vue pour afficher les résultats d'une faille avec pagination."""
    
    def __init__(self, cards: List[Card], user_id: int):
        super().__init__(timeout=300)  # 5 minutes de timeout
        self.cards = cards
        self.user_id = user_id
        self.current_index = 0

    def get_card_embed(self, card: Card, index: int) -> discord.Embed:
        """Crée un embed pour une carte avec le numéro de page."""
        return create_card_embed(card, footer_text=f"Carte {index + 1}/{len(self.cards)}")

    def create_summary_embed(self) -> discord.Embed:
        """Crée un embed résumant toutes les cartes obtenues."""
        embed = discord.Embed(
            title="🌀 Résumé de la Faille des Légendes",
            description="Voici toutes les cartes que vous avez obtenues !",
            color=discord.Color.blue()
        )
        
        # Grouper par rareté
        by_rarity = {rarity: [] for rarity in Rarity}
        for card in self.cards:
            by_rarity[card.rarity].append(card)
        
        # Afficher par rareté (du plus rare au moins rare)
        for rarity in RARITY_ORDER:
            cards_list = by_rarity[rarity]
            if cards_list:
                card_names = ", ".join([f"`{c.name}`" for c in cards_list])
                embed.add_field(
                    name=f"{rarity.emoji} {rarity.display_name} ({len(cards_list)})",
                    value=card_names,
                    inline=False
                )
        
        # Valeur totale
        total_value = sum(card.value for card in self.cards)
        embed.add_field(
            name="💰 Valeur totale",
            value=f"**{total_value}** pièces sacrées",
            inline=False
        )
        
        return embed

    @discord.ui.button(label="◀️ Précédent", style=discord.ButtonStyle.secondary)
    async def previous_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not await check_user_ownership(interaction, self.user_id, "❌ Ce n'est pas votre faille !"):
            return
        self.current_index = (self.current_index - 1) % (len(self.cards) + 1)
        await self._update_view(interaction)

    @discord.ui.button(label="Suivant ▶️", style=discord.ButtonStyle.secondary)
    async def next_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not await check_user_ownership(interaction, self.user_id, "❌ Ce n'est pas votre faille !"):
            return
        self.current_index = (self.current_index + 1) % (len(self.cards) + 1)
        await self._update_view(interaction)

    @discord.ui.button(label="📋 Résumé", style=discord.ButtonStyle.primary)
    async def summary_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not await check_user_ownership(interaction, self.user_id, "❌ Ce n'est pas votre faille !"):
            return
        self.current_index = len(self.cards)  # Index du résumé
        await self._update_view(interaction)

    async def _update_view(self, interaction: discord.Interaction):
        """Met à jour l'affichage."""
        if self.current_index < len(self.cards):
            embed = self.get_card_embed(self.cards[self.current_index], self.current_index)
        else:
            embed = self.create_summary_embed()
        await interaction.response.edit_message(embed=embed, view=self)


class SellConfirmView(discord.ui.View):
    """Vue de confirmation pour la vente de cartes."""
    
    def __init__(self, user_id: int, card: Card, quantity: int, total_value: int):
        super().__init__(timeout=60)
        self.user_id = user_id
        self.card = card
        self.quantity = quantity
        self.total_value = total_value

    def _disable_buttons(self):
        """Désactive tous les boutons."""
        for item in self.children:
            item.disabled = True

    @discord.ui.button(label="✅ Confirmer la vente", style=discord.ButtonStyle.success)
    async def confirm_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not await check_user_ownership(interaction, self.user_id, "❌ Ce n'est pas votre vente !"):
            return
        
        player = db.get_player(self.user_id)
        coins_earned = player.sell_card(self.card.id, self.quantity)
        
        if coins_earned > 0:
            db.save()
            embed = discord.Embed(
                title="✅ Vente réussie !",
                description=f"Vous avez vendu **{self.quantity}x {self.card.name}** pour **{coins_earned}** pièces sacrées !",
                color=discord.Color.green()
            )
            embed.add_field(name="💰 Nouveau solde", value=f"{player.sacred_coins} pièces sacrées")
        else:
            embed = discord.Embed(
                title="❌ Erreur",
                description="La vente a échoué. Vérifiez votre inventaire.",
                color=discord.Color.red()
            )
        
        self._disable_buttons()
        await interaction.response.edit_message(embed=embed, view=self)

    @discord.ui.button(label="❌ Annuler", style=discord.ButtonStyle.danger)
    async def cancel_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        if not await check_user_ownership(interaction, self.user_id, "❌ Ce n'est pas votre vente !"):
            return
        
        embed = discord.Embed(
            title="❌ Vente annulée",
            description="La vente a été annulée.",
            color=discord.Color.red()
        )
        self._disable_buttons()
        await interaction.response.edit_message(embed=embed, view=self)
