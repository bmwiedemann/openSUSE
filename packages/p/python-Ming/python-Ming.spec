#
# spec file for package python-Ming
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-Ming
Version:        0.9.1
Release:        0
Summary:        Bringing order to Mongo since 2009
License:        MIT
Group:          Development/Languages/Python
URL:            http://merciless.sourceforge.net
Source:         https://files.pythonhosted.org/packages/source/M/Ming/Ming-%{version}.tar.gz
Patch0:         0001-disable_test_gridfs.patch
Patch1:         pymongo-reqs.patch
BuildRequires:  %{python_module FormEncode >= 1.2.1}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module mock >= 0.8.0}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pymongo >= 2.4}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pymongo >= 3.0
Requires:       python-pytz
Requires:       python-six >= 1.6.1
Recommends:     python-FormEncode >= 1.2.1
Recommends:     python-python-spidermonkey >= 0.0.10
BuildArch:      noarch
%python_subpackages

%description
Database mapping layer for MongoDB on Python. Includes schema enforcement and some facilities for schema migration.

%prep
%setup -q -n Ming-%{version}
%patch0 -p1
%patch1 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py -q test

%files %{python_files}
%doc README.rst
# no license available, neither in the tarball nor upstream
%{python_sitelib}/*

%changelog
