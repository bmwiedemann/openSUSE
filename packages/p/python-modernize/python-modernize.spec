#
# spec file for package python-modernize
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-modernize
Version:        0.7
Release:        0
Summary:        A tool for modernizing Python code using lib2to3
License:        BSD-3-Clause AND Python-2.0
URL:            https://github.com/python-modernize/python-modernize
Source:         https://github.com/python-modernize/python-modernize/archive/%{version}.tar.gz#//modernize-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dbm
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
A hack on top of 2to3 for modernizing Python code.

%prep
%setup -q -n python-modernize-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%python3_only %{_bindir}/python-modernize
%{python_sitelib}/*

%changelog
