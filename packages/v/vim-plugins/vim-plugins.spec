#
# spec file for package vim-plugins
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define ack_version		1.0.9
%define airline_version		0.11
%define ale_version		3.3.0
%define align_version_orig	37-43
%define align_version		37.43
%define a_version		2.18
%define bufexplorer_version	7.4.25
%define bufexplorer_version_orig v.%{bufexplorer_version}
%define calendar_version	2.5
%define colorsel_version	20110107
%define colorschemes_version	1.0
%define diffchanges_tag		346dae2
%define diffchanges_version	0.6+g346dae2
%define editorconfig_version	1.1.1
%define file_line_version	1.0+20161020
%define fugitive_version	3.7
%define gitdiff_version		2
%define gnupg_version		2.7.1
%define latex_version		1.10.0+20220519
%define locateopen_version	1.3
%define markdown_version	2.0.0+20220926
%define matrix_version		1.10
%define minibufexpl_version	6.3.2
%define multiplesearch_version	1.3
%define neomutt_version		20220612
%define NERDcommenter_version	2.7.0
%define NERDtree_version	6.10.16
%define project_version		1.4.1
%define quilt_version		0.9.7
%define rails_version		5.2
%define salt_version		20170630
%define searchcomplete_version	1.1
%define showmarks_version	2.3
%define snipmate_version	0.83
%define supertab_version	2.1
%define taglist_version		4.6
%define tlib_version		1.28
%define tregisters_version	0.2
%define tselectbuffer_version	0.7
%define tselectfiles_version	0.11
%define utl_version		2.0
%define vimwiki_version		2.1
%define zoomwin_version		24

