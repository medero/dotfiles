# make the default editor vim
export EDITOR='vim'

# make the git editor vim
export GIT_EDITOR=vim

# set history to 2000 lines
HISTSIZE=2000

# fix permissions
umask 0002

function co() { svn co https://engineroom.svn.cvsdude.com/"$@" ;}
alias untar='tar -xvzf'
