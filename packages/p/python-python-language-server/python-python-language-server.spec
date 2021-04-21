#
# spec file for package python-python-language-server
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
%bcond_without python2
Name:           python-python-language-server
Version:        0.36.2
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/palantir/python-language-server
Source:         https://files.pythonhosted.org/packages/source/p/python-language-server/python-language-server-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pyls-jedi-newer.patch gh#palantir/python-language-server#901 -- remove jedi upper version boundary
Patch0:         pyls-jedi-newer.patch
# PATCH-FIX-UPSTREAM test_snippet_fix.patch -- gh#python-ls/python-ls#7
Patch1:         test_snippet_fix.patch
# PATCH-FIX-UPSTREAM test_numpy_hover_fix.patch -- gh#python-ls/python-ls#7
Patch2:         test_numpy_hover_fix.patch
# PATCH-FIX-UPSTREAM test_py39-code_folding.patch -- gh#python-ls/python-ls#9
Patch3:         test_py39-code_folding.patch
# PATCH-FIX-OPENSUSE pyls-openSUSE-unpin-extras.patch -- unpin extras_requires,
# because entrypoints requiring pyls[all] now check the requirements in the egg-info/requires.txt
Patch4:         pyls-openSUSE-unpin-extras.patch
BuildRequires:  %{python_module jedi >= 0.17.2}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module python-jsonrpc-server >= 0.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ujson}
BuildRequires:  %{python_module versioneer}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jedi >= 0.17.2
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
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8}
BuildRequires:  %{python_module flake8 >= 3.8.0}
BuildRequires:  %{python_module future >= 0.14.0}
BuildRequires:  %{python_module mccabe >= 0.6.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pycodestyle >= 2.6.0}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pyflakes >= 2.2.0}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rope >= 0.10.5}
BuildRequires:  %{python_module yapf}
BuildRequires:  %{python_module matplotlib  if (%python-base without python36-base)}
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas  if (%python-base without python36-base)}
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
Requires:       python-ujson >= 3.0.0
%endif
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
%autosetup -p1 -n python-language-server-%{version}
#unpin jedi -- use this if we don't need a patch for the current version
#sed -i 's/\(jedi>=[0-9\.]*\),<[0-9\.]*/\1/' setup.py
# need to unpin from egg-info too: e.g. pyls-black checks it.
#sed -i 's/\(jedi\)<[0-9\.]*,\(>=[0-9\.]*\)/\1\2/' python_language_server.egg-info/requires.txt

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
%if 0%{?sle_version} >= 150000 && 0%{?is_opensuse}
  # Test failure on Leap 15 due to mock hiccup
  donttest+=" or test_flake8_config_param or test_flake8_executable_param"
%endif
%if 0%{?sle_version} == 150100 && 0%{?is_opensuse}
  # Test failure on Leap 15.1 due to different pylint version
  donttest+=" or test_syntax_error_pylint_py"
%endif
# don't test numpy on python36: NEP 29
python36_donttest=" or test_numpy or test_pandas or test_matplotlib"
%pytest -ra -k "not (dummy_k_expr_start ${donttest} ${$python_donttest})" -vv

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pyls
%{python_sitelib}/python_language_server-%{version}-py*.egg-info
%{python_sitelib}/pyls/

%changelog
