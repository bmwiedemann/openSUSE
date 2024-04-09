#
# spec file for package poke-elf
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


Name:           poke-elf
Version:        1.0
Release:        0
Summary:        Plug-in for GNU poke for editing ELF files
License:        GPL-3.0-or-later
URL:            https://www.jemarch.net/poke-elf.html
Source:         https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/poke/%{name}-%{version}.tar.gz.sig
Source3:        https://savannah.gnu.org/people/viewgpg.php?user_id=829#/%{name}.keyring
Requires:       poke >= 4.0
Supplements:    poke >= 4.0
BuildArch:      noarch

%description
poke-elf is a GNU poke pickle for editing ELF object files, executables, shared
libraries and core dumps. It supports many architectures and extensions.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/prelinkr
%{_infodir}/poke-elf.info%{?ext_info}
%dir %{_datadir}/poke
%{_datadir}/poke/pickles

%changelog
