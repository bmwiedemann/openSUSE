#
# spec file for package galaxis
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


Name:           galaxis
Version:        1.11
Release:        0
Summary:        Clone of the nifty little Macintosh game
License:        BSD-3-Clause
Group:          Amusements/Games/Strategy/Turn Based
URL:            http://www.catb.org/~esr/galaxis/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM - galaxis-Makefile.patch -- Fix paths and installation
Patch0:         %{name}-Makefile.patch
# PATCH-FIX-UPSTREAM - galaxis-superhack.c.patch -- Fix bad C++ code
Patch1:         %{name}-galaxis.c.patch
BuildRequires:  libncurses6
BuildRequires:  ncurses-devel
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
GALAXIS for UNIX

Lifeboats from a crippled interstellar liner are adrift in a starfield.
To find them, you can place probes that look in all eight compass
directions and tell you how many lifeboats they see. If you drop a probe
directly on a lifeboat it will be revealed immediately. Your objective:
find the lifeboats as quickly as possible, before the stranded passengers
run out of oxygen!

This is a UNIX-hosted, curses-based clone of the nifty little Macintosh
freeware game Galaxis. It doesn't have the super-simple, point-and-click
interface of the original, but compensates by automating away some of
the game's simpler deductions.

%prep
%autosetup -p0

cp -af %{SOURCE1} .

%build
%make_build CFLAGS="%{optflags}"

%install
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%license COPYING
%doc NEWS.adoc README.adoc galaxis.adoc
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
