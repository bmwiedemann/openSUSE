#
# spec file for package python-oslo.messaging
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        17.1.0
Release:        0
Summary:        OpenStack oslo.messaging library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://docs.openstack.org/oslo.messaging
Source0:        https://files.pythonhosted.org/packages/source/o/oslo_messaging/oslo_messaging-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.13}
BuildRequires:  %{python_module WebOb >= 1.7.1}
BuildRequires:  %{python_module amqp >= 2.5.2}
BuildRequires:  %{python_module cachetools >= 2.0.0}
BuildRequires:  %{python_module confluent-kafka}
BuildRequires:  %{python_module debtcollector >= 1.2.0}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module futurist >= 1.2.0}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module kombu >= 4.6.6}
BuildRequires:  %{python_module oslo.config >= 5.2.0}
BuildRequires:  %{python_module oslo.i18n}
BuildRequires:  %{python_module oslo.log >= 3.36.0}
BuildRequires:  %{python_module oslo.metrics >= 0.2.1}
BuildRequires:  %{python_module oslo.middleware >= 3.31.0}
BuildRequires:  %{python_module oslo.serialization >= 2.18.0}
BuildRequires:  %{python_module oslo.service >= 1.24.0}
BuildRequires:  %{python_module oslo.utils >= 3.37.0}
BuildRequires:  %{python_module oslotest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module stestr}
BuildRequires:  %{python_module stevedore >= 1.20.0}
BuildRequires:  %{python_module testscenarios}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  openstack-macros
Requires:       python-PyYAML >= 3.13
Requires:       python-WebOb >= 1.7.1
Requires:       python-amqp >= 2.5.2
Requires:       python-cachetools >= 2.0.0
Requires:       python-debtcollector >= 1.2.0
Requires:       python-futurist >= 1.2.0
Requires:       python-greenlet
Requires:       python-kombu >= 4.6.6
Requires:       python-oslo.config >= 5.2.0
Requires:       python-oslo.i18n
Requires:       python-oslo.log >= 3.36.0
Requires:       python-oslo.metrics >= 0.2.1
Requires:       python-oslo.middleware >= 3.31.0
Requires:       python-oslo.serialization >= 2.18.0
Requires:       python-oslo.service >= 1.24.0
Requires:       python-oslo.utils >= 3.37.0
Requires:       python-stevedore >= 1.20.0
BuildArch:      noarch
%if "python%{python_nodots_ver}" == "%{primary_python}"
Obsoletes:      python3-oslo.messaging < %{version}
%else
Conflicts:      python3-oslo.messaging < %{version}
%endif
%python_subpackages

%description
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.

%package -n python3-oslo.messaging-doc
Summary:        Documentation for OpenStack messaging library
BuildRequires:  python3-Sphinx
BuildRequires:  python3-openstackdocstheme

%description -n python3-oslo.messaging-doc
The Oslo messaging API supports RPC and notifications over a number
of different messaging transports.
This package contains the documentation.

%prep
%autosetup -p1 -n oslo_messaging-%{version}

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=. PBR_VERSION=%{version} sphinx-build -b html doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/oslo-messaging-send-notification

%pre
%python_libalternatives_reset_alternative oslo-messaging-send-notification

%post
%python_install_alternative oslo-messaging-send-notification

%postun
%python_uninstall_alternative oslo-messaging-send-notification

%check
rm -rf oslo_messaging/tests/functional
# 3 cyrus tests fail on rdo with time out
%{openstack_stestr_run} --exclude-regex '^oslo_messaging.tests.(functional|drivers.test_amqp_driver.TestCyrusAuthentication.test_authentication_(ok|ignore_default_realm|default_realm))'

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/oslo-messaging-send-notification
%{python_sitelib}/oslo_messaging
%{python_sitelib}/oslo_messaging-%{version}.dist-info

%files -n python3-oslo.messaging-doc
%license LICENSE
%doc doc/build/html

%changelog
