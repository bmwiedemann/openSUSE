#
# spec file for package python-cracklib
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-cracklib
Version:        2.9.6
Release:        0
Summary:        A CPython extension module wrapping the libcrack library
License:        GPL-2.0-or-later
URL:            https://github.com/cracklib/cracklib
Source:         https://files.pythonhosted.org/packages/source/c/cracklib/cracklib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cracklib-devel
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This CPython extension provides Python bindings for cracklib. It
contains a pythonic interface to cracklib's functions and some Python
convenience functions.

%prep
%setup -q -n cracklib-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
# Do not install tests
%python_expand rm %{buildroot}%{$python_sitearch}/test_cracklib.py %{buildroot}%{$python_sitearch}/__pycache__/test_cracklib.*.pyc

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test_cracklib.py

%files %{python_files}
%{python_sitearch}/cracklib.py
%pycache_only %{python_sitearch}/__pycache__/cracklib.*.pyc
%{python_sitearch}/_cracklib.cpython-*-linux-gnu.so
%{python_sitearch}/cracklib-%{version}.dist-info

%changelog
