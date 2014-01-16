# make the default editor vim
export EDITOR='vim'

# make the git editor vim
export GIT_EDITOR=vim

# set history to 2000 lines
HISTSIZE=2000

# fix permissions
umask 0002

# shortcut checkout function
function co() { svn co https://engineroom.svn.cvsdude.com/"$@" ;}

# can never remember the arguments to untar
alias untar='tar -xvzf'

# add color
alias ls='ls --color'
