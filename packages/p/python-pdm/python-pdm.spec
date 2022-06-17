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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pdm%{psuffix}
Version:        1.15.3
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm/
Source0:        https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module click >= 7}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pdm-pep517}
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module python-dotenv >= 0.15}
BuildRequires:  %{python_module pythonfinder}
BuildRequires:  %{python_module resolvelib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module shellingham >= 1.3.2}
BuildRequires:  %{python_module tomli >= 1.1.0}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module wheel >= 0.36.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-click >= 7
Requires:       python-installer >= 0.5
Requires:       python-packaging
Requires:       python-pdm-pep517
Requires:       python-pep517
Requires:       python-pip
Requires:       python-platformdirs
Requires:       python-poetry
Requires:       python-python-dotenv >= 0.15
Requires:       python-pythonfinder
Requires:       python-resolvelib
Requires:       python-setuptools
Requires:       python-shellingham >= 1.3.2
Requires:       python-tomli >= 1.1.0
Requires:       python-tomlkit
Requires:       python-wheel >= 0.36.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module findpython}
BuildRequires:  %{python_module installer >= 0.5}
BuildRequires:  %{python_module pdm}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  git
BuildRequires:  git-lfs
%endif
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pdm
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%post
%python_install_alternative pdm

%postun
%python_uninstall_alternative pdm

%if %{with test}
%check
%pytest -x -k 'not (network or path or test_use_command)'
%endif

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pdm
%{python_sitelib}/pdm*
%endif

%changelog
