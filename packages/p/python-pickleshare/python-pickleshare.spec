#
# spec file for package python-pickleshare
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


%bcond_without test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pickleshare
Version:        0.7.5
Release:        0
Summary:        Tiny shelve-like database with concurrency support
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/vivainio/pickleshare
Source:         https://files.pythonhosted.org/packages/source/p/pickleshare/pickleshare-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-pathlib2
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%ifpython2
Requires:       python-pathlib2
%endif
BuildArch:      noarch
%python_subpackages

%description
PickleShare - a small 'shelve' like datastore with concurrency support

Like shelve, a PickleShareDB object acts like a normal dictionary. Unlike shelve,
many processes can access the database simultaneously. Changing a value in 
database is immediately visible to other processes accessing the same database.

Concurrency is possible because the values are stored in separate files. Hence
the "database" is a directory where *all* files are governed by PickleShare.

This module is certainly not ZODB, but can be used for low-load
(non-mission-critical) situations where tiny code size trumps the 
advanced features of a "real" object database.

Installation guide: pip install path pickleshare

%prep
%setup -q -n pickleshare-%{version}
# Remove shebang
sed -i '1{\@^#!/usr/bin/env python@d}' pickleshare.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
# need to set locale to avoid UnicodeEncodeError
export LANG=en_US.UTF-8
%python_expand py.test-%{$python_bin_suffix} .
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pickleshare.py*
%{python_sitelib}/pickleshare-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/pickleshare.*.py*

%changelog
