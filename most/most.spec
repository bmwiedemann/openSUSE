#
# spec file for package most
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           most
Version:        5.1.0
Release:        0
Summary:        File viewer and pager
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://www.jedsoft.org/most/
Source:         https://www.jedsoft.org/snapshots/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  slang-devel

%description
Most is a paging program.
It supports multiple windows and can scroll left and right.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --prefix=%{_prefix}
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
