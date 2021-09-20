#
# spec file for package python-pyRFC3339
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyRFC3339
Version:        1.1
Release:        0
Summary:        Generate and parse RFC 3339 timestamps
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/kurtraschke/pyRFC3339
Source:         https://github.com/kurtraschke/pyRFC3339/archive/refs/tags/v1.1.tar.gz#/pyRFC3339-%{version}.tar.gz
Patch0:         switch-to-pytest.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
BuildArch:      noarch
%python_subpackages

%description
pyRFC3339 parses and generates :RFC:`3339`-compliant timestamps using Python `datetime.datetime` objects.

%prep
%setup -q -n pyRFC3339-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/pyrfc3339

%check
%pytest pyrfc3339/tests/tests.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
