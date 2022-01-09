#
# spec file for package python-python-lsp-server
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-python-lsp-server
Version:        1.3.3
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-server
Source:         https://files.pythonhosted.org/packages/source/p/python-lsp-server/python-lsp-server-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 39.0.0}
BuildRequires:  python-rpm-macros >= 20210628
# SECTION test requirements
BuildRequires:  %{python_module jedi >= 0.17.2}
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8 >= 1.6.0 with %python-autopep8 < 1.7.0}
BuildRequires:  %{python_module flake8 >= 4.0.0 with %python-flake8 < 4.1.0}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module mccabe >= 0.6.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pycodestyle >= 2.8.0 with %python-pycodestyle < 2.9.0}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pyflakes >= 2.4.0 with %python-pyflakes < 2.5.0}
BuildRequires:  %{python_module pylint >= 2.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lsp-jsonrpc >= 1.0.0}
BuildRequires:  %{python_module rope >= 0.10.5}
BuildRequires:  %{python_module ujson >= 3.0.0}
BuildRequires:  %{python_module yapf}

# /SECTION
BuildRequires:  fdupes
Requires:       python-jedi >= 0.17.2
Requires:       python-pluggy
Requires:       python-python-lsp-jsonrpc >= 1.0.0
Requires:       python-setuptools >= 39.0.0
Requires:       python-ujson >= 3.0.0
Suggests:       python-autopep8 >= 1.6.0
Conflicts:      python-autopep8 >= 1.7.0
Suggests:       python-flake8 >= 4.0.0
Conflicts:      python-flake8 >= 4.1.0
Suggests:       python-mccabe >= 0.6.0
Suggests:       python-pycodestyle >= 2.8.0
Conflicts:      python-pycodestyle >= 2.9.0
Suggests:       python-pydocstyle >= 2.0.0
Suggests:       python-pyflakes >= 2.4.0
Conflicts:      python-pyflakes >= 2.5.0
Suggests:       python-pylint >= 2.5.0
Suggests:       python-rope >= 0.10.5
Suggests:       python-yapf
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
Python Language Server for the Language Server Protocol

Fork of the python-language-server project, maintained by
the Spyder IDE team and the community

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
%autosetup -p1 -n python-lsp-server-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pylsp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # provide pylint command in correct flavor
mkdir -p build/testbin
ln -s %{_bindir}/pylint-%{$python_bin_suffix} build/testbin/pylint
}
export PATH="$PWD/build/testbin:$PATH"
# Remove pytest addopts
rm setup.cfg
%if 0%{?sle_version} >= 150000 && 0%{?is_opensuse}
  # Test failure on Leap 15 due to mock hiccup
  donttest+=" or test_flake8_config_param or test_flake8_executable_param"
%endif
%pytest -ra -k "not (dummy_k_expr_start ${donttest} ${$python_donttest})" -vv

%post
%python_install_alternative pylsp

%postun
%python_uninstall_alternative pylsp

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pylsp
%{python_sitelib}/pylsp
%{python_sitelib}/python_lsp_server-%{version}*-info

%changelog
