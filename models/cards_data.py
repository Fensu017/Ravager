"""
Base de données des cartes légendaires.
Toutes les cartes du jeu sont définies ici.
"""
from models.rarity import Rarity
from models.card import Card


# === CARTES ASCENDANT (75% - 10 pièces) ===
ASCENDANT_CARDS = [
    # --- Grecque ---
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
    Card(
        id="pomme_discorde",
        name="Pomme de Discorde",
        description="La pomme d'or qui déclencha la guerre de Troie.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PomDis.png"
    ),
    Card(
        id="fil_ariane",
        name="Fil d'Ariane",
        description="Le fil qui guida Thésée hors du labyrinthe.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FilAri.png"
    ),
    Card(
        id="fleche_eros",
        name="Flèche d'Éros",
        description="Une flèche du dieu de l'amour.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FleEros.png"
    ),
    Card(
        id="amphore_dionysos",
        name="Amphore de Dionysos",
        description="Le récipient du dieu du vin et de la fête.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/AmpDio.png"
    ),
    Card(
        id="torche_promethee",
        name="Torche de Prométhée",
        description="La flamme volée aux dieux pour les mortels.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/TorPro.png"
    ),
    Card(
        id="casque_achille",
        name="Casque d'Achille",
        description="Le casque du plus grand héros grec.",
        mythology="Grecque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CasAch.png"
    ),
    # --- Égyptienne ---
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
        id="scarabee_khepri",
        name="Scarabée de Khépri",
        description="L'amulette du dieu scarabée du soleil levant.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ScarKhe.png"
    ),
    Card(
        id="lotus_nefertem",
        name="Lotus de Néfertem",
        description="La fleur sacrée du dieu des parfums.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/LotNef.png"
    ),
    Card(
        id="sistre_hathor",
        name="Sistre d'Hathor",
        description="L'instrument de la déesse de la joie.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/SisHat.png"
    ),
    Card(
        id="bandeau_sekhmet",
        name="Bandeau de Sekhmet",
        description="Le diadème de la déesse lionne.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/BanSek.png"
    ),
    Card(
        id="crochet_sobek",
        name="Crochet de Sobek",
        description="L'arme du dieu crocodile du Nil.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CroSob.png"
    ),
    Card(
        id="papyrus_thot",
        name="Papyrus de Thot",
        description="Un parchemin du dieu de la sagesse.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PapTho.png"
    ),
    Card(
        id="collier_bastet",
        name="Collier de Bastet",
        description="Le bijou de la déesse chat protectrice.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ColBas.png"
    ),
    Card(
        id="uraeus_wadjet",
        name="Uraeus de Wadjet",
        description="Le cobra sacré protecteur des pharaons.",
        mythology="Égyptienne",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/UraWad.png"
    ),
    # --- Nordique ---
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
        id="corde_gleipnir",
        name="Corde Gleipnir",
        description="La chaîne magique retenant Fenrir.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CorGle.png"
    ),
    Card(
        id="plume_huginn",
        name="Plume de Huginn",
        description="Une plume du corbeau de la pensée.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PluHug.png"
    ),
    Card(
        id="plume_muninn",
        name="Plume de Muninn",
        description="Une plume du corbeau de la mémoire.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PluMun.png"
    ),
    Card(
        id="corne_mead",
        name="Corne d'Hydromel",
        description="La coupe des festins du Valhalla.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CorMea.png"
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
    Card(
        id="filet_ran",
        name="Filet de Rán",
        description="Le filet de la déesse des noyés.",
        mythology="Nordique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FilRan.png"
    ),
    # --- Japonaise ---
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
        id="grelot_inari",
        name="Grelot d'Inari",
        description="La clochette du dieu renard de la prospérité.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/GreIna.png"
    ),
    Card(
        id="ombrelle_tsukuyomi",
        name="Ombrelle de Tsukuyomi",
        description="Le parasol du dieu de la lune.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/OmbTsu.png"
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
        id="peigne_izanami",
        name="Peigne d'Izanami",
        description="Le peigne de la déesse des enfers.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PeiIza.png"
    ),
    Card(
        id="lance_izanagi",
        name="Lance d'Izanagi",
        description="Ame-no-nuhoko, la lance céleste de la création.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/LanIza.png"
    ),
    Card(
        id="magatama_simple",
        name="Magatama Simple",
        description="Une perle courbe aux pouvoirs spirituels.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/MagSim.png"
    ),
    Card(
        id="sake_susanoo",
        name="Saké de Susanoo",
        description="Le breuvage qui vainquit Yamata no Orochi.",
        mythology="Japonaise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/SakSus.png"
    ),
    # --- Aztèque / Maya ---
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
    Card(
        id="coquillage_tlaloc",
        name="Coquillage de Tláloc",
        description="Le coquillage du dieu de la pluie.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CoqTla.png"
    ),
    Card(
        id="obsidienne_huitzilopochtli",
        name="Obsidienne d'Huitzilopochtli",
        description="La pierre noire du dieu de la guerre.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ObsHui.png"
    ),
    Card(
        id="fleur_xochiquetzal",
        name="Fleur de Xochiquetzal",
        description="La fleur de la déesse de la beauté.",
        mythology="Aztèque",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FloXoc.png"
    ),
    Card(
        id="jade_kukulkan",
        name="Jade de Kukulkán",
        description="Une pierre précieuse du serpent maya.",
        mythology="Maya",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/JadKuk.png"
    ),
    Card(
        id="glyphe_itzamna",
        name="Glyphe d'Itzamná",
        description="Un symbole du dieu créateur maya.",
        mythology="Maya",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/GlyItz.png"
    ),
    # --- Celtique ---
    Card(
        id="gui_druide",
        name="Gui du Druide",
        description="La plante sacrée des anciens druides.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/GuiDru.png"
    ),
    Card(
        id="torque_cernunnos",
        name="Torque de Cernunnos",
        description="Le collier du dieu aux bois de cerf.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/TorCer.png"
    ),
    Card(
        id="broche_brigid",
        name="Broche de Brigid",
        description="Le bijou de la déesse du foyer.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/BroBri.png"
    ),
    Card(
        id="harpe_dagda",
        name="Harpe du Dagda",
        description="Uaithne, la harpe aux saisons.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/HarDag.png"
    ),
    Card(
        id="faucille_druide",
        name="Faucille d'Or",
        description="L'outil sacré pour récolter le gui.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FauOr.png"
    ),
    Card(
        id="crane_bran",
        name="Crâne de Brân",
        description="La tête prophétique du géant.",
        mythology="Celtique",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/CraBra.png"
    ),
    # --- Hindoue ---
    Card(
        id="flute_krishna",
        name="Flûte de Krishna",
        description="L'instrument enchanté du dieu bleu.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/FluKri.png"
    ),
    Card(
        id="lotus_lakshmi",
        name="Lotus de Lakshmi",
        description="La fleur de la déesse de la fortune.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/LotLak.png"
    ),
    Card(
        id="plume_paon_saraswati",
        name="Plume de Paon",
        description="Une plume du véhicule de Saraswati.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PluPao.png"
    ),
    Card(
        id="conque_vishnu",
        name="Conque de Vishnu",
        description="Panchajanya, la conque du préservateur.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/ConVis.png"
    ),
    Card(
        id="tambourin_shiva",
        name="Tambourin de Shiva",
        description="Damaru, le tambour de la création.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/TamShi.png"
    ),
    Card(
        id="defenses_ganesh",
        name="Défense de Ganesh",
        description="Une défense brisée du dieu éléphant.",
        mythology="Hindoue",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/DefGan.png"
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
    # --- Chinoise ---
    Card(
        id="peche_immortalite",
        name="Pêche d'Immortalité",
        description="Le fruit du jardin de Xi Wangmu.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PecImm.png"
    ),
    Card(
        id="eventail_zhongli",
        name="Éventail de Zhongli Quan",
        description="L'éventail d'un des Huit Immortels.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/EveZho.png"
    ),
    Card(
        id="gourde_li_tieguai",
        name="Gourde de Li Tieguai",
        description="La gourde magique de l'immortel boiteux.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/GouLi.png"
    ),
    Card(
        id="perle_dragon",
        name="Perle de Dragon",
        description="Une perle convoitée par les dragons.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PerDra.png"
    ),
    Card(
        id="piece_fu",
        name="Pièce de Fu",
        description="Une pièce de chance et de prospérité.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PieFu.png"
    ),
    Card(
        id="ecaille_ao_guang",
        name="Écaille d'Ao Guang",
        description="Une écaille du roi dragon des mers de l'Est.",
        mythology="Chinoise",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/EcaAo.png"
    ),
    # --- Slave ---
    Card(
        id="oeuf_rod",
        name="Œuf de Rod",
        description="L'œuf cosmique du dieu créateur slave.",
        mythology="Slave",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/OeuRod.png"
    ),
    Card(
        id="roue_svarog",
        name="Roue de Svarog",
        description="Le symbole solaire du dieu forgeron.",
        mythology="Slave",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/RouSva.png"
    ),
    Card(
        id="plume_simargl",
        name="Plume de Simargl",
        description="Une plume du chien ailé gardien.",
        mythology="Slave",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/PluSim.png"
    ),
    Card(
        id="kokoshnik_lada",
        name="Kokoshnik de Lada",
        description="La couronne de la déesse de l'amour.",
        mythology="Slave",
        rarity=Rarity.ASCENDANT,
        image_url="https://i.imgur.com/KokLad.png"
    ),
]


