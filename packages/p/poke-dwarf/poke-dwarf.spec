#
# spec file for package poke-dwarf
#
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           poke-dwarf
Version:        0.1~git20231115
Release:        0
Summary:        Plug-in for GNU poke for editing DWARF files
License:        GPL-3.0-or-later
URL:            https://www.jemarch.net/poke-dwarf.html
Source:         %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
# pull in poke-devel for bootstrapping
BuildRequires:  pkgconfig(poke)
Requires:       poke >= 4.0
Supplements:    poke >= 4.0
BuildArch:      noarch

%description
poke-dwarf is a GNU poke pickle for editing DWARF debugginf information. It
covers Call Frame Information, DIE tree, debug types, expressions, and much
more.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS README
%{_infodir}/poke-dwarf.info%{?ext_info}
%dir %{_datadir}/poke
%{_datadir}/poke/pickles

%changelog
