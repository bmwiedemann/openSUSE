#
# spec file for package vms-empire
#
# Copyright (c) 2020 SUSE LLC
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


Name:           vms-empire
Version:        1.15
Release:        0
Summary:        Simulation of a full-scale war between two emperors
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Turn Based
URL:            http://www.catb.org/~esr/vms-empire/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Pull-all-globals-into-a-context-struct.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files

%description
The ancestor of all 4x (expand/explore/exploit/exterminate) games.
VMS-Empire is a simulation of a full-scale war between two emperors,
the computer and you. Naturally, there is only room for one, so the
object of the game is to destroy the other. The computer plays by the
same rules that you do. This game is the ancestor of all the multiplayer
4X simulations out there, including Civilization and Master of Orion.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install

%suse_update_desktop_file %{name}

%files
%license COPYING
%doc AUTHORS BUGS HACKING NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/appdata/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
