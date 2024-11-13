#
# spec file for package bomns
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


Name:           bomns
Version:        0.99.3
Release:        0
Summary:        Best old-school Deathmatch game ever (only for two players)
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/keithfancher/Bomns-for-Linux
# Downloaded from https://github.com/keithfancher/Bomns-for-Linux
# Packed as tar.bz2
Source:         %{name}-%{version}+git-113be27.tar.bz2
# PATCH-FIX-UPSTREAM - bomns-bomns.desktop.patch -- Add GenericName
Patch0:         %{name}-%{name}.desktop.patch
# PATCH-FIX-UPSTREAM - fix-missing-header.patch -- Add missing header for isspace
Patch1:         fix-missing-header.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
%endif
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sdl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The gameplay of Bomns for Linux is quite simple: just move around the level,
picking up powerups and avoiding powerdowns, all the while laying bomns and
plotting your opponent's desctruction. A bomn will do 5 damage to the other
player, and running into them will do 1 damage. The first to kill their
opponent before the time runs out is declared the winner.

Player one controls:
  Move      : arrow keys
  Drop Bomn : enter

Player two controls:
  Move      : w,a,s,d
  Drop Bomn : spacebar

Other controls:
  Enter/exit fullscreen mode: f
  Quit current game         : escape

%prep
%autosetup -p1 -n Bomns-for-Linux

%build
%cmake
make %{?_smp_mflags}

%install
cd build
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README TODO
%{_bindir}/%{name}
%{_bindir}/%{name}edit
%{_bindir}/%{name}launcher
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%changelog
