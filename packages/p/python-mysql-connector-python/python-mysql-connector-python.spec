#
# spec file for package python-mysql-connector-python
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-mysql-connector-python
Version:        8.0.19
Release:        0
Summary:        MySQL driver written in Python
License:        SUSE-GPL-2.0-with-FLOSS-exception
Group:          Development/Languages/Python
URL:            http://dev.mysql.com/doc/connector-python/en/index.html
Source:         https://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-python-%{version}.tar.gz
Patch0:         remove-require-version-constraint.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
Requires:       python-protobuf
BuildArch:      noarch
%python_subpackages

%description
MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0 specification (PEP-249).

%prep
%setup -q -n mysql-connector-python-%{version}
%patch0 -p1

%build
%python_build

%install
# bug in setuptools prevents proper c lib installation
# when using python_install so use custom python_exec instead
%python_exec setup.py install --prefix=%{_prefix} --root=%{buildroot}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#FIXME(toabctl): Reenable testuite
# probably won't work against mariadb 10
# the test script is using rather deep details
# of `mysql` table structure
# --matejcik
#check
#python unittests.py --with-mysql=/usr

%files %{python_files}
%license LICENSE.txt
%doc README.txt CHANGES.txt
%{python_sitelib}/*

%changelog
