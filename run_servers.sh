#!/bin/bash

VENV=".venv"

REQUIREMENTS="requirements.txt"

PROGRAM="main.py"


while true; do
    clear
    echo "===================="
    echo "   MENU DE SERVERS  "
    echo "===================="
    echo "1 - FRONT           "
    echo "2 - BACK            "
    echo "0 - Sair            "
    echo "===================="
    echo -n "Escolher opção: "
    read opcao

    case $opcao in
        1)
        echo "Opção escolhida Front"

        ;;

        2)

            cd back_end

            echo "Opção escolhida Back"

            if [ ! -d $VENV ]; then
                python3 -m venv $VENV
            fi

            source $VENV/bin/activate

            if [ -f $REQUIREMENTS ]; then
                pip install -r $REQUIREMENTS
            fi

            gnome-terminal -- bash -c "source $VENV/bin/activate; python3 $PROGRAM; exec bash"

            cd ..

            deactivate
            ;;

        0)
            echo "Saindo..."
            break;
            ;;

        *)
            echo "Opção inválida! Por favor, escolha uma opção válida."
    esac

    echo "Pressione Enter para continuar..."
    read
done

        



    
