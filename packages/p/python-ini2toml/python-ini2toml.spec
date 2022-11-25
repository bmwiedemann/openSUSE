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

%bcond_with ringdisabled
#              | Ring1 | Factory |
# ringdisabled |   x   |         |
# ------       | ----- | ------- |
# lite         |   x   |    x    |
# full         |       |    x    |
# all          |       |    x    |
# experimental |       |         |
%bcond_without lite
%if %{with ringdisabled}
%bcond_with full
%bcond_with all
%else
%bcond_without full
%bcond_without all
%endif
%bcond_with experimental

%define skip_python2 1
Name:           python-ini2toml%{psuffix}
Version:        0.11.3
Release:        0
Summary:        Automatic conversion of .ini/cfg files to TOML equivalents
License:        MPL-2.0
URL:            https://github.com/abravalheri/ini2toml/
Source:         https://files.pythonhosted.org/packages/source/i/ini2toml/ini2toml-%{version}.tar.gz
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 20.7
Requires(post): update-alternatives
Requires(postun):update-alternatives
%if %{with test}
BuildRequires:  %{python_module packaging >= 20.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module validate-pyproject >= 0.6 with %python-validate-pyproject < 2}
%if %{with lite}
BuildRequires:  %{python_module ini2toml-lite = %{version}}
%endif
%if %{with full}
BuildRequires:  %{python_module ini2toml-full = %{version}}
%endif
%if %{with all}
BuildRequires:  %{python_module ini2toml-all = %{version}}
%endif
%if %{with experimental}
BuildRequires:  %{python_module ini2toml-experimental = %{version}}
%endif
%endif
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
The original purpose of this project is to help migrating setup.cfg files
to PEP 621, but by extension it can also be used to convert any compatible ini_cfg
file to TOML.

%if %{with lite}
%package lite
Summary:        Python ini2toml[lite] extra requirement
Requires:       python-ini2toml = %{version}
Requires:       (python-importlib-metadata if python-base < 3.8)
Requires:       (python-tomli-w >= 0.4.0 with python-tomli-w < 2)

%description lite
The ini2toml[lite] extra requirements for %{python_flavor}-ini2toml
%endif

%if %{with full}
%package full
Summary:        Python ini2toml[full] extra requirement
Requires:       python-ini2toml = %{version}
Requires:       (python-configupdater >= 3.0.1 with python-configupdater < 4)
Requires:       (python-tomlkit >= 0.10 with python-tomlkit < 2)

%description full
The ini2toml[full] extra requirements for %{python_flavor}-ini2toml
%endif

%if %{with all}
%package all
Summary:        Python ini2toml[all] extra requirement
Requires:       python-ini2toml = %{version}
Requires:       (python-configupdater >= 3.0.1 with python-configupdater < 4)
Requires:       (python-importlib-metadata if python-base < 3.8)
Requires:       (python-tomli-w >= 0.4.0 with python-tomli-w < 2)
Requires:       (python-tomlkit >= 0.10 with python-tomlkit < 2)

%description all
The ini2toml[all] extra requirements for %{python_flavor}-ini2toml
%endif

%if %{with experimental}
%package experimental
Summary:        Python ini2toml[experimental] extra requirement
Requires:       python-ini2toml = %{version}
Requires:       python-pyproject-fmt >= 0.4.0

%description experimental
The ini2toml[experimental] extra requirements for %{python_flavor}-ini2toml
%endif

%prep
%setup -q -n ini2toml-%{version}
sed -i 's/--cov ini2toml --cov-report term-missing//' setup.cfg

%if !%{with test}
%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ini2toml
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%if %{without all} && %{without full}
ignoretests=(
    --ignore tests/test_examples.py
    --ignore tests/test_transformations.py
    --ignore tests/test_translator.py
    --ignore tests/drivers/test_configupdater.py
    --ignore tests/plugins/test_best_effort.py
    --ignore tests/plugins/test_coverage.py
    --ignore tests/drivers/test_full_toml.py
    --ignore tests/plugins/test_isort.py
    --ignore tests/plugins/test_mypy.py
    --ignore tests/plugins/test_pytest.py
    --ignore tests/plugins/test_setuptools_pep621.py
)
%endif
%if %{without experimental}
donttest=(-k "not test_auto_formatting")
%endif
%pytest "${ignoretests[@]}" "${donttest[@]}"
%endif

%post
%python_install_alternative ini2toml

%postun
%python_uninstall_alternative ini2toml

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/ini2toml
%{python_sitelib}/ini2toml
%{python_sitelib}/ini2toml-%{version}*-info

%if %{with lite}
%files %{python_files lite}
%license LICENSE.txt
%endif

%if %{with full}
%files %{python_files full}
%license LICENSE.txt
%endif

%if %{with all}
%files %{python_files all}
%license LICENSE.txt
%endif

%if %{with experimental}
%files %{python_files experimental}
%license LICENSE.txt
%endif
%endif

%changelog
