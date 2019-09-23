#
# spec file for package python-murano-pkg-check
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global sname murano-pkg-check
Name:           python-murano-pkg-check
Version:        0.3.0
Release:        0
Summary:        Murano package validator tool
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://docs.openstack.org/developer/murano/
Source0:        https://files.pythonhosted.org/packages/source/m/murano-pkg-check/murano-pkg-check-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PyYAML >= 3.10
BuildRequires:  python-devel
BuildRequires:  python-oslo.i18n >= 3.15.3
BuildRequires:  python-oslotest >= 3.2.0
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-python-subunit >= 1.0.0
BuildRequires:  python-semantic_version
BuildRequires:  python-setuptools >= 16.0
BuildRequires:  python-stevedore >= 1.20.0
BuildRequires:  python-testrepository >= 0.0.18
BuildRequires:  python-testscenarios >= 0.4
BuildRequires:  python-testtools >= 2.2.0
BuildRequires:  python-yaql >= 1.1.3
Requires:       python-PyYAML >= 3.10
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-semantic_version
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-yaql >= 1.1.3
BuildArch:      noarch

%description
Murano package validator tool

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup

%build
%{py2_build}

%install
%{py2_install}

%check
%{__python2} setup.py testr

%files
%doc README.rst
%license LICENSE
%{_bindir}/murano-pkg-check
%{python2_sitelib}/muranopkgcheck
%{python2_sitelib}/*.egg-info

%changelog
