# ZSH configuration

export ZSH=$HOME/.oh-my-zsh

## Theme
ZSH_THEME="robbyrussell"

## Plugins
plugins=(
    asdf
    git
    docker
)

source $ZSH/oh-my-zsh.sh

# ==================

## Machine extra configuration

if [ -f ~/.zsh_local ]; then
    source ~/.zsh_local
fi

## [BEGIN] Aliases
alias ll='ls -lah'
alias goto-new-temp="cd $(mktemp -d)"
## [END] Aliases

## [BEGIN] PATH
## [END] PATH
