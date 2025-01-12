#
# spec file for package cmatrix
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


Name:           cmatrix
Version:        2.0
Release:        0
Summary:        The Matrix screensaver
License:        GPL-3.0-only
Group:          Amusements/Games/Other
URL:            https://github.com/abishekvashok/cmatrix
Source:         %{name}-%{version}.tar.xz
Patch0:         fix_compilation_errors.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  kbd
BuildRequires:  m4
BuildRequires:  mkfontdir
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
Requires:       filesystem
Requires:       kbd

%description
CMatrix is based on the screensaver from The Matrix website. It shows text flying in and out in a terminal like as seen in "The Matrix" movie. It can scroll lines all at the same rate or asynchronously and at a user-defined speed

%prep
%setup -q

%autopatch -p1

%build
autoreconf -vfi
%configure --enable-fonts
%make_build

%install
mkdir -p %{buildroot}%{_datadir}/fonts/misc
mkdir -p %{buildroot}%{_datadir}/kbd/consolefonts

%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/fonts/misc/*
%dir %{_datadir}/fonts/misc
%{_datadir}/kbd/consolefonts/*

%changelog
