#
# spec file for package python-isort
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
Name:           python-isort%{psuffix}
Version:        5.4.2
Release:        0
Summary:        A Python utility / library to sort Python imports
License:        MIT
URL:            https://timothycrosley.github.io/isort/
Source:         https://files.pythonhosted.org/packages/source/i/isort/isort-%{version}.tar.gz
# tests and test data are not packaged for PyPI, get them from git sources
Source1:        https://github.com/timothycrosley/isort/archive/%{version}.tar.gz#/isort-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pip-api
Recommends:     python-pipreqs
Recommends:     python-requirementslib >= 1.5.4
Recommends:     python-tomlkit
Suggests:       git
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hypothesis-auto}
BuildRequires:  %{python_module isort = %{version}}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip-api}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requirementslib >= 1.5.4}
BuildRequires:  %{python_module tomlkit}
BuildRequires:  git
%endif
%python_subpackages

%description
isort your python imports for you so you don’t have to.

isort is a Python utility / library to sort imports alphabetically, and 
automatically separated into sections and by type. It provides a command line 
utility, Python library and plugins for various editors to quickly sort all your 
imports. It requires Python 3.6+ to run but supports formatting Python 2 code 
too.

%prep
%if !%{with test}
%setup -q -n isort-%{version}
chmod -x LICENSE
%else
%setup -q -n isort-%{version} -T -b 1
%endif

%if !%{with test}
%build
%python_build
%endif

%if !%{with test}
%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_clone -a %{buildroot}%{_bindir}/isort
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%{python_expand # create egg-info for example projects
for exampledir in example_shared_isort_profile example_isort_formatting_plugin; do
  pushd $exampledir
  # no exact environment as upstreams devel project
  rm poetry.lock
  # no dependency download, we have it by BuildRequires
  sed -i '/tool.poetry.dependencies/,/^$/ d' pyproject.toml
  poetry-%{$python_bin_suffix} install
  # append current dir, only use colon if not empty
  export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}$(pwd)"
  popd
done
}
# no test_hypothesmith because no libcst because no pyre-check
%pytest -W "ignore::UserWarning" -W "ignore::DeprecationWarning" --ignore tests/test_hypothesmith.py
%endif

%if !%{with test}
%post
%python_install_alternative isort

%postun
%python_uninstall_alternative isort

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/isort
%{python_sitelib}/isort
%{python_sitelib}/isort-%{version}-py*.egg-info
%endif

%changelog
