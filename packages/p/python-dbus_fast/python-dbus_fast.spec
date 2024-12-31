#
# spec file for package python-dbus_fast
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


%global flavor @BUILD_FLAVOR@%{nil}

%define mname dbus_fast
%define pname python-%{mname}

%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}

Name:           %{pname}%{?psuffix}
Version:        2.24.4
Release:        0
Summary:        Python library for DBus
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bluetooth-devices/dbus-fast
Source0:        %{pname}-%{version}.tar.xz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}

%if %{with test}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module gobject}
BuildRequires:  %{python_module pycairo}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  dbus-1
%if 0%{?suse_version} && 0%{?suse_version} > 1500
BuildRequires:  dbus-1-daemon
%endif
%endif

BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
python-dbus-fast is a Python library for DBus that aims to be a performant fully featured high level library primarily geared towards integration of applications into Linux desktop and mobile environments.

Desktop application developers can use this library for integrating their applications into desktop environments by implementing common DBus standard interfaces or creating custom plugin interfaces.

Desktop users can use this library to create their own scripts and utilities to interact with those interfaces for customization of their desktop environment.

%prep
%setup -q -n %{pname}-%{version}

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
# Tests imports utils from /test folder.
export PYTHONPATH=$PWD
eval $(dbus-launch --sh-syntax)
%pytest -k "not test_peer_interface"
%endif

%if !%{with test}
%files %python_files
%defattr(-,root,root,-)
%{python_sitearch}/%{mname}*
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE
%endif

%changelog
