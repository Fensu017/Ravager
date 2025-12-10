"""
Base de données des cartes légendaires.
Toutes les cartes du jeu sont définies ici.
"""
from models.rarity import Rarity
from models.card import Card


# === CARTES ASCENDANT (75% - 10 pièces) ===
ASCENDANT_CARDS = [
    Card(
        id="arc_apollon",
        name="Arc d'Apollon",
        description="L'arc doré du dieu grec de la lumière et de la musique.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/8qY5Z3N.png"
    ),
    Card(
        id="sandales_hermes",
        name="Sandales d'Hermès",
        description="Les sandales ailées du messager des dieux.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/JK7vX2M.png"
    ),
    Card(
        id="corne_abondance",
        name="Corne d'Abondance",
        description="La corne magique offrant richesse infinie.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Lm9pQ4R.png"
    ),
    Card(
        id="plume_maat",
        name="Plume de Maât",
        description="La plume de vérité de la déesse égyptienne.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Nw3xK8S.png"
    ),
    Card(
        id="ankh_isis",
        name="Ankh d'Isis",
        description="Le symbole de vie de la déesse de la magie.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Pv5yT9U.png"
    ),
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
        id="eventail_amaterasu",
        name="Éventail d'Amaterasu",
        description="L'éventail sacré de la déesse du soleil.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Sy8cC3X.png"
    ),
    Card(
        id="masque_tengu",
        name="Masque de Tengu",
        description="Le masque d'un esprit de la montagne.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Tz9dD4Y.png"
    ),
    Card(
        id="plume_quetzalcoatl",
        name="Plume de Quetzalcóatl",
        description="Une plume du serpent à plumes.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Ua0eE5Z.png"
    ),
]


# === CARTES ÉLITE (20% - 300 pièces) ===
ELITE_CARDS = [
    Card(
        id="trident_poseidon",
        name="Trident de Poséidon",
        description="L'arme légendaire du dieu des mers.",
        mythology="Grecque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Vb1fF6A.png"
    ),
    Card(
        id="casque_hades",
        name="Casque d'Hadès",
        description="Le casque d'invisibilité du seigneur des Enfers.",
        mythology="Grecque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Wc2gG7B.png"
    ),
    Card(
        id="bouclier_athena",
        name="Égide d'Athéna",
        description="Le bouclier divin orné de la tête de Méduse.",
        mythology="Grecque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Xd3hH8C.png"
    ),
    Card(
        id="oeil_ra",
        name="Œil de Râ",
        description="L'œil flamboyant du dieu soleil égyptien.",
        mythology="Égyptienne",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ye4iI9D.png"
    ),
    Card(
        id="sceptre_anubis",
        name="Sceptre d'Anubis",
        description="Le bâton du guide des âmes.",
        mythology="Égyptienne",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Zf5jJ0E.png"
    ),
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
        id="miroir_yata",
        name="Miroir Yata",
        description="Le miroir sacré révélant la vérité.",
        mythology="Japonaise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ci8mM3H.png"
    ),
    Card(
        id="joyau_yasakani",
        name="Joyau Yasakani",
        description="La perle impériale de bienveillance.",
        mythology="Japonaise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Dj9nN4I.png"
    ),
    Card(
        id="calendrier_maya",
        name="Calendrier Maya",
        description="Le disque prophétique des cycles cosmiques.",
        mythology="Maya",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ek0oO5J.png"
    ),
]


# === CARTES TRANSCENDATEUR (5% - 2000 pièces) ===
TRANSCENDATEUR_CARDS = [
    Card(
        id="eclair_zeus",
        name="Éclair de Zeus",
        description="La foudre ultime du roi des dieux de l'Olympe.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Fl1pP6K.png"
    ),
    Card(
        id="excalibur",
        name="Excalibur",
        description="L'épée légendaire du Roi Arthur, symbole de justice.",
        mythology="Arthurienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Gm2qQ7L.png"
    ),
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
    Card(
        id="kusanagi",
        name="Kusanagi-no-Tsurugi",
        description="L'épée céleste trouvée dans le dragon Yamata.",
        mythology="Japonaise",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Jp5tT0O.png"
    ),
    Card(
        id="crosse_osiris",
        name="Crosse d'Osiris",
        description="Le sceptre du dieu de la résurrection.",
        mythology="Égyptienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Kq6uU1P.png"
    ),
    Card(
        id="graal",
        name="Saint Graal",
        description="La coupe sacrée offrant la vie éternelle.",
        mythology="Arthurienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Lr7vV2Q.png"
    ),
    Card(
        id="arc_artemis",
        name="Arc d'Artémis",
        description="L'arc argenté de la déesse de la chasse.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Ms8wW3R.png"
    ),
    Card(
        id="anneau_draupnir",
        name="Draupnir",
        description="L'anneau d'or d'Odin se multipliant à l'infini.",
        mythology="Nordique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Nt9xX4S.png"
    ),
    Card(
        id="caducee_hermes",
        name="Caducée d'Hermès",
        description="Le bâton aux serpents entrelacés du messager divin.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Ou0yY5T.png"
    ),
]


# Base de données complète des cartes
CARDS_DATABASE = ASCENDANT_CARDS + ELITE_CARDS + TRANSCENDATEUR_CARDS
