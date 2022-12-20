#
# spec file for package python-python-lsp-server
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


Name:           python-python-lsp-server
Version:        1.6.0
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-server
Source:         https://files.pythonhosted.org/packages/source/p/python-lsp-server/python-lsp-server-%{version}.tar.gz
#PATCH-FIX-UPSTREAM python-lsp-server-pr316-flake8v6.patch gh#python-lsp/python-lsp-server#316
Patch0:         python-lsp-server-pr316-flake8v6.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module tomli}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros >= 20210628
# SECTION test requirements
BuildRequires:  %{python_module docstring-to-markdown}
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8 >= 1.6.0 with %python-autopep8 < 1.7.0}
BuildRequires:  %{python_module flake8 >= 5.0.0 with %python-flake8 < 7}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module jedi >= 0.17.2 with %python-jedi < 0.19.0}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pydocstyle >= 2.0.0}
BuildRequires:  %{python_module pylint >= 2.5.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lsp-jsonrpc >= 1.0.0}
BuildRequires:  %{python_module rope >= 0.10.5}
BuildRequires:  %{python_module ujson >= 3.0.0}
BuildRequires:  %{python_module whatthepatch}
BuildRequires:  %{python_module yapf}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docstring-to-markdown
Requires:       python-pluggy >= 1.0.0
Requires:       python-python-lsp-jsonrpc >= 1.0.0
Requires:       python-setuptools >= 39.0.0
Requires:       python-ujson >= 3.0.0
Requires:       (python-jedi >= 0.17.2 with python-jedi < 0.19.0)
Suggests:       python-autopep8 >= 1.6.0
Conflicts:      python-autopep8 >= 1.7.0
Suggests:       python-pydocstyle >= 2.0.0
Suggests:       python-pylint >= 2.5.0
Suggests:       python-rope >= 0.10.5
Suggests:       python-yapf
Suggests:       python-whatthepatch
# SECTION flake8 pins
Suggests:       python-flake8 >= 5.0.0
Conflicts:      python-flake8 >= 7
Suggests:       python-mccabe >= 0.7.0
Conflicts:      python-mccabe >= 0.8.0
Suggests:       python-pycodestyle >= 2.9.0
Conflicts:      python-pycodestyle >= 2.11.0
Suggests:       python-pyflakes >= 2.5.0
Conflicts:      python-pyflakes >= 3.1.0
# /SECTION
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
# Remove pytest addopts
sed -i '/addopts/d' pyproject.toml

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pylsp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

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
