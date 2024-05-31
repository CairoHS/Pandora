@echo off
set "VENV=venv"
set "REQUIREMENTS=requirements.txt"
set "PROGRAM=main.py"

:MENU
cls
echo ====================
echo    MENU DE SERVERS
echo ====================
echo 1 - FRONT
echo 2 - BACK
echo 3 - Sair
echo ====================
set /p opcao=Escolher opção:

if "%opcao%"=="1" (
    echo Opção escolhida Front
) elseif "%opcao%"=="2" (
    cd back_end
    echo Opção escolhida Back

    python -m venv %VENV%

    if exist %REQUIREMENTS% (
        pip install -r %REQUIREMENTS%
    )

    start "" python %PROGRAM%

    cd ..
) elseif "%opcao%"=="0" (
    echo Saindo...
    exit /b
) else (
    echo Opção inválida! Por favor, escolha uma opção válida.
)

pause
goto MENU
