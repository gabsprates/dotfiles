set is
set ic
set hls
set expandtab
set shiftwidth=2
set softtabstop=2
set tabstop=2
set t_Co=256
colorscheme biel
set number
execute pathogen#infect()
let NERDTreeShowHidden=1

let g:vim_markdown_folding_disabled = 1

autocmd vimenter * NERDTree

" set omnifunc=htmlcomplete#CompleteTags

set nocompatible
" filetype off
filetype plugin indent on
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'Xuyuanp/nerdtree-git-plugin'
Plugin 'editorconfig/editorconfig-vim'
Plugin 'cakebaker/scss-syntax.vim'
Plugin 'othree/html5.vim'
Plugin 'mattn/emmet-vim'
Plugin 'shawncplus/phpcomplete.vim'
Plugin 'scrooloose/nerdcommenter'
Plugin 'jistr/vim-nerdtree-tabs'
Plugin 'godlygeek/tabular'
Plugin 'plasticboy/vim-markdown'

call vundle#end()

if (exists('+colorcolumn'))
set colorcolumn=80
endif

function! PhpSyntaxOverride()
hi! def link phpDocTags  phpDefine
hi! def link phpDocParam phpType
endfunction

augroup phpSyntaxOverride
autocmd!
autocmd FileType php call PhpSyntaxOverride()
augroup END

set ai
