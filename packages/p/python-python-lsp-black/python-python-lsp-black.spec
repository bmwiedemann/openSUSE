#
# spec file for package python-python-lsp-black
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-python-lsp-black
Version:        1.3.0
Release:        0
Summary:        Black plugin for the Python LSP Server
License:        MIT
URL:            https://github.com/python-lsp/python-lsp-black
Source:         https://github.com/python-lsp/python-lsp-black/archive/refs/tags/v%{version}.tar.gz#/python-lsp-black-%{version}-gh.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module black >= 22.3.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-lsp-server >= 1.4.0}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
# /SECTION
BuildRequires:  fdupes
Requires:       python-black >= 22.3.0
Requires:       python-python-lsp-server
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli
%endif
BuildArch:      noarch
%python_subpackages

%description
Black plugin for the Python LSP Server

To avoid unexpected results you should make sure yapf and autopep8 are not installed.

- pyls-black can either format an entire file or just the selected text.
- The code will only be formatted if it is syntactically valid Python.
- Text selections are treated as if they were a separate Python file.
  Unfortunately this means you can't format an indented block of code.
- python-lsp-black will use your project's pyproject.toml if it has one.

%prep
%setup -q -n python-lsp-black-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/pylsp_black
%{python_sitelib}/python_lsp_black-%{version}.dist-info

%changelog
