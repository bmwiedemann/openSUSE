#
# spec file
#
# Copyright (c) 2021 SUSE LLC
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
Version:        5.10.1
Release:        0
Summary:        A Python utility / library to sort Python imports
License:        MIT
URL:            https://pycqa.github.io/isort/
# tests and example projects are not packaged for PyPI, get them from Github
Source:         https://github.com/PyCQA/isort/archive/%{version}.tar.gz#/isort-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210127.3a18043
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-colorama >= 0.4.3
Recommends:     python-pip-api
Recommends:     python-pipreqs
Suggests:       git
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module colorama >= 0.4.3}
BuildRequires:  %{python_module hypothesmith}
BuildRequires:  %{python_module libcst}
BuildRequires:  %{python_module natsort}
BuildRequires:  %{python_module pip-api}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest > 6.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  git
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
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

echo "
# increase test deadline for slow obs executions
import hypothesis
hypothesis.settings.register_profile(
    'obs',
    deadline=5000,
    suppress_health_check=[hypothesis.HealthCheck.too_slow]
)
" >> tests/conftest.py

# unpin natsort in example plugin
sed -i 's/natsort = "^/natsort = ">=/' example_isort_sorting_plugin/pyproject.toml

%build
%pyproject_wheel

%if !%{with test}
%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/isort
%python_clone -a %{buildroot}%{_bindir}/isort-identify-imports
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
# test_projects_using_isort.py: these tests try to clone from online git repositories.
ignoretests="--ignore tests/integration/test_projects_using_isort.py"
# don't run benchmarks
ignoretests+=" --ignore tests/benchmark"
# test_setting_combinations.py::test_isort_is_idempotent
# is flaky https://github.com/PyCQA/isort/issues/1466
donttest="(test_setting_combinations and test_isort_is_idempotent)"
# requirementslib is not available yet for python 3.9 or greater, 
# it's a deprecated finder for isort so we drop it
# https://github.com/sarugaku/requirementslib/issues/288
donttest+=" or (test_deprecated_finders and test_pipfile_finder)"

ORIGPATH=$PATH
%{python_expand # install isort and required example projects into custom root
mkdir isort-test-%{$python_bin_suffix}
export PATH="$(pwd)/isort-test-%{$python_bin_suffix}/usr/bin:$ORIGPATH"
export PYTHONPATH="$(pwd)/isort-test-%{$python_bin_suffix}%{$python_sitelib}"
export PYTHONDONTWRITEBYTECODE=1

for proj in build/isort-%{version}-py3-none-any.whl \
            ./example_shared_isort_profile \
            ./example_isort_formatting_plugin \
            ./example_isort_sorting_plugin
do
  $python -m pip install --verbose \
                         --no-index \
                         --root $(pwd)/isort-test-%{$python_bin_suffix} \
                         --no-deps \
                         --use-pep517 \
                         --no-cache-dir\
                         --no-build-isolation \
                         --progress-bar off \
                         --disable-pip-version-check \
                         ${proj}
done

pytest-%{$python_bin_suffix} -v \
         -W "ignore::UserWarning" \
         -W "ignore::DeprecationWarning" \
         --hypothesis-profile="obs" \
         ${ignoretests} \
         -k "not (${donttest} ${$python_donttest})"
}

%endif

%if !%{with test}
%post
%python_install_alternative isort isort-identify-imports

%postun
%python_uninstall_alternative isort

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/isort
%python_alternative %{_bindir}/isort-identify-imports
%{python_sitelib}/isort
%{python_sitelib}/isort-%{version}.dist-info
%endif

%changelog
