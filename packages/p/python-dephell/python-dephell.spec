#
# spec file for package python-dephell
#
# Copyright (c) 2020 SUSE LLC
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
%define unflavoredpython python
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-dephell%{psuffix}
Version:        0.8.3
Release:        0
Summary:        Dependency resolution for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dephell/dephell
Source:         https://files.pythonhosted.org/packages/source/d/dephell/dephell-%{version}.tar.gz
Source1:        macros.py-dephell
# PATCH-FIX-OPENSUSE we don't pin package versions
Patch0:         never-pin-deps.patch
# PATCH-FIX-UPSTREAM dephell-pytest6.patch -- support the pytest 6 entrypoints. Part of gh#dephell/dephell#458 
Patch1:         https://github.com/dephell/dephell/commit/b34011c04e49562b5afe3e946f01024ad5629ac1.patch#/dephell-pytest6.patch
# PATCH-FIX-UPSTREAM dephell-pr473-pip-20-2.patch gh#dephell#dephell#473 -- support pip 20.2 changed internal API (rebased because of patch1)
Patch2:         dephell-pr473-pip-20-2.patch
# PATCH-FIX-UPSTREAM dephell-pr474-bowler-09.patch gh#dephell#dephell#474 -- support updated bowler 0.9
Patch3:         https://patch-diff.githubusercontent.com/raw/dephell/dephell/pull/474.patch#/dephell-pr474-bowler-09.patch
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  bash
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cerberus >= 1.3
Requires:       python-Jinja2
Requires:       python-aiohttp
Requires:       python-appdirs
Requires:       python-attrs >= 19.2.0
Requires:       python-bowler
Requires:       python-dephell-archive >= 0.1.5
Requires:       python-dephell-argparse >= 0.1.1
Requires:       python-dephell-discover >= 0.2.6
Requires:       python-dephell-licenses >= 0.1.6
Requires:       python-dephell-links >= 0.1.4
Requires:       python-dephell-markers >= 1.0.2
Requires:       python-dephell-pythons >= 0.1.11
Requires:       python-dephell-setuptools >= 0.2.1
Requires:       python-dephell-shells >= 0.1.3
Requires:       python-dephell-specifier >= 0.1.7
Requires:       python-dephell-venvs >= 0.1.16
Requires:       python-dephell-versioning
Requires:       python-dephell_changelogs
Requires:       (python-dephell-rpm-macros if python-rpm-macros)
# Yeah, html5lib is required by dephell, and no, autodiscovery won’t find it.
# rpmlint is stupid
Requires:       python-docker
Requires:       python-dockerpty
Requires:       python-fissix
Requires:       python-html5lib
Requires:       python-m2r
Requires:       python-packaging
Requires:       python-pip >= 18.0
Requires:       python-pygments
Requires:       python-requests
Requires:       python-ruamel.yaml
Requires:       python-setuptools
Requires:       python-tabulate
Requires:       python-tomlkit
Requires:       python-yaspin
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     git-core
Recommends:     python-aiofiles
Recommends:     python-colorama
Recommends:     python-graphviz
Suggests:       python-autopep8
Suggests:       python-yapf
# For python-dephell-rpm-macros
Provides:       %{unflavoredpython}-dephell = %{version}
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aioresponses}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module bowler}
BuildRequires:  %{python_module dephell-archive >= 0.1.5}
BuildRequires:  %{python_module dephell-argparse >= 0.1.1}
BuildRequires:  %{python_module dephell-discover >= 0.2.6}
BuildRequires:  %{python_module dephell-licenses >= 0.1.6}
BuildRequires:  %{python_module dephell-links >= 0.1.4}
BuildRequires:  %{python_module dephell-markers >= 1.0.2}
BuildRequires:  %{python_module dephell-pythons >= 0.1.11}
BuildRequires:  %{python_module dephell-setuptools >= 0.2.1}
BuildRequires:  %{python_module dephell-shells >= 0.1.3}
BuildRequires:  %{python_module dephell-specifier >= 0.1.7}
BuildRequires:  %{python_module dephell-venvs >= 0.1.16}
BuildRequires:  %{python_module dephell-versioning}
BuildRequires:  %{python_module dephell_changelogs}
BuildRequires:  %{python_module dockerpty}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module fissix}
BuildRequires:  %{python_module graphviz}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module m2r}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip >= 18.0}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module yaspin}
BuildRequires:  git-core
BuildRequires:  graphviz-gnome
%endif
# /SECTION
%python_subpackages

%description
Dependency resolution for Python.
Manage packages: convert between formats, lock, install, resolve, isolate,
test, build graph, show outdated, audit. Manage venvs, build package, bump version.

%prep
%autosetup -p1 -n dephell-%{version}

sed -i -e '1i #!/bin/sh' dephell/templates/docker_prepare.sh

%package -n %{unflavoredpython}-dephell-rpm-macros
Summary:        RPM macros to help develop Python packages using python-dephell
Group:          Development/Libraries/Python
Requires:       %{name} = %{version}

%description -n %{unflavoredpython}-dephell-rpm-macros
Contains the RPM definition of the macro dephell_gensetup, which
generates setup.py from the provided pyproject.toml.

%build
%python_build

%install
%if ! %{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/dephell
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# Install macros.lua for rpm to have centralized place to
# manage dephell_genspec macro
install -D -m 644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.py-dephell
%endif

%check
%if %{with test}
# Emulate Travis, which disables tests which expect a git repository
export TRAVIS_OS_NAME=1
# test_params_all_described requires the docs to be packaged https://github.com/dephell/dephell/pull/448
%pytest --no-network -k 'not test_params_all_described'
%endif

%if ! %{with test}
%post
%python_install_alternative dephell

%postun
%python_uninstall_alternative dephell

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%python_alternative %{_bindir}/dephell
%{python_sitelib}/*

%files -n %{unflavoredpython}-dephell-rpm-macros
%{_rpmmacrodir}/macros.py-dephell
%endif

%changelog
