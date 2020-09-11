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
Version:        5.5.1
Release:        0
Summary:        A Python utility / library to sort Python imports
License:        MIT
URL:            https://pycqa.github.io/isort/
# only PyPI archive contains setup.py
Source:         https://files.pythonhosted.org/packages/source/i/isort/isort-%{version}.tar.gz
# ... but test data are not packaged for PyPI, get them from git sources
Source1:        https://github.com/PyCQA/isort/archive/%{version}.tar.gz#/isort-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-hypothesmith
Recommends:     python-pip-api
Recommends:     python-pipreqs
Recommends:     python-requirementslib >= 1.5.4
Recommends:     python-tomlkit
Suggests:       git
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hypothesis-auto}
BuildRequires:  %{python_module hypothesmith}
# we cannot just use the source dir on test flavor because tests expect the
# installed entrypoint (through alternatives)
BuildRequires:  %{python_module isort = %{version}}
BuildRequires:  %{python_module libcst}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip-api}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest-mock}
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
%setup -q -n isort-%{version}
chmod -x LICENSE
%if %{with test}
tar -x --strip-components=1 -f %{SOURCE1} \
    isort-%{version}/example_isort_formatting_plugin \
    isort-%{version}/example_shared_isort_profile \
    isort-%{version}/.isort.cfg \
    isort-%{version}/setup.cfg
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
  # don't enforce exact same environment as upstream's devel project
  rm poetry.lock
  # no dependency download, we have them all by BuildRequires
  sed -i '/tool.poetry.dependencies/,/^$/ d' pyproject.toml
  poetry-%{$python_bin_suffix} install
  # append current dir, only use colon if not empty
  export PYTHONPATH="${PYTHONPATH:+$PYTHONPATH:}$(pwd)"
  popd
done
}
# test_projects_using_isort.py: these tests try to clone from
# online git repositories.
# test_settung_combinations.py::test_isort_is_idempotent
# is flaky https://github.com/PyCQA/isort/issues/1466
%{pytest -W "ignore::UserWarning" \
         -W "ignore::DeprecationWarning" \
         --ignore tests/integration/test_projects_using_isort.py \
         -k "not (test_setting_combinations and test_isort_is_idempotent)"
}
%endif

%if !%{with test}
%post
%python_install_alternative isort

%postun
%python_uninstall_alternative isort

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/isort
%{python_sitelib}/isort
%{python_sitelib}/isort-%{version}-py*.egg-info
%endif

%changelog
