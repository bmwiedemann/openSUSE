"
" /etc/gvimrc
"
" from original source copied and modified by Klaus Franken
" Version: 21.1.97

" other settings:
:se guipty
:se guioptions=amr

" Menues:
" copied and modified from:
" *vim_menu.txt*   For Vim version 4.5.  Last modification: 1996 Oct 12
"
" These menu commands should recreate the default Vim menus.
" You can use this as a start for your own set of menus.
" The colons at the start of each line are just to indicate these are colon
" commands, they could be omitted.
" If the <Esc> and <CR> string appear literally in the output of ":menu", you
" need to remove the '<' flag from 'cpoptions' |'cpoptions'|

" First remove any menus that are currently present
:unmenu *
:unmenu! *

" Help menu
" Note that the help commands use <Esc> to leave Insert/Visual/Command-line
" mode
:nnoremenu Help.Overview\ \ <F1>	:help<CR>
:vnoremenu Help.Overview\ \ <F1>	<Esc>:help<CR>
:noremenu! Help.Overview\ \ <F1>	<Esc>:help<CR>

:nnoremenu Help.How\ to\.\.\.	:help how_to<CR>
:vnoremenu Help.How\ to\.\.\.	<Esc>:help how_to<CR>
:noremenu! Help.How\ to\.\.\.	<Esc>:help how_to<CR>

:nnoremenu Help.GUI			:help gui<CR>
:vnoremenu Help.GUI			<Esc>:help gui<CR>
:noremenu! Help.GUI			<Esc>:help gui<CR>

:nnoremenu Help.Version		:version<CR>
:vnoremenu Help.Version		<Esc>:version<CR>
:noremenu! Help.Version		<Esc>:version<CR>

:nnoremenu Help.Credits		:help credits<CR>
:vnoremenu Help.Credits		<Esc>:help credits<CR>
:noremenu! Help.Credits		<Esc>:help credits<CR>

:nnoremenu Help.Copying		:help uganda<CR>
:vnoremenu Help.Copying		<Esc>:help uganda<CR>
:noremenu! Help.Copying		<Esc>:help uganda<CR>

" File menu
:nnoremenu File.Save\ \ \ \ \ \ \ :w	:w<CR>
:inoremenu File.Save\ \ \ \ \ \ \ :w	<C-O>:w<CR>

:nnoremenu File.Close\ \ \ \ \ \ :q		:q<CR>
:vnoremenu File.Close\ \ \ \ \ \ :q		<Esc>:q<CR>
:noremenu! File.Close\ \ \ \ \ \ :q		<Esc>:q<CR>

:nnoremenu File.Quit\ \ \ \ \ \ \ :qa	:qa<CR>
:vnoremenu File.Quit\ \ \ \ \ \ \ :qa	<Esc>:qa<CR>
:noremenu! File.Quit\ \ \ \ \ \ \ :qa	<Esc>:qa<CR>

:nnoremenu File.Save-Quit\ \ :wqa		:wqa<CR>
:vnoremenu File.Save-Quit\ \ :wqa		<Esc>:wqa<CR>
:noremenu! File.Save-Quit\ \ :wqa		<Esc>:wqa<CR>

" Edit menu
:nnoremenu Edit.Undo			u
:nnoremenu Edit.Redo			<C-R>

:vnoremenu Edit.Cut				x
:vnoremenu Edit.Copy			y

:nnoremenu Edit.Put\ Before			[p
:inoremenu Edit.Put\ Before			<C-O>[p
:nnoremenu Edit.Put\ After			]p
:inoremenu Edit.Put\ After			<C-O>]p

:nnoremenu Edit.Paste			i<C-R>*<Esc>
:noremenu! Edit.Paste			<C-R>*

" new kfr@suse.de

" MenuNamen:
" :nnoremenu Normal
" :vnoremenu Visual
" :noremenu! Input?

:nnoremenu File.Reload\ \ \ \ \ :e!		:e!<CR>
:vnoremenu File.Reload\ \ \ \ \ :e!		<Esc>:e!<CR>
:noremenu! File.Reload\ \ \ \ \ :e!		<Esc>:e!<CR>

:nnoremenu File.Quit\ All!\ \ :qa!		:qa!<CR>

