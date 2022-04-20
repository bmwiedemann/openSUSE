#
# spec file for package python-time-travel
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
%define skip_python2 1
Name:           python-time-travel
Group:          Development/Languages/Python
Version:        1.1.2
Release:        0
Summary:        Python time mocking
License:        MIT
URL:            https://github.com/snudler6/time-travel
# pypi archive does not contain the tests
Source:         https://github.com/snudler6/time-travel/archive/refs/tags/v%{version}.tar.gz#/time_travel-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A python library that helps users write deterministic tests for time sensitive and I/O intensive code.

%prep
%setup -q -n time-travel-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/snudler6/time-travel/issues/67
sed -i 's:import mock:from unittest import mock:' src/tests/example/test_wait_and_respond.py
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
