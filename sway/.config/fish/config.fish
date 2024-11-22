if status is-interactive
    # Commands to run in interactive sessions can go here
end

oh-my-posh init fish --config ~/.config/poshthemes/slim.omp.json | source
zoxide init --cmd cd fish | source
thefuck --alias | source
fastfetch

# Aliases
alias ls="logo-ls"
alias v="nvim"
alias cat="bat"
alias catp="bat -p"
alias shot="XDG_CURRENT_DESKTOP=sway flameshot gui"
