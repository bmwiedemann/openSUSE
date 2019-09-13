#
# spec file for package openstack-tempest
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


%global sname tempest
Name:           openstack-tempest
Version:        20.0.0
Release:        0
Summary:        The OpenStack Integration Test Suite
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/tempest
Source0:        https://files.pythonhosted.org/packages/source/T/Tempest/%{sname}-%{version}.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-PrettyTable >= 0.7.1
BuildRequires:  python-PyYAML >= 3.10
BuildRequires:  python-cliff >= 2.8.0
BuildRequires:  python-debtcollector >= 1.2.0
BuildRequires:  python-devel
BuildRequires:  python-fixtures >= 3.0.0
BuildRequires:  python-jsonschema >= 2.6.0
BuildRequires:  python-mock
BuildRequires:  python-netaddr >= 0.7.18
BuildRequires:  python-os-testr
BuildRequires:  python-oslo.concurrency >= 3.25.0
BuildRequires:  python-oslo.config >= 5.1.0
BuildRequires:  python-oslo.log >= 3.36.0
BuildRequires:  python-oslo.serialization >= 2.18.0
BuildRequires:  python-oslo.utils >= 3.33.0
BuildRequires:  python-oslotest
BuildRequires:  python-paramiko >= 2.0.0
BuildRequires:  python-pep8
BuildRequires:  python-python-subunit >= 1.0.0
BuildRequires:  python-six >= 1.10.0
BuildRequires:  python-stevedore >= 1.20.0
BuildRequires:  python-testrepository
BuildRequires:  python-testscenarios
BuildRequires:  python-testtools >= 2.2.0
BuildRequires:  python-urllib3 >= 1.21.1
Requires:       python-PrettyTable >= 0.7.1
Requires:       python-PyYAML >= 3.10
Requires:       python-cliff >= 2.8.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-fixtures >= 3.0.0
Requires:       python-jsonschema >= 2.6.0
Requires:       python-netaddr >= 0.7.18
Requires:       python-os-testr
Requires:       python-oslo.concurrency >= 3.25.0
Requires:       python-oslo.config >= 5.1.0
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-paramiko >= 2.0.0
Requires:       python-python-subunit >= 1.0.0
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
Requires:       python-testrepository
Requires:       python-testscenarios
Requires:       python-testtools >= 2.2.0
Requires:       python-urllib3 >= 1.21.1
BuildArch:      noarch

%description
Tempest is a set of integration tests to be run against a live OpenStack
cluster. Tempest has batteries of tests for OpenStack API validation,
Scenarios, and other specific tests useful in validating an OpenStack
deployment.

%package doc
Summary:        Documentation for the OpenStack Integration Test Suite
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description doc
Documentation for the OpenStack Integration Test Suite.

%prep
%autosetup -n %{sname}-%{version}
%py_req_cleanup

%build
%{py2_build}

%install
%{py2_install}

# NOTE(toabctl): config files are installed into usr/etc/
install -d -m 755 %{buildroot}%{_sysconfdir}/tempest
mv %{buildroot}/%{_prefix}/%{_sysconfdir}/%{sname}/accounts.yaml.sample %{buildroot}/%{_sysconfdir}/%{sname}/accounts.yaml
mv %{buildroot}/%{_prefix}/%{_sysconfdir}/%{sname}/logging.conf.sample %{buildroot}/%{_sysconfdir}/%{sname}/logging.conf
mv %{buildroot}/%{_prefix}/%{_sysconfdir}/%{sname}/whitelist.yaml %{buildroot}/%{_sysconfdir}/%{sname}/whitelist.yaml

# generate html docs
PBR_VERSION=%version sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
###rm -rf doc/build/html/.{doctrees,buildinfo}

##%check
##export OS_TEST_PATH=./tempest/tests
##PYTHONPATH=. %{__python2} setup.py testr

%files
%license LICENSE
%doc README.rst ChangeLog
%{python2_sitelib}/tempest
%{python2_sitelib}/*.egg-info
%{_bindir}/tempest
%{_bindir}/verify-tempest-config
%{_bindir}/tempest-account-generator
%{_bindir}/skip-tracker
%{_bindir}/check-uuid
%{_bindir}/subunit-describe-calls
%dir %{_sysconfdir}/tempest
%config(noreplace) %{_sysconfdir}/tempest/logging.conf
%config(noreplace) %{_sysconfdir}/tempest/accounts.yaml
%config(noreplace) %{_sysconfdir}/tempest/whitelist.yaml

%files doc
%license LICENSE
%doc doc/build/html

%changelog
