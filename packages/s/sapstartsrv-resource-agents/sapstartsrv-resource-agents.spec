#
# spec file for package sapstartsrv-resource-agents
#
# Copyright (c) 2020-2025 SUSE LLC.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/

%if 0%{?suse_version} < 1600
%bcond_with test
%else
%bcond_without test
%endif

Name:           sapstartsrv-resource-agents
License:        GPL-2.0
Group:          Productivity/Clustering/HA
Summary:        Resource agent for SAP instance specific sapstartsrv service
Version:        0.9.4+git.1739992536.298b1ce
Release:        0
URL:            https://github.com/SUSE/SAPStartSrv-resourceAgent
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  resource-agents
Requires:       resource-agents
Requires:       pacemaker > 1.1.1
Requires:       python3
Requires:       python3-psutil
Recommends:     supportutils-plugin-ha-sap
%if %{with test}
BuildRequires:  python3-pytest
BuildRequires:  python3-psutil
%endif

%define raname SAPStartSrv
%define srvname sapservices-move
%define ocf_dir %{_prefix}/lib/ocf

%description
This is a resource agent for the instance specific SAP start framework.
It controls the instance specific sapstartsrv process which provides the
API to start, stop and check an SAP instance.

Authors:
--------
    Fabian Herschel
    Lars Pinne
    Xabier Arbulu

%prep
%setup -q

%build
gzip man/*

%install
install -D -m 0755 ra/%{raname}.in %{buildroot}%{ocf_dir}/resource.d/suse/%{raname}
install -d %{buildroot}%{_mandir}/man7
install -d %{buildroot}%{_mandir}/man8
install -m 0444 man/*.7.gz %{buildroot}%{_mandir}/man7
install -m 0444 man/*.8.gz %{buildroot}%{_mandir}/man8
install -D -m 0644 sbin/%{srvname}.in %{buildroot}%{_sbindir}/%{srvname}
install -d %{buildroot}%{_unitdir}
install -m 0644 service/* %{buildroot}%{_unitdir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcsapping
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcsappong

sed -i 's+@PYTHON@+%{_bindir}/python3+' %{buildroot}%{ocf_dir}/resource.d/suse/%{raname}
sed -i 's+@PYTHON@+%{_bindir}/python3+' %{buildroot}%{_sbindir}/%{srvname}

%if %{with test}
%check
pytest tests
%endif

%pre
%service_add_pre sapping.service sappong.service

%post
%service_add_post sapping.service sappong.service

%preun
%service_del_preun sapping.service sappong.service

%postun
%service_del_postun sapping.service sappong.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_mandir}/man7/*.7.gz
%{_mandir}/man8/*.8.gz
%dir %{ocf_dir}
%dir %{ocf_dir}/resource.d
%dir %{ocf_dir}/resource.d/suse
%defattr(755,root,root,-)
%{ocf_dir}/resource.d/suse/%{raname}
%{_sbindir}/*
%defattr(644,root,root,-)
%{_unitdir}/*

%changelog
