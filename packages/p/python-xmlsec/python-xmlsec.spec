#
# spec file for package python-xmlsec
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
# gh#mehcode/python-xmlsec#204 and gh#mehcode/python-xmlsec#210
%define skip_python310 1
Name:           python-xmlsec
Version:        1.3.12
Release:        0
Summary:        Python bindings for the XML Security Library
License:        MIT
URL:            https://github.com/mehcode/python-xmlsec
Source:         https://files.pythonhosted.org/packages/source/x/xmlsec/xmlsec-%{version}.tar.gz
# PATCH-FIX-UPSTREAM avoid_lxml_tests_failing.patch gh#mehcode/python-xmlsec#84 mcepl@suse.com
# work around the lxml issue
Patch0:         avoid_lxml_tests_failing.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module lxml >= 3.0}
BuildRequires:  %{python_module lxml-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# we need at least one backend
BuildRequires:  libxmlsec1-openssl1
BuildRequires:  pkgconfig(xmlsec1)
# we need at least one xmlsec backend on runtime
Recommends:     libxmlsec1-openssl1
Requires:       python-lxml >= 3.0
Requires:       python-pkgconfig
%python_subpackages

%description
Python bindings for the XML Security Library

%prep
%autosetup -p1 -n xmlsec-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# %%pytest_arch tests/
%ifarch %ix86
export skip_tests="not test_reinitialize_module"
%else
export skip_tests=""
%endif
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch} PYTHONDONTWRITEBYTECODE=1
rm -rf .hypothesis/ .pytest_cache/
$python -mpytest --ignore=_build.python39 --ignore=_build.python310 --ignore=_build.python38 -v -k "$skip_tests" tests/
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/xmlsec
%{python_sitearch}/xmlsec-%{version}*-info
%{python_sitearch}/xmlsec*.so

%changelog
