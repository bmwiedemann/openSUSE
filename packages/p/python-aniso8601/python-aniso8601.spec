#
# spec file for package python-aniso8601
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
%define modname aniso8601
%bcond_without python2
Name:           python-%{modname}
Version:        9.0.1
Release:        0
Summary:        A library for parsing ISO 8601 strings
License:        BSD-3-Clause
URL:            https://bitbucket.org/nielsenb/aniso8601
Source:         https://files.pythonhosted.org/packages/source/a/aniso8601/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
%if %{with python2}
BuildRequires:  python-mock
%endif
BuildRequires:  python-rpm-macros
Recommends:     python-python-dateutil
BuildArch:      noarch
%python_subpackages

%description
aniso8601 is a Python library for parsing date strings
in ISO 8601 format into datetime format.

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover aniso8601/tests/

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
