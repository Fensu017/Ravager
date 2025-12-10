"""
Module de gestion de la base de données JSON pour la persistance des données.
"""
import json
import os
from typing import Dict, Optional
from models.player import Player


class DatabaseService:
    """Service de gestion de la base de données des joueurs."""
    
    def __init__(self, filepath: str = "data/players.json"):
        """
        Initialise le service de base de données.
        
        Args:
            filepath: Chemin vers le fichier JSON de sauvegarde.
        """
        self.filepath = filepath
        self._players: Dict[int, Player] = {}
        self._ensure_data_directory()
        self._load_data()

    def _ensure_data_directory(self) -> None:
        """Crée le dossier data s'il n'existe pas."""
        directory = os.path.dirname(self.filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)

    def _load_data(self) -> None:
        """Charge les données depuis le fichier JSON."""
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for user_id_str, player_data in data.items():
                        user_id = int(user_id_str)
                        self._players[user_id] = Player.from_dict(player_data)
                print(f"✅ Base de données chargée: {len(self._players)} joueurs")
            except (json.JSONDecodeError, Exception) as e:
                print(f"⚠️ Erreur lors du chargement de la base de données: {e}")
                self._players = {}
        else:
            print("📁 Nouvelle base de données créée")

    def save(self) -> None:
        """Sauvegarde les données dans le fichier JSON."""
        try:
            data = {
                str(user_id): player.to_dict() 
                for user_id, player in self._players.items()
            }
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Erreur lors de la sauvegarde: {e}")

    def get_player(self, user_id: int, username: str = "Inconnu") -> Player:
        """
        Récupère un joueur ou le crée s'il n'existe pas.
        
        Args:
            user_id: L'ID Discord du joueur.
            username: Le nom d'utilisateur (utilisé à la création).
            
        Returns:
            L'instance Player correspondante.
        """
        if user_id not in self._players:
            self._players[user_id] = Player(user_id=user_id, username=username)
            self.save()
        else:
            # Mettre à jour le nom d'utilisateur s'il a changé
            if self._players[user_id].username != username:
                self._players[user_id].username = username
        return self._players[user_id]

    def player_exists(self, user_id: int) -> bool:
        """Vérifie si un joueur existe dans la base de données."""
        return user_id in self._players

    def get_all_players(self) -> Dict[int, Player]:
        """Retourne tous les joueurs."""
        return self._players.copy()

    def get_leaderboard(self, limit: int = 10, sort_by: str = "coins") -> list:
        """
        Retourne le classement des joueurs.
        
        Args:
            limit: Nombre maximum de joueurs à retourner.
            sort_by: Critère de tri ('coins', 'cards', 'rifts').
            
        Returns:
            Liste de tuples (player, valeur) triée.
        """
        if sort_by == "coins":
            key_func = lambda p: p.sacred_coins
        elif sort_by == "cards":
            key_func = lambda p: p.get_total_cards()
        elif sort_by == "rifts":
            key_func = lambda p: p.total_rifts_opened
        else:
            key_func = lambda p: p.sacred_coins

        sorted_players = sorted(
            self._players.values(),
            key=key_func,
            reverse=True
        )
        return sorted_players[:limit]

    def update_player(self, player: Player) -> None:
        """
        Met à jour un joueur et sauvegarde.
        
        Args:
            player: L'instance Player à mettre à jour.
        """
        self._players[player.user_id] = player
        self.save()


# Instance globale du service de base de données
db = DatabaseService()
