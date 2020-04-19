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
%if %{without python2}
  %define skip_python2 1
%endif
Name:           python-python-language-server
Version:        0.31.9
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/palantir/python-language-server
Source:         https://files.pythonhosted.org/packages/source/p/python-language-server/python-language-server-%{version}.tar.gz
# gh#palantir/python-language-server#778
Patch0:         pyls-pr778-multiplerefs.patch 
# gh#palantir/python-language-server#781
Patch1:         pyls-pr781-jedi016-017.patch 
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module future >= 0.14.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mccabe}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pyflakes >= 1.6.0}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module rope >= 0.10.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module versioneer}
BuildRequires:  %{python_module yapf}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jedi >= 0.16
Requires:       python-pluggy
Requires:       python-python-jsonrpc-server >= 0.3.2
Requires:       python-setuptools
Recommends:     python-autopep8
Recommends:     python-flake8
Recommends:     python-mccabe
Recommends:     python-pycodestyle
Recommends:     python-pydocstyle >= 2.0.0
Recommends:     python-pyflakes >= 1.6.0
Recommends:     python-pylint
Recommends:     python-rope >= 0.10.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jedi >= 0.16}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-jsonrpc-server >= 0.3.2}
%if %{with python2}
BuildRequires:  python2-backports.functools_lru_cache
BuildRequires:  python2-configparser
%endif
# /SECTION
%ifpython2
Requires:       python2-backports.functools_lru_cache
Requires:       python2-configparser
Requires:       python2-future >= 0.14.0
%endif
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
%setup -q -n python-language-server-%{version}
%autopatch -p1
# Use system python3-ujson without regards which version it is
sed -i "s/'ujson<=.*'/'ujson'/" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Remove pytest addopts
rm setup.cfg
# unclean tear down
skip_tests="test_missing_message"
# Test failure on Leap 15.1 due to different pylint version
%if 0%{?sle_version} == 150100 && 0%{?is_opensuse}
  skip_tests+=" or test_syntax_error_pylint_py"
%endif
# unknown encoding utd-8 on python2
%ifpython2
  skip_tests+=" or test_references_builtin"
%endif
%pytest  -k "not ( $skip_tests )"

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/pyls
%{python_sitelib}/python_language_server-%{version}-py*.egg-info
%{python_sitelib}/pyls/

%changelog
