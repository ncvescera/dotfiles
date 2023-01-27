#!/bin/bash
function pacman_install () {
  sudo pacman -S --noconfirm "$@"
}

function paru_install() {
  paru -S --noconfirm "$@"
}

mkdir tmp

echo "Installing packages ..."
pacman_install git curl
echo "... Done"

echo "Installing paru ..."
sudo pacman -Syu
pacman_install "base-devel"
(cd tmp && git clone https://aur.archlinux.org/paru.git && cd paru && makepkg -si)
echo "... Done"

# installing aur packages
echo "Installing AUR packages ..."
paru_install python-pip ranger alacritty brave gnome-tweaks visual-studio-code-bin thunderbird ttf-meslo-nerd
echo "... Done"

echo "Installing gnome-browser-connector"
(cd tmp && git clone https://aur.archlinux.org/gnome-browser-connector.git && cd gnome-browser-connector/ && makepkg -si)
echo "... Done"

echo "Installing Gnome Extentions"
pip install gnome-extensions-cli
export PATH="/home/test/.local/bin:$PATH"
gext install arcmenu@arcmenu.com awesome-tiles@velitasali.com azclock@azclock.gitlab.com burn-my-windows@schneegans.github.com dash-to-panel@jderose9.github.com extension-list@tu.berry just-perfection-desktop@just-perfection no-overview@fthx rounded-window-corners@yilozt tophat@fflewddur.github.io user-theme@gnome-shell-extensions.gcampax.github.com
echo "... Done"

echo "Installing Dynamic Wallpaper"
curl -s https://wallpapers.manishk.dev/install.sh | bash -s THEME_CODE
echo "... Done"

echo "Installing Icon Theme"
(cd tmp && git clone https://github.com/vinceliuice/Qogir-icon-theme.git && cd Qogir-icon-theme/ && ./install.sh)
echo "... Done"

echo "Installig Configs"
mkdir ~/.config/alacritty
cp ./configs/alacritty/alacritty.yml ~/.config/alacritty
echo "... Done"

echo "Cleanup ..."
paru -R --noconfirm gnome-software gnome-text-editor
rm -rf tmp

