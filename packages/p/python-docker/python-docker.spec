#
# spec file for package python-docker
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
Name:           python-docker
Version:        7.1.0
Release:        0
Summary:        A Python library for the Docker Engine API
License:        Apache-2.0
URL:            https://github.com/docker/docker-py
Source:         https://github.com/docker/docker-py/archive/refs/tags/%{version}.tar.gz#/docker-%{version}.tar.gz
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm >= 6.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module packaging >= 14.0}
BuildRequires:  %{python_module paramiko >= 2.11.0}
BuildRequires:  %{python_module pytest >= 7.1.2}
BuildRequires:  %{python_module pytest-timeout >= 2.1.0}
BuildRequires:  %{python_module requests >= 2.26.0}
BuildRequires:  %{python_module setuptools >= 65.5.1}
BuildRequires:  %{python_module urllib3 >= 2.0}
BuildRequires:  %{python_module websocket-client >= 0.32.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging >= 14.0
Requires:       python-requests >= 2.26.0
Requires:       python-urllib3 >= 1.26.0
Requires:       python-websocket-client >= 0.32.0
Suggests:       python-pywin32 >= 304
Suggests:       python-paramiko >= 2.4.3
BuildArch:      noarch
%python_subpackages

%description
A Python library for the Docker Engine API.

%prep
%autosetup -p1 -n docker-py-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/unit

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/docker
%{python_sitelib}/docker-%{version}.dist-info

%changelog
