if status is-interactive
    # Commands to run in interactive sessions can go here
end

oh-my-posh init fish --config ~/.poshthemes/slim.omp.json | source
thefuck --alias | source
neofetch

# Aliases
alias ls="logo-ls"

# ENV Variables
# Google Chrome Executable
set -gx CHROME_EXECUTABLE /usr/bin/google-chrome-stable
