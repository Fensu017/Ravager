"""
Cartes des mythologies Aztèque, Maya et Celtique.
"""
from models.rarity import Rarity
from models.card import Card


# === AZTÈQUE / MAYA ===
AZTEC_MAYA_CARDS = [
    # MORTEL
    Card(
        id="coquillage_tlaloc",
        name="Coquillage de Tláloc",
        description="Le coquillage du dieu de la pluie.",
        mythology="Aztèque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CoqTla.png"
    ),
    Card(
        id="obsidienne_huitzilopochtli",
        name="Obsidienne d'Huitzilopochtli",
        description="La pierre noire du dieu de la guerre.",
        mythology="Aztèque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/ObsHui.png"
    ),
    Card(
        id="fleur_xochiquetzal",
        name="Fleur de Xochiquetzal",
        description="La fleur de la déesse de la beauté.",
        mythology="Aztèque",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FloXoc.png"
    ),
    Card(
        id="jade_kukulkan",
        name="Jade de Kukulkán",
        description="Une pierre précieuse du serpent maya.",
        mythology="Maya",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/JadKuk.png"
    ),
    Card(
        id="glyphe_itzamna",
        name="Glyphe d'Itzamná",
        description="Un symbole du dieu créateur maya.",
        mythology="Maya",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/GlyItz.png"
    ),
    # ASCENDANT
    Card(
        id="plume_quetzalcoatl",
        name="Plume de Quetzalcóatl",
        description="Une plume du serpent à plumes.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Ua0eE5Z.png"
    ),
    Card(
        id="miroir_tezcatlipoca",
        name="Miroir de Tezcatlipoca",
        description="Le miroir fumant du dieu de la nuit.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/MirTez.png"
    ),
    Card(
        id="masque_xiuhtecuhtli",
        name="Masque de Xiuhtecuhtli",
        description="Le masque turquoise du dieu du feu.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/MasXiu.png"
    ),
    # ÉLITE
    Card(
        id="calendrier_maya",
        name="Calendrier Maya",
        description="Le disque prophétique des cycles cosmiques.",
        mythology="Maya",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ek0oO5J.png"
    ),
]

# === CELTIQUE ===
CELTIC_CARDS = [
    # MORTEL
    Card(
        id="gui_druide",
        name="Gui du Druide",
        description="La plante sacrée des anciens druides.",
        mythology="Celtique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/GuiDru.png"
    ),
    Card(
        id="broche_brigid",
        name="Broche de Brigid",
        description="Le bijou de la déesse du foyer.",
        mythology="Celtique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/BroBri.png"
    ),
    Card(
        id="faucille_druide",
        name="Faucille d'Or",
        description="L'outil sacré pour récolter le gui.",
        mythology="Celtique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/FauOr.png"
    ),
    Card(
        id="crane_bran",
        name="Crâne de Brân",
        description="La tête prophétique du géant.",
        mythology="Celtique",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/CraBra.png"
    ),
    # ASCENDANT
    Card(
        id="torque_cernunnos",
        name="Torque de Cernunnos",
        description="Le collier du dieu aux bois de cerf.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/TorCer.png"
    ),
    Card(
        id="harpe_dagda",
        name="Harpe du Dagda",
        description="Uaithne, la harpe aux saisons.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/HarDag.png"
    ),
    # ÉLITE
    Card(
        id="chaudron_dagda",
        name="Chaudron du Dagda",
        description="Le chaudron d'abondance infinie.",
        mythology="Celtique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/ChaDag.png"
    ),
    Card(
        id="lance_lug",
        name="Lance de Lug",
        description="La lance invincible du dieu solaire.",
        mythology="Celtique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/LanLug.png"
    ),
    # TRANSCENDATEUR
    Card(
        id="pierre_fal",
        name="Pierre de Fál",
        description="La pierre du destin qui crie pour le vrai roi.",
        mythology="Celtique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/PieFal.png"
    ),
    Card(
        id="epee_nuada",
        name="Épée de Nuada",
        description="Claíomh Solais, l'épée de lumière invincible.",
        mythology="Celtique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/EpeNua.png"
    ),
]

# === ARTHURIENNE ===
ARTHURIAN_CARDS = [
    # TRANSCENDATEUR
    Card(
        id="excalibur",
        name="Excalibur",
        description="L'épée légendaire du Roi Arthur, symbole de justice.",
        mythology="Arthurienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Gm2qQ7L.png"
    ),
    Card(
        id="graal",
        name="Saint Graal",
        description="La coupe sacrée offrant la vie éternelle.",
        mythology="Arthurienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Lr7vV2Q.png"
    ),
]
