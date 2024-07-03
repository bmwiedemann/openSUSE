#
# spec file for package python-time-machine
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-time-machine
Group:          Development/Languages/Python
Version:        2.14.2
Release:        0
Summary:        Travel through time in your tests
License:        MIT
URL:            https://github.com/adamchainz/time-machine
# pypi packages don't contain the tests anymore since 2.2.0, see changelog
Source:         https://github.com/adamchainz/time-machine/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION tests
BuildRequires:  %{python_module backports.zoneinfo if %python-base < 3.9}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  timezone
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
Requires:       python-python-dateutil
Requires:       timezone
%python_subpackages

%description
This library mocks all functions from Python's standard library that return the current date or datetime.
It can be used independently, as a function decorator, or as a context manager.

%prep
%setup -q -n time-machine-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch

%files %{python_files}
%doc README.rst HISTORY.rst
%license LICENSE
%{python_sitearch}/time_machine
%{python_sitearch}/_time_machine.*.so
%{python_sitearch}/time_machine-%{version}.dist-info

%changelog
