#
# spec file for package python-autopage
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
%global skip_python2 1
Name:           python-autopage
Version:        0.4.0
Release:        0
Summary:        A library to provide automatic paging for console output
License:        Apache-2.0
URL:            https://github.com/zaneb/autopage
Source:         https://files.pythonhosted.org/packages/source/a/autopage/autopage-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Autopage is a Python library to
automatically display terminal output from a program
in a pager (like `less`)

%prep
%setup -q -n autopage-%{version}

# workaround broken python_build macros
echo "import setuptools; setuptools.setup()" > setup.py

%build
%python_build

%install
%python_install

%check
unset LESS
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
