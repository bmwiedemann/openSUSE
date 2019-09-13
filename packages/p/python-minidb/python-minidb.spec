#
# spec file for package python-minidb
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define         skip_python2 1
%bcond_without  test
Name:           python-minidb
Version:        2.0.2
Release:        0
Summary:        SQLite3-based store for Python objects
License:        ISC
Group:          Development/Languages/Python
Url:            http://thp.io/2010/minidb/
Source:         https://files.pythonhosted.org/packages/source/m/minidb/minidb-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module nose}
BuildRequires:  python3-testsuite
%endif
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Minidb 2 allows you to store Python objects in a SQLite 3 database.

%prep
%setup -q -n minidb-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_expand nosetests-%{$python_bin_suffix}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/minidb.py*
%{python_sitelib}/minidb-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/minidb*.py*

%changelog