Name:           vim-plugins
Version:        7.3.0
Release:        0
Summary:        Plug-ins pack for Vim
License:        MIT
Group:          Productivity/Text/Editors
URL:            http://www.vim.org/
Source0:        https://github.com/vim-scripts/Align/archive/refs/tags/%{align_version_orig}.tar.gz#/vimplugin-align-%{align_version}.tar.gz
Source1:        https://github.com/vim-scripts/a.vim/archive/refs/tags/%{a_version}.tar.gz#/vimplugin-a-%{a_version}.tar.gz
Source2:        https://github.com/jlanzarotta/bufexplorer/archive/refs/tags/%{bufexplorer_version_orig}.tar.gz#/bufexplorer-%{bufexplorer_version}.tar.gz
Source3:        https://github.com/vim-scripts/calendar.vim--Matsumoto/archive/refs/tags/%{calendar_version}.tar.gz#/calendar.vim--Matsumoto-%{calendar_version}.tar.gz
Source4:        https://github.com/vim-scripts/colorsel.vim/archive/refs/tags/%{colorsel_version}.tar.gz#/vimplugin-colorsel-%{colorsel_version}.tar.gz
Source5:        vimplugin-colorschemes-%{colorschemes_version}.tar.bz2
Source6:        https://github.com/vim-scripts/diffchanges.vim/archive/refs/tags/%{diffchanges_tag}.tar.gz#/vimplugin-diffchanges-%{diffchanges_version}.tar.gz
Source7:        https://github.com/vim-scripts/LocateOpen/archive/refs/tags/%{locateopen_version}.tar.gz#/vimplugin-locateopen-%{locateopen_version}.tar.gz
Source9:        https://github.com/vim-scripts/matrix.vim--Yang/archive/refs/tags/%{matrix_version}.tar.gz#/vimplugin-matrix-%{matrix_version}.tar.gz
Source10:       https://github.com/vim-scripts/minibufexpl.vim/archive/refs/tags/%{minibufexpl_version}.tar.gz#/vimplugin-minibufexpl-%{minibufexpl_version}.tar.gz
Source11:       https://github.com/vim-scripts/MultipleSearch/archive/refs/tags/%{multiplesearch_version}.tar.gz#/vimplugin-multiplesearch-%{multiplesearch_version}.tar.gz
Source12:       https://github.com/preservim/nerdcommenter/archive/refs/tags/%{NERDcommenter_version}.tar.gz#/vimplugin-NERDcommenter-%{NERDcommenter_version}.tar.gz
Source13:       https://github.com/preservim/nerdtree/archive/refs/tags/%{NERDtree_version}.tar.gz#/vimplugin-NERDtree-%{NERDtree_version}.tar.gz
Source14:       https://github.com/vim-scripts/project.tar.gz/archive/refs/tags/%{project_version}.tar.gz#/vimplugin-project-%{project_version}.tar.gz
Source15:       https://github.com/vim-scripts/SearchComplete/archive/refs/tags/%{searchcomplete_version}.tar.gz#/vimplugin-searchcomplete-%{searchcomplete_version}.tar.gz
Source16:       https://github.com/vim-scripts/ShowMarks7/archive/refs/tags/%{showmarks_version}.tar.gz#/vimplugin-showmarks-%{showmarks_version}.tar.gz
Source17:       https://github.com/vim-scripts/SuperTab--Van-Dewoestine/archive/refs/tags/%{supertab_version}.tar.gz#/vimplugin-supertab-%{supertab_version}.tar.gz
Source18:       https://github.com/yegappan/taglist/archive/refs/tags/v%{taglist_version}.tar.gz#/vimplugin-taglist-%{taglist_version}.tar.gz
Source19:       https://github.com/tomtom/tlib_vim/archive/refs/tags/%{tlib_version}.tar.gz#/vimplugin-tlib-%{tlib_version}.tar.gz
Source20:       https://github.com/vim-scripts/tregisters/archive/refs/tags/%{tregisters_version}.tar.gz#/vimplugin-tregisters-%{tregisters_version}.tar.gz
Source21:       https://github.com/vim-scripts/tselectbuffer/archive/refs/tags/%{tselectbuffer_version}.tar.gz#/vimplugin-tselectbuffer-%{tselectbuffer_version}.tar.gz
Source22:       https://github.com/vim-scripts/tselectfiles/archive/refs/tags/%{tselectfiles_version}.tar.gz#/vimplugin-tselectfiles-%{tselectfiles_version}.tar.gz
Source23:       https://github.com/vim-scripts/utl.vim/archive/refs/tags/%{utl_version}.tar.gz#/vimplugin-utl-%{utl_version}.tar.gz
Source24:       https://github.com/vim-scripts/ZoomWin/archive/refs/tags/%{zoomwin_version}.tar.gz#/vimplugin-zoomwin-%{zoomwin_version}.tar.gz
Source26:       https://github.com/vim-scripts/quilt/archive/refs/tags/%{quilt_version}.tar.gz#/vimplugin-quilt-%{quilt_version}.tar.gz
Source27:       https://github.com/vim-scripts/vimwiki/archive/refs/tags/%{vimwiki_version}.tar.gz#/vimplugin-vimwiki-%{vimwiki_version}.tar.gz
Source28:       https://github.com/jamessan/vim-gnupg/releases/download/v%{gnupg_version}/vim-gnupg-v%{gnupg_version}.tar.gz#/vimplugin-gnupg-%{gnupg_version}.tar.gz
Source29:       https://github.com/jamessan/vim-gnupg/releases/download/v%{gnupg_version}/vim-gnupg-v%{gnupg_version}.tar.gz.asc#/vimplugin-gnupg-%{gnupg_version}.tar.gz.asc
Source30:       https://github.com/vim-scripts/gitdiff.vim/archive/refs/tags/%{gitdiff_version}.tar.gz#/vimplugin-gitdiff-%{gitdiff_version}.tar.gz
Source31:       https://github.com/vim-scripts/snipMate/archive/refs/tags/%{snipmate_version}.tar.gz#/vimplugin-snipmate-%{snipmate_version}.tar.gz
Source32:       https://github.com/vim-scripts/rails.vim/archive/refs/tags/%{rails_version}.tar.gz#/vimplugin-rails-%{rails_version}.tar.gz
Source33:       https://github.com/mileszs/ack.vim/archive/refs/tags/%{ack_version}.tar.gz#/vimplugin-ack-%{ack_version}.tar.gz
Source34:       https://github.com/editorconfig/editorconfig-vim/archive/refs/tags/v%{editorconfig_version}.tar.gz#/vimplugin-editorconfig-%{editorconfig_version}.tar.gz
Source35:       https://github.com/tpope/vim-fugitive/archive/refs/tags/v%{fugitive_version}.tar.gz#/vimplugin-fugitive-%{fugitive_version}.tar.gz
Source36:       https://github.com/vim-airline/vim-airline/archive/refs/tags/v%{airline_version}.tar.gz#/vimplugin-airline-%{airline_version}.tar.gz
Source37:       https://github.com/dense-analysis/ale/archive/refs/tags/v%{ale_version}.tar.gz#/vimplugin-ale-%{ale_version}.tar.gz
# from _service
Source100:      file-line-%{file_line_version}.tar.xz
Source101:      vim-markdown-%{markdown_version}.tar.xz
Source102:      neomutt.vim-%{neomutt_version}.tar.xz
Source103:      salt-vim-%{salt_version}.tar.xz
Source104:      vim-latex-%{latex_version}.tar.xz
Source200:      gitrebase.vim
Source300:      global-rsync-filter
Source1000:     https://raw.githubusercontent.com/openSUSE/pack-tools/master/contrib/vim/spec.snippets
Source1001:     check_for_updates.pl
Patch0:         salt-syntax-avoid-multiline-lets.patch
Patch1:         locateopen-1.3-locate-support.patch
Patch2:         showmarks-signs.patch
Patch3:         file-line-Fix-other-plugins-loading.patch
BuildRequires:  rsync
BuildRequires:  vim
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%define     vimplugin_dir %{_datadir}/vim/site

%description
Subpackages of this packages contains some plugins for Vi iMproved text editor.

%package -n vim-plugin-a
Version:        %a_version
Release:        0
Summary:        Alternate files quickly
License:        ISC
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-a
Vim plugin to quickly switch between corresponding files. E.g. if you are
editing foo.c and need to edit foo.h simply execute :A and you will be editing
foo.h, to switch back to foo.c execute :A again. It has builtin support for C,
C++ and ADA95 and can be configured to support a variety of languages.

%package -n vim-plugin-ack
Version:        %ack_version
Release:        0
Summary:        Run the ack search tool from Vim
License:        Vim
Group:          Productivity/Text/Editors
Requires:       ack >= 2.0
Obsoletes:      vim-plugin-ag <= 20160213
Provides:       vim-plugin-ag = 20160231

%description -n vim-plugin-ack
Run the ack search tool from Vim, with enhanced results listing.

%package -n vim-plugin-airline
Version:        %airline_version
Release:        0
Summary:        Lean & mean status/tabline for vim that's light as air.
License:        MIT
Group:          Productivity/Text/Editors

%description -n vim-plugin-airline
When the plugin is correctly loaded, there will be a nice
statusline at the bottom of each vim window.

