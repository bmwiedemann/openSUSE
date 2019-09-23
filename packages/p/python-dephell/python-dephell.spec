#
# spec file for package python-dephell
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-dephell
Version:        0.7.6
Release:        0
Summary:        Dependency resolution for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dephell/dephell
Source:         https://files.pythonhosted.org/packages/source/d/dephell/dephell-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cerberus
Requires:       python-Jinja2
Requires:       python-PyYAML
Requires:       python-aiohttp
Requires:       python-appdirs
Requires:       python-attrs
Requires:       python-bowler
Requires:       python-dephell-archive >= 0.1.5
Requires:       python-dephell-discover >= 0.2.6
Requires:       python-dephell-licenses >= 0.1.6
Requires:       python-dephell-links >= 0.1.4
Requires:       python-dephell-markers >= 1.0.0
Requires:       python-dephell-pythons >= 0.1.11
Requires:       python-dephell-shells >= 0.1.3
Requires:       python-dephell-specifier >= 0.1.7
Requires:       python-dephell-venvs >= 0.1.16
Requires:       python-dephell-versioning
Requires:       python-docker
Requires:       python-dockerpty
Requires:       python-fissix
Requires:       python-html5lib
Requires:       python-m2r
Requires:       python-packaging
Requires:       python-pip >= 18.0
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-tomlkit
Requires:       python-yaspin
Recommends:     git-core
Recommends:     python-aiofiles
Recommends:     python-colorama
Recommends:     python-graphviz
Suggests:       python-autopep8
Suggests:       python-yapf
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Cerberus}
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aioresponses}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module bowler}
BuildRequires:  %{python_module dephell-archive >= 0.1.5}
BuildRequires:  %{python_module dephell-discover >= 0.2.6}
BuildRequires:  %{python_module dephell-licenses >= 0.1.6}
BuildRequires:  %{python_module dephell-links >= 0.1.4}
BuildRequires:  %{python_module dephell-markers >= 1.0.0}
BuildRequires:  %{python_module dephell-pythons >= 0.1.11}
BuildRequires:  %{python_module dephell-shells >= 0.1.3}
BuildRequires:  %{python_module dephell-specifier >= 0.1.7}
BuildRequires:  %{python_module dephell-venvs >= 0.1.16}
BuildRequires:  %{python_module dephell-versioning}
BuildRequires:  %{python_module dockerpty}
BuildRequires:  %{python_module docker}
BuildRequires:  %{python_module fissix}
BuildRequires:  %{python_module html5lib}
BuildRequires:  %{python_module m2r}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip >= 18.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  %{python_module yaspin}
BuildRequires:  git-core
# /SECTION
%python_subpackages

%description
Dependency resolution for Python.
Manage packages: convert between formats, lock, install, resolve, isolate,
test, build graph, show outdated, audit. Manage venvs, build package, bump version.

%prep
%setup -q -n dephell-%{version}
find tests -type d -name __pycache__ | xargs rm -rf
# Network and missing dependencies
rm \
  tests/test_commands/test_deps_outdated.py \
  tests/test_commands/test_deps_install.py \
  tests/test_commands/test_deps_licenses.py \
  tests/test_commands/test_deps_tree.py \
  tests/test_commands/test_generate_license.py \
  tests/test_commands/test_inspect_venv.py \
  tests/test_commands/test_jail_install.py \
  tests/test_commands/test_package_downloads.py \
  tests/test_commands/test_package_install.py \
  tests/test_commands/test_package_search.py \
  tests/test_commands/test_package_show.py \
  tests/test_controllers/test_safety.py \
  tests/test_controllers/test_snyk.py \
  tests/test_converters/test_imports.py \
  tests/test_repositories/test_conda.py \
  tests/test_resolving/test_smoke.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Emulate Travis, which disables tests which expect a git repository
export TRAVIS_OS_NAME=1
%pytest -k 'not (test_load or test_repository_preserve or test_idempotency or test_get_deps_auth or test_get_deps or test_extra or test_get_releases or test_info_from_files or test_deps_file or test_preserve_path or test_git_parsing or test_bump_command_with_placeholder_tag)'

%files %{python_files}
%doc README.md README.rst
%license LICENSE
%python3_only %{_bindir}/dephell
%{python_sitelib}/*

%changelog
