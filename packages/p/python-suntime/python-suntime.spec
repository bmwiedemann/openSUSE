#
# spec file for package python-suntime
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-suntime
Version:        1.3.2
Release:        0
Summary:        Python sunset and sunrise time calculation
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/SatAgro/suntime
Source:         https://files.pythonhosted.org/packages/source/s/suntime/suntime-%{version}.tar.gz
# Copied from https://raw.githubusercontent.com/SatAgro/suntime/master/tests.py
Source1:        tests.py
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module python-dateutil}
# /SECTION
%python_subpackages

%description
Python sunset and sunrise time calculation library.

%prep
%autosetup -p1 -n suntime-%{version}
cp %{SOURCE1} .

%build
export LANG=en_US.UTF-8
%pyproject_wheel

%install
export LANG=en_US.UTF-8
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/suntime
%{python_sitelib}/suntime-%{version}*-info

%changelog
