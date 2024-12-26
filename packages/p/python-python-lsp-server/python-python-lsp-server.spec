#
# spec file for package python-python-lsp-server
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}

Name:           python-python-lsp-server
Version:        1.12.0
Release:        0
Summary:        Python Language Server for the Language Server Protocol
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-server
Source:         https://files.pythonhosted.org/packages/source/p/python-lsp-server/python_lsp_server-%{version}.tar.gz
Patch1:         unpin-autopep8.patch
# PATCH-FIX-UPSTREAM pylsp-issues-602-605.patch gh#python-lsp/python-lsp-server#602 gh#python-lsp/python-lsp-server#605
Patch2:         pylsp-issues-602-605.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm >= 3.4.3}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros >= 20210628
# SECTION test requirements
BuildRequires:  %{python_module docstring-to-markdown}
BuildRequires:  %{python_module PyQt5}
BuildRequires:  %{python_module autopep8 >= 2.0.4}
BuildRequires:  %{python_module flake8 >= 7.1 with %python-flake8 < 8}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module importlib_metadata > 4.8.3 if %python-base < 3.10}
BuildRequires:  %{python_module jedi >= 0.17.2 with %python-jedi < 0.20}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pluggy}
BuildRequires:  %{python_module pydocstyle >= 6.3.0 with %python-pydocstyle < 6.4.0}
BuildRequires:  %{python_module pylint >= 3.1 with %python-pylint < 4}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lsp-jsonrpc >= 1.1.0 with %python-python-lsp-jsonrpc < 2}
BuildRequires:  %{python_module rope >= 1.2.0}
BuildRequires:  %{python_module ujson >= 3.0.0}
BuildRequires:  %{python_module whatthepatch >= 1.0.2 with %python-whatthepatch < 2}
BuildRequires:  %{python_module yapf >= 0.33}
# /SECTION
BuildRequires:  fdupes
Requires:       python-docstring-to-markdown
Requires:       python-pluggy >= 1.0.0
Requires:       python-ujson >= 3.0.0
Requires:       (python-jedi >= 0.17.2 with python-jedi < 0.20)
Requires:       (python-python-lsp-jsonrpc >= 1.1.0 with python-python-lsp-jsonrpc < 2)
%if 0%{?python_version_nodots} < 310
Requires:       python-importlib_metadata >= 4.8.3
%endif
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
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

%package all
Summary:        The python-lsp-server[all] extra
# Note: check flake8 pins as well
Requires:       python-rope >= 1.2.0
Requires:       python-autopep8 >= 2.0.4
Requires:       python-yapf >= 0.33
Requires:       (python-flake8 >= 7.1 with python-flake8 < 8)
Requires:       (python-mccabe >= 0.7.0 with python-mccabe < 0.8.0)
Requires:       (python-pycodestyle >= 2.12.0 with python-pycodestyle < 2.13.0)
Requires:       (python-pydocstyle >= 6.3.0 with python-pydocstyle < 6.4.0)
Requires:       (python-pyflakes >= 3.2.0 with python-pyflakes < 3.3.0)
Requires:       (python-pylint >= 3.1 with python-pylint < 4)
Requires:       (python-whatthepatch >= 1.0.2 with python-whatthepatch < 2)

%description all
Python Language Server for the Language Server Protocol

This package provides the dependencies for the pip
python-lsp-server[all] extra requirement

%prep
%autosetup -p1 -n python_lsp_server-%{version}
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
%{python_sitelib}/python_lsp_server-%{version}.dist-info

%files %{python_files all}
%doc README.md
%license LICENSE

%changelog
