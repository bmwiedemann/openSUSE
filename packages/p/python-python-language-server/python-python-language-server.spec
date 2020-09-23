#
# spec file for package python-python-language-server
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
%bcond_without python2
Name:           python-python-language-server
Version:        0.35.1
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/palantir/python-language-server
Source:         https://files.pythonhosted.org/packages/source/p/python-language-server/python-language-server-%{version}.tar.gz
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8}
BuildRequires:  %{python_module flake8 >= 3.8.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mccabe >= 0.6.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pycodestyle >= 2.6.0}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pyflakes >= 2.2.0}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module rope >= 0.10.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module yapf}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jedi >= 0.17
Requires:       python-pluggy
Requires:       python-python-jsonrpc-server >= 0.4.0
Requires:       python-setuptools
Recommends:     python-autopep8
Recommends:     python-flake8 >= 3.8.0
Recommends:     python-mccabe >= 0.6.0
Recommends:     python-pycodestyle >= 2.6.0
Recommends:     python-pydocstyle >= 2.0.0
Recommends:     python-pyflakes >= 2.2.0
Recommends:     python-pylint
Recommends:     python-rope >= 0.10.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module future >= 0.14.0}
BuildRequires:  %{python_module jedi >= 0.17}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jsonrpc-server >= 0.4.0}
%if %{with python2}
BuildRequires:  python2-backports.functools_lru_cache
BuildRequires:  python2-configparser
%endif
# /SECTION
%ifpython2
Requires:       python2-backports.functools_lru_cache
Requires:       python2-configparser
Requires:       python2-future >= 0.14.0
Requires:       python2-ujson <= 2.3.0
%else
Requires:       python3-ujson >= 3.0.0
%endif
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Python Language Server for the Language Server Protocol.

If the respective recommended packages are installed, the following optional providers
will be enabled:

- Rope for Completions and renaming
- Pyflakes linter to detect various errors
- McCabe linter for complexity checking
- pycodestyle linter for style checking
- pydocstyle linter for docstring style checking (disabled by default)
- autopep8 for code formatting
- YAPF for code formatting (preferred over autopep8)

%prep
%autosetup -n python-language-server-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pyls
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pyls

%postun
%python_uninstall_alternative pyls

%check
# Remove pytest addopts
rm setup.cfg
# define custom macros to skip tests in pytest
%define pytest_addskiptest() \
   for t in %{**}; do \
     pytest_skippedtests+="${pytest_skippedtests:+ or }${t}"; \
   done
%define pytest_skiptests ${pytest_skippedtests:+-k "not (${pytest_skippedtests})"}
%if 0%{?sle_version} == 150100 && 0%{?is_opensuse}
  # Test failure on Leap 15.1 due to different pylint version
  %pytest_addskiptest test_syntax_error_pylint_py
%endif
%if 0%{?sle_version} >= 150000 && 0%{?is_opensuse}
  # Test failure on Leap 15 due to mock hiccup
  %pytest_addskiptest test_flake8_config_param
  %pytest_addskiptest test_flake8_executable_param
%endif
%pytest %{pytest_skiptests}

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pyls
%{python_sitelib}/python_language_server-%{version}-py*.egg-info
%{python_sitelib}/pyls/

%changelog
