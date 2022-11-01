#
# spec file
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


%define skip_python2 1
%{?!python_module:%define python_module() python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-podman%{psuffix}
Version:        4.3.0
Release:        0
Summary:        A library to interact with a Podman server
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/containers/podman-py
Source:         https://github.com/containers/podman-py/archive/refs/tags/v%{version}.tar.gz#/podman-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-psutil
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-setuptools >= 39
Requires:       python-varlink
Suggests:       python-fixtures
Suggests:       python-pbr
Suggests:       python-pytoml
Suggests:       python-pyxdg
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module podman >= %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools >= 39}
BuildRequires:  %{python_module varlink}
BuildRequires:  %{python_module wheel}
# /SECTION
%endif
%python_subpackages

%description
A library to interact with a Podman server

%prep
%setup -q -n podman-py-%{version}

%build
%python_build

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
rm -rvf podman/tests/integration
%pyunittest discover -v podman/tests/
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%endif

%changelog