%package -n vim-plugin-ale
Version:        %ale_version
Release:        0
Summary:        Asynchronous Lint Engine plugin for VIM
License:        BSD-2-Clause
Group:          Productivity/Text/Editors

%description -n vim-plugin-ale
ALE makes use of NeoVim and Vim 8 job control functions and timers
to run linters on the contents of text buffers and return errors as
text is changed in Vim. This allows for displaying warnings and
errors in files being edited in Vim before files have been saved
back to a filesystem.

In other words, this plugin allows you to lint while you type.

%package -n vim-plugin-align
Version:        %align_version
Release:        0
Summary:        Plugin to produce aligned text, equations, declarations, etc
License:        Vim
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-align
Align lets you align statements on their equal signs, make comment boxes, align
comments, align declarations, etc. It handles alignment on multiple separators,
not just the first one, and the separators may be the same across the line or
different.

%package -n vim-plugin-bufexplorer
Version:        %bufexplorer_version
Release:        0
Summary:        Buffer Explorer / Browser
License:        BSD-3-Clause
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-bufexplorer
With bufexplorer, you can quickly and easily switch between buffers by using
the one of the default public interfaces:
\<Leader\>be normal open
\<Leader\>bt toggle open / close
\<Leader\>bs force horizontal split open
\<Leader\>bv force vertical split open

Once the bufexplorer window is open you can use the normal movement keys (hjkl)
to move around and then use or to select the buffer you would like to open. If
you would like to have the selected buffer opened in a new tab, simply press
either or 't'. Please note that when opening a buffer in a tab, that if the
buffer is already in another tab, bufexplorer can switch to that tab
automatically for you if you would like.

%package -n vim-plugin-calendar
Version:        %calendar_version
Release:        0
Summary:        Calendar for vim
License:        BSD-3-Clause
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-calendar
Plugin for vim that displays simple calendar in the side window.

%package -n vim-plugin-colorschemes
Version:        %colorschemes_version
Release:        0
Summary:        Vim color schemes selection
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-colorschemes
Selection of vim color schemes based on Colors Sample Pack -
http://www.vim.org/scripts/script.php?script_id=625.

%package -n vim-plugin-colorsel
Version:        %colorsel_version
Release:        0
Summary:        A RGB/HSV color selector
License:        SUSE-Public-Domain
Group:          Productivity/Text/Editors
Requires:       gvim
Requires:       vim

%description -n vim-plugin-colorsel
A simple interactive RGB/HSV color selector modelled after Gimp2 RGB/HSV color
selector.

%package -n vim-plugin-diffchanges
Version:        %diffchanges_version
Release:        0
Summary:        Show changes since the last save
License:        Vim
Group:          Productivity/Text/Editors
Requires:       diffutils
Requires:       vim

%description -n vim-plugin-diffchanges
Show changes made to current buffer since the last save. This plugin is based
from an example in the Hacking Vim book. The differences are that this
functionality is in the form of a plugin, is a bit more robust, and can be
toggled.

%package -n vim-plugin-editorconfig
Version:        %editorconfig_version
Release:        0
Summary:        EditorConfig plugin for Vim
License:        BSD-2-Clause
Group:          Productivity/Text/Editors
Requires:       editorconfig

%description -n vim-plugin-editorconfig
EditorConfig helps developers define and maintain consistent coding styles
between different editors and IDEs. The EditorConfig project consists of a file
format for defining coding styles and a collection of text editor plugins that
enable editors to read the file format and adhere to defined styles.
EditorConfig files are easily readable and they work nicely with version
control systems.

This package contains a Vim plugin to support EditorConfig.

%package -n vim-plugin-file-line
Version:        %file_line_version
Release:        0
Summary:        File-line plugin for Vim
License:        GPL-3.0-only
Group:          Productivity/Text/Editors

%description -n vim-plugin-file-line
Plugin for vim to enable opening a file in a given line.

%package -n vim-plugin-fugitive
Version:        %fugitive_version
Release:        0
Summary:        Fugitive plugin for Vim
License:        Vim
Group:          Productivity/Text/Editors
Requires:       git-core

%description -n vim-plugin-fugitive
Provides git integration with vim.

%package -n vim-plugin-gitdiff
Version:        %gitdiff_version
Release:        0
Summary:        Show git diff in a split window
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       git-core

%description -n vim-plugin-gitdiff
This script provides two functions to display git diffs in vim.
:GITDiff [commitish]
    Split the vim window vertically, display the HEAD, or some other changeset, version of the file in the split, then diff them.
:GITChanges [commitish]
    Highlight lines that were changed since the HEAD or some other changeset.

%package -n vim-plugin-gitrebase-keywordprg
Version:        1
Release:        0
Summary:        Set keywordprg in git rebase --interactive
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       git-core

%description -n vim-plugin-gitrebase-keywordprg
Set keywordprg in git rebase --interactive. This used to done before vim
8.2.4529, but was changed afterwards. For details, see
https://github.com/vim/vim/issues/9845.

%package -n vim-plugin-gnupg
Version:        %gnupg_version
Release:        0
Summary:        Plugin for transparent editing of gpg encrypted files
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
URL:            https://github.com/jamessan/vim-gnupg
Requires:       gpg2

%description -n vim-plugin-gnupg
This script implements transparent editing of gpg encrypted files. The filename
must have a ".gpg", ".pgp" or ".asc" suffix. When opening such a file the
content is decrypted, when opening a new file the script will ask for the
recipients of the encrypted file. The file content will be encrypted to all
recipients before it is written. The script turns off viminfo, swapfile, and
undofile to increase security.

