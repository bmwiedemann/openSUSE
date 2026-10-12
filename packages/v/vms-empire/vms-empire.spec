#
# spec file for package vms-empire
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.23
Release:        0
Summary:        Simulation of a full-scale war between two emperors
License:        GPL-2.0-only
URL:            http://www.catb.org/~esr/vms-empire/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  hicolor-icon-theme
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)

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
# build the binary only: the man page ships pre-generated, no asciidoctor needed
%make_build vms-empire CFLAGS="%{optflags}"

%install
# upstream Makefile ignores DESTDIR, install paths derive from PREFIX
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%license COPYING
%doc AUTHORS BUGS HACKING NEWS.adoc README.adoc
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.adoc
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
