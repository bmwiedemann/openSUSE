#
# spec file for package python-pyRXP
#
# Copyright (c) 2020 SUSE LLC
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


Name:           python-pyRXP
Version:        2.2.0
Release:        0
Summary:        Python RXP interface - fast validating XML parser
License:        BSD-3-Clause
URL:            https://www.reportlab.com
Source0:        https://files.pythonhosted.org/packages/source/p/pyRXP/pyRXP-%{version}.tar.gz
# LICENSE MISSING IN SOURCE TARBALL
Source1:        https://hg.reportlab.com/hg-public/pyRXP/raw-file/9ee8c8d7cc04/LICENSE.txt
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PyRXP is a Python language wrapper around the excellent RXP parser, a
validating, namespace-aware XML parser written in C.

%prep
%setup -q -n pyRXP-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# No way to execute the tests and they are mostly just py2 syntax based.

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/*

%changelog
