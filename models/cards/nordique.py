"""
Cartes de la mythologie Nordique.
"""
from models.rarity import Rarity
from models.card import Card


NORSE_CARDS = [
    # === MORTEL ===
    Card(
        id="corne_mead",
        name="Corne d'Hydromel",
        description="La coupe des festins du Valhalla.",
        mythology="Nordique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CorMea.png"
    ),
    Card(
        id="plume_huginn",
        name="Plume de Huginn",
        description="Une plume du corbeau de la pensée.",
        mythology="Nordique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PluHug.png"
    ),
    Card(
        id="plume_muninn",
        name="Plume de Muninn",
        description="Une plume du corbeau de la mémoire.",
        mythology="Nordique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PluMun.png"
    ),
    Card(
        id="filet_ran",
        name="Filet de Rán",
        description="Le filet de la déesse des noyés.",
        mythology="Nordique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FilRan.png"
    ),
    Card(
        id="corde_gleipnir",
        name="Corde Gleipnir",
        description="La chaîne magique retenant Fenrir.",
        mythology="Nordique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CorGle.png"
    ),
    # === ASCENDANT ===
    Card(
        id="rune_odin",
        name="Rune d'Odin",
        description="Une rune ancestrale gravée par le père de tous.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Qw6zA1V.png"
    ),
    Card(
        id="bracelet_freya",
        name="Bracelet de Freya",
        description="Le bijou enchanté de la déesse de l'amour.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Rx7bB2W.png"
    ),
    Card(
        id="pomme_idun",
        name="Pomme d'Idunn",
        description="Le fruit d'immortalité des dieux nordiques.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PomIdu.png"
    ),
    Card(
        id="gant_thor",
        name="Gant de Thor",
        description="Járngreipr, le gant pour manier Mjölnir.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/GanTho.png"
    ),
    Card(
        id="epee_tyr",
        name="Épée de Týr",
        description="La lame du dieu manchot de la guerre.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/EpeTyr.png"
    ),
    # === ÉLITE ===
    Card(
        id="ceinture_thor",
        name="Ceinture de Thor",
        description="Megingjörð, la ceinture doublant la force.",
        mythology="Nordique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ag6kK1F.png"
    ),
    Card(
        id="corne_heimdall",
        name="Corne de Heimdall",
        description="Gjallarhorn, la corne annonçant le Ragnarök.",
        mythology="Nordique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Bh7lL2G.png"
    ),
    Card(
        id="skidbladnir",
        name="Skidbladnir",
        description="Le navire pliable des dieux nordiques.",
        mythology="Nordique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Skidbl.png"
    ),
    # === TRANSCENDATEUR ===
    Card(
        id="mjolnir",
        name="Mjölnir",
        description="Le marteau de Thor, arme des dieux nordiques.",
        mythology="Nordique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Hn3rR8M.png"
    ),
    Card(
        id="gungnir",
        name="Gungnir",
        description="La lance d'Odin qui ne manque jamais sa cible.",
        mythology="Nordique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Io4sS9N.png"
    ),
]
