if status is-interactive
    # Commands to run in interactive sessions can go here
end

oh-my-posh init fish --config ~/.poshthemes/slim.omp.json | source
thefuck --alias | source
neofetch

# Aliases
alias ls="logo-ls"
alias v=nvim
alias t=tmux
alias c=bat
alias cat=bat
alias android="scrcpy --tcpip=192.168.178.21 &"

# Zoxide (better cd) configuration
zoxide init --cmd cd fish | source
