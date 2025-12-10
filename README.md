# 🌀 Failles des Légendes

Bot Discord de collection de cartes mythologiques.

## 📋 Prérequis

- **Python 3.10+** : [Télécharger ici](https://www.python.org/downloads/)
  - ⚠️ **IMPORTANT** : Cochez "Add Python to PATH" lors de l'installation !
- **Un compte Discord Developer** : [Créer une application](https://discord.com/developers/applications)

## 🚀 Installation rapide (Windows)

1. **Téléchargez** le projet depuis GitHub
2. **Double-cliquez** sur `setup.bat` pour installer automatiquement
3. **Éditez** le fichier `.env` et remplacez `VOTRE_TOKEN_ICI` par votre token Discord
4. **Double-cliquez** sur `run.bat` pour lancer le bot

## 🔧 Installation manuelle

```bash
# Créer l'environnement virtuel
python -m venv myenv

# Activer l'environnement (Windows)
myenv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Créer le fichier .env
echo DISCORD_TOKEN=votre_token_ici > .env

# Lancer le bot
python bot.py
```

## 🎮 Commandes du bot

| Commande | Description |
|----------|-------------|
| `/faille` | Ouvrir une Faille des Légendes (10 cartes) |
| `/inventaire` | Voir vos cartes |
| `/vendre` | Vendre une carte |
| `/boutique` | Voir la boutique |
| `/carte` | Voir les détails d'une carte |
| `/collection` | Voir toutes les cartes du jeu |
| `/profil` | Voir votre profil |
| `/classement` | Voir le classement |

## 💎 Raretés des cartes

| Rareté | Taux | Valeur |
|--------|------|--------|
| ⚪ Mortel | 50% | 5 💰 |
| 🟢 Ascendant | 30% | 25 💰 |
| 🟣 Élite | 15% | 150 💰 |
| 🟡 Transcendateur | 5% | 1000 💰 |

## 📁 Structure du projet

```
Ravager/
├── bot.py              # Point d'entrée
├── setup.bat           # Script d'installation (Windows)
├── run.bat             # Script de lancement (Windows)
├── requirements.txt    # Dépendances Python
├── .env                # Token Discord (à créer)
├── cogs/               # Commandes du bot
├── models/             # Modèles de données
├── services/           # Services (base de données)
├── assets/             # Images
└── data/               # Sauvegardes
```

## 🔑 Obtenir un token Discord

1. Allez sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Cliquez sur "New Application" et donnez un nom
3. Allez dans "Bot" → "Add Bot"
4. Cliquez sur "Reset Token" puis "Copy"
5. Collez le token dans le fichier `.env`

### Permissions du bot

Dans "OAuth2" → "URL Generator" :
- Scopes : `bot`, `applications.commands`
- Permissions : `Send Messages`, `Embed Links`, `Attach Files`, `Use Slash Commands`

## ❓ FAQ

**Q: Quand mes failles gratuites se réinitialisent ?**
> À minuit (heure serveur), vous récupérez 5 failles gratuites.

**Q: Puis-je échanger des cartes avec d'autres joueurs ?**
> Non, les échanges ne sont pas disponibles actuellement.

**Q: Comment voir mes cartes manquantes ?**
> Utilisez `/collection` - les cartes non possédées ont une ❌.

## ❓ Problèmes courants

**"Python n'est pas reconnu"**
→ Réinstallez Python en cochant "Add Python to PATH"

**"Module not found"**
→ Exécutez `setup.bat` ou `pip install -r requirements.txt`

**"Invalid token"**
→ Vérifiez que le token dans `.env` est correct et complet

---
📜 Projet éducatif - SupDeVinci B2B Python 2

Bonne chance dans votre quête des légendes ! 🌟
