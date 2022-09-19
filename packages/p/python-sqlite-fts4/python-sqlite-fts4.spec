#
# spec file for package python-sqlite-fts4
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
Name:           python-sqlite-fts4
Version:        1.0.3
Release:        0
Summary:        Python functions for working with SQLite FTS4 search
License:        Apache-2.0
URL:            https://github.com/simonw/sqlite-fts4
Source:         https://github.com/simonw/sqlite-fts4/archive/%{version}.tar.gz#/sqlite-fts4-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python functions for working with SQLite FTS4 search

%prep
%setup -q -n sqlite-fts4-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/sqlite_fts4
%{python_sitelib}/sqlite_fts4-%{version}-*.egg-info

%changelog