# === CARTES ÉLITE (20% - 300 pièces) ===
ELITE_CARDS = [
    # --- Grecque ---
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
    # --- Égyptienne ---
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
        id="couronne_osiris",
        name="Couronne Atef",
        description="La couronne blanche d'Osiris.",
        mythology="Égyptienne",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/CouOsi.png"
    ),
    Card(
        id="fleaux_pharaon",
        name="Fléau du Pharaon",
        description="Le nekhekh, symbole de pouvoir royal.",
        mythology="Égyptienne",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/FlePha.png"
    ),
    # --- Nordique ---
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
        id="navire_naglfar",
        name="Fragment de Naglfar",
        description="Un morceau du navire fait d'ongles des morts.",
        mythology="Nordique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/NavNag.png"
    ),
    Card(
        id="skidbladnir",
        name="Skidbladnir",
        description="Le navire pliable des dieux nordiques.",
        mythology="Nordique",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Skidbl.png"
    ),
    # --- Japonaise ---
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
    # --- Maya / Aztèque ---
    Card(
        id="calendrier_maya",
        name="Calendrier Maya",
        description="Le disque prophétique des cycles cosmiques.",
        mythology="Maya",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/Ek0oO5J.png"
    ),
    Card(
        id="couteau_sacrificiel",
        name="Couteau Sacrificiel",
        description="Le tecpatl d'obsidienne des rituels aztèques.",
        mythology="Aztèque",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/CouSac.png"
    ),
    # --- Celtique ---
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
    # --- Hindoue ---
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
    # --- Chinoise ---
    Card(
        id="baton_wukong",
        name="Bâton de Wukong",
        description="Ruyi Jingu Bang, le bâton extensible.",
        mythology="Chinoise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/BatWuk.png"
    ),
    Card(
        id="eventail_nezha",
        name="Anneaux de Nezha",
        description="Les anneaux célestes du prince dragon.",
        mythology="Chinoise",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/AnnNez.png"
    ),
    # --- Slave ---
    Card(
        id="epee_perun",
        name="Épée de Perun",
        description="La lame du dieu slave du tonnerre.",
        mythology="Slave",
        rarity=Rarity.ELITE,
        image_url="https://i.imgur.com/EpePer.png"
    ),
]


