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
%bcond_without python2
Name:           python-isort%{psuffix}
Version:        4.3.21
Release:        0
Summary:        A Python utility / library to sort Python imports
License:        MIT
URL:            https://github.com/timothycrosley/isort
Source:         https://files.pythonhosted.org/packages/source/i/isort/isort-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-appdirs >= 1.4.0
Recommends:     python-pip
Recommends:     python-pipreqs
Recommends:     python-requirementslib
Recommends:     python-toml
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-backports.functools_lru_cache
BuildRequires:  python-futures
%endif
%if %{with test}
BuildRequires:  %{python_module appdirs >= 1.4.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pipreqs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requirementslib}
BuildRequires:  %{python_module toml}
%endif
%ifpython2
Requires:       python-backports.functools_lru_cache
Requires:       python-futures
%endif
%python_subpackages

%description
isort your python imports for you so you don’t have to.

isort is a Python utility / library to sort imports alphabetically,
and automatically separated into sections. It provides a command line
utility, Python library and plugins for various editors to quickly
sort all your imports. It currently cleanly supports Python 2.7 - 3.6 without
any dependencies.

%prep
%setup -q -n isort-%{version}
chmod -x LICENSE

%build
%python_build

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/isort
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
# test_pipfile_finder - broken upstrem in tomlkit
%if %{with test}
%pytest -k 'not (test_settings_path_skip_issue_909 or test_standard_library_deprecates_user_issue_778 or test_skip_paths_issue_938 or test_requirements_finder or test_pipfile_finder)'
%endif

%if !%{with test}
%post
%python_install_alternative isort

%postun
%python_uninstall_alternative isort

%files %{python_files}
%{python_sitelib}/isort*
%python_alternative %{_bindir}/isort
%license LICENSE
%endif

%changelog