%package -n vim-plugin-latex
Version:        %latex_version
Release:        0
Summary:        A rich set of tools for editing LaTeX
License:        Vim
Group:          Productivity/Text/Editors
Requires:       texlive-latex
Requires:       vim

%description -n vim-plugin-latex
Vim-LaTeX (aka LaTeX-suite) is a mature project which aims at bringing
together the rich set of LaTeX tools the vim community has produced over
the years into one comprehensive package. It provides a set of tools
which enable you to do all your LaTeX-ing without needing to quit Vim.

%package -n vim-plugin-locateopen
Version:        %locateopen_version
Release:        0
Summary:        Edit file without entering the whole path
License:        Vim
Group:          Productivity/Text/Editors
Requires:       findutils-locate
Requires:       vim

%description -n vim-plugin-locateopen
This script uses slocate (or a similar application) to allow the user to open a
file without having to enter a path. If multiple files are found the user is
given the choice of which file to open.

Usage:
  :LocateEdit somefile.txt
  :LocateSplit somefile.txt
  :LocateSource somefile.vim
  :LocateRead somefile.txt

%package -n vim-plugin-markdown
Version:        %markdown_version
Release:        0
Summary:        Markdown support for vim
License:        MIT
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-markdown
Syntax highlighting, matching rules and mappings for the original Markdown and
extensions.

%package -n vim-plugin-matrix
Version:        %matrix_version
Release:        0
Summary:        Matrix screensaver for vim
License:        MIT
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-matrix
Matrix screensaver for VIM, inspired by Chris Allegretta's cmatrix.

%package -n vim-plugin-minibufexpl
Version:        %minibufexpl_version
Release:        0
Summary:        Elegant buffer explorer that takes very little screen space
License:        ISC
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-minibufexpl
Minibufexplorer allows to quickly switch buffers by double-clicking the
appropriate "tab". Tabs get updated as buffers are opened and closed.
Buffers that are modified get visually marked and buffers that are open in a
window get visually marked.

%package -n vim-plugin-multiplesearch
Version:        %multiplesearch_version
Release:        0
Summary:        Display multiple searches at the same time
License:        Vim
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-multiplesearch
MultipleSearch allows you to have the results of multiple searches displayed
on the screen at the same time.  Each search highlights its results in a
different color, and all searches are displayed at once.  After the maximum
number of colors is used, the script starts over with the first color.

%package -n vim-plugin-neomutt
Version:        %neomutt_version
Release:        0
Summary:        Neomutt plugin for Vim
License:        Vim
Group:          Productivity/Text/Editors

%description -n vim-plugin-neomutt
This plugin provides syntax for the neomutt configuration file. In addition, it
sets the mail filetype to temporary mail files created by neomutt when writing
or editing emails.

%package -n vim-plugin-NERDcommenter
Version:        %NERDcommenter_version
Release:        0
Summary:        A plugin that allows for easy commenting of code for many filetypes
License:        WTFPL
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-NERDcommenter
The NERD commenter provides many different commenting operations and styles
which may be invoked via key mappings and a commenting menu. These operations
are available for most filetypes.

%package -n vim-plugin-NERDtree
Version:        %NERDtree_version
Release:        0
Summary:        A tree explorer plugin for navigating the filesystem
License:        WTFPL
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-NERDtree
The NERD tree allows you to explore your filesystem and to open files and
directories. It presents the filesystem to you in the form of a tree which you
manipulate with the keyboard and/or mouse. It also allows you to perform simple
filesystem operations.

%package -n vim-plugin-project
Version:        %project_version
Release:        0
Summary:        Organize/Navigate projects of files
License:        SUSE-Public-Domain
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-project
You can use this plugin's basic functionality to set up a list of
frequently-accessed files for easy navigation. The list of files will be
displayed in a window on the left side of the vim window, and you can press
<Return> or double-click on filenames in the list to open the files. This is
similar to how some IDEs I've used work. I find this easier to use than having
to navigate a directory hierarchy with the file-explorer.  It also obviates the
need for a buffer explorer because you have your list of files on the left of
the vim window.

%package -n vim-plugin-quilt
Version:        %quilt_version
Release:        0
Summary:        Quilt support for vim
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       quilt
Requires:       vim

%description -n vim-plugin-quilt
Vim plugin that helps with quilt operations from inside vim.

%package -n vim-plugin-rails
Version:        %rails_version
Release:        0
Summary:        Support for Ruby on Rails development
License:        Vim
Group:          Productivity/Text/Editors
Recommends:     rubygem(rails)

%description -n vim-plugin-rails
This plugin offers the many features for Ruby on Rails application development.

%package -n vim-plugin-salt
Version:        %salt_version
Release:        0
Summary:        Salt plugin for Vim
License:        Apache-2.0
Group:          Productivity/Text/Editors
URL:            https://github.com/saltstack/salt-vim

%description -n vim-plugin-salt
This Vim plugin provides support for editing Saltstack .sls files.

%package -n vim-plugin-searchcomplete
Version:        %searchcomplete_version
Release:        0
Summary:        Tab completion of words inside of a search
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-searchcomplete
This plugin allows to tab-complete words while typing in a
search ('/').

