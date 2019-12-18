#
# spec file for package python-poetry
#
# Copyright (c) 2019 SUSE LLC
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
Name:           python-poetry
Version:        1.0.0
Release:        0
Summary:        Python dependency management and packaging
License:        MIT
Group:          Development/Languages/Python
URL:            https://poetry.eustace.io/
# GitHub archive doesnt contain setup.py; sdist doesnt contain tests
Source:         https://github.com/sdispater/poetry/archive/%{version}.tar.gz#/poetry-%{version}.tar.gz
# https://github.com/dephell/dephell/issues/330
Patch0:         simplify-toml.patch
BuildRequires:  %{python_module CacheControl >= 0.12.4}
BuildRequires:  %{python_module cachy >= 0.2}
BuildRequires:  %{python_module cleo >= 0.6.7}
BuildRequires:  %{python_module dephell}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module html5lib >= 1.0}
BuildRequires:  %{python_module httpretty}
BuildRequires:  %{python_module jsonschema >= 2.6}
BuildRequires:  %{python_module keyring > 18.0}
BuildRequires:  %{python_module lockfile}
BuildRequires:  %{python_module pkginfo >= 1.4}
BuildRequires:  %{python_module pyparsing >= 2.2}
BuildRequires:  %{python_module pyrsistent >= 0.14.2}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18}
BuildRequires:  %{python_module requests-toolbelt >= 0.8.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module shellingham >= 1.1}
BuildRequires:  %{python_module tomlkit >= 0.5.1}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-CacheControl >= 0.12.4
Requires:       python-cachy >= 0.2
Requires:       python-cleo >= 0.6
Requires:       python-html5lib >= 1.0
Requires:       python-jsonschema >= 2.6
Requires:       python-keyring > 18.0
Requires:       python-lockfile
Requires:       python-pkginfo >= 1.4
Requires:       python-pyparsing >= 2.2
Requires:       python-pyrsistent >= 0.14.2
Requires:       python-requests >= 2.18
Requires:       python-requests-toolbelt >= 0.8.0
Requires:       python-shellingham >= 1.1
Requires:       python-tomlkit >= 0.5.1
Recommends:     git-core
Recommends:     python-devel
BuildArch:      noarch
%python_subpackages

%description
Python dependency management and packaging made easy.

%prep
%setup -q -n poetry-%{version}
%patch0
dephell deps convert --traceback --level=DEBUG --from pyproject.toml --to setup.py
# https://github.com/dephell/dephell_markers/issues/6
sed -i '/package_dir/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# A venv is necessary gh#python-poetry/poetry#1645#issuecomment-566872684
python3 -m venv testenv
source testenv/bin/activate
# test_default_with_excluded_data fails, see the above ticket for
# discussion on this.
pytest -k 'not test_default_with_excluded_data'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%python3_only %{_bindir}/poetry

%changelog
