#
# spec file for package python-oslo.messaging
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


Name:           python-oslo.messaging
Version:        14.8.0
Release:        0
Summary:        OpenStack oslo.messaging library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.messaging
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.messaging/oslo.messaging-14.8.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python3-PyYAML >= 3.13
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-amqp >= 2.5.2
BuildRequires:  python3-cachetools >= 2.0.0
BuildRequires:  python3-confluent-kafka
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-futurist >= 1.2.0
BuildRequires:  python3-greenlet
BuildRequires:  python3-kombu >= 4.6.6
BuildRequires:  python3-monotonic
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.metrics >= 0.2.1
BuildRequires:  python3-oslo.middleware >= 3.31.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.service >= 1.24.0
BuildRequires:  python3-oslo.utils >= 3.37.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pyngus
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
BuildArch:      noarch

%description
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.

%package -n python3-oslo.messaging
Summary:        OpenStack oslo.messaging library
Requires:       python3-PyYAML >= 3.13
Requires:       python3-WebOb >= 1.7.1
Requires:       python3-amqp >= 2.5.2
Requires:       python3-cachetools >= 2.0.0
Requires:       python3-debtcollector >= 1.2.0
Requires:       python3-futurist >= 1.2.0
Requires:       python3-greenlet
Requires:       python3-kombu >= 4.6.6
Requires:       python3-oslo.config >= 5.2.0
Requires:       python3-oslo.i18n
Requires:       python3-oslo.log >= 3.36.0
Requires:       python3-oslo.metrics >= 0.2.1
Requires:       python3-oslo.middleware >= 3.31.0
Requires:       python3-oslo.serialization >= 2.18.0
Requires:       python3-oslo.service >= 1.24.0
Requires:       python3-oslo.utils >= 3.37.0
Requires:       python3-stevedore >= 1.20.0
%if 0%{?suse_version}
Obsoletes:      python2-oslo.messaging < 12.0.0
%endif

%description -n python3-oslo.messaging
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.

This package contains the Python 3.x module.

%package -n python3-oslo.messaging-doc
Summary:        Documentation for OpenStack messaging library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-oslo.messaging-doc
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.messaging-14.8.0
%py_req_cleanup

%build
%py3_build

# generate html docs
PYTHONPATH=. PBR_VERSION=%{version} %sphinx_build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%py3_install

%check
# NOTE(jpena): we do not want to run functional tests, just unit tests
# python3-pifpaf is not available in RDO, but loading functional tests would
# fail without it
rm -rf oslo_messaging/tests/functional
# 3 cyrus tests fail on rdo with time out
%{openstack_stestr_run} --exclude-regex '^oslo_messaging.tests.(functional|drivers.test_amqp_driver.TestCyrusAuthentication.test_authentication_(ok|ignore_default_realm|default_realm))'

%files -n python3-oslo.messaging
%license LICENSE
%doc README.rst ChangeLog
%{python3_sitelib}/oslo_messaging
%{python3_sitelib}/*.egg-info
%{_bindir}/oslo-messaging-send-notification

%files -n python3-oslo.messaging-doc
%license LICENSE
%doc doc/build/html

%changelog
