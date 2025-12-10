"""
Cartes de la mythologie Grecque.
"""
from models.rarity import Rarity
from models.card import Card


GREEK_CARDS = [
    # === MORTEL ===
    Card(
        id="fil_ariane",
        name="Fil d'Ariane",
        description="Le fil qui guida Thésée hors du labyrinthe.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FilAri.png"
    ),
    Card(
        id="fleche_eros",
        name="Flèche d'Éros",
        description="Une flèche du dieu de l'amour.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FleEros.png"
    ),
    Card(
        id="amphore_dionysos",
        name="Amphore de Dionysos",
        description="Le récipient du dieu du vin et de la fête.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/AmpDio.png"
    ),
    Card(
        id="torche_promethee",
        name="Torche de Prométhée",
        description="La flamme volée aux dieux pour les mortels.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/TorPro.png"
    ),
    Card(
        id="casque_achille",
        name="Casque d'Achille",
        description="Le casque du plus grand héros grec.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CasAch.png"
    ),
    Card(
        id="pomme_discorde",
        name="Pomme de Discorde",
        description="La pomme d'or qui déclencha la guerre de Troie.",
        mythology="Grecque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PomDis.png"
    ),
    # === ASCENDANT ===
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
        id="lyre_orphee",
        name="Lyre d'Orphée",
        description="L'instrument qui charmait les bêtes et les dieux.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/LyreOrp.png"
    ),
    # === ÉLITE ===
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
        id="ceinture_hippolyte",
        name="Ceinture d'Hippolyte",
        description="La ceinture de la reine des Amazones.",
        mythology="Grecque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/CeiHip.png"
    ),
    Card(
        id="arc_herakles",
        name="Arc d'Héraclès",
        description="L'arc empoisonné du plus grand héros.",
        mythology="Grecque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/ArcHer.png"
    ),
    # === TRANSCENDATEUR ===
    Card(
        id="eclair_zeus",
        name="Éclair de Zeus",
        description="La foudre ultime du roi des dieux de l'Olympe.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Fl1pP6K.png"
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
