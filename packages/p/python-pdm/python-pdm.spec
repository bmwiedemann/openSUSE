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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%endif
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-pdm%{psuffix}
Version:        2.3.3
Release:        0
Summary:        Python Development Master
License:        MIT
URL:            https://github.com/pdm-project/pdm/
Source0:        https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pdm-pep517 >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blinker
Requires:       python-cachecontrol >= 0.12.11
Requires:       python-certifi
Requires:       python-findpython >= 0.2.2
Requires:       python-packaging >= 20.9
Requires:       python-pep517 >= 0.11.0
Requires:       python-platformdirs
Requires:       python-pyproject-hooks
Requires:       python-python-dotenv >= 0.15
Requires:       python-requests-toolbelt
Requires:       python-rich >= 12.3.0
Requires:       python-shellingham >= 1.3.2
Requires:       python-unearth >= 0.6.3
Requires:       python-virtualenv >= 20
Requires:       (python-installer >= 0.6 with python-installer < 0.7)
Requires:       (python-resolvelib >= 0.8 with python-resolvelib < 0.9)
Requires:       (python-tomlkit >= 0.8.0 with python-tomlkit < 1)
# from python-cachecontrol[filecache]
Requires:       python-lockfile >= 0.9
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli >= 1.1.0
%endif
%if 0%{?python_version_nodots} < 38
Requires:       python-importlib-metadata
Requires:       python-typing-extensions
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module pdm = %{version}}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
PDM is a modern Python package manager with PEP 582 support. It
installs and manages packages in a similar way to npm that
doesn't need to create a virtualenv at all!

%prep
%autosetup -p1 -n pdm-%{version}
#  we don't care about certifi version, the distro package replaces the certificates with system ones anyway
sed -i 's/"certifi>=[0-9.]*"/"certifi"/' pyproject.toml

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

%if %{with test}
%check
# no network
donttest="network"
# mock testing finds the wrong python versions in our multiflavor setup
donttest="$donttest or test_project_packages_path or test_conda_backend_create"
donttest="$donttest or test_init_non_interactive"
%pytest -k "not ($donttest)"
%endif

%post
%python_install_alternative pdm

%postun
%python_uninstall_alternative pdm

%if !%{with test}
%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pdm
%{python_sitelib}/pdm
%{python_sitelib}/pdm-%{version}*-info
%endif

%changelog
