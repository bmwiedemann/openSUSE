#
# spec file for package python-pyDOE2
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
Name:           python-pyDOE2
Version:        1.2.1
Release:        0
Summary:        Design of experiments for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            https://github.com/clicumu/pyDOE2
Source:         https://files.pythonhosted.org/packages/source/p/pyDOE2/pyDOE2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
# /SECTION
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch

%python_subpackages

%description
The pyDOE2 package is a fork of the pyDOE package that is designed to
help the scientist, engineer, statistician, etc., to construct
appropriate experimental designs.

This fork came to life to solve bugs and issues that remained unsolved in the
original package.

%prep
%setup -q -n pyDOE2-%{version}
sed -i 's/\r$//' setup.py
sed -i 's/\r$//' README.md

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
