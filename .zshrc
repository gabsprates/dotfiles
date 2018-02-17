# $PATH
export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$HOME/.npm-global/bin:$PATH

export ZSH=$HOME/.oh-my-zsh

# Theme
ZSH_THEME="robbyrussell"

# Plugins
plugins=(
  git
)

source $ZSH/oh-my-zsh.sh

# Aliases
alias xClip="xclip -sel clip"
alias ll='ls -lah'