%package -n vim-plugin-showmarks
Version:        %showmarks_version
Release:        0
Summary:        Visually shows the location of marks
License:        SUSE-Public-Domain
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-showmarks
ShowMarks provides a visual representation of the location marks.  Marks are
useful for jumping back and forth between interesting points in a buffer, but
can be hard to keep track of without any way to see where you have placed them.
ShowMarks hopefully makes life easier by placing a sign in the leftmost column
of the buffer.  The sign indicates the label of the mark and its location.  It
can be toggled on and off and individual marks can be hidden.

%package -n vim-plugin-snipmate
Version:        %snipmate_version
Release:        0
Summary:        Implements some of TextMate's snippets features in Vim
License:        MIT
Group:          Productivity/Text/Editors

%description -n vim-plugin-snipmate
snipMate aims to be an unobtrusive, concise vim script that implements some of
TextMate's snippets features in Vim. A snippet is a piece of often-typed text
that you can insert into your document using a trigger word followed by a
<tab>.

For instance, in a C file using the default installation of snipMate.vim, if
you type "for<tab>" in insert mode, it will expand a typical for loop in C:

for (i = 0; i < count; i++) {
}

%package -n vim-plugin-supertab
Version:        %supertab_version
Release:        0
Summary:        Easy insert mode completion with Tab key
License:        BSD-3-Clause
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-supertab
This script allows you to use the tab key to do all your insert completion.

%package -n vim-plugin-taglist
Version:        %taglist_version
Release:        0
Summary:        Source code browser with support for many languages
License:        ISC
Group:          Productivity/Text/Editors
Requires:       ctags
Requires:       vim

%description -n vim-plugin-taglist
The "Tag List" plugin is a source code browser plugin for Vim and provides an
overview of the structure of source code files and allows you to efficiently
browse through source code files for different programming languages.

%package -n vim-plugin-tlib
Version:        %tlib_version
Release:        0
Summary:        Utility functions for vim
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-tlib
This library provides some utility functions. There isn't much need to install
it unless another plugin requires you to do so.

%package -n vim-plugin-tregisters
Version:        %tregisters_version
Release:        0
Summary:        List, edit, and run/execute registers/clipboards
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Requires:       vim
Requires:       vim-plugin-tlib

%description -n vim-plugin-tregisters
List, edit, and run or execute registers and/or clipboards

%package -n vim-plugin-tselectbuffer
Version:        %tselectbuffer_version
Release:        0
Summary:        A quick buffer selector/switcher
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-tselectbuffer
This plugin provides a simple buffer selector. It doesn't have all the features
other buffer selectors have but can be useful for quickly switching to a
different buffer or for deleting buffers.

%package -n vim-plugin-tselectfiles
Version:        %tselectfiles_version
Release:        0
Summary:        A quick file selector/browser/explorer
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Requires:       vim
Requires:       vim-plugin-tlib

%description -n vim-plugin-tselectfiles
This plugin provides a simple file browser. It is not a full blown explorer but
can be nevertheless be useful for quickly selecting a few files or renaming
them.

%package -n vim-plugin-utl
Version:        %utl_version
Release:        0
Summary:        Universal text linking for vim
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-utl
Universal text link allows you to set hyperlinks within your text documents.
Hyperlinks can be used to start applications, open related documents, or
bookmark parts of your text document.

%package -n vim-plugin-vimwiki
Version:        %vimwiki_version
Release:        0
Summary:        Personal wiki for vim
License:        GPL-2.0-only
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-vimwiki
Vimwiki is a personal wiki for Vim. Using it you can organize text files with
hyperlinks. To do a quick start press <Leader>ww (this is usually \ww) to go
to your index wiki file. By default it is located in ~/vimwiki/index.wiki.
You do not have to create it manually - vimwiki can make it for you.

%package -n vim-plugin-zoomwin
Version:        %zoomwin_version
Release:        0
Summary:        Zoom in/out of windows (toggle between one window and multi-window)
License:        Vim
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-zoomwin
The idea is to make it easy to zoom into and out of a window.
Usage:

     Press <c-w>o : the current window zooms into a full screen
     Press <c-w>o again: the previous set of windows is restored

%prep
%setup -q -c -n %{name} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a26 -a27 -a28 -a30 -a31 -a32 -a33 -a34 -a35 -a36 -a37 -a100 -a101 -a102 -a103 -a104
pushd salt-vim-%{salt_version}
%patch0 -p1
popd
# ------- patch locateopen ------
pushd LocateOpen-%locateopen_version
%patch1
popd
pushd ShowMarks7-%showmarks_version
%patch2 -p1
popd
pushd file-line-%file_line_version
%patch3 -p1
popd

find tlib_vim-%{tlib_version} -type f \( -name '*.vim' -o -name '*.txt' \) -exec chmod -v 644 {} +
chmod -v 644 taglist-%{taglist_version}/doc/taglist.txt

%build

%install
# BEGIN EXCLUDES
cat > ale-%{ale_version}/.rsync-filter <<EOF
- /supported-tools.md
EOF

cat > editorconfig-vim-%{editorconfig_version}/.rsync-filter <<EOF
- /plugin/editorconfig-core-py/
- /tests/
- /mkzip.sh
EOF

cat > nerdtree-%{NERDtree_version}/.rsync-filter <<EOF
- /_config.yml
- /nerdtree_plugin/
- /screenshot.png
EOF

cat > salt-vim-%{salt_version}/.rsync-filter <<EOF
- /salt-vim.spec
EOF

cat > tlib_vim-%{tlib_version}/.rsync-filter <<EOF
- /addon-info.json
- /doc/tags
- /etc/
- /samples/
- /scripts/
- /test/
EOF

