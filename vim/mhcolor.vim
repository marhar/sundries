" mhcolor.vim : Vim color file
" Maintainer  :	Mark Harrison (marhar@gmail.com)
" optimized for red-colorblind

let g:colors_name = "mhcolor"
set background=dark
syntax reset

" Console
highlight Normal     ctermfg=Green	ctermbg=Black
highlight Search     ctermfg=Black	ctermbg=Red	cterm=NONE
highlight Visual					cterm=reverse
highlight Cursor     ctermfg=Black	ctermbg=Green	cterm=bold
highlight Special    ctermfg=Brown
highlight Comment    ctermfg=LightBlue
highlight StatusLine ctermfg=blue	ctermbg=white
highlight Statement  ctermfg=Yellow			cterm=NONE
highlight Constant  ctermfg=LightBlue			cterm=NONE
highlight MatchParen cterm=underline ctermfg=White ctermbg=Black
highlight Type			cterm=NONE
highlight Pmenu      ctermfg=White ctermbg=Blue
highlight PmenuSel   ctermfg=Black ctermbg=LightBlue

" GUI -- just copied and :s/cterm/gui/g
highlight Normal     guifg=Green	guibg=Black
highlight Search     guifg=Black	guibg=Red	gui=NONE
highlight Visual					gui=reverse
highlight Cursor     guifg=Black	guibg=Green	gui=bold
highlight Special    guifg=Brown
highlight Comment    guifg=LightBlue
highlight StatusLine guifg=blue	guibg=white
highlight Statement  guifg=Yellow			gui=NONE
highlight Constant  guifg=LightBlue			gui=NONE
highlight MatchParen gui=underline guifg=White guibg=Black
highlight Type			gui=NONE
highlight Pmenu      guifg=White guibg=Blue
highlight PmenuSel   guifg=Black guibg=LightBlue
