#
# spec file for package vim-plugins
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define     align_version           36.42
%define     a_version           2.18
%define     bufexplorer_version     7.2.8
%define     calendar_version        2.4
%define     colorsel_version        20110107
%define     colorschemes_version        1.0
%define     diffchanges_version     0.6.346dae2
%define     locateopen_version      1.3
%define     matrix_version          1.10
%define     minibufexpl_version     6.3.2
%define     multiplesearch_version      1.3
%define     NERDcommenter_version       2.3.0
%define     NERDtree_version        4.2.0
%define     project_version         1.4.1
%define     searchcomplete_version      1.1
%define     showmarks_version       2.2
%define     supertab_version        1.0
%define     taglist_version         4.5
%define     tlib_version            0.42
%define     tregisters_version      0.2
%define     tselectbuffer_version       0.7
%define     tselectfiles_version        0.10
%define     utl_version         2.0
%define     zoomwin_version         24
%define     latex_version           20120125
%define     quilt_version           0.9.7
%define     vimwiki_version         2.1
%define     gnupg_version           2.6
%define     gitdiff_version         2
%define     snipmate_version        0.83
%define     rails_version           4.4
%define     ack_version         1.0.9
%define     editorconfig_version        0.3.3
%define     fugitive_version    2.2
%define     neomutt_version         20180104

Name:           vim-plugins
Version:        7.2.22
Release:        0
Summary:        Plug-ins pack for Vim
License:        MIT
Group:          Productivity/Text/Editors
Url:            http://www.vim.org/
Source0:        vimplugin-align-%{align_version}.tar.bz2
Source1:        vimplugin-a-%{a_version}.tar.bz2
Source2:        vimplugin-bufexplorer-%{bufexplorer_version}.tar.bz2
Source3:        vimplugin-calendar-%{calendar_version}.tar.bz2
Source4:        vimplugin-colorsel-%{colorsel_version}.tar.bz2
Source5:        vimplugin-colorschemes-%{colorschemes_version}.tar.bz2
Source6:        vimplugin-diffchanges-%{diffchanges_version}.tar.bz2
Source7:        vimplugin-locateopen-%{locateopen_version}.tar.bz2
Source9:        vimplugin-matrix-%{matrix_version}.tar.bz2
Source10:       vimplugin-minibufexpl-%{minibufexpl_version}.tar.bz2
Source11:       vimplugin-multiplesearch-%{multiplesearch_version}.tar.bz2
Source12:       vimplugin-NERDcommenter-%{NERDcommenter_version}.tar.bz2
Source13:       vimplugin-NERDtree-%{NERDtree_version}.tar.bz2
Source14:       vimplugin-project-%{project_version}.tar.bz2
Source15:       vimplugin-searchcomplete-%{searchcomplete_version}.tar.bz2
Source16:       vimplugin-showmarks-%{showmarks_version}.tar.bz2
Source17:       vimplugin-supertab-%{supertab_version}.tar.bz2
Source18:       vimplugin-taglist-%{taglist_version}.tar.bz2
Source19:       vimplugin-tlib-%{tlib_version}.tar.bz2
Source20:       vimplugin-tregisters-%{tregisters_version}.tar.bz2
Source21:       vimplugin-tselectbuffer-%{tselectbuffer_version}.tar.bz2
Source22:       vimplugin-tselectfiles-%{tselectfiles_version}.tar.bz2
Source23:       vimplugin-utl-%{utl_version}.tar.bz2
Source24:       vimplugin-zoomwin-%{zoomwin_version}.tar.bz2
Source25:       vimplugin-latex-%{latex_version}.tar.bz2
Source26:       vimplugin-quilt-%{quilt_version}.tar.bz2
Source27:       vimplugin-vimwiki-%{vimwiki_version}.tar.bz2
Source28:       vimplugin-gnupg-%{gnupg_version}.tar.bz2
Source29:       vimplugin-gitdiff-%{gitdiff_version}.tar.bz2
Source30:       vimplugin-snipmate-%{snipmate_version}.tar.bz2
Source31:       vimplugin-rails-%{rails_version}.tar.bz2
Source32:       https://github.com/mileszs/ack.vim/archive/%{ack_version}.tar.gz#/vimplugin-ack-%{ack_version}.tar.gz
Source34:       https://github.com/editorconfig/editorconfig-vim/archive/v%{editorconfig_version}.tar.gz#/vimplugin-editorconfig-%{editorconfig_version}.tar.gz
Source35:       https://github.com/tpope/vim-fugitive/archive/v%{fugitive_version}.tar.gz#/vimplugin-fugitive-%{fugitive_version}.tar.gz
Source36:       vimplugin-neomutt-%{neomutt_version}.tar.bz2
Source100:      https://raw.githubusercontent.com/openSUSE/pack-tools/master/contrib/vim/spec.snippets
Patch1:         locateopen-1.3-locate-support.patch
Patch2:         showmarks-signs.patch
BuildRequires:  vim
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%define     vimplugin_dir %{_datadir}/vim/site