cat > vim-airline-%{airline_version}/.rsync-filter <<EOF
- /t/
- /ISSUE_TEMPLATE.md
- /Gemfile
- /Rakefile
EOF

cat > vim-latex-%{latex_version}/.rsync-filter <<EOF
- /Makefile*
- /vim-latex.metainfo.xml
- /doc/*.css
- /doc/*.xml
- /doc/*.xsl
- /doc/Makefile*
- /doc/README*
EOF
# END EXCLUDES

install -d %buildroot/%vimplugin_dir
for i in */; do
	test "$i" = 'vim-markdown-%{markdown_version}/' && continue
	rsync -FFXHav --filter='merge %{SOURCE300}' \
		"$i" %buildroot/%{vimplugin_dir}/
done

install -d %buildroot/%vimplugin_dir/after/ftplugin/
install -m 644 %{SOURCE200} %buildroot/%vimplugin_dir/after/ftplugin/

install -d %{buildroot}/%vimplugin_dir/snippets/
install -m 644 %{SOURCE1000} %{buildroot}/%vimplugin_dir/snippets/

pushd nerdtree-%{NERDtree_version}
install -d %{buildroot}%{_defaultdocdir}/vimplugin-NERDtree/
install -m 644 nerdtree_plugin/* %{buildroot}%{_defaultdocdir}/vimplugin-NERDtree/
popd

pushd vim-latex-%{latex_version}
install -d %{buildroot}%{_datadir}/appdata
install -m 644 vim-latex.metainfo.xml %{buildroot}%{_datadir}/appdata/
popd

pushd vim-markdown-%{markdown_version}
chmod 644 indent/markdown.vim
%{makeinstall} 'ADDONS=${VIMDIR}/site'
popd

# For every plugin providing documentation, we have to call the post and postun
# scriptlets.

%define vim_doc_post(n:) \
%%post %{-n:-n %{-n*}} \
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null \
%%postun %{-n:-n %{-n*}} \
if [ $1 = 0 ]; then \
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null \
fi \
%{nil}

%vim_doc_post -n vim-plugin-ack
%vim_doc_post -n vim-plugin-airline
%vim_doc_post -n vim-plugin-ale
%vim_doc_post -n vim-plugin-align
%vim_doc_post -n vim-plugin-bufexplorer
%vim_doc_post -n vim-plugin-colorsel
%vim_doc_post -n vim-plugin-diffchanges
%vim_doc_post -n vim-plugin-editorconfig
%vim_doc_post -n vim-plugin-fugitive
%vim_doc_post -n vim-plugin-gnupg
%vim_doc_post -n vim-plugin-latex
%vim_doc_post -n vim-plugin-markdown
%vim_doc_post -n vim-plugin-multiplesearch
%vim_doc_post -n vim-plugin-neomutt
%vim_doc_post -n vim-plugin-NERDcommenter
%vim_doc_post -n vim-plugin-NERDtree
%vim_doc_post -n vim-plugin-project
%vim_doc_post -n vim-plugin-quilt
%vim_doc_post -n vim-plugin-rails
%vim_doc_post -n vim-plugin-snipmate
%vim_doc_post -n vim-plugin-supertab
%vim_doc_post -n vim-plugin-taglist
%vim_doc_post -n vim-plugin-tlib
%vim_doc_post -n vim-plugin-tselectbuffer
%vim_doc_post -n vim-plugin-tselectfiles
%vim_doc_post -n vim-plugin-utl
%vim_doc_post -n vim-plugin-vimwiki
%vim_doc_post -n vim-plugin-zoomwin
%vim_doc_post

%files -n vim-plugin-a
%doc a.vim-%{a_version}/README
%vimplugin_dir/plugin/a.vim

%files -n vim-plugin-ack
%defattr(-,root,root,0755)
%doc ack.vim-%{ack_version}/README.md
%license ack.vim-%{ack_version}/LICENSE
%vimplugin_dir/plugin/ack.vim
%vimplugin_dir/autoload/ack.vim
%vimplugin_dir/doc/ack.txt
%vimplugin_dir/doc/ack_quick_help.txt
%dir %vimplugin_dir/ftplugin
%vimplugin_dir/ftplugin/qf.vim

%files -n vim-plugin-airline
%defattr(-,root,root,0755)
%license vim-airline-%{airline_version}/LICENSE
%doc vim-airline-%{airline_version}/README.md
%vimplugin_dir/autoload/airline*
%vimplugin_dir/doc/airline.txt
%vimplugin_dir/plugin/airline.vim

%files -n vim-plugin-ale
%defattr(-,root,root,0755)
%license ale-%{ale_version}/LICENSE
%doc ale-%{ale_version}/supported-tools.md
%vimplugin_dir/ale_linters
%vimplugin_dir/autoload/ale
%vimplugin_dir/autoload/ale.vim
%dir %vimplugin_dir/autoload/asyncomplete
%dir %vimplugin_dir/autoload/asyncomplete/sources
%vimplugin_dir/autoload/asyncomplete/sources/ale.vim
%vimplugin_dir/doc/ale*
%vimplugin_dir/ftplugin/ale-*.vim
%vimplugin_dir/plugin/ale.vim
%dir %vimplugin_dir/rplugin
%dir %vimplugin_dir/rplugin/python3
%dir %vimplugin_dir/rplugin/python3/deoplete
%dir %vimplugin_dir/rplugin/python3/deoplete/sources
%vimplugin_dir/rplugin/python3/deoplete/sources/ale.py
%vimplugin_dir/syntax/ale-*.vim

%files -n vim-plugin-align
%defattr(-,root,root,0755)
%vimplugin_dir/doc/Align.txt
%vimplugin_dir/autoload/AlignMaps.vim
%vimplugin_dir/autoload/Align.vim
%vimplugin_dir/plugin/AlignMapsPlugin.vim
%vimplugin_dir/plugin/AlignPlugin.vim
%vimplugin_dir/plugin/cecutil.vim

%files -n vim-plugin-bufexplorer
%defattr(-,root,root,0755)
%license bufexplorer-%{bufexplorer_version_orig}/LICENSE
%vimplugin_dir/doc/bufexplorer.txt
%vimplugin_dir/plugin/bufexplorer.vim

%files -n vim-plugin-calendar
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/calendar.vim

%files -n vim-plugin-colorsel
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/colorsel.vim
%vimplugin_dir/autoload/colorsel.vim
%vimplugin_dir/doc/colorsel.txt

%files -n vim-plugin-colorschemes
%defattr(-,root,root,0755)
%vimplugin_dir/colors/*.vim

%files -n vim-plugin-diffchanges
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/diffchanges.vim
%vimplugin_dir/doc/diffchanges.txt

%files -n vim-plugin-editorconfig
%defattr(-,root,root,0755)
%license editorconfig-vim-%{editorconfig_version}/LICENSE
%vimplugin_dir/plugin/editorconfig.vim
%vimplugin_dir/autoload/editorconfig_core/
%vimplugin_dir/autoload/editorconfig_core.vim
%vimplugin_dir/autoload/editorconfig.vim
%vimplugin_dir/doc/editorconfig.txt

%files -n vim-plugin-file-line
%doc file-line-%{file_line_version}/README.md
%vimplugin_dir/plugin/file_line.vim

%files -n vim-plugin-fugitive
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/fugitive.vim
%vimplugin_dir/doc/fugitive.txt
%vimplugin_dir/autoload/fugitive.vim
%vimplugin_dir/ftdetect/fugitive.vim
%dir %vimplugin_dir/ftplugin/
%vimplugin_dir/ftplugin/fugitiveblame.vim
%vimplugin_dir/syntax/fugitive.vim
%vimplugin_dir/syntax/fugitiveblame.vim

%files -n vim-plugin-gitdiff
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/gitdiff.vim

%files -n vim-plugin-gitrebase-keywordprg
%vimplugin_dir/after/ftplugin/gitrebase.vim

%files -n vim-plugin-gnupg
%defattr(-,root,root,0755)
%vimplugin_dir/autoload/gnupg.vim
%vimplugin_dir/doc/gnupg.txt
%vimplugin_dir/plugin/gnupg.vim

%files -n vim-plugin-latex
%defattr(-,root,root,0755)
%doc vim-latex-%{latex_version}/README.md
%{_datadir}/appdata/vim-latex.metainfo.xml
%vimplugin_dir/doc/db2vim/
%vimplugin_dir/doc/latex*.txt
%vimplugin_dir/doc/imaps.txt
%vimplugin_dir/plugin/imaps.vim
%vimplugin_dir/plugin/remoteOpen.vim
%vimplugin_dir/plugin/filebrowser.vim
%vimplugin_dir/plugin/SyntaxFolds.vim
%dir %vimplugin_dir/compiler/
%vimplugin_dir/compiler/tex.vim
%dir %vimplugin_dir/indent/
%vimplugin_dir/indent/tex.vim
%dir %vimplugin_dir/ftplugin/
%vimplugin_dir/ftplugin/latex-suite
%vimplugin_dir/ftplugin/tex_latexSuite.vim
%vimplugin_dir/ftplugin/bib_latexSuite.vim
%vimplugin_dir/ltags
%vimplugin_dir/latextags

%files -n vim-plugin-locateopen
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/locateopen.vim

%files -n vim-plugin-markdown
%doc vim-markdown-%{markdown_version}/README.md vim-markdown-%{markdown_version}/CONTRIBUTING.md
%dir %vimplugin_dir/after/
%dir %vimplugin_dir/after/ftplugin/
%vimplugin_dir/after/ftplugin/markdown.vim
%dir %vimplugin_dir/ftdetect/
%vimplugin_dir/ftdetect/markdown.vim
%dir %vimplugin_dir/ftplugin/
%vimplugin_dir/ftplugin/markdown.vim
%dir %vimplugin_dir/indent/
%vimplugin_dir/indent/markdown.vim
%dir %{_datadir}/vim/registry/
%{_datadir}/vim/registry/markdown.yaml
%dir %vimplugin_dir/syntax/
%vimplugin_dir/syntax/markdown.vim
%vimplugin_dir/doc/vim-markdown.txt

%files -n vim-plugin-matrix
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/matrix.vim

%files -n vim-plugin-minibufexpl
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/minibufexpl.vim

%files -n vim-plugin-multiplesearch
%defattr(-,root,root,0755)
%vimplugin_dir/doc/MultipleSearch.txt
%vimplugin_dir/autoload/MultipleSearch.vim
%vimplugin_dir/plugin/MultipleSearch.vim

%files -n vim-plugin-neomutt
%defattr(-,root,root,0755)
%vimplugin_dir/doc/neomutt.txt
%vimplugin_dir/ftdetect/logfile.vim
%vimplugin_dir/ftdetect/mail.vim
%vimplugin_dir/ftdetect/neomuttrc.vim
%vimplugin_dir/ftplugin/neomuttrc.vim
%vimplugin_dir/syntax/neomuttlog.vim
%vimplugin_dir/syntax/neomuttrc.vim

%files -n vim-plugin-NERDcommenter
%defattr(-,root,root,0755)
%doc nerdcommenter-%{NERDcommenter_version}/README.md
%vimplugin_dir/autoload/nerdcommenter.vim
%vimplugin_dir/doc/nerdcommenter.txt
%vimplugin_dir/plugin/nerdcommenter.vim

%files -n vim-plugin-NERDtree
%defattr(-,root,root,0755)
%license nerdtree-%{NERDtree_version}/LICENCE
%doc nerdtree-%{NERDtree_version}/README.markdown
%vimplugin_dir/doc/NERDTree.txt
%vimplugin_dir/autoload/nerdtree.vim
%dir %vimplugin_dir/autoload/nerdtree/
%vimplugin_dir/autoload/nerdtree/ui_glue.vim
%dir %vimplugin_dir/lib/
%vimplugin_dir/lib/nerdtree/
%vimplugin_dir/plugin/NERD_tree.vim
%vimplugin_dir/syntax/nerdtree.vim
%doc %{_defaultdocdir}/vimplugin-NERDtree

%files -n vim-plugin-project
%defattr(-,root,root,0755)
%vimplugin_dir/doc/project.txt
%vimplugin_dir/plugin/project.vim

%files -n vim-plugin-quilt
%defattr(-,root,root,0755)
%vimplugin_dir/doc/quilt.txt
%vimplugin_dir/plugin/quilt.vim

%files -n vim-plugin-rails
%defattr(-,root,root,0755)
%vimplugin_dir/compiler/rails.vim
%vimplugin_dir/plugin/rails.vim
%vimplugin_dir/autoload/rails.vim
%vimplugin_dir/doc/rails.txt

%files -n vim-plugin-salt
%defattr(-,root,root,0755)
%vimplugin_dir/ftdetect/sls.vim
%vimplugin_dir/ftplugin/sls.vim
%vimplugin_dir/syntax/sls.vim

%files -n vim-plugin-searchcomplete
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/SearchComplete.vim

%files -n vim-plugin-showmarks
%doc ShowMarks7-%{showmarks_version}/README
%vimplugin_dir/plugin/showmarks.vim

%files -n vim-plugin-snipmate
%defattr(-,root,root,0755)
%vimplugin_dir/snippets
%vimplugin_dir/syntax/snippet.vim
%vimplugin_dir/plugin/snipMate.vim
%vimplugin_dir/ftplugin/html_snip_helper.vim
%dir %vimplugin_dir/after/
%dir %vimplugin_dir/after/plugin/
%vimplugin_dir/after/plugin/snipMate.vim
%vimplugin_dir/autoload/snipMate.vim
%vimplugin_dir/doc/snipMate.txt

%files -n vim-plugin-supertab
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/supertab.vim
%vimplugin_dir/doc/supertab.txt

%files -n vim-plugin-taglist
%defattr(-,root,root,0755)
%vimplugin_dir/doc/taglist.txt
%vimplugin_dir/plugin/taglist.vim

%files -n vim-plugin-tlib
%defattr(-,root,root,0755)
%license tlib_vim-%{tlib_version}/LICENSE.TXT
%vimplugin_dir/doc/tlib.txt
%vimplugin_dir/autoload/tlib
%vimplugin_dir/autoload/tinykeymap
%vimplugin_dir/plugin/02tlib.vim
%vimplugin_dir/autoload/tlib.vim
%dir %vimplugin_dir/macros/
%vimplugin_dir/macros/tlib.vim
%dir %vimplugin_dir/spec/
%vimplugin_dir/spec/tlib/

%files -n vim-plugin-tregisters
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/tregisters.vim

%files -n vim-plugin-tselectbuffer
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/tselectbuffer.vim
%vimplugin_dir/autoload/tselectbuffer.vim
%vimplugin_dir/doc/tselectbuffer.txt

%files -n vim-plugin-tselectfiles
%defattr(-,root,root,0755)
%vimplugin_dir/doc/tselectfiles.txt
%vimplugin_dir/autoload/tselectfiles.vim
%vimplugin_dir/plugin/tselectfiles.vim

%files -n vim-plugin-utl
%defattr(-,root,root,0755)
%doc utl.vim-%{utl_version}/README
%vimplugin_dir/doc/utl_ref.txt
%vimplugin_dir/doc/utl_usr.txt
%vimplugin_dir/plugin/utl_scm.vim
%vimplugin_dir/plugin/utl_rc.vim
%vimplugin_dir/plugin/utl_uri.vim
%vimplugin_dir/plugin/utl.vim
%vimplugin_dir/plugin/utl_arr.vim

%files -n vim-plugin-vimwiki
%defattr(-,root,root,0755)
%vimplugin_dir/doc/vimwiki.txt
%vimplugin_dir/plugin/vimwiki.vim
%dir %vimplugin_dir/ftplugin
%vimplugin_dir/ftplugin/vimwiki.vim
%vimplugin_dir/autoload/vimwiki
%vimplugin_dir/syntax/vimwiki*.vim

%files -n vim-plugin-zoomwin
%defattr(-,root,root,0755)
%vimplugin_dir/doc/ZoomWin.txt
%vimplugin_dir/plugin/ZoomWinPlugin.vim
%vimplugin_dir/autoload/ZoomWin.vim

%changelog
