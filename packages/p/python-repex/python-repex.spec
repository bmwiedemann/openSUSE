#
# spec file for package python-repex
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-repex
Version:        1.2.2
Release:        0
Summary:        Module to replace strings in files based on regular expressions
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/cloudify-cosmo/repex
Source:         https://github.com/cloudify-cosmo/repex/archive/v%{version}.tar.gz#/repex-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML >= 3.12}
BuildRequires:  %{python_module click >= 6.7}
BuildRequires:  %{python_module jsonschema >= 2.5.1}
BuildRequires:  %{python_module jsonschema < 3}
BuildRequires:  %{python_module pytest-runner}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML >= 3.12
Requires:       python-click >= 6.7
Requires:       python-jsonschema >= 2.5.1
Requires:       python-jsonschema < 3
BuildArch:      noarch

%python_subpackages

%description
Repex replaces strings in single/multiple files based on regular expressions.

%prep
%setup -q -n repex-%{version}
sed -i 's/==/>=/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py pytest

%files %{python_files}
%doc CHANGES README.md README.rst
%license LICENSE
%python3_only %{_bindir}/rpx
%{python_sitelib}/*

%changelog
