#
# spec file for package python-pycrdt-store
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-pycrdt-store%{?psuffix}
Version:        0.1.3
Release:        0
Summary:        Persistent storage for pycrdt
License:        MIT
URL:            https://github.com/y-crdt/pycrdt-store
Source:         https://files.pythonhosted.org/packages/source/p/pycrdt_store/pycrdt_store-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-anyio >= 3.6.2 with python-anyio < 5)
Requires:       (python-pycrdt >= 0.12.13 with python-pycrdt < 0.13)
Requires:       (python-sqlite-anyio >= 0.2.3 with python-sqlite-anyio < 0.3)
%if %{with test}
BuildRequires:  %{python_module pycrdt-store = %{version}}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module trio >= 0.25.0}
%endif
%python_subpackages

%description
Persistent storage for pycrdt.

This is a package extracted out from pycrdt-websocket

%prep
%autosetup -p1 -n pycrdt_store-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%{python_expand #
%fdupes %{buildroot}%{$python_sitelib}
mkdir -p %{buildroot}%{$python_sitearch}/pycrdt
ln -s %{$python_sitelib}/pycrdt/store %{buildroot}%{$python_sitearch}/pycrdt/store
}
%endif

%check
%if %{with test}
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/pycrdt
%dir %{python_sitearch}/pycrdt
%{python_sitearch}/pycrdt/store
%{python_sitelib}/pycrdt/store
%{python_sitelib}/pycrdt_store-%{version}.dist-info
%endif

%changelog
