#
# spec file for package sapstartsrv-resource-agents
#
# Copyright (c) 2020 SUSE LLC.
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

%if 0%{?suse_version} < 1500
%bcond_with test
%else
%bcond_without test
%endif

Name:           sapstartsrv-resource-agents
License:        GPL-2.0
Group:          Productivity/Clustering/HA
AutoReqProv:    on
Summary:        Resource agent for SAP instance specific sapstartsrv service
Version:        0.9.0+git.1617199081.815e7ba
Release:        0
Url:            https://github.com/SUSE/SAPStartSrv-resourceAgent

BuildArch:      noarch

Source0:        %{name}-%{version}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       pacemaker > 1.1.1
Requires:       resource-agents
Requires:       python3
BuildRequires:  resource-agents
%if %{with test}
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
%endif

%define raname SAPStartSrv
%define srvname sapservices-move
%define ocf_dir /usr/lib/ocf

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
mkdir -p %{buildroot}%{ocf_dir}/resource.d/suse
mkdir -p %{buildroot}%{_mandir}/man7
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}

install -m 0755 ra/%{raname}.in %{buildroot}%{ocf_dir}/resource.d/suse/%{raname}
install -m 0444 man/*.7.gz %{buildroot}%{_mandir}/man7
install -m 0444 man/*.8.gz %{buildroot}%{_mandir}/man8
install -m 0644 sbin/%{srvname}.in %{buildroot}%{_sbindir}/%{srvname}
install -m 0644 service/* %{buildroot}%{_unitdir}
sed -i 's+@PYTHON@+%{_bindir}/python3+' %{buildroot}%{ocf_dir}/resource.d/suse/%{raname}
sed -i 's+@PYTHON@+%{_bindir}/python3+' %{buildroot}%{_sbindir}/%{srvname}

%if %{with test}
%check
pytest tests
%endif

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_mandir}/man7/*.7.gz
%{_mandir}/man8/*.8.gz
%dir %{ocf_dir}
%dir %{ocf_dir}/resource.d
%defattr(755,root,root,-)
%dir %{ocf_dir}/resource.d/suse
%{_sbindir}*
%{ocf_dir}/resource.d/suse/*
%defattr(644,root,root,-)
%{_unitdir}/*

%changelog