%description
Subpackages of this packages contains some plugins for Vi iMproved text editor.

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

%package -n vim-plugin-bufexplorer
Version:        %bufexplorer_version
Release:        0
Summary:        Buffer Explorer / Browser
License:        ISC
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-bufexplorer
With bufexplorer, you can quickly switch between buffers by using '\be' to open
the explorer.vim. Then by using the normal movement keys or mouse to select the
needed buffer and then finally pressing <Enter> or <Left Mouse Click> to open
the buffer in the current window or <Shift Enter> or 't' to open that buffer in
a new tab.  If the buffer is in another tab already, bufexplorer can switch to
that tab if you would like.

%package -n vim-plugin-calendar
Version:        %calendar_version
Release:        0
Summary:        Calendar for vim
License:        BSD-3-Clause
Group:          Productivity/Text/Editors
Requires:       vim

%description -n vim-plugin-calendar
Plugin for vim that displays simple calendar in the side window.

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

%package -n vim-plugin-gnupg
Version:        %gnupg_version
Release:        0
Summary:        Plugin for transparent editing of gpg encrypted files
License:        GPL-1.0-or-later
Group:          Productivity/Text/Editors
Url:            https://github.com/jamessan/vim-gnupg
Requires:       gpg2

%description -n vim-plugin-gnupg
This script implements transparent editing of gpg encrypted files. The filename
must have a ".gpg", ".pgp" or ".asc" suffix. When opening such a file the
content is decrypted, when opening a new file the script will ask for the
recipients of the encrypted file. The file content will be encrypted to all
recipients before it is written. The script turns off viminfo, swapfile, and
undofile to increase security.

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

%package -n vim-plugin-rails

Version:        %rails_version
Release:        0
Summary:        Support for Ruby on Rails development
License:        Vim
Group:          Productivity/Text/Editors
Recommends:     rubygem(rails)

%description -n vim-plugin-rails
This plugin offers the many features for Ruby on Rails application development.

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

%package -n vim-plugin-editorconfig

Version:        %editorconfig_version
Release:        0
Summary:        EditorConfig plugin for Vim
License:        BSD-2-Clause
Group:          Productivity/Text/Editors
Requires:       editorconfig

%description -n vim-plugin-editorconfig
EditorConfig helps developers define and maintain consistent coding styles between 
different editors and IDEs. The EditorConfig project consists of a file format for 
defining coding styles and a collection of text editor plugins that enable editors 
to read the file format and adhere to defined styles. EditorConfig files are 
easily readable and they work nicely with version control systems.

This package contains a Vim plugin to support EditorConfig.

%package -n vim-plugin-fugitive

Version:        %fugitive_version
Release:        0
Summary:        Fugitive plugin for Vim
License:        Vim
Group:          Productivity/Text/Editors
Requires:       git-core

%description -n vim-plugin-fugitive
Provides git integration with vim.

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

%prep
%setup -q -c -n %{name} -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a9 -a10 -a11 -a12 -a13 -a14 -a15 -a16 -a17 -a18 -a19 -a20 -a21 -a22 -a23 -a24 -a25 -a26 -a27 -a28 -a29 -a30 -a31 -a32 -a34 -a35 -a36
# ------- patch locateopen ------
pushd vimplugin-locateopen-%locateopen_version
%patch1
popd
pushd vimplugin-showmarks-%showmarks_version
%patch2 -p1
popd

%build

%install
for i in vimplugin-*; do
    pushd $i
    mkdir -p %buildroot/%vimplugin_dir
    cp -a * %buildroot/%vimplugin_dir/
    popd
done
mkdir -p %{buildroot}%{_defaultdocdir}/vimplugin-NERDtree/
mv %{buildroot}/%vimplugin_dir/nerdtree_plugin %{buildroot}%{_defaultdocdir}/vimplugin-NERDtree/

# vim-plugin-ack
pushd ack.vim-%{ack_version}
cp -a autoload doc plugin %{buildroot}/%{vimplugin_dir}
# vim-plugin-latext creates ftplugin
cp -a ftplugin/qf.vim %{buildroot}%{vimplugin_dir}/ftplugin/
popd

