set is
set ic
set hls
colorscheme biel
set number
execute pathogen#infect()
autocmd vimenter * NERDTree
let NERDTreeShowHidden=1


set omnifunc=htmlcomplete#CompleteTags

set nocompatible
" filetype off
filetype plugin indent on
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'cakebaker/scss-syntax.vim'
Plugin 'othree/html5.vim'
Plugin 'mattn/emmet-vim'
Plugin 'shawncplus/phpcomplete.vim'


call vundle#end()

function! PhpSyntaxOverride()
hi! def link phpDocTags  phpDefine
hi! def link phpDocParam phpType
endfunction

augroup phpSyntaxOverride
autocmd!
autocmd FileType php call PhpSyntaxOverride()
augroup END
