#
# spec file for package python-cffi
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-cffi
Version:        1.15.1
Release:        0
Summary:        Foreign Function Interface for Python calling C code
License:        MIT
URL:            https://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/source/c/cffi/cffi-%{version}.tar.gz
Source1:        python-cffi-rpmlintrc
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycparser}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libffi)
Requires:       python-pycparser
%python_subpackages

%description
Foreign Function Interface for Python calling C code. The aim of this project
is to provide a convenient and reliable way of calling C code from Python.

%prep
%setup -q -n cffi-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -W ignore::UserWarning c/ testing/

%files %{python_files}
%license LICENSE
%doc README.md doc/source/*.rst doc/misc/*.rst
%{python_sitearch}/*

%changelog
