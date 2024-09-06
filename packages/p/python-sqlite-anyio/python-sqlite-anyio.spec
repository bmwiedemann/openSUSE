#
# spec file for package python-sqlite-anyio
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


Name:           python-sqlite-anyio
Version:        0.2.3
Release:        0
Summary:        Asynchronous client for SQLite using AnyIO
License:        MIT
URL:            https://github.com/davidbrochart/sqlite-anyio
Source0:        https://files.pythonhosted.org/packages/source/s/sqlite_anyio/sqlite_anyio-%{version}.tar.gz
Source99:       python-sqlite-anyio.rpmlintrc
BuildRequires:  %{python_module base >  3.8}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-anyio >= 4.0 with python-anyio < 5)
# This is provided by the full python stack
Requires:       python-sqlite3
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module anyio >= 4.0}
BuildRequires:  %{python_module pytest >= 8}
BuildRequires:  %{python_module sqlite3}
BuildRequires:  %{python_module trio >= 0.24.0}
# /SECTION
%python_subpackages

%description
Asynchronous client for SQLite using AnyIO
Originally from https://gist.github.com/agronholm/458637aa569720fb1305cc74347e3e1d

%prep
%autosetup -p1 -n sqlite_anyio-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/sqlite_anyio
%{python_sitelib}/sqlite_anyio-%{version}.dist-info

%changelog
