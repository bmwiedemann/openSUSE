" /etc/vimrc (configuration file for vim only)
" author: Klaus Franken     <kfr@suse.de>
" author: Werner Fink       <werner@suse.de> 
" author: Florian La Roche  <florian@suse.de> 
" version: 2017/04/28
" commented lines start with `"'

" show matching brackets
set showmatch

" display mode INSERT/REPLACE/...
set showmode

" Required to be able to use keypad keys and map missed escape sequences
set esckeys

" Try to get the correct main terminal type
if &term =~ "xterm"
    let myterm = "xterm"
elseif &term =~ "screen"
    let myterm = "screen"
else
    let myterm =  &term
endif
if has('eval')
    let myterm = substitute(myterm, "cons[0-9][0-9].*$",  "linux", "")
    let myterm = substitute(myterm, "cons[0-9][0-9].*$",  "linux", "")
    let myterm = substitute(myterm, "vt1[0-9][0-9].*$",   "vt100", "")
    let myterm = substitute(myterm, "vt2[0-9][0-9].*$",   "vt220", "")
    let myterm = substitute(myterm, "\\([^-]*\\)[_-].*$", "\\1",   "")
endif

" Here we define the keys of the NumLock in keyboard transmit mode of xterm
" which misses or hasn't activated Alt/NumLock Modifiers.  Often not defined
" within termcap/terminfo and we should map the character printed on the keys.
if myterm == "xterm" || myterm == "kvt" || myterm == "gnome"
    " keys in insert/command mode.
    map! <ESC>Oo  :
    map! <ESC>Oj  *
    map! <ESC>Om  -
    map! <ESC>Ok  +
    map! <ESC>Ol  ,
    map! <ESC>OM  
    map! <ESC>Ow  7
    map! <ESC>Ox  8
    map! <ESC>Oy  9
    map! <ESC>Ot  4
    map! <ESC>Ou  5
    map! <ESC>Ov  6
    map! <ESC>Oq  1
    map! <ESC>Or  2
    map! <ESC>Os  3
    map! <ESC>Op  0
    map! <ESC>On  .
    " 8bit control characters
    map! <Char-0x8F>o  :
    map! <Char-0x8F>j  *
    map! <Char-0x8F>m  -
    map! <Char-0x8F>k  +
    map! <Char-0x8F>l  ,
    map! <Char-0x8F>M  
    map! <Char-0x8F>w  7
    map! <Char-0x8F>x  8
    map! <Char-0x8F>y  9
    map! <Char-0x8F>t  4
    map! <Char-0x8F>u  5
    map! <Char-0x8F>v  6
    map! <Char-0x8F>q  1
    map! <Char-0x8F>r  2
    map! <Char-0x8F>s  3
    map! <Char-0x8F>p  0
    map! <Char-0x8F>n  .
    " keys in normal mode
    map <ESC>Oo  :
    map <ESC>Oj  *
    map <ESC>Om  -
    map <ESC>Ok  +
    map <ESC>Ol  ,
    map <ESC>OM  
    map <ESC>Ow  7
    map <ESC>Ox  8
    map <ESC>Oy  9
    map <ESC>Ot  4
    map <ESC>Ou  5
    map <ESC>Ov  6
    map <ESC>Oq  1
    map <ESC>Or  2
    map <ESC>Os  3
    map <ESC>Op  0
    map <ESC>On  .
    " 8bit control characters
    map <Char-0x8F>o  :
    map <Char-0x8F>j  *
    map <Char-0x8F>m  -
    map <Char-0x8F>k  +
    map <Char-0x8F>l  ,
    map <Char-0x8F>M  
    map <Char-0x8F>w  7
    map <Char-0x8F>x  8
    map <Char-0x8F>y  9
    map <Char-0x8F>t  4
    map <Char-0x8F>u  5
    map <Char-0x8F>v  6
    map <Char-0x8F>q  1
    map <Char-0x8F>r  2
    map <Char-0x8F>s  3
    map <Char-0x8F>p  0
    map <Char-0x8F>n  .
endif

