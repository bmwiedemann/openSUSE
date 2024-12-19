#
# spec file for package python-yaql
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


%global oldpython python
Name:           python-yaql
Version:        3.0.0
Release:        0
Summary:        YAQL - Yet Another Query Language
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/yaql
Source0:        https://files.pythonhosted.org/packages/source/y/yaql/yaql-3.0.0.tar.gz
BuildRequires:  openstack-macros
# for testing
BuildRequires:  python3-Sphinx
BuildRequires:  python3-fixtures
BuildRequires:  python3-pbr
BuildRequires:  python3-ply
BuildRequires:  python3-python-dateutil
BuildRequires:  python3-python-subunit
BuildRequires:  python3-setuptools
BuildRequires:  python3-stestr
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. YAQL is
written in python and is distributed via PyPI.

%package -n python3-yaql
Summary:        YAQL - Yet Another Query Language
Requires:       python3-Babel
Requires:       python3-ply
Requires:       python3-python-dateutil
Conflicts:      %{oldpython}-yaql < %version-%release

%description -n python3-yaql
YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. YAQL is
written in python and is distributed via PyPI.

This package contains the Python 3.x module.

%prep
%autosetup -p1 -n yaql-3.0.0
%py_req_cleanup

%build
%{py3_build}

%install
%{py3_install}

%check
%{openstack_stestr_run}

%files -n python3-yaql
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/yaql
%{python3_sitelib}/yaql
%{python3_sitelib}/yaql*.egg-info

%changelog
