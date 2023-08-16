#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


# For aliases
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi


PS1="\[\e[0;32m\]\u\[\e[0m\]@:\[\e[0;36m\]\W\[\e[0;37m\]> $ \[\e[0m\]"


#
# ~ $PATH
#
export PATH=$PATH:$HOME/.npm-global/bin

# see it in /etc/bash.bashrc or /etc/profile or /etc/bash.bashrc
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