" xterm but without activated keyboard transmit mode
" and therefore not defined in termcap/terminfo.
if myterm == "xterm" || myterm == "kvt" || myterm == "gnome"
    " keys in insert/command mode.
    map! <Esc>[H  <Home>
    map! <Esc>[F  <End>
    map! <Char-0x8F>H  <Home>
    map! <Char-0x8F>F  <End>
    " Home/End: older xterms do not fit termcap/terminfo.
    map! <Esc>[1~ <Home>
    map! <Esc>[4~ <End>
    " Up/Down/Right/Left
    map! <Esc>[A  <Up>
    map! <Esc>[B  <Down>
    map! <Esc>[C  <Right>
    map! <Esc>[D  <Left>
    " 8bit control characters
    map! <Char-0x8F>A  <Up>
    map! <Char-0x8F>B  <Down>
    map! <Char-0x8F>C  <Right>
    map! <Char-0x8F>D  <Left>
    map! <Char-0x9B>5~ <PageUp>
    map! <Char-0x9B>6~ <PageDown>
    map! <Char-0x9B>2~ <Insert>
    map! <Char-0x9B>3~ <Delete>
    " KP_5 (NumLock off)
    map! <Esc>[E  <Insert>
    " keys in normal mode
    map <ESC>[H  0
    map <ESC>[F  $
    map <Char-0x8F>H  0
    map <Char-0x8F>F  $
    " Home/End: older xterms do not fit termcap/terminfo.
    map <ESC>[1~ 0
    map <ESC>[4~ $
    " Up/Down/Right/Left
    map <ESC>[A  k
    map <ESC>[B  j
    map <ESC>[C  l
    map <ESC>[D  h
    " 8bit control characters
    map <Char-0x8F>A  k
    map <Char-0x8F>B  j
    map <Char-0x8F>C  l
    map <Char-0x8F>D  h
    map <Char-0x9B>5~ <PageUp>
    map <Char-0x9B>6~ <PageDown>
    map <Char-0x9B>2~ <Insert>
    map <Char-0x9B>3~ <Delete>
    " KP_5 (NumLock off)
    map <ESC>[E  i
    map <Char-0x8F>E  i
endif

" xterm/kvt but with activated keyboard transmit mode.
" Sometimes not or wrong defined within termcap/terminfo.
if myterm == "xterm" || myterm == "kvt" || myterm == "gnome"
    " keys in insert/command mode.
    map! <Esc>OH <Home>
    map! <Esc>OF <End>
    map! <ESC>O2H <Home>
    map! <ESC>O2F <End>
    map! <ESC>O5H <Home>
    map! <ESC>O5F <End>
    " Cursor keys which works mostly
    " map! <Esc>OA <Up>
    " map! <Esc>OB <Down>
    " map! <Esc>OC <Right>
    " map! <Esc>OD <Left>
    map! <Esc>[2;2~ <Insert>
    map! <Esc>[3;2~ <Delete>
    map! <Esc>[2;5~ <Insert>
    map! <Esc>[3;5~ <Delete>
    map! <Esc>O2A <PageUp>
    map! <Esc>O2B <PageDown>
    map! <Esc>O2C <S-Right>
    map! <Esc>O2D <S-Left>
    map! <Esc>O5A <PageUp>
    map! <Esc>O5B <PageDown>
    map! <Esc>O5C <S-Right>
    map! <Esc>O5D <S-Left>
    " KP_5 (NumLock off)
    map! <Esc>OE <Insert>
    " keys in normal mode
    map <ESC>OH  0
    map <ESC>OF  $
    map <ESC>O2H  0
    map <ESC>O2F  $
    map <ESC>O5H  0
    map <ESC>O5F  $
    " Cursor keys which works mostly
    " map <ESC>OA  k
    " map <ESC>OB  j
    " map <ESC>OD  h
    " map <ESC>OC  l
    map <Esc>[2;2~ i
    map <Esc>[3;2~ x
    map <Esc>[2;5~ i
    map <Esc>[3;5~ x
    map <ESC>O2A  ^B
    map <ESC>O2B  ^F
    map <ESC>O2D  b
    map <ESC>O2C  w
    map <ESC>O5A  ^B
    map <ESC>O5B  ^F
    map <ESC>O5D  b
    map <ESC>O5C  w
    " KP_5 (NumLock off)
    map <ESC>OE  i
endif

if myterm == "linux"
    " keys in insert/command mode.
    map! <Esc>[G  <Insert>
    " KP_5 (NumLock off)
    " keys in normal mode
    " KP_5 (NumLock off)
    map <ESC>[G  i
endif

if myterm == "screen"
    map! <ESC>[1;2D <S-Left>
    map! <ESC>[1;2C <S-Right>
    map! <ESC>[1;2A <S-Up>
    map! <ESC>[1;2B <S-Down>
    map! <ESC>[1;2H <Home>
    map! <ESC>[1;2F <End>
    map! <ESC>[2;2~ <Insert>
    map! <ESC>[3;2~ <Delete>
    map! <ESC>[5;2~ <PageUp>
    map! <ESC>[6;2~ <PageDown>
    map! <ESC>[1;5D <C-Left>
    map! <ESC>[1;5C <C-Right>
    map! <ESC>[1;5A <C-Up>
    map! <ESC>[1;5B <C-Down>
    map! <ESC>[1;5H <Home>
    map! <ESC>[1;5F <End>
    map! <ESC>[2;5~ <Insert>
    map! <ESC>[3;5~ <Delete>
    map! <ESC>[5;5~ <PageUp>
    map! <ESC>[6;5~ <PageDown>
    map! <ESC>[1;3D <A-Left>
    map! <ESC>[1;3C <A-Right>
    map! <ESC>[1;3A <A-Up>
    map! <ESC>[1;3B <A-Down>
    map! <ESC>[1;3H <Home>
    map! <ESC>[1;3F <End>
    map! <ESC>[2;3~ <Insert>
    map! <ESC>[3;3~ <Delete>
    map! <ESC>[5;3~ <PageUp>
    map! <ESC>[6;3~ <PageDown>
endif

" This escape sequence is the well known ANSI sequence for
" Remove Character Under The Cursor (RCUTC[tm])
map! <Esc>[3~ <Delete>
map  <ESC>[3~    x

" Only do this part when compiled with support for autocommands.
if has("autocmd")
    "Remember the positions in files with some git-specific exceptions"
    autocmd BufReadPost *
      \ if line("'\"") > 0 && line("'\"") <= line("$")
      \           && expand("%") !~ "COMMIT_EDITMSG"
      \           && expand("%") !~ "ADD_EDIT.patch"
      \           && expand("%") !~ "addp-hunk-edit.diff"
      \           && expand("%") !~ "git-rebase-todo" |
      \   exe "normal g`\"" |
      \ endif
endif " has("autocmd")

" Changed default required by SuSE security team--be aware if enabling this
" that it potentially can open for malicious users to do harmful things.
set nomodeline

" get easier to use and more user friendly vim defaults
" /etc/vimrc ends here
