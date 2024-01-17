#
# spec file for package most
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


Name:           most
Version:        5.2.0
Release:        0
Summary:        File viewer and pager
License:        GPL-2.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.jedsoft.org/most/
Source:         https://www.jedsoft.org/releases/most/%{name}-%{version}.tar.gz
Source2:        https://www.jedsoft.org/releases/most/%{name}-%{version}.tar.gz.asc
Source3:        https://www.jedsoft.org/jedavis_public_key2.asc#/%{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(slang)

%description
Most is a paging program.
It supports multiple windows and can scroll left and right.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"

%files
%license COPYING
%doc README changes.txt doc/{lesskeys.rc,most-fun.txt,most.rc}
%{_bindir}/%{name}
%{_mandir}/man1/most.1%{?ext_man}

%changelog
