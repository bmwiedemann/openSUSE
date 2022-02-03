#
# spec file for package python-pdm
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
Name:           python-pdm
Version:        1.12.6
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm/
Source0:        https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
# Artifacts for tests from gh#pdm-project/pdm#864
Source1:        artifacts.tar.gz
# PATCH-FIX-UPSTREAM mark-network-tests.patch gh#pdm-project/pdm#858 mcepl@suse.com
# mark tests which require network connection (gh#pdm-project/pdm#864)
Patch0:         mark-network-tests.patch
# PATCH-FIX-OPENSUSE sys-exec-failures.patch mcepl@suse.com
# sys.executable is too long with python3.10
Patch1:         sys-exec-failures.patch
# PATCH-FIX-UPSTREAM mark-tests-path.patch gh#pdm-project/pdm#865 mcepl@suse.com
# mark tests which depend on exact paths of executables
# https://github.com/pdm-project/pdm/commit/23f1cf62a302
Patch2:         mark-tests-path.patch
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module click >= 7}
BuildRequires:  %{python_module importlib-metadata if %python-base < 3.8}
BuildRequires:  %{python_module installer}
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
BuildRequires:  %{python_module typing-extensions if %python-base < 3.8}
BuildRequires:  %{python_module wheel >= 0.36.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-click >= 7
Requires:       python-installer
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
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  git
BuildRequires:  git-lfs
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pdm
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pdm

%postun
%python_uninstall_alternative pdm

%check
# the test_show_self_package is gh#pdm-project/pdm#865
%pytest -s -k 'not (network or path or test_show_self_package or test_use_python_by_version)'

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pdm
%{python_sitelib}/pdm*

%changelog
