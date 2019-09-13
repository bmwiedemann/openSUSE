#
# spec file for package python-pytest-socket
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pytest-socket
Version:        0.3.3
Release:        0
License:        MIT
Summary:        Pytest Plugin to disable socket
Url:            https://github.com/miketheman/pytest-socket
Group:          Development/Languages/Python
Source:         https://github.com/miketheman/pytest-socket/archive/%{version}.tar.gz#/pytest-socket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 3.6.3}
# /SECTION
Requires:       python-pytest >= 3.6.3
BuildArch:      noarch

%python_subpackages

%description
A Pytest Plugin to disable socket calls during tests.

%prep
%setup -q -n pytest-socket-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require a network connection
# %%check
# %%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
