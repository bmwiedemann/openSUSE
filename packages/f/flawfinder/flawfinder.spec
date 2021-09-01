#
# spec file for package flawfinder
#
# Copyright (c) 2021 SUSE LLC
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


Name:           flawfinder
Version:        2.0.19
Release:        0
Summary:        C/C++ source code security flaw examination tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.dwheeler.com/flawfinder/
Source:         https://dwheeler.com/flawfinder/flawfinder-%{version}.tar.gz
BuildRequires:  python3-setuptools
Requires:       python3
BuildArch:      noarch

%description
Flawfinder scans through C/C++ source code, identifying lines
("hits") with potential security flaws. By default it reports hits
sorted by severity, with the riskiest lines first.

%prep
%setup -q

%build
%python3_build

%install
%python3_install

%files
%license COPYING
%doc README.md ChangeLog flawfinder.ps
%{_bindir}/flawfinder
%{_mandir}/man1/flawfinder.1%{?ext_man}
%{python3_sitelib}

%changelog
