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
Version:        5.6.4
Release:        0
Summary:        A Python utility / library to sort Python imports
License:        MIT
URL:            https://pycqa.github.io/isort/
# tests and example projects are not packaged for PyPI, get them from Github
Source:         https://github.com/PyCQA/isort/archive/%{version}.tar.gz#/isort-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-colorama >= 0.4.3
Recommends:     python-hypothesmith
Recommends:     python-pip-api
Recommends:     python-pipreqs
Recommends:     python-requirementslib
Suggests:       git
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module hypothesis-auto}
BuildRequires:  %{python_module hypothesmith}
BuildRequires:  %{python_module libcst}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pip-api}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requirementslib >= 1.5}
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

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/isort
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
ORIGPATH=$PATH
%{python_expand # install isort and required example projects into custom root
mkdir isort-test-%{$python_bin_suffix}
for proj in isort*.whl ./example_shared_isort_profile ./example_isort_formatting_plugin; do
  $python -m pip install --verbose \
                         --no-index \
                         --root $(pwd)/isort-test-%{$python_bin_suffix} \
                         --no-deps \
                         --use-pep517 \
                         --no-build-isolation \
                         --progress-bar off \
                         --disable-pip-version-check \
                         ${proj}
done

export PATH="$(pwd)/isort-test-%{$python_bin_suffix}/usr/bin:$ORIGPATH"
export PYTHONPATH="$(pwd)/isort-test-%{$python_bin_suffix}%{$python_sitelib}"
export PYTHONDONTWRITEBYTECODE=1
# test_projects_using_isort.py: these tests try to clone from
# online git repositories.
# test_settung_combinations.py::test_isort_is_idempotent
# is flaky https://github.com/PyCQA/isort/issues/1466
pytest-%{$python_bin_suffix} -v \
         -W "ignore::UserWarning" \
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
%{python_sitelib}/isort-%{version}.dist-info
%endif

%changelog
