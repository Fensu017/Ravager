"""
Cartes des mythologies Hindoue, Chinoise et Slave.
"""
from models.rarity import Rarity
from models.card import Card


# === HINDOUE ===
HINDU_CARDS = [
    # MORTEL
    Card(
        id="flute_krishna",
        name="Flûte de Krishna",
        description="L'instrument enchanté du dieu bleu.",
        mythology="Hindoue",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FluKri.png"
    ),
    Card(
        id="lotus_lakshmi",
        name="Lotus de Lakshmi",
        description="La fleur de la déesse de la fortune.",
        mythology="Hindoue",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/LotLak.png"
    ),
    Card(
        id="plume_paon_saraswati",
        name="Plume de Paon",
        description="Une plume du véhicule de Saraswati.",
        mythology="Hindoue",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PluPao.png"
    ),
    Card(
        id="tambourin_shiva",
        name="Tambourin de Shiva",
        description="Damaru, le tambour de la création.",
        mythology="Hindoue",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/TamShi.png"
    ),
    Card(
        id="defenses_ganesh",
        name="Défense de Ganesh",
        description="Une défense brisée du dieu éléphant.",
        mythology="Hindoue",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/DefGan.png"
    ),
    # ASCENDANT
    Card(
        id="conque_vishnu",
        name="Conque de Vishnu",
        description="Panchajanya, la conque du préservateur.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ConVis.png"
    ),
    Card(
        id="arc_rama",
        name="Arc de Rama",
        description="L'arc du prince avatar de Vishnu.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ArcRam.png"
    ),
    Card(
        id="masse_hanuman",
        name="Masse d'Hanuman",
        description="La massue du dieu singe.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/MasHan.png"
    ),
    # ÉLITE
    Card(
        id="trident_shiva",
        name="Trident de Shiva",
        description="Le trishula du dieu destructeur.",
        mythology="Hindoue",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/TriShi.png"
    ),
    Card(
        id="disque_vishnu",
        name="Disque de Vishnu",
        description="Sudarshana Chakra, l'arme tournoyante.",
        mythology="Hindoue",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/DisVis.png"
    ),
]

# === CHINOISE ===
CHINESE_CARDS = [
    # MORTEL
    Card(
        id="peche_immortalite",
        name="Pêche d'Immortalité",
        description="Le fruit du jardin de Xi Wangmu.",
        mythology="Chinoise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PecImm.png"
    ),
    Card(
        id="eventail_zhongli",
        name="Éventail de Zhongli Quan",
        description="L'éventail d'un des Huit Immortels.",
        mythology="Chinoise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/EveZho.png"
    ),
    Card(
        id="gourde_li_tieguai",
        name="Gourde de Li Tieguai",
        description="La gourde magique de l'immortel boiteux.",
        mythology="Chinoise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/GouLi.png"
    ),
    Card(
        id="piece_fu",
        name="Pièce de Fu",
        description="Une pièce de chance et de prospérité.",
        mythology="Chinoise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PieFu.png"
    ),
    Card(
        id="ecaille_ao_guang",
        name="Écaille d'Ao Guang",
        description="Une écaille du roi dragon des mers de l'Est.",
        mythology="Chinoise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/EcaAo.png"
    ),
    # ASCENDANT
    Card(
        id="perle_dragon",
        name="Perle de Dragon",
        description="Une perle convoitée par les dragons.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PerDra.png"
    ),
    # ÉLITE
    Card(
        id="baton_wukong",
        name="Bâton de Wukong",
        description="Ruyi Jingu Bang, le bâton extensible.",
        mythology="Chinoise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/BatWuk.png"
    ),
]

# === SLAVE ===
SLAVIC_CARDS = [
    # MORTEL
    Card(
        id="oeuf_rod",
        name="Œuf de Rod",
        description="L'œuf cosmique du dieu créateur slave.",
        mythology="Slave",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/OeuRod.png"
    ),
    Card(
        id="roue_svarog",
        name="Roue de Svarog",
        description="Le symbole solaire du dieu forgeron.",
        mythology="Slave",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/RouSva.png"
    ),
    Card(
        id="plume_simargl",
        name="Plume de Simargl",
        description="Une plume du chien ailé gardien.",
        mythology="Slave",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PluSim.png"
    ),
    Card(
        id="kokoshnik_lada",
        name="Kokoshnik de Lada",
        description="La couronne de la déesse de l'amour.",
        mythology="Slave",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/KokLad.png"
    ),
    # ÉLITE
    Card(
        id="epee_perun",
        name="Épée de Perun",
        description="La lame du dieu slave du tonnerre.",
        mythology="Slave",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/EpePer.png"
    ),
]