# vim-plugin-editorconfig
pushd editorconfig-vim-%{editorconfig_version}
rm -rf plugin/editorconfig-core-py/ tests/
rm mkzip.sh README.md LICENSE CONTRIBUTORS
mkdir -p %buildroot/%vimplugin_dir
cp -a * %buildroot/%vimplugin_dir/
popd

# vim-plugin-fugitive
pushd vim-fugitive-%{fugitive_version}
mkdir -p %buildroot/%vimplugin_dir
cp -a plugin doc %{buildroot}/%{vimplugin_dir}
popd

cp %{SOURCE100} %{buildroot}/%vimplugin_dir/snippets/

# delete unneeded files
rm -rf %{buildroot}/%vimplugin_dir/doc/Makefile*
rm -rf %{buildroot}/%vimplugin_dir/doc/README*
rm -rf %{buildroot}/%vimplugin_dir/doc/*.{xml,xsl,css}

%clean
rm -rf %{buildroot}

# For every plugin providing documentation, we have to call the post and postun scriptlets
# Unfortunatelly, there is no easy way how to achieve that except listing them manually :(

# documentation: vim-plugin-align

%post -n vim-plugin-align
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-align
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-a

%post -n vim-plugin-a
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-a
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-bufexplorer

%post -n vim-plugin-bufexplorer
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-bufexplorer
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-multiplesearch

%post -n vim-plugin-multiplesearch
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-multiplesearch
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-NERDcommenter

%post -n vim-plugin-NERDcommenter
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-NERDcommenter
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-NERDtree

%post -n vim-plugin-NERDtree
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-NERDtree
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-project

%post -n vim-plugin-project
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-project
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-showmarks

%post -n vim-plugin-showmarks
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-showmarks
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-taglist

%post -n vim-plugin-taglist
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-taglist
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-tlib

%post -n vim-plugin-tlib
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-tlib
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-tselectfiles

%post -n vim-plugin-tselectfiles
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-tselectfiles
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-utl

%post -n vim-plugin-utl
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-utl
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-zoomwin

%post -n vim-plugin-zoomwin
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-zoomwin
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-latex

%post -n vim-plugin-latex
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-latex
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-quilt

%post -n vim-plugin-quilt
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-quilt
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-vimwiki

%post -n vim-plugin-vimwiki
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-vimwiki
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-snipmate

%post -n vim-plugin-snipmate
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-snipmate
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-rails

%post -n vim-plugin-rails
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-rails
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-colorsel

%post -n vim-plugin-colorsel
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-colorsel
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-diffchanges

%post -n vim-plugin-diffchanges
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-diffchanges
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-ack

%post -n vim-plugin-ack
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-ack
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-editorconfig

%post -n vim-plugin-editorconfig
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-editorconfig
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-fugitive

%post -n vim-plugin-fugitive
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-fugitive
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

# documentation: vim-plugin-neomutt

%post -n vim-plugin-neomutt
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun -n vim-plugin-neomutt
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

%post
vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null

%postun
if [ $1 == 0 ]; then
  vim -u NONE -U NONE -X -n '+set nobackup nomore' '+helptags %vimplugin_dir/doc/' '+qa!' < /dev/null &> /dev/null
fi

%files -n vim-plugin-align
%defattr(-,root,root,0755)
%vimplugin_dir/doc/Align.txt
%vimplugin_dir/autoload/AlignMaps.vim
%vimplugin_dir/autoload/Align.vim
%vimplugin_dir/plugin/AlignMapsPlugin.vim
%vimplugin_dir/plugin/AlignPlugin.vim
%vimplugin_dir/plugin/cecutil.vim

%files -n vim-plugin-a
%defattr(-,root,root,0755)
%vimplugin_dir/doc/alternate.txt
%vimplugin_dir/plugin/a.vim

%files -n vim-plugin-bufexplorer
%defattr(-,root,root,0755)
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

%files -n vim-plugin-locateopen
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/locateopen.vim

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

%files -n vim-plugin-NERDcommenter
%defattr(-,root,root,0755)
%vimplugin_dir/doc/NERD_commenter.txt
%vimplugin_dir/plugin/NERD_commenter.vim

%files -n vim-plugin-NERDtree
%defattr(-,root,root,0755)
%vimplugin_dir/doc/NERD_tree.txt
%vimplugin_dir/plugin/NERD_tree.vim
%vimplugin_dir/syntax/nerdtree.vim
%doc %{_defaultdocdir}/vimplugin-NERDtree

%files -n vim-plugin-project
%defattr(-,root,root,0755)
%vimplugin_dir/doc/project.txt
%vimplugin_dir/plugin/project.vim

%files -n vim-plugin-searchcomplete
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/SearchComplete.vim

%files -n vim-plugin-showmarks
%defattr(-,root,root,0755)
%vimplugin_dir/doc/showmarks.txt
%vimplugin_dir/plugin/showmarks.vim

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
%vimplugin_dir/doc/tlib.txt
%vimplugin_dir/autoload/tlib
%vimplugin_dir/plugin/02tlib.vim
%vimplugin_dir/autoload/tlib.vim

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
%vimplugin_dir/doc/utl_ref.txt
%vimplugin_dir/doc/utl_usr.txt
%vimplugin_dir/plugin/utl_scm.vim
%vimplugin_dir/plugin/utl_rc.vim
%vimplugin_dir/plugin/utl_uri.vim
%vimplugin_dir/plugin/utl.vim
%vimplugin_dir/plugin/utl_arr.vim

%files -n vim-plugin-zoomwin
%defattr(-,root,root,0755)
%vimplugin_dir/doc/ZoomWin.txt
%vimplugin_dir/plugin/ZoomWinPlugin.vim
%vimplugin_dir/autoload/ZoomWin.vim

%files -n vim-plugin-latex
%defattr(-,root,root,0755)
%vimplugin_dir/doc/latex*.txt
%vimplugin_dir/doc/imaps.txt
%vimplugin_dir/plugin/imaps.vim
%vimplugin_dir/plugin/libList.vim
%vimplugin_dir/plugin/remoteOpen.vim
%vimplugin_dir/plugin/filebrowser.vim
%vimplugin_dir/plugin/SyntaxFolds.vim
%vimplugin_dir/compiler/tex.vim
%dir %vimplugin_dir/compiler
%vimplugin_dir/indent/tex.vim
%dir %vimplugin_dir/indent
%dir %vimplugin_dir/ftplugin
%vimplugin_dir/ftplugin/latex-suite
%vimplugin_dir/ftplugin/tex_latexSuite.vim
%vimplugin_dir/ftplugin/bib_latexSuite.vim
%vimplugin_dir/ltags
%vimplugin_dir/latextags

%files -n vim-plugin-quilt
%defattr(-,root,root,0755)
%vimplugin_dir/doc/quilt.txt
%vimplugin_dir/plugin/quilt.vim

%files -n vim-plugin-vimwiki
%defattr(-,root,root,0755)
%vimplugin_dir/doc/vimwiki.txt
%vimplugin_dir/plugin/vimwiki.vim
%dir %vimplugin_dir/ftplugin
%vimplugin_dir/ftplugin/vimwiki.vim
%dir %vimplugin_dir/indent
%vimplugin_dir/autoload/vimwiki
%vimplugin_dir/syntax/vimwiki*.vim

%files -n vim-plugin-gnupg
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/gnupg.vim

%files -n vim-plugin-gitdiff
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/gitdiff.vim

%files -n vim-plugin-snipmate
%defattr(-,root,root,0755)
%vimplugin_dir/snippets
%vimplugin_dir/syntax/snippet.vim
%vimplugin_dir/plugin/snipMate.vim
%vimplugin_dir/ftplugin/html_snip_helper.vim
%vimplugin_dir/after
%vimplugin_dir/autoload/snipMate.vim
%vimplugin_dir/doc/snipMate.txt

%files -n vim-plugin-rails
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/rails.vim
%vimplugin_dir/autoload/rails.vim
%vimplugin_dir/doc/rails.txt

%files -n vim-plugin-ack
%defattr(-,root,root,0755)
%doc ack.vim-%{ack_version}/README.md
%vimplugin_dir/plugin/ack.vim
%vimplugin_dir/autoload/ack.vim
%vimplugin_dir/doc/ack.txt
%vimplugin_dir/doc/ack_quick_help.txt
%dir %vimplugin_dir/ftplugin
%vimplugin_dir/ftplugin/qf.vim

%files -n vim-plugin-editorconfig
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/editorconfig.vim
%vimplugin_dir/autoload/editorconfig.vim
%vimplugin_dir/doc/editorconfig.txt

%files -n vim-plugin-fugitive
%defattr(-,root,root,0755)
%vimplugin_dir/plugin/fugitive.vim
%vimplugin_dir/doc/fugitive.txt

%files -n vim-plugin-neomutt
%defattr(-,root,root,0755)
%vimplugin_dir/doc/neomutt.txt
%vimplugin_dir/ftdetect/mail.vim
%vimplugin_dir/ftdetect/neomuttrc.vim
%vimplugin_dir/ftplugin/neomuttrc.vim
%vimplugin_dir/syntax/neomuttrc.vim

%changelog
