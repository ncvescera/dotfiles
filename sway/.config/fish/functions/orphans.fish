function orphans
    echo -e "\e[1mOrphans PKGS: \e[0m \n"
    sudo pacman -Qtd
end

function orphans_purge 
        echo -e "\e[1m\e[31mKilling Orphans !! \e[0m \n"
        sudo pacman -Rns (pacman -Qtdq)
end
