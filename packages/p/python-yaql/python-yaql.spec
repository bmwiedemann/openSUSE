#
# spec file for package python-yaql
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


%global sname yaql
Name:           python-yaql
Version:        1.1.3
Release:        0
Summary:        YAQL - Yet Another Query Language
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/y/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
# for testing
BuildRequires:  python-Sphinx
BuildRequires:  python-devel
BuildRequires:  python-fixtures
BuildRequires:  python-oslosphinx
BuildRequires:  python-pbr
BuildRequires:  python-ply
BuildRequires:  python-python-dateutil
BuildRequires:  python-python-subunit
BuildRequires:  python-six
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools
Requires:       python-Babel
Requires:       python-ply
Requires:       python-python-dateutil
Requires:       python-six
BuildArch:      noarch

%description
YAQL (Yet Another Query Language) is an embeddable and extensible query
language, that allows performing complex queries against arbitrary objects. It
has a vast and comprehensive standard library of frequently used querying
functions and can be extend even further with user-specified functions. YAQL is
written in python and is distributed via PyPI.

%prep
%autosetup -n yaql-%{version}
%py_req_cleanup

%build
%py2_build

%install
%py2_install

%check
%{__python2} setup.py testr

%files
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/yaql
%{python2_sitelib}/%{sname}
%{python2_sitelib}/%{sname}*.egg-info

%changelog
