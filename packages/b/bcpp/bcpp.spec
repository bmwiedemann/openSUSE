#
# spec file for package bcpp
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           bcpp
Version:        20250914
Release:        0
Summary:        Beautify C++ programs
License:        MIT
URL:            https://invisible-island.net/bcpp/bcpp.html
Source:         https://invisible-island.net/archives/bcpp/bcpp-%{version}.tgz
Source2:        https://invisible-island.net/archives/bcpp/bcpp-%{version}.tgz.asc
# https://invisible-island.net/public/public.html
# https://invisible-island.net/public/dickey@invisible-island.net-rsa3072.asc
Source3:        %{name}.keyring
BuildRequires:  c++_compiler

%description
bcpp indents C/C++ source programs, replacing tabs with spaces or the reverse.
Unlike indent, it does (by design) not attempt to wrap long statements.

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
%doc VERSION README CHANGES MANIFEST
%{_bindir}/bcpp
%{_bindir}/cb++
%{_mandir}/man1/bcpp.1%{?ext_man}
%{_mandir}/man1/cb++.1%{?ext_man}

%changelog
