#
# spec file for package python
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


%global sname aci-integration-module
%define skip_python3 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{sname}
Version:        0.14.3
Release:        0
Summary:        Python library for programming ACI
License:        Apache-2.0
URL:            https://github.com/noironetworks/aci-integration-module
Source:         https://github.com/noironetworks/aci-integration-module/archive/%{version}.tar.gz
BuildRequires:  %{python_module acitoolkit >= 0.3.2}
BuildRequires:  %{python_module apicapi}
BuildRequires:  %{python_module click >= 3.3}
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oslo.concurrency}
BuildRequires:  %{python_module oslo.config}
BuildRequires:  %{python_module oslo.db}
BuildRequires:  %{python_module oslo.log}
BuildRequires:  %{python_module oslo.messaging}
BuildRequires:  %{python_module oslo.utils}
BuildRequires:  %{python_module oslotest >= 1.10.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module python-subunit >= 0.0.18}
BuildRequires:  %{python_module semantic_version}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tabulate >= 0.7.5}
BuildRequires:  %{python_module websocket-client}
BuildRequires:  fdupes
BuildRequires:  logrotate
BuildRequires:  python-rpm-macros
Requires:       logrotate
Requires:       python-acitoolkit >= 0.3.2
Requires:       python-alembic
Requires:       python-apicapi
Requires:       python-click >= 3.3
Requires:       python-jsonschema
Requires:       python-kubernetes
Requires:       python-oslo.concurrency
Requires:       python-oslo.config
Requires:       python-oslo.db
Requires:       python-oslo.log
Requires:       python-oslo.messaging
Requires:       python-oslo.utils
Requires:       python-semantic_version
Requires:       python-tabulate >= 0.7.5
Requires:       python-websocket-client
BuildArch:      noarch
%python_subpackages

%description
Module to bring together libraries and tools for integrating ACI with cloud.

%prep
%setup -q -n %{sname}-%{version}

%build
export PBR_VERSION=%{version}
%python_build

%install
export PBR_VERSION=%{version}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -p -D -m 0644 rpm/aim-aid.service %{buildroot}/%{_unitdir}/aim-aid.service
install -p -D -m 0644 rpm/aim-event-service-polling.service %{buildroot}/%{_unitdir}/aim-event-service-polling.service
install -p -D -m 0644 rpm/aim-event-service-rpc.service %{buildroot}/%{_unitdir}/aim-event-service-rpc.service
mkdir -p %{buildroot}/run/aid/events
# Install logrotate
install -p -D -m 0644 etc/logrotate.d/aim %{buildroot}%{_sysconfdir}/logrotate.d/aim

# Remove unused files
%python_expand rm -rf %{buildroot}%{$python_sitelib}/aim/tests

# Move files to the expected locations
mv %{buildroot}%{_prefix}%{_sysconfdir}/aim/  %{buildroot}%{_sysconfdir}

%check
export LANG=en_US.UTF-8
# TODO: unfortunatly the tests require runing APIC server
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m subunit.run discover

%pre
%service_add_pre aim-aid.service aim-event-service-polling.service aim-event-service-rpc.service

%post
%service_add_post aim-aid.service aim-event-service-polling.service aim-event-service-rpc.service

%preun
%service_del_preun aim-aid.service aim-event-service-polling.service aim-event-service-rpc.service

%postun
%service_del_postun aim-aid.service aim-event-service-polling.service aim-event-service-rpc.service

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/aim
%{python_sitelib}/aci_integration_module-*.egg-info
%{_bindir}/aimctl
%{_bindir}/aimdebug
%{_bindir}/aim-aid
%{_bindir}/aim-event-service-polling
%{_bindir}/aim-event-service-rpc
%{_bindir}/aim-http-server
%config(noreplace) %{_sysconfdir}/aim/aim.conf
%config(noreplace) %{_sysconfdir}/aim/aimctl.conf
%{_unitdir}/aim-aid.service
%{_unitdir}/aim-event-service-polling.service
%{_unitdir}/aim-event-service-rpc.service
%ghost /run/aid
%ghost /run/aid/events
%dir %{_sysconfdir}/aim
%config(noreplace) %{_sysconfdir}/logrotate.d/*

%changelog
