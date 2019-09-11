#
# spec file for package python-coards
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
Name:           python-coards
Version:        1.0.5
Release:        0
Summary:        A parser for COADS-compliant dates
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/hadfieldnz/python3-coards
Source:         https://files.pythonhosted.org/packages/source/c/coards/coards-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/hadfieldnz/python3-coards/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-tools
BuildArch:      noarch

%python_subpackages

%description
This module parses time values represented using the COARDS
convention.

%prep
%setup -q -n coards-%{version}
cp %{SOURCE1} .

# Make the doctests python3-compatible
2to3 -wnd src/coards/__init__.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{python_sitelib}

# This only does a test
rm %{buildroot}%{_bindir}/coards

%check
%python_expand $python %{buildroot}%{$python_sitelib}/coards/__init__.py -v

%files %{python_files}
%license LICENSE
%doc NEWS.txt README.rst
%{python_sitelib}/*

%changelog
