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


Name:           python-xmlsec
Version:        1.3.13
Release:        0
Summary:        Python bindings for the XML Security Library
License:        MIT
URL:            https://github.com/mehcode/python-xmlsec
Source:         https://files.pythonhosted.org/packages/source/x/xmlsec/xmlsec-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module lxml >= 3.8.0}
BuildRequires:  %{python_module lxml-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pkgconfig}
BuildRequires:  %{python_module pytest-xdist}
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
Requires:       python-lxml >= 3.8.0
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
# gh#xmlsec/python-xmlsec#244
donttest="test_sign_case5"

# Run tests with -n 1 to avoid race condition in tests
# gh#xmlsec/python-xmlsec#210
%pytest_arch -n 1 -k "not (${donttest})" tests/

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/xmlsec
%{python_sitearch}/xmlsec-%{version}*-info
%{python_sitearch}/xmlsec*.so

%changelog
