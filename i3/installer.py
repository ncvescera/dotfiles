import subprocess, sys

def main():
    install_base()
    install_paru()
    install_ohmyposh()
    install_packages()
    install_configs()
    config_nvim()
    config_espanso()
    config_docker()


def install_base():
    # updates and needed
    __execute_command("sudo pacman -Syu", shell="bash")
    __execute_command("sudo pacman -S git", shell="bash")
    __execute_command("sudo pacman -S --needed base-devel", shell="bash")

    # fish
    __execute_command("sudo pacman -S fish", shell="bash")

    # default shell
    __execute_command("chsh \"$(which fish)\"", shell="bash")

    # paths
    __execute_command("fish_add_path /usr/local/bin")
    __execute_command("fish_add_path ~/.local/bin")


def install_paru():
    __execute_command("git clone https://aur.archlinux.org/paru.git")
    __execute_command("cd paru && makepkg -si && cd ..")
    __execute_command("paru")
    __execute_command("rm -rf paru")

    # uncomment Color form pacman_conf.d
    # uncomment reversoredr from paru.conf

def install_ohmyposh():
    __execute_command("paru -S ttf-juliamono noto-fonts-emoji") # ttf-meslo-nerd-font-powerlevel10k")
    __execute_command("curl -s https://ohmyposh.dev/install.sh | bash -s")


def install_packages():
    packages = [
        "alacritty",
        "bat",
        "openfortivpn",
        "tmux",
        "smug",
        "tldr",
        "neovim",
        "visual-studio-code-bin",
        "librewolf",
        "brave-bin",
        "docker",
        "docker-compose",
        "nvidia-container-toolkit",
        "libnvidia-container",
        "go",
        "python-poetry",
        "thunderbird",
        "ferdium",
        "discord",
        "teams-for-linux",
        # "flameshot",
        "lorien-bin",
        "xournalpp",
        # "zenmonitor3-git",
        "jabref-bin",
        # "gwe",
        "localsend",
        "qbittorrent",
        "zathura",
        "zathura-pdf-mupdf",
        "ripgrep",
        "fzf",
        "logo-ls",
        "zoxide",
        "rofi"
    ]

    __execute_command(f"paru -S {' '.join(packages)}")


def install_configs():
    __execute_command("cp -r .config /home/ncvescera/")
    __execute_command("cp .tmux.conf /home/ncvescera/")


def config_nvim():
    __execute_command("cargo install tree-sitter-cli")
    __execute_command("git clone --depth 1 https://github.com/AstroNvim/template ~/.config/nvim")
    __execute_command("rm -rf ~/.config/nvim/.git")
    __execute_command("nvim")


def config_espanso():
    window_system = input("wayland or x11?")

    __execute_command(f"paru -S espanso-{window_system}")
    __execute_command("espanso service register")
    __execute_command("espanso service start")


def config_docker():
    __execute_command("sudo systemctl enable docker.service")
    __execute_command("sudo usermod -aG docker $USER")


def __execute_command(command, shell="fish"):
    subprocess.run(command, shell=True, executable=f"/bin/{shell}")


if __name__ == "__main__":
    main()
