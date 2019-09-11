#
# spec file for package python-pyprel
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
Name:           python-pyprel
Version:        2018.9.14.1501
Release:        0
Summary:        Python print elegant
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/wdbm/pyprel
Source0:        https://files.pythonhosted.org/packages/source/p/pyprel/pyprel-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/wdbm/pyprel/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-pyfiglet
Requires:       python-shijian
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pyfiglet}
BuildRequires:  %{python_module shijian}
# /SECTION
%python_subpackages

%description
This module provides Python rendering functionality. It can render a
dictionary such that it is displayed with indentations for
illustration of hierarchy. It can center blocks of text for terminal
output. It can render segment displays. It can render and display
tables of various specified widths and column widths with various
text wrapping features and delimiters. It can provide color palettes,
extend them and save images of them.

%prep
%setup -q -n pyprel-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no unit tests found

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
