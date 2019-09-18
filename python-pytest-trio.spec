#
# spec file for package python-pytest-trio
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-pytest-trio
Version:        0.5.2
Release:        0
Summary:        Pytest plugin for trio
License:        MIT OR Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/python-trio/pytest-trio
Source:         file:///home/herman/OBS/home:Simmphonie:python/python-pytest-trio/pytest-trio-%{version}.tar.gz#/pytest-trio-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-async_generator >= 1.9
Requires:       python-pytest >= 3.6
Requires:       python-trio >= 0.11
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module async_generator >= 1.9}
BuildRequires:  %{python_module contextvars >= 2.1}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest >= 3.6}
BuildRequires:  %{python_module trio >= 0.11}
# /SECTION
%python_subpackages

%description
This is a pytest plugin to help you test projects that use Trio, a friendly library for concurrency and async I/O in Python.

%prep
%setup -q -n pytest-trio-%{version}

# Temporary hack on a temporary hack
# https://github.com/pytest-dev/pytest/issues/4039
sed -i /RemovedInPytest4Warning/d pytest_trio/_tests/conftest.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE LICENSE.APACHE2 LICENSE.MIT
%{python_sitelib}/*

%changelog
