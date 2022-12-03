#
# spec file for package python-rt
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


# Tests require internet connection
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rt
Version:        3.0.4
Release:        0
Summary:        Python interface to Request Tracker API
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/CZ-NIC/python-rt
Source:         https://files.pythonhosted.org/packages/source/r/rt/rt-%{version}.tar.gz
Source1:        setup.cfg
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-six
BuildArch:      noarch

%python_subpackages

%description
Python implementation of Request Tracker (a ticketing system) REST API described here: https://rt-wiki.bestpractical.com/wiki/REST

%prep
%setup -q -n rt-%{version}
cp %{SOURCE1} setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS CHANGELOG.md README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
