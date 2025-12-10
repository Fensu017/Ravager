"""
Cog pour le système de Failles des Légendes et de collection de cartes.
"""
import discord
from discord.ext import commands
from discord import app_commands
from typing import Optional, List

from models import Rarity, draw_cards, get_card_by_id, CARDS_DATABASE, get_cards_by_rarity
from services.database import db
from cogs.utils import (
    CARDS_PER_RIFT, RIFT_COST, DAILY_FREE_RIFTS, RARITY_ORDER,
    count_cards_by_rarity, count_inventory_by_rarity, format_rarity_summary,
    find_card_by_name_or_id, create_card_embed,
    RiftResultView, SellConfirmView
)


class LegendsCog(commands.Cog):
    """Cog gérant le système de collection de cartes légendaires."""

    def __init__(self, client: commands.Bot):
        self.client = client

    # === AUTOCOMPLÉTION ===

    async def inventory_card_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> List[app_commands.Choice[str]]:
        """Autocomplétion pour les cartes de l'inventaire du joueur."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        choices = []
        
        for card_id, qty in player.inventory.items():
            card = get_card_by_id(card_id)
            if card and (not current or current.lower() in card.name.lower()):
                # Affiche le nom + quantité possédée
                label = f"{card.rarity.emoji} {card.name} (x{qty})"
                choices.append(app_commands.Choice(name=label[:100], value=card.name))
            if len(choices) >= 25:  # Discord limite à 25 choix
                break
        
        return choices

    async def all_cards_autocomplete(
        self, interaction: discord.Interaction, current: str
    ) -> List[app_commands.Choice[str]]:
        """Autocomplétion pour toutes les cartes du jeu."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        choices = []
        
        for card in CARDS_DATABASE:
            if not current or current.lower() in card.name.lower():
                owned = player.get_card_count(card.id)
                # Affiche le nom + quantité possédée si > 0
                if owned > 0:
                    label = f"{card.rarity.emoji} {card.name} (x{owned})"
                else:
                    label = f"{card.rarity.emoji} {card.name}"
                choices.append(app_commands.Choice(name=label[:100], value=card.name))
            if len(choices) >= 25:
                break
        
        return choices

    # === COMMANDES PRINCIPALES ===

    @app_commands.command(name="faille", description="🌀 Ouvrir une Faille des Légendes pour obtenir 10 cartes")
    async def open_rift(self, interaction: discord.Interaction):
        """Ouvre une faille des légendes (5 gratuites par jour)."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        player.check_daily_reset()
        
        # Déterminer le type de faille
        if player.daily_rifts_remaining > 0:
            player.use_free_rift()
            rift_type = "gratuite"
        elif player.can_buy_rift(RIFT_COST):
            player.buy_rift(RIFT_COST)
            rift_type = "achetée"
        else:
            embed = discord.Embed(
                title="❌ Aucune faille disponible",
                description=(
                    f"Vous n'avez plus de failles gratuites aujourd'hui.\n"
                    f"**Failles restantes:** 0/{DAILY_FREE_RIFTS}\n"
                    f"**Vos pièces:** {player.sacred_coins} 💰\n"
                    f"**Coût d'une faille:** {RIFT_COST} pièces sacrées\n\n"
                    f"Vendez des cartes ou attendez demain !"
                ),
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Tirer et ajouter les cartes
        cards = draw_cards(CARDS_PER_RIFT)
        player.add_cards(cards)
        db.save()

        # Créer l'embed
        embed = discord.Embed(
            title="🌀 Faille des Légendes ouverte !",
            description=(
                f"**Type:** Faille {rift_type}\n"
                f"**Failles gratuites restantes:** {player.daily_rifts_remaining}/{DAILY_FREE_RIFTS}\n"
                f"**Pièces sacrées:** {player.sacred_coins} 💰\n\n"
                f"Utilisez les boutons pour voir vos {CARDS_PER_RIFT} cartes !"
            ),
            color=discord.Color.purple()
        )
        
        rarity_counts = count_cards_by_rarity(cards)
        embed.add_field(name="📊 Résumé des raretés", value=format_rarity_summary(rarity_counts), inline=False)

        await interaction.response.send_message(embed=embed, view=RiftResultView(cards, interaction.user.id))

    @app_commands.command(name="inventaire", description="📦 Voir votre inventaire de cartes")
    async def inventory(self, interaction: discord.Interaction, page: int = 1):
        """Affiche l'inventaire du joueur."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        
        if not player.inventory:
            embed = discord.Embed(
                title="📦 Inventaire vide",
                description="Vous n'avez pas encore de cartes.\nUtilisez `/faille` pour en obtenir !",
                color=discord.Color.orange()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return

        # Préparer et trier les cartes
        cards_data = [(get_card_by_id(cid), qty) for cid, qty in player.inventory.items()]
        cards_data = [(c, q) for c, q in cards_data if c]
        rarity_sort = {r: i for i, r in enumerate(RARITY_ORDER)}
        cards_data.sort(key=lambda x: (rarity_sort[x[0].rarity], x[0].name))
        
        # Pagination
        per_page = 10
        total_pages = max(1, (len(cards_data) + per_page - 1) // per_page)
        page = max(1, min(page, total_pages))
        start, end = (page - 1) * per_page, page * per_page
        
        embed = discord.Embed(title=f"📦 Inventaire de {interaction.user.display_name}", color=discord.Color.blue())
        embed.add_field(
            name="📊 Statistiques",
            value=(
                f"💰 **Pièces sacrées:** {player.sacred_coins}\n"
                f"🃏 **Cartes totales:** {player.get_total_cards()}\n"
                f"✨ **Cartes uniques:** {player.get_unique_cards()}/{len(CARDS_DATABASE)}\n"
                f"🌀 **Failles ouvertes:** {player.total_rifts_opened}"
            ),
            inline=False
        )
        
        cards_text = "\n".join([f"{c.rarity.emoji} **{c.name}** x{q} ({c.value}💰)" for c, q in cards_data[start:end]])
        embed.add_field(name=f"🃏 Vos cartes (Page {page}/{total_pages})", value=cards_text or "Aucune", inline=False)
        embed.set_footer(text="Utilisez /inventaire [page] pour naviguer • /vendre [carte] pour vendre")
        
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="vendre", description="💰 Vendre une carte de votre collection")
    @app_commands.describe(carte="Le nom de la carte à vendre", quantite="Nombre à vendre (défaut: 1)")
    @app_commands.autocomplete(carte=inventory_card_autocomplete)
    async def sell_card(self, interaction: discord.Interaction, carte: str, quantite: int = 1):
        """Vend une ou plusieurs cartes."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        
        # Rechercher la carte
        inv_cards = [get_card_by_id(cid) for cid in player.inventory.keys()]
        found_card = find_card_by_name_or_id(carte, [c for c in inv_cards if c])
        
        if not found_card:
            available = [f"`{get_card_by_id(cid).name}`" for cid in list(player.inventory.keys())[:5] if get_card_by_id(cid)]
            embed = discord.Embed(
                title="❌ Carte non trouvée",
                description=f"**{carte}** n'est pas dans votre inventaire.\n\n**Disponibles:**\n" + ("\n".join(available) or "Aucune"),
                color=discord.Color.red()
            )
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        # Vérifier la quantité
        owned = player.get_card_count(found_card.id)
        if owned == 0:
            embed = discord.Embed(title="❌ Carte non possédée", description=f"Vous n'avez pas de **{found_card.name}** dans votre inventaire.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        quantite = max(1, min(quantite, owned))
        remaining = owned - quantite
        
        # Confirmation
        total = found_card.value * quantite
        embed = discord.Embed(
            title="💰 Confirmer la vente",
            description=(
                f"**Carte:** {found_card.rarity.emoji} {found_card.name}\n"
                f"**Quantité à vendre:** {quantite}\n"
                f"**Restant après vente:** {remaining}\n"
                f"**Total:** {total} pièces"
            ),
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url=found_card.image_url)
        await interaction.response.send_message(embed=embed, view=SellConfirmView(interaction.user.id, found_card, quantite, total))

    @app_commands.command(name="boutique", description="🏪 Voir la boutique des failles")
    async def shop(self, interaction: discord.Interaction):
        """Affiche la boutique."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        player.check_daily_reset()
        
        embed = discord.Embed(title="🏪 Boutique des Failles", description="Achetez des Failles des Légendes !", color=discord.Color.gold())
        embed.add_field(name="🌀 Faille des Légendes", value=f"**Prix:** {RIFT_COST} pièces\n**Contenu:** {CARDS_PER_RIFT} cartes", inline=False)
        embed.add_field(name="📊 Vos ressources", value=f"💰 {player.sacred_coins} pièces\n🌀 {player.daily_rifts_remaining}/{DAILY_FREE_RIFTS} gratuites\n🛒 {player.sacred_coins // RIFT_COST} achetables", inline=False)
        embed.add_field(name="📈 Taux de drop", value="🟢 Ascendant: 75% (10💰)\n🟣 Élite: 20% (300💰)\n🟡 Transcendateur: 5% (2000💰)", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="carte", description="🃏 Voir les détails d'une carte")
    @app_commands.describe(nom="Le nom de la carte")
    @app_commands.autocomplete(nom=all_cards_autocomplete)
    async def card_info(self, interaction: discord.Interaction, nom: str):
        """Affiche les informations d'une carte."""
        found_card = find_card_by_name_or_id(nom)
        
        if not found_card:
            matches = [c for c in CARDS_DATABASE if nom.lower() in c.name.lower()][:5]
            if matches:
                embed = discord.Embed(title="❓ Carte non trouvée", description=f"Vouliez-vous dire :\n" + "\n".join([f"• `{c.name}`" for c in matches]), color=discord.Color.orange())
            else:
                embed = discord.Embed(title="❌ Carte non trouvée", description=f"**{nom}** n'existe pas.", color=discord.Color.red())
            await interaction.response.send_message(embed=embed, ephemeral=True)
            return
        
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        await interaction.response.send_message(embed=create_card_embed(found_card, show_image=True, owned=player.get_card_count(found_card.id)))

    @app_commands.command(name="collection", description="📚 Voir toutes les cartes du jeu")
    @app_commands.describe(rarete="Filtrer par rareté")
    @app_commands.choices(rarete=[
        app_commands.Choice(name="🟢 Ascendant", value="ASCENDANT"),
        app_commands.Choice(name="🟣 Élite", value="ELITE"),
        app_commands.Choice(name="🟡 Transcendateur", value="TRANSCENDATEUR"),
    ])
    async def collection(self, interaction: discord.Interaction, rarete: Optional[str] = None):
        """Affiche toutes les cartes disponibles."""
        player = db.get_player(interaction.user.id, interaction.user.display_name)
        
        if rarete:
            rarity = Rarity[rarete]
            cards = get_cards_by_rarity(rarity)
            title = f"📚 Collection - {rarity.emoji} {rarity.display_name}"
        else:
            cards = CARDS_DATABASE
            title = "📚 Collection complète"
        
        embed = discord.Embed(title=title, description=f"**{len(cards)}** cartes", color=discord.Color.blue())
        
        if rarete:
            # Afficher par pages de 20 cartes max pour éviter la limite de 1024 caractères
            lines = [f"{'✅' if player.get_card_count(c.id) > 0 else '❌'} **{c.name}** - {c.mythology}" for c in cards]
            # Diviser en chunks de 20
            chunk_size = 20
            for i in range(0, len(lines), chunk_size):
                chunk = lines[i:i + chunk_size]
                field_name = "Cartes" if i == 0 else f"Cartes (suite {i // chunk_size + 1})"
                embed.add_field(name=field_name, value="\n".join(chunk) or "Aucune", inline=False)
        else:
            # Vue résumée par rareté (juste le compte)
            for r in RARITY_ORDER:
                r_cards = get_cards_by_rarity(r)
                owned = sum(1 for c in r_cards if player.get_card_count(c.id) > 0)
                embed.add_field(
                    name=f"{r.emoji} {r.display_name}",
                    value=f"**{owned}/{len(r_cards)}** obtenues\n💰 {r.sell_value} pièces",
                    inline=True
                )
            embed.add_field(
                name="💡 Astuce",
                value="Utilisez `/collection rarete:` pour voir les cartes d'une rareté spécifique !",
                inline=False
            )
        
        progress = (player.get_unique_cards() / len(CARDS_DATABASE)) * 100
        embed.set_footer(text=f"Progression: {player.get_unique_cards()}/{len(CARDS_DATABASE)} ({progress:.1f}%)")
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="profil", description="👤 Voir votre profil de collectionneur")
    @app_commands.describe(membre="Le membre à consulter")
    async def profile(self, interaction: discord.Interaction, membre: Optional[discord.Member] = None):
        """Affiche le profil d'un joueur."""
        target = membre or interaction.user
        player = db.get_player(target.id, target.display_name)
        player.check_daily_reset()
        
        embed = discord.Embed(title=f"👤 Profil de {target.display_name}", color=discord.Color.blue())
        embed.set_thumbnail(url=target.display_avatar.url)
        embed.add_field(name="💰 Économie", value=f"**{player.sacred_coins}** pièces", inline=True)
        embed.add_field(name="🌀 Failles/jour", value=f"{player.daily_rifts_remaining}/{DAILY_FREE_RIFTS}", inline=True)
        embed.add_field(name="🎯 Total failles", value=str(player.total_rifts_opened), inline=True)
        embed.add_field(
            name="🃏 Collection",
            value=f"**Total:** {player.get_total_cards()}\n**Uniques:** {player.get_unique_cards()}/{len(CARDS_DATABASE)}\n**Progression:** {(player.get_unique_cards()/len(CARDS_DATABASE)*100):.1f}%",
            inline=False
        )
        embed.add_field(name="📊 Par rareté", value=format_rarity_summary(count_inventory_by_rarity(player.inventory)) or "Aucune carte", inline=False)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="classement", description="🏆 Voir le classement des collectionneurs")
    @app_commands.describe(type="Type de classement")
    @app_commands.choices(type=[
        app_commands.Choice(name="💰 Pièces sacrées", value="coins"),
        app_commands.Choice(name="🃏 Nombre de cartes", value="cards"),
        app_commands.Choice(name="🌀 Failles ouvertes", value="rifts"),
    ])
    async def leaderboard(self, interaction: discord.Interaction, type: str = "coins"):
        """Affiche le classement des joueurs."""
        players = db.get_leaderboard(limit=10, sort_by=type)
        titles = {"coins": "💰 Les plus riches", "cards": "🃏 Meilleurs collectionneurs", "rifts": "🌀 Explorateurs de failles"}
        
        embed = discord.Embed(title=titles.get(type, "🏆 Classement"), color=discord.Color.gold())
        
        if not players:
            embed.description = "Aucun joueur n'a encore joué !"
        else:
            medals = ["🥇", "🥈", "🥉"]
            lines = []
            for i, p in enumerate(players):
                medal = medals[i] if i < 3 else f"**{i+1}.**"
                val = f"{p.sacred_coins} 💰" if type == "coins" else (f"{p.get_total_cards()} cartes" if type == "cards" else f"{p.total_rifts_opened} failles")
                lines.append(f"{medal} **{p.username}** - {val}")
            embed.description = "\n".join(lines)
        
        await interaction.response.send_message(embed=embed)


async def setup(client: commands.Bot):
    """Charge le cog."""
    await client.add_cog(LegendsCog(client))
