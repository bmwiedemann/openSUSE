#
# spec file for package nsnake
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


Name:           nsnake
Version:        3.0.1
Release:        0
Summary:        Classic snake game on the terminal
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/alexdantas/nSnake
#Git-Clone:     https://github.com/alexdantas/nSnake.git
Source:         https://github.com/alexdantas/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         nsnake-3.0.1-ESCDELAY.patch
Patch1:         reproducible.patch
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  ncurses-devel

%description
nsnake is a clone of the classic snake game that we all used to play on our
cellphones. You play this game on the terminal, with textual interface.

Here are some features:

- Customizable gameplay, appearance and keybindings
- Neat GUI-like interface with nice animations
- Lots of possible game modes, with scores saved for eac

%prep
%setup -q -n nSnake-%{version}
%patch0 -p1
%patch1 -p1

%build
make %{?_smp_mflags}

%install
%make_install DESTDIR=%{buildroot}

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog NEWS TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
