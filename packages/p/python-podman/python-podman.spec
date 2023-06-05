#
# spec file for package python-podman
#
# Copyright (c) 2023 SUSE LLC
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-podman%{psuffix}
Version:        4.5.1
Release:        0
Summary:        A library to interact with a Podman server
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/containers/podman-py
Source:         https://github.com/containers/podman-py/archive/refs/tags/v%{version}.tar.gz#./podman-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module pyxdg}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytoml
Requires:       python-pyxdg
Requires:       python-requests
Requires:       python-urllib3 < 2.0
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module podman >= %{version}}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools >= 39}
BuildRequires:  %{python_module urllib3 < 2.0}
BuildRequires:  %{python_module varlink}
BuildRequires:  %{python_module wheel}
# /SECTION
%endif
%python_subpackages

%description
A library to interact with a Podman server

%prep
%autosetup -n podman-py-%{version}

%build
%python_build

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand $python -m pytest podman/tests/unit}
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/podman/
%{python_sitelib}/podman-*.egg-info/
%endif

%changelog
