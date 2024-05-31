@echo off
setlocal
set "VENV=.venv"
set "REQUIREMENTS=requirements.txt"
set "PROGRAM=main.py"
set "SCRIPT_NODE=teste"

:MENU
cls
echo ====================
echo    MENU DE SERVERS
echo ====================
echo 1 - FRONT
echo 2 - BACK
echo 0 - Sair
echo ====================
set /p opcao=Escolher opcaoo:

if "%opcao%"=="1" (
    echo Opção escolhida Front

    rem Verifica se o npm está instalado
    where npm >nul 2>nul

    if %errorlevel% neq 0 (
        echo npm não está instalado. Por favor, instale-o para continuar.
    exit /b
    )

    rem Verifica se o package.json está presente
        if not exist "package.json" (
            echo Arquivo package.json não encontrado neste diretório.
        exit /b
    )

    rem Executa o comando npm run
    start cmd /k npm run %SCRIPT_NODE%




) else if "%opcao%"=="2" (
    cd back_end
    echo Opção escolhida Back

    if not exist %VENV% (
        python -m venv %VENV%
    )

    call %VENV%\Scripts\activate

    if exist %REQUIREMENTS% (
        pip install -r %REQUIREMENTS%
    )

    start "" cmd /k "%VENV%\Scripts\python %PROGRAM%"


    cd ..

) else if "%opcao%"=="0" (
    echo Saindo...
    endlocal
    exit /b
) else (
    echo Opção inválida! Por favor, escolha uma opção válida.
)

pause
goto MENU
