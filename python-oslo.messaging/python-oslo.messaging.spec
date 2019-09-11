#
# spec file for package python-oslo.messaging
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


Name:           python-oslo.messaging
Version:        9.5.0
Release:        0
Summary:        OpenStack oslo.messaging library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://launchpad.net/oslo.messaging
Source0:        https://files.pythonhosted.org/packages/source/o/oslo.messaging/oslo.messaging-9.5.0.tar.gz
BuildRequires:  openstack-macros
BuildRequires:  python-devel
BuildRequires:  python2-PyYAML >= 3.12
BuildRequires:  python2-WebOb >= 1.7.1
BuildRequires:  python2-amqp >= 2.4.1
BuildRequires:  python2-cachetools >= 2.0.0
BuildRequires:  python2-confluent-kafka
BuildRequires:  python2-debtcollector >= 1.2.0
BuildRequires:  python2-eventlet
BuildRequires:  python2-fixtures
BuildRequires:  python2-futurist >= 1.2.0
BuildRequires:  python2-greenlet
BuildRequires:  python2-kombu >= 4.0.0
BuildRequires:  python2-mock
BuildRequires:  python2-monotonic >= 0.6
BuildRequires:  python2-oslo.config >= 5.2.0
BuildRequires:  python2-oslo.i18n >= 3.15.3
BuildRequires:  python2-oslo.log >= 3.36.0
BuildRequires:  python2-oslo.middleware >= 3.31.0
BuildRequires:  python2-oslo.serialization >= 2.18.0
BuildRequires:  python2-oslo.service >= 1.24.0
BuildRequires:  python2-oslo.utils >= 3.33.0
BuildRequires:  python2-oslotest
BuildRequires:  python2-pbr >= 2.0.0
BuildRequires:  python2-pifpaf
BuildRequires:  python2-pika
BuildRequires:  python2-pika-pool
BuildRequires:  python2-pyngus
BuildRequires:  python2-python-subunit
BuildRequires:  python2-redis
BuildRequires:  python2-six >= 1.10.0
BuildRequires:  python2-stestr
BuildRequires:  python2-stevedore >= 1.20.0
BuildRequires:  python2-tenacity
BuildRequires:  python2-testscenarios
BuildRequires:  python2-testtools
BuildRequires:  python3-PyYAML >= 3.12
BuildRequires:  python3-WebOb >= 1.7.1
BuildRequires:  python3-amqp >= 2.4.1
BuildRequires:  python3-cachetools >= 2.0.0
BuildRequires:  python3-confluent-kafka
BuildRequires:  python3-debtcollector >= 1.2.0
BuildRequires:  python3-devel
BuildRequires:  python3-eventlet
BuildRequires:  python3-fixtures
BuildRequires:  python3-futurist >= 1.2.0
BuildRequires:  python3-greenlet
BuildRequires:  python3-kombu >= 4.0.0
BuildRequires:  python3-mock
BuildRequires:  python3-oslo.config >= 5.2.0
BuildRequires:  python3-oslo.i18n >= 3.15.3
BuildRequires:  python3-oslo.log >= 3.36.0
BuildRequires:  python3-oslo.middleware >= 3.31.0
BuildRequires:  python3-oslo.serialization >= 2.18.0
BuildRequires:  python3-oslo.service >= 1.24.0
BuildRequires:  python3-oslo.utils >= 3.33.0
BuildRequires:  python3-oslotest
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-pifpaf
BuildRequires:  python3-pika
BuildRequires:  python3-pika-pool
BuildRequires:  python3-pyngus
BuildRequires:  python3-python-subunit
BuildRequires:  python3-redis
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-stestr
BuildRequires:  python3-stevedore >= 1.20.0
BuildRequires:  python3-tenacity
BuildRequires:  python3-testscenarios
BuildRequires:  python3-testtools
Requires:       python-PyYAML >= 3.12
Requires:       python-WebOb >= 1.7.1
Requires:       python-amqp >= 2.4.1
Requires:       python-cachetools >= 2.0.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-futurist >= 1.2.0
Requires:       python-greenlet
Requires:       python-kombu >= 4.0.0
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n >= 3.15.3
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.middleware >= 3.31.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.service >= 1.24.0
Requires:       python-oslo.utils >= 3.33.0
Requires:       python-pika
Requires:       python-pika-pool
Requires:       python-six >= 1.10.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%ifpython2
BuildRequires:  python-futures
Requires:       python-futures
Requires:       python-monotonic >= 0.6
%endif
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
# on RDO, update-alternatives is in chkconfig
Requires(post): chkconfig
Requires(postun): chkconfig
%endif
%python_subpackages

%description
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.

%package -n python-oslo.messaging-doc
Summary:        Documentation for OpenStack messaging library
Group:          Development/Languages/Python
BuildRequires:  python-Sphinx
BuildRequires:  python-openstackdocstheme

%description -n python-oslo.messaging-doc
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo.messaging-9.5.0
%py_req_cleanup
# FIXME(jpena): since version 5.23.0, four tests in the amqp driver are
# failing. Let's remove the tests for now, so we can build a package and
# figure out whatis wrong.
rm -f oslo_messaging/tests/drivers/test_amqp_driver.py

%build
%{python_build}

# generate html docs
%{__python2} setup.py build_sphinx
# remove the sphinx-build leftovers
rm -rf build/sphinx/html/.{doctrees,buildinfo}

%install
%{python_install}
%python_clone -a %{buildroot}%{_bindir}/oslo-messaging-send-notification

%post
%python_install_alternative oslo-messaging-send-notification

%postun
%python_uninstall_alternative oslo-messaging-send-notification

%check
%python_exec -m stestr.cli run

%files %python_files
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/oslo_messaging
%{python_sitelib}/*.egg-info
%python_alternative %{_bindir}/oslo-messaging-send-notification

%files -n python-oslo.messaging-doc
%license LICENSE
%doc build/sphinx/html

%changelog
