#
# spec file for package legendary
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:             legendary
Version:          0.20.42
Release:          0
Summary:          An Epic Games Launcher alternative
License:          GPL-3.0-only
URL:              https://github.com/Heroic-Games-Launcher/legendary.git
Source:           %{name}-%{version}.tar.gz
Source1:          legendary.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-build
BuildRequires:  python3-installer
Requires:       python3
Requires:       python3-requests < 3.0
Requires:       python3-filelock
Requires:       python3-requests-futures
BuildArch:      noarch

%description
Legendary is an open-source game launcher that can install and manage games from the Epic Games Store.

%prep
%autosetup -p1
find . -name "*.py" -exec sed -i '1{/^#!/d}' {} +

%build
python3 -m build --wheel --no-isolation

%install
python3 -m installer --destdir=%{buildroot} dist/*.whl

find %{buildroot}%{python3_sitelib} -name "*.pyc" -delete

%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE*
%doc README.md
%{_bindir}/legendary
%{python3_sitelib}/legendary
%{python3_sitelib}/legendary_gl-%{version}*.dist-info

%changelog