# === CARTES TRANSCENDATEUR (5% - 2000 pièces) ===
TRANSCENDATEUR_CARDS = [
    # --- Grecque ---
    Card(
        id="eclair_zeus",
        name="Éclair de Zeus",
        description="La foudre ultime du roi des dieux de l'Olympe.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Fl1pP6K.png"
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
        id="caducee_hermes",
        name="Caducée d'Hermès",
        description="Le bâton aux serpents entrelacés du messager divin.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Ou0yY5T.png"
    ),
    Card(
        id="tete_meduse",
        name="Tête de Méduse",
        description="Le trophée pétrifiant de Persée.",
        mythology="Grecque",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/TetMed.png"
    ),
    # --- Nordique ---
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
        id="anneau_draupnir",
        name="Draupnir",
        description="L'anneau d'or d'Odin se multipliant à l'infini.",
        mythology="Nordique",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Nt9xX4S.png"
    ),
    # --- Japonaise ---
    Card(
        id="kusanagi",
        name="Kusanagi-no-Tsurugi",
        description="L'épée céleste trouvée dans le dragon Yamata.",
        mythology="Japonaise",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Jp5tT0O.png"
    ),
    Card(
        id="masamune",
        name="Masamune",
        description="Le katana parfait du maître forgeron légendaire.",
        mythology="Japonaise",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Masamu.png"
    ),
    # --- Égyptienne ---
    Card(
        id="crosse_osiris",
        name="Crosse d'Osiris",
        description="Le sceptre du dieu de la résurrection.",
        mythology="Égyptienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/Kq6uU1P.png"
    ),
    Card(
        id="livre_morts",
        name="Livre des Morts",
        description="Le papyrus guidant les âmes vers l'au-delà.",
        mythology="Égyptienne",
        rarity=Rarity.TRANSCENDATEUR,
        image_url="https://i.imgur.com/LivMor.png"
    ),
    # --- Arthurienne ---
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
    # --- Celtique ---
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


# Base de données complète des cartes
CARDS_DATABASE = ASCENDANT_CARDS + ELITE_CARDS + TRANSCENDATEUR_CARDS
