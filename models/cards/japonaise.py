"""
Cartes de la mythologie Japonaise.
"""
from models.rarity import Rarity
from models.card import Card


JAPANESE_CARDS = [
    # === MORTEL ===
    Card(
        id="masque_tengu",
        name="Masque de Tengu",
        description="Le masque d'un esprit de la montagne.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/Tz9dD4Y.png"
    ),
    Card(
        id="grelot_inari",
        name="Grelot d'Inari",
        description="La clochette du dieu renard de la prospérité.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/GreIna.png"
    ),
    Card(
        id="ombrelle_tsukuyomi",
        name="Ombrelle de Tsukuyomi",
        description="Le parasol du dieu de la lune.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/OmbTsu.png"
    ),
    Card(
        id="peigne_izanami",
        name="Peigne d'Izanami",
        description="Le peigne de la déesse des enfers.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/PeiIza.png"
    ),
    Card(
        id="magatama_simple",
        name="Magatama Simple",
        description="Une perle courbe aux pouvoirs spirituels.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/MagSim.png"
    ),
    Card(
        id="sake_susanoo",
        name="Saké de Susanoo",
        description="Le breuvage qui vainquit Yamata no Orochi.",
        mythology="Japonaise",
        rarity=Rarity.MORTEL,
        image_url="https://i.imgur.com/SakSus.png"
    ),
    # === ASCENDANT ===
    Card(
        id="eventail_amaterasu",
        name="Éventail d'Amaterasu",
        description="L'éventail sacré de la déesse du soleil.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/Sy8cC3X.png"
    ),
    Card(
        id="tambour_raijin",
        name="Tambour de Raijin",
        description="Un tambour du dieu du tonnerre.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/TamRai.png"
    ),
    Card(
        id="sac_fujin",
        name="Sac de Fūjin",
        description="Le sac des vents du dieu des tempêtes.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/SacFuj.png"
    ),
    Card(
        id="lance_izanagi",
        name="Lance d'Izanagi",
        description="Ame-no-nuhoko, la lance céleste de la création.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/LanIza.png"
    ),
    # === ÉLITE ===
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
        id="katana_muramasa",
        name="Katana Muramasa",
        description="Une lame maudite assoiffée de sang.",
        mythology="Japonaise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/KatMur.png"
    ),
    # === TRANSCENDATEUR ===
    Card(
        id="kusanagi",
        name="Kusanagi-no-Tsurugi",
        description="L'épée céleste trouvée dans le dragon Yamata.",
        mythology="Japonaise",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Jp5tT0O.png"
    ),
]
