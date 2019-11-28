#
# spec file for package python-PyBindGen
#
# Copyright (c) 2019 SUSE LLC
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

Name:           python-PyBindGen
Version:        0.20.1
Release:        0
Summary:        Python Bindings Generator
License:        LGPL-2.1-only
Group:          Development/Libraries/Python
URL:            https://github.com/gjcarneiro/pybindgen
Source0:        https://pypi.io/packages/source/P/PyBindGen/PyBindGen-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
A tool to generate Python bindings for C/C++ code.

%prep
%setup -q -n PyBindGen-%{version}
find . -iname \*.py -exec sed -ie '1s#/usr/bin/env python#/usr/bin/python#' \{\} \;

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%files %{python_files}
%license COPYING
%{python_sitelib}/*

%changelog
