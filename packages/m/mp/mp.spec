#
# spec file for package mp
#
# Copyright (c) 2024 SUSE LLC
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
Version:        5.2.13
Release:        0
Summary:        A text editor for programmers
License:        GPL-2.0-only
URL:            https://triptico.com/software/mp.html
Source0:        mp-%{version}.tar.gz
Source1:        mp-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        %{name}-5.desktop
Source4:        %{name}-5.png
Source5:        %{name}-rpmlintrc
Source6:        %{name}-5-gtk3.desktop
Patch0:         %{name}-docdir.patch
Patch1:         %{name}-scrollevent.patch
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Widgets)
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
%autosetup -p1

%build
export CFLAGS="%{optflags}"
./config.sh --prefix=%{_prefix} --docdir=%{_docdir}/mp-5
%make_build
mv mp-5 mp-5-qt5
WITHOUT_QT5=1 WITHOUT_QT4=1 ./config.sh --prefix=%{_prefix} --docdir=%{_docdir}/mp-5
%make_build
mv mp-5 mp-5-gtk3
mv mp-5-qt5 mp-5

%install
%make_install

install -D -p -m 644 %{SOURCE3} %{buildroot}/%{_datadir}/applications/%{name}-5.desktop
install -D -p -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/pixmaps/%{name}-5.png
install -p -m 644 %{SOURCE6} %{buildroot}/%{_datadir}/applications/%{name}-5-gtk3.desktop
install -m 755 mp-5-gtk3 %{buildroot}%{_bindir}/mp-5-gtk3
install -m 644 mp-5.1 %{buildroot}/%{_mandir}/man1/mp-5-gtk3.1

%suse_update_desktop_file %{name}-5 TextEditor

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
%{_datadir}/applications/%{name}-5.desktop
%{_datadir}/pixmaps/%{name}-5.png

%files gtk3
%{_bindir}/%{name}-5-gtk3
%{_datadir}/applications/%{name}-5-gtk3.desktop
%{_mandir}/man1/%{name}-5-gtk3.1%{?ext_man}

%changelog
