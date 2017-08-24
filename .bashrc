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
export PATH=$PATH:/home/gabriel/.npm-global/bin
