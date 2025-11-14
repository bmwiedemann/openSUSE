#
# spec file for package python-pytest-docker
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


%{?sle15_python_module_pythons}
Name:           python-pytest-docker
Version:        3.2.5
Release:        0
Summary:        Simple pytest fixtures for Docker and Docker Compose based tests
License:        MIT
URL:            https://github.com/avast/pytest-docker
Source:         https://github.com/avast/pytest-docker/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module mypy >= 0.500}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module pytest-mypy >= 0.10}
BuildRequires:  %{python_module pytest-pycodestyle >= 2.0.0}
BuildRequires:  %{python_module pytest-pylint >= 0.14.1}
BuildRequires:  %{python_module requests >= 2.22.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module types-requests >= 2.31}
BuildRequires:  %{python_module types-setuptools >= 69.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  docker
BuildRequires:  docker-compose
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 19.2.0
Requires:       python-pytest >= 4.0
BuildArch:      noarch
%python_subpackages

%description
Simple pytest fixtures that help you write integration tests with
Docker and Docker Compose. Specify all necessary containers in a
docker-compose.yml file and and pytest-docker will spin them up
for the duration of your tests.

%prep
%autosetup -p1 -n pytest-docker-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable test_integration as it requires docker daemon to be running
export PYTHONPATH=./src
%pytest -c setup.cfg -v -k 'not test_integration'

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/pytest_docker
%{python_sitelib}/pytest_docker-%{version}.dist-info

%changelog
