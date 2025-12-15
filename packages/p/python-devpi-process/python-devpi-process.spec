#
# spec file for package python-devpi-process
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
%define skip_python39 1
Name:           python-devpi-process%{psuffix}
Version:        1.1.0
Release:        0
Summary:        Programmatic API to create and use a devpi server process
License:        MIT
URL:            https://github.com/tox-dev/devpi-process
Source:         https://files.pythonhosted.org/packages/source/d/devpi_process/devpi_process-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs >= 0.3}
BuildRequires:  %{python_module hatchling >= 1.18}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing-extensions >= 4.7.1 if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-devpi-client >= 6.0.5
Requires:       python-devpi-server >= 6.9.2
Suggests:       python-httpx >= 0.24.1
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module covdefaults >= 2.3}
BuildRequires:  %{python_module devpi-client >= 6.0.5}
BuildRequires:  %{python_module devpi-server >= 6.8}
BuildRequires:  %{python_module httpx >= 0.24.1}
BuildRequires:  %{python_module pytest >= 7.4}
BuildRequires:  %{python_module pytest-cov}
%endif
# /SECTION
%python_subpackages

%description
This package provides a programmatic API to create and use a
devpi server process.

%prep
%autosetup -p1 -n devpi_process-%{version}
# Fix version check for pytest
sed -i -e '/import devpi_process/a\ \ \ \ from importlib import metadata' tests/test_devpi_process.py
sed -i "s/^.*assert devpi_process.__version__/    assert metadata.version('devpi_process')/" tests/test_devpi_process.py
sed -i "s/from ._version import __version__/from ._version import version/" src/devpi_process/__init__.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if %{with test}
%pytest
%python_expand rm -r -f %{buildroot}/usr
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/devpi_process
%{python_sitelib}/devpi_process-%{version}*-info
%endif

%changelog
