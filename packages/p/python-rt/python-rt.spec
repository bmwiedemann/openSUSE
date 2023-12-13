#
# spec file for package python-rt
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-rt
Version:        3.1.3
Release:        0
Summary:        Python interface to Request Tracker API
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/CZ-NIC/python-rt
Source:         https://files.pythonhosted.org/packages/source/r/rt/rt-%{version}.tar.gz
Source1:        setup.cfg
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-requests-toolbelt
BuildArch:      noarch

%python_subpackages

%description
Python implementation of Request Tracker (a ticketing system) REST API described here: https://rt-wiki.bestpractical.com/wiki/REST

%prep
%setup -q -n rt-%{version}
cp %{SOURCE1} setup.cfg
sed -i 's/^dynamic = \["version"]/version = "%{version}"/' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Tests require internet connection

%files %{python_files}
%doc AUTHORS CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/rt-%{version}*-info*
%{python_sitelib}/rt/

%changelog
