#
# spec file for package python-bleak
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
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define pname bleak
%{?sle15_python_module_pythons}
Name:           python-%{pname}%{psuffix}
Version:        0.22.3
Release:        0
Summary:        Python GATT client
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hbldh/bleak
Source0:        python-%{pname}-%{version}.tar.xz
BuildArch:      noarch
BuildRequires:  %{python_module dbus_fast >= 1.83.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
%if %python_version_nodots < 311
BuildRequires:  %{python_module async_timeout >= 3.0.0}
%endif
%if %{with test}
BuildRequires:  %{python_module async_timeout}
BuildRequires:  %{python_module bleak}
BuildRequires:  %{python_module pytest >= 7.0.0}
BuildRequires:  %{python_module pytest-asyncio >= 0.19.0}
BuildRequires:  %{python_module pytest-cov >= 3.0.0}
BuildRequires:  %{python_module typing_extensions >= 4.7.0}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dbus_fast >= 1.83.0
%if %python_version_nodots < 311
Requires:       python-async_timeout >= 3.0.0
%endif
%if %python_version_nodots < 312
Requires:       python-typing_extensions >= 4.7.0
%endif
%python_subpackages

%description
Bleak is an acronym for Bluetooth Low Energy platform Agnostic Klient.

Bleak is a GATT client software, capable of connecting to BLE devices acting as GATT servers. It is designed to provide a asynchronous, cross-platform Python API to connect and communicate with e.g. sensors.

%prep
%setup -q -n python-%{pname}-%{version}

%if !%{with test}
%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %python_files
%defattr(-,root,root,-)
%{python_sitelib}/%{pname}*
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%license LICENSE
%endif

%changelog
