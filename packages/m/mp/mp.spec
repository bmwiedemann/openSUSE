#
# spec file for package mp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           mp
Version:        5.62
Release:        0
Summary:        A text editor for programmers
License:        GPL-2.0-only
URL:            https://triptico.com/software/mp.html
Source0:        https://github.com/ttcdt/mp-5.x/archive/refs/tags/%{version}.tar.gz#/mp-%{version}.tar.gz
Source5:        %{name}-rpmlintrc
Source101:      https://triptico.com/download/grutatxt.tar.gz
Source102:      https://triptico.com/download/mp_doccer-1.2.2.tar.gz
Patch2:         mp-5.62-releasenotes.patch
Patch3:         mp-5.62-installdirs.patch
Patch4:         mp-5.62-config-msgfmt.patch
Patch5:         mp-5.62-mpdm-config.patch
Patch6:         mp-5.62-mpsl-make-quickref.patch
Patch7:         mp-5.62-config-qt6.patch
Patch8:         mp-5.62-qt6-isnull.patch
Patch9:         mp-5.62-qt6-weight.patch
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
Minimum Profit
A text editor for programmers

Features

    * Fully scriptable using a C-like scripting language.
    * Unlimited undo levels.
    * Complete Unicode support.
    * Multiple files can be edited at the same time and blocks copied and pasted among them.
    * Syntax highlighting for many popular languages / file formats: C, C++, Perl, Shell Scripts,
      Ruby, Php, Python, HTML...
    * Creative use of tags: tags created by the external utility ctags are used to move
      instantaneously to functions or variables inside your current source tree. Tags are
      visually highlighted (underlined), and symbol completion can be triggered to avoid typing
      your own function names over and over.
    * Intelligent help system: pressing F1 over any word of a text being edited triggers the
      underlying system help (calling man when editing C or Shell files, perldoc with Perl, ri
      on Ruby, winhelp on MS Windows...).
    * Understandable interface: drop-down menus, reasonable default key bindings.
    * Configurable keys, menus and colors.
    * Text templates can be easily defined / accessed.
    * Multiplatform: Console/curses, GTK+, MS Windows.
    * Automatic indentation, word wrapping, internal grep, learning / repeating functions.
    * Spellchecking support (via the ispell package).
    * Multilingual.
    * Password-protected, encrypted text files (using the ARCFOUR algorithm).
    * It helps you abandon vi, emacs and other six-legged freaks definitely.

%package        gtk3
Summary:        A text editor for programmers (GTK+3 version)
Requires:       %{name} = %{version}

%description    gtk3
Minimum Profit
A text editor for programmers (GTK+3 version)

Features

    * Fully scriptable using a C-like scripting language.
    * Unlimited undo levels.
    * Complete Unicode support.
    * Multiple files can be edited at the same time and blocks copied and pasted among them.
    * Syntax highlighting for many popular languages / file formats: C, C++, Perl, Shell Scripts,
      Ruby, Php, Python, HTML...
    * Creative use of tags: tags created by the external utility ctags are used to move
      instantaneously to functions or variables inside your current source tree. Tags are
      visually highlighted (underlined), and symbol completion can be triggered to avoid typing
      your own function names over and over.
    * Intelligent help system: pressing F1 over any word of a text being edited triggers the
      underlying system help (calling man when editing C or Shell files, perldoc with Perl, ri
      on Ruby, winhelp on MS Windows...).
    * Understandable interface: drop-down menus, reasonable default key bindings.
    * Configurable keys, menus and colors.
    * Text templates can be easily defined / accessed.
    * Multiplatform: Console/curses, GTK+, MS Windows.
    * Automatic indentation, word wrapping, internal grep, learning / repeating functions.
    * Spellchecking support (via the ispell package).
    * Multilingual.
    * Password-protected, encrypted text files (using the ARCFOUR algorithm).
    * It helps you abandon vi, emacs and other six-legged freaks definitely.

%prep
## helper tools needed to build docs and man page
%setup -q -T -c -n helpers -a 101
cd ..
%setup -q -T -D -c -n helpers -a 102
cd ..
mv helpers/Grutatxt*/{Grutatxt.pm,grutatxt} helpers/mp_doccer*/mp_doccer helpers
sed -e "s:use lib '.':use lib '%{_builddir}/helpers':" -i helpers/grutatxt

%autosetup -p1 -n mp-5.x-%{version}

%build
## nneded for Qt6, see qt6-base / qt6-core-devel
%if 0%{?suse_version} == 1500
export CC=gcc-13
export CPP=g++-13
%endif
export CFLAGS="%{optflags}"
export PATH=${PATH}:%{_builddir}/helpers
./config.sh --prefix=%{_prefix} --docdir=%{_docdir}/mp-5 --with-moc=%{_libexecdir}/qt6/moc
%make_build
mv mp-5 mp-5-qt5
WITHOUT_MSGFMT=0 WITHOUT_QT5=1 ./config.sh --prefix=%{_prefix} --docdir=%{_docdir}/mp-5
%make_build
%make_build docs
sed -e 's/^Exec=mp-5/&-gtk3/' -e 's/^Name=.*/& (GTK+3 version)/' <minimum-profit.desktop >minimum-profit.desktop-gtk3
mv mp-5 mp-5-gtk3
mv mp-5-qt5 mp-5

%install
%make_install install-arch
%make_install -C mpsl

install -m 755 mp-5-gtk3 %{buildroot}%{_bindir}/mp-5-gtk3
install -m 644 mp-5.1 %{buildroot}/%{_mandir}/man1/mp-5-gtk3.1
install -m 644 minimum-profit.desktop-gtk3 %{buildroot}/%{_datadir}/applications/minimum-profit-gtk3.desktop

%find_lang minimum-profit
rm %{buildroot}%{_docdir}/mp-5/mpsl_quickref.ps
%fdupes -s %{buildroot}

%files -f minimum-profit.lang
%{_bindir}/%{name}-5
%{_bindir}/%{name}sl
%dir %{_docdir}/%{name}-5
%{_docdir}/%{name}-5/*
%{_mandir}/man1/%{name}-5.1%{?ext_man}
%dir %{_datadir}/%{name}-5
%{_datadir}/%{name}-5/*
%{_datadir}/applications/minimum-profit.desktop
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/metainfo/*

%files gtk3
%{_bindir}/%{name}-5-gtk3
%{_datadir}/applications/minimum-profit-gtk3.desktop
%{_mandir}/man1/%{name}-5-gtk3.1%{?ext_man}

%changelog
