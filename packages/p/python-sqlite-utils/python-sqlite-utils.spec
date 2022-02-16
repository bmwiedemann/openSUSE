#
# spec file for package python-sqlite-utils
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
%define skip_python2 1
%define skip_python36 1
Name:           python-sqlite-utils
Version:        3.24
Release:        0
Summary:        Python CLI tool and library for manipulating SQLite databases
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/simonw/sqlite-utils
Source:         https://files.pythonhosted.org/packages/source/s/sqlite-utils/sqlite-utils-%{version}.tar.gz
BuildRequires:  %{python_module click-default-group}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sqlite-fts4}
BuildRequires:  %{python_module tabulate}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-click-default-group
Requires:       python-sqlite-fts4
Requires:       python-tabulate
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
CLI tool and Python utility functions for manipulating SQLite databases.

%prep
%setup -q -n sqlite-utils-%{version}
# https://github.com/simonw/sqlite-utils/issues/357
sed -i 's:pytest-runner:pytest:' setup.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/sqlite-utils
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative sqlite-utils

%postun
%python_uninstall_alternative sqlite-utils

%check
export LANG=en_US.UTF-8
%pytest

%files %{python_files}
%doc README.md docs
%license LICENSE
%python_alternative %{_bindir}/sqlite-utils
%{python_sitelib}/*

%changelog
