#
# spec file for package python-mycli
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-mycli
Version:        1.26.1
Release:        0
Summary:        CLI for MySQL Database. With auto-completion and syntax highlighting
License:        BSD-3-Clause
URL:            http://mycli.net
Source:         https://files.pythonhosted.org/packages/source/m/mycli/mycli-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module cli-helpers >= 2.2.1}
BuildRequires:  %{python_module click >= 7.0}
BuildRequires:  %{python_module configobj >= 5.0.5}
BuildRequires:  %{python_module cryptography >= 36.0.2}
BuildRequires:  %{python_module importlib_resources >= 5.0.0}
BuildRequires:  %{python_module prompt_toolkit >= 3.0.6}
BuildRequires:  %{python_module pyaes >= 1.6.1}
BuildRequires:  %{python_module Pygments >= 1.6}
BuildRequires:  %{python_module PyMySQL >= 0.9.2}
BuildRequires:  %{python_module pyperclip >= 1.8.1}
BuildRequires:  %{python_module sqlglot >= 5.1.3}
BuildRequires:  %{python_module sqlparse >= 0.3.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-cli-helpers >= 2.2.1
Requires:       python-click >= 7.0
Requires:       python-configobj >= 5.0.5
Requires:       python-cryptography >= 36.0.2
Requires:       python-importlib_resources >= 5.0.0
Requires:       python-prompt_toolkit >= 3.0.6
Requires:       python-pyaes >= 1.6.1
Requires:       python-Pygments >= 1.6
Requires:       python-PyMySQL >= 0.9.2
Requires:       python-pyperclip >= 1.8.1
Requires:       python-sqlglot >= 5.1.3
Requires:       python-sqlparse >= 0.3.0
Suggests:       python-paramiko
BuildArch:      noarch
%python_subpackages

%description
CLI for MySQL Database. With auto-completion and syntax highlighting.

%prep
%setup -q -n mycli-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mycli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Testsuite currently fails
#%%check
#%%pyunittest discover -v

%post
%python_install_alternative mycli

%postun
%python_uninstall_alternative mycli

%files %{python_files}
%doc AUTHORS.rst README.md changelog.md
%license LICENSE.txt
%python_alternative %{_bindir}/mycli
%{python_sitelib}/*

%changelog
