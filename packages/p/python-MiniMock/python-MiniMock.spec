#
# spec file for package python-MiniMock
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


%define oldpython python
%define skip_python2 1
%define modname minimock
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-MiniMock
Version:        1.3.0
Release:        0
Summary:        A mock library for Python
License:        MIT
URL:            https://github.com/lowks/minimock/
Source:         https://github.com/lowks/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-tools
BuildArch:      noarch
%ifpython2
Provides:       %{oldpython}-minimock = %{version}
Obsoletes:      %{oldpython}-minimock < %{version}
%endif
%python_subpackages

%description
Minimock is a library for doing Mock objects with doctest.
When using doctest, mock objects can be very simple.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -B %{buildroot}%{$python_sitelib}/minimock.py

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.txt README.rst
%pycache_only %{python_sitelib}/__pycache__/minimock*
%{python_sitelib}/minimock.py
%{python_sitelib}/minimock-*-info

%changelog
