#
# spec file for package nudoku
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nudoku
Version:        2.0.0
Release:        0
Summary:        Ncurses based sudoku game
License:        GPL-3.0-only
Group:          Amusements/Games/Board/Puzzle
URL:            https://github.com/jubalh/%{name}
Source:         https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  ncurses-devel
BuildRequires:  xz
Recommends:     %{name}-lang

%description
nudoku is a ncurses based sudoku game.

%lang_package

%prep
%setup -q

%build
autoreconf -fi
%configure --enable-cairo
make %{?_smp_mflags}

%install
%make_install

%find_lang %{name}

%files
%{_bindir}/nudoku
%{_mandir}/man?/nudoku.*

%files lang -f %{name}.lang
%{_datadir}/locale/??/LC_MESSAGES/nudoku.mo

%changelog
