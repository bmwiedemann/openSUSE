#
# spec file for package python-brotlicffi
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
%define skip_python2 1
Name:           python-brotlicffi
Version:        1.0.9.2
Release:        0
Summary:        Python CFFI bindings to the Brotli library
License:        MIT
URL:            https://github.com/python-hyper/brotlicffi
Source:         brotlicffi-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  gcc-c++
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module cffi >= 1.0.0}
# SECTION test requirements
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module hypothesis}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cffi >= 1.0.0
%python_subpackages

%description
Python CFFI bindings to the Brotli library

%prep
%setup -q -n brotlicffi-%{version}
rm -Rf libbrotli/python

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/*

%changelog
