"""
Cartes de la mythologie Égyptienne.
"""
from models.rarity import Rarity
from models.card import Card


EGYPTIAN_CARDS = [
    # === MORTEL ===
    Card(
        id="scarabee_khepri",
        name="Scarabée de Khépri",
        description="L'amulette du dieu scarabée du soleil levant.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/ScarKhe.png"
    ),
    Card(
        id="lotus_nefertem",
        name="Lotus de Néfertem",
        description="La fleur sacrée du dieu des parfums.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/LotNef.png"
    ),
    Card(
        id="sistre_hathor",
        name="Sistre d'Hathor",
        description="L'instrument de la déesse de la joie.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/SisHat.png"
    ),
    Card(
        id="bandeau_sekhmet",
        name="Bandeau de Sekhmet",
        description="Le diadème de la déesse lionne.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/BanSek.png"
    ),
    Card(
        id="crochet_sobek",
        name="Crochet de Sobek",
        description="L'arme du dieu crocodile du Nil.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CroSob.png"
    ),
    Card(
        id="papyrus_thot",
        name="Papyrus de Thot",
        description="Un parchemin du dieu de la sagesse.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PapTho.png"
    ),
    Card(
        id="collier_bastet",
        name="Collier de Bastet",
        description="Le bijou de la déesse chat protectrice.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/ColBas.png"
    ),
    Card(
        id="uraeus_wadjet",
        name="Uraeus de Wadjet",
        description="Le cobra sacré protecteur des pharaons.",
        mythology="Égyptienne",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/UraWad.png"
    ),
    # === ASCENDANT ===
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
    # === ÉLITE ===
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
    # === TRANSCENDATEUR ===
    Card(
        id="crosse_osiris",
        name="Crosse d'Osiris",
        description="Le sceptre du dieu de la résurrection.",
        mythology="Égyptienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Kq6uU1P.png"
    ),
]
