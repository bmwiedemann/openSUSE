#
# spec file for package s-tui
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           s-tui
Version:        1.1.4
Release:        0
Summary:        Terminal based CPU stress and monitoring utility
License:        GPL-2.0-or-later
URL:            https://github.com/amanusk/s-tui
Source:         https://github.com/amanusk/s-tui/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
## MANUAL BEGIN
Requires:       python3-psutil
Requires:       python3-urwid
Recommends:     stress-ng
## MANUAL END
BuildArch:      noarch

%description
Terminal UI for monitoring your computer to monitor CPU temperature, frequency,
power and utilization in a graphical way from the terminal.

%prep
%autosetup
find s_tui/ -name "*.py" -exec sed -i 's|#!%{_bindir}/env python|#%{_bindir}/python3|' {} ";"
find s_tui/ -name "*.py" -exec sed -i 's|#!%{_bindir}/python|#%{_bindir}/python3|' {} ";"

%build
export LC_ALL=en_US.utf8
%python3_build

%install
%python3_install
%python_expand %fdupes %{buildroot}%{python3_sitelib}/

%files
%license LICENSE
%doc README.*
%{_bindir}/s-tui
%{python3_sitelib}/s_tui*

%changelog
