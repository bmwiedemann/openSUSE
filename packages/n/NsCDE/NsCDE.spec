#
# spec file for package NsCDE
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


Name:           NsCDE
Version:        2.3
Release:        0
Summary:        Not so Common Desktop Environment (NsCDE)
License:        GPL-3.0-only
URL:            https://github.com/NsCDE/NsCDE
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE leafpad.patch maurizio.galli@suse.com -- add leafpad to recognized texteditors
Patch0:         leafpad.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  ksh
BuildRequires:  make
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
Requires:       fvwm2
Recommends:     leafpad
Recommends:     pcmanfm
Recommends:     xscreensaver

%description
Visually, NsCDE mimics CDE, the well known Common Desktop Environment of
many commercial UNIX systems of the nineties. It supports CDE backdrops and
palettes with FVWM colorsets and has a theme generator for Xt, Xaw, Motif,
GTK2, GTK3, Qt4 and Qt5.

Integrating all these bits and pieces, the user gets a retro visual experience
across almost all X11 applications. Enriched with a bunch of powerful
FVWM concepts and functions, modern applications and font rendering,
NsCDE acts as a link between classic CDE look and a fast and
extensible environment, well suited for modern day computing.

%package doc
Summary:        Docs for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%lang_package

%prep
%autosetup -p1

# Fix .desktop files
sed -i 's/OnlyShowIn=NsCDE;/OnlyShowIn=X-NsCDE;/g' ./xdg/applications/*.desktop

# Fix python shebangs
find . -name '*.in' -exec sed -i 's:#!@PYTHON@:#!/usr/bin/python3:g' {} +

%build
%configure
%make_build

%install
%make_install
%fdupes -s %{buildroot}
%find_lang %{name} --all-name

#fix upstream
chmod -x %{buildroot}%{_libdir}/%{name}/python/SpritesGtk2.py

%files
%license COPYING
%doc ChangeLog
%{_bindir}/nscde
%{_bindir}/nscde_fvwmclnt

%{_datadir}/icons/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/
%{_datadir}/xsessions/nscde.desktop
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*

%{_libexecdir}/%{name}

%{_libdir}/%{name}

%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/nscde-applications.menu

%files lang -f %{name}.lang

%files doc
%{_datadir}/doc/nscde

%changelog
