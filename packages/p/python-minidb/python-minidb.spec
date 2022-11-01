#
# spec file for package python-minidb
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


%define modname minidb
%define         skip_python2 1
%bcond_without  test
Name:           python-minidb
Version:        2.0.7
Release:        0
Summary:        SQLite3-based store for Python objects
License:        ISC
Group:          Development/Languages/Python
URL:            https://thp.io/2010/minidb/
Source:         https://github.com/thp/%{modname}/archive/refs/tags/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  python3-testsuite
%endif
%python_subpackages

%description
Minidb 2 allows you to store Python objects in a SQLite 3 database.

%prep
%autosetup -p1 -n minidb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest -v
%endif

%files %{python_files}
%doc README.md
%{python_sitelib}/minidb.py*
%{python_sitelib}/minidb-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/minidb*.py*

%changelog
