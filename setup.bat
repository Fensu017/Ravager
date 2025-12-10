@echo off
echo ========================================
echo   Installation de Failles des Legendes
echo ========================================
echo.

:: Vérifier si Python est installé
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH.
    echo Veuillez installer Python 3.10+ depuis https://www.python.org/downloads/
    echo IMPORTANT: Cochez "Add Python to PATH" lors de l'installation!
    pause
    exit /b 1
)

echo [OK] Python detecte.
echo.

:: Créer l'environnement virtuel s'il n'existe pas
if not exist "myenv" (
    echo [INFO] Creation de l'environnement virtuel...
    python -m venv myenv
    echo [OK] Environnement virtuel cree.
) else (
    echo [OK] Environnement virtuel existe deja.
)
echo.

:: Activer l'environnement et installer les dépendances
echo [INFO] Installation des dependances...
call myenv\Scripts\activate.bat
pip install -r requirements.txt --quiet
echo [OK] Dependances installees.
echo.

:: Vérifier le fichier .env
if not exist ".env" (
    echo [ATTENTION] Fichier .env manquant!
    echo Creez un fichier .env avec votre token Discord:
    echo.
    echo   DISCORD_TOKEN=votre_token_ici
    echo.
    echo Pour obtenir un token:
    echo   1. Allez sur https://discord.com/developers/applications
    echo   2. Creez une application
    echo   3. Allez dans "Bot" et copiez le token
    echo.
    
    :: Créer un fichier .env template
    echo DISCORD_TOKEN=VOTRE_TOKEN_ICI> .env
    echo [INFO] Fichier .env cree. Editez-le avec votre token!
) else (
    echo [OK] Fichier .env trouve.
)
echo.

:: Créer le dossier data s'il n'existe pas
if not exist "data" (
    mkdir data
    echo [OK] Dossier data cree.
)

echo ========================================
echo   Installation terminee!
echo ========================================
echo.
echo Pour lancer le bot, executez: run.bat
echo.
pause
