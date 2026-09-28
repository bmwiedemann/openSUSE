#
# spec file for package python-time-travel
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-time-travel
Version:        1.1.2
Release:        0
Summary:        Python time mocking
License:        MIT
URL:            https://github.com/snudler6/time-travel
# pypi archive does not contain the tests
Source:         https://github.com/snudler6/time-travel/archive/refs/tags/v%{version}.tar.gz#/time_travel-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Use importlib.metadata rather than pkg_resources
Patch0:         no-more-pkg-resources.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n time-travel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/snudler6/time-travel/issues/67
sed -i 's:import mock:from unittest import mock:' src/tests/example/test_wait_and_respond.py
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/time_travel
%{python_sitelib}/time_travel-%{version}.dist-info

%changelog