:nnoremenu Settings.Show :se<CR>
:nnoremenu Settings.Autoindent.off\ F7 :se noautoindent<CR>
:nnoremenu Settings.Autoindent.on\ \ F8 :se autoindent<CR>
:nnoremenu Settings.Tabs.Expand\ on :se expandtab<CR>
:nnoremenu Settings.Tabs.Expand\ off :se noexpandtab<CR>
:nnoremenu Settings.Tabs.2 :se tabstop=2<CR>:se shiftwidth=2<CR>
:nnoremenu Settings.Tabs.4 :se tabstop=4<CR>:se shiftwidth=4<CR>
:nnoremenu Settings.Tabs.8 :se tabstop=8<CR>:se shiftwidth=8<CR>
:nnoremenu Settings.Mouse.All :se mouse=a<CR>
:nnoremenu Settings.Mouse.Visual :se mouse=v<CR>
:nnoremenu Settings.Mouse.Insert :se mouse=i<CR>
:nnoremenu Settings.Mouse.Command-line :se mouse=c<CR>
:nnoremenu Settings.Textwidth.off :se textwidth=0<CR>
:nnoremenu Settings.Textwidth.70 :se textwidth=70<CR>
:nnoremenu Settings.Textwidth.75 :se textwidth=75<CR>
:nnoremenu Settings.Textwidth.80 :se textwidth=80<CR>
:nnoremenu Settings.Wrap.on :se wrap<CR>
:nnoremenu Settings.Wrap.off :se nowrap<CR>
:nnoremenu Settings.Numbers.on :se nu<CR>
:nnoremenu Settings.Numbers.off :se nonu<CR>
:nnoremenu Settings.Search\ case-sensitiv.on :se ignorecase<CR>
:nnoremenu Settings.Search\ case-sensitiv.off :se noignorecase<CR>
:nnoremenu Settings.Scrollbar.Right :se guioptions=mr<CR>
:nnoremenu Settings.Scrollbar.Right+Bottom :se guioptions=mrb<CR>
:nnoremenu Settings.Scrollbar.Left :se guioptions=ml<CR>
:nnoremenu Settings.Scrollbar.Left+Bottom :se guioptions=mlb<CR>

:nnoremenu Settings.RightLeft.Show\ -> :se norightleft<CR>
:nnoremenu Settings.RightLeft.Show\ <- :se rightleft<CR>
:nnoremenu Settings.RightLeft.Input\ -> :se norevins<CR>
:nnoremenu Settings.RightLeft.Input\ <- :se revins<CR>
:nnoremenu Settings.RightLeft.Hebrew\ mapping :se hkmap<CR>
:nnoremenu Settings.RightLeft.Normal\ mapping :se nohkmap<CR>

:nnoremenu Window.Buffer\ Next :bnext<CR>
:nnoremenu Window.Buffer\ Prev :bNext<CR>
:nnoremenu Window.Buffer\ All :ball<CR>
:nnoremenu Window.Zoom :only<CR>
:nnoremenu Window.Show\ Buffers :buffers<CR>
:nnoremenu Window.Go\ Buffer.1 :buf1<CR>
:nnoremenu Window.Go\ Buffer.2 :buf2<CR>
:nnoremenu Window.Go\ Buffer.3 :buf3<CR>
:nnoremenu Window.Go\ Buffer.4 :buf4<CR>
:nnoremenu Window.Go\ Buffer.5 :buf5<CR>
:nnoremenu Window.New :new<CR>
:nnoremenu Window.Split :split<CR>
:nnoremenu Window.Close :close<CR>

:nnoremenu Input.Return <CR>


:nnoremenu Help.40      :help vim_40.txt<CR>
:nnoremenu Help.ami     :help vim_ami.txt<CR>
:nnoremenu Help.arch    :help vim_arch.txt<CR>
:nnoremenu Help.diff    :help vim_diff.txt<CR>
:nnoremenu Help.digr    :help vim_digr.txt<CR>
:nnoremenu Help.dos	    :help vim_dos.txt<CR>
:nnoremenu Help.gui	    :help vim_gui.txt<CR>
:nnoremenu Help.help    :help vim_help.txt<CR>
:nnoremenu Help.idx	    :help vim_idx.txt<CR>
:nnoremenu Help.kcc	    :help vim_kcc.txt<CR>
:nnoremenu Help.mac	    :help vim_mac.txt<CR>
:nnoremenu Help.menu    :help vim_menu.txt<CR>
:nnoremenu Help.mint    :help vim_mint.txt<CR>
:nnoremenu Help.os2	    :help vim_os2.txt<CR>
:nnoremenu Help.ref	    :help vim_ref.txt<CR>
:nnoremenu Help.rlh	    :help vim_rlh.txt<CR>
:nnoremenu Help.tags    :help vim_tags<CR>
:nnoremenu Help.tips    :help vim_tips.txt<CR>
:nnoremenu Help.unix    :help vim_unix.txt<CR>
:nnoremenu Help.w32	    :help vim_w32.txt<CR>
:nnoremenu Help.win	    :help vim_win.txt<CR>
