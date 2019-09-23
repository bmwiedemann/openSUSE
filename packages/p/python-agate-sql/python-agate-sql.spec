#
# spec file for package python-agate-sql
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
Name:           python-agate-sql
Version:        0.5.4
Release:        0
Summary:        SQL read/write support for agate
License:        MIT
Group:          Development/Languages/Python
Url:            http://agate-sql.readthedocs.org/
Source:         https://github.com/wireservice/agate-sql/archive/%{version}.tar.gz
# we do not have crate dialect
Patch0:         python-agate-sql-no-crate.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module SQLAlchemy >= 1.0.8}
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module nose}
# /SECTION
Requires:       python-SQLAlchemy >= 1.0.8
Requires:       python-agate >= 1.5.0
BuildArch:      noarch

%python_subpackages

%description
Agate-sql adds SQL read/write support to agate.

%prep
%setup -q -n agate-sql-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' agatesql/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%defattr(-,root,root,-)
%doc AUTHORS.rst README.rst CHANGELOG.rst
%license COPYING
%{python_sitelib}/*

%changelog
