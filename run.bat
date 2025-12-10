@echo off
echo ========================================
echo   Failles des Legendes - Demarrage
echo ========================================
echo.

:: Vérifier si l'environnement virtuel existe
if not exist "myenv\Scripts\activate.bat" (
    echo [ERREUR] Environnement virtuel non trouve.
    echo Executez d'abord: setup.bat
    pause
    exit /b 1
)

:: Vérifier le fichier .env
if not exist ".env" (
    echo [ERREUR] Fichier .env manquant!
    echo Executez d'abord: setup.bat
    pause
    exit /b 1
)

:: Lancer le bot
echo [INFO] Demarrage du bot...
echo [INFO] Appuyez sur Ctrl+C pour arreter.
echo.
call myenv\Scripts\activate.bat
python bot.py

:: Si le bot s'arrête
echo.
echo [INFO] Bot arrete.
pause
