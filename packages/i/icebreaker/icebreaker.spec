#
# spec file for package icebreaker
#
# Copyright (c) 2022 SUSE LLC
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


Name:           icebreaker
Version:        2.2.1
Release:        0
Summary:        An action-puzzle game involving bouncing penguins
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Puzzle
URL:            http://www.mattdm.org/icebreaker/
Source:         https://mattdm.org/icebreaker/2.2.x/icebreaker-%{version}.tar.xz
# PATCH-FIX-OPENSUSE icebreaker-makefile-fix.patch - fixes unterminated call to function 'shell' in makefile for openSUSE Leap and use $(CC) instead hardcoded gcc
Patch1:         icebreaker-makefile-fix.patch
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(sdl)
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10
%else
BuildRequires:  gcc
%endif

%description
IceBreaker is an action-puzzle game in which the player must section
off level space, preferably in the least amount of time with the
least amount of mistakes. IceBreaker was inspired by (but is far from
an exact clone of) the 1992 game Jezzball by Dima Pavlovsky, itself
having similarities to the 1981 game of Qix.

%prep
%setup -q
%patch1 -p1

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-10
%else
export CC=gcc
%endif
%make_build OPTIMIZE="%{optflags}" prefix=%{_prefix}

%install
%make_install prefix=%{buildroot}%{_prefix}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications icebreaker.desktop
install -Dm0644 metainfo.xml %{buildroot}%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml

%files
%license LICENSE
%doc README README.themes TODO ChangeLog
%{_bindir}/icebreaker
%{_datadir}/applications/icebreaker.desktop
%{_datadir}/metainfo/org.mattdm.icebreaker.metainfo.xml
%{_datadir}/icebreaker
%{_mandir}/man6/*

%changelog
