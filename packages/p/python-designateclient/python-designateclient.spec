#
# spec file for package python-designateclient
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


%global sname python-designateclient
Name:           python-designateclient
Version:        2.11.0
Release:        0
Summary:        OpenStack DNS as a Service - Client
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/%{sname}
Source0:        https://files.pythonhosted.org/packages/source/p/%{sname}/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-jsonschema >= 2.6.0
BuildRequires:  python-jsonschema < 3
BuildRequires:  python-keystoneclient
BuildRequires:  python-mock
BuildRequires:  python-oslotest
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-python-subunit
BuildRequires:  python-requests-mock
BuildRequires:  python-setuptools
BuildRequires:  python-stestr
Requires:       python-cliff >= 2.8.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-jsonschema >= 2.6.0
Requires:       python-jsonschema < 3
Requires:       python-keystoneauth1 >= 3.4.0
Requires:       python-keystoneclient
Requires:       python-osc-lib >= 1.8.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-requests >= 2.14.2
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch

%description
OpenStack DNS as a Service - Client

%package doc
Summary:        Documentation for the OpenStack DNS as a Service - Client
Group:          Documentation/HTML
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description doc
Documentation for the OpenStack DNS as a Service - Client.

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup

%build
%py2_build

# generate html docs
%{__python2} setup.py build_sphinx --builder=html,man
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py2_install
# man pages
install -p -D -m 644 doc/build/man/*designateclient.1 %{buildroot}%{_mandir}/man1/designateclient.1

%check
stestr run

%files
%license LICENSE
%doc README.rst ChangeLog
%{python2_sitelib}/designateclient
%{python2_sitelib}/python_designateclient-%{version}-py2.?.egg-info
%{_bindir}/designate
%{_mandir}/man1/designateclient.1.*

%files doc
%license LICENSE
%doc doc/build/html

%changelog
