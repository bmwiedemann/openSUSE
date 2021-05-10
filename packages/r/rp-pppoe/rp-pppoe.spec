#
# spec file for package rp-pppoe
#
# Copyright (c) 2021 SUSE LLC
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


%define _name pppoe
%define _group dialout
Name:           rp-%{_name}
Version:        3.15
Release:        0
Summary:        A PPP Over Ethernet Redirector for PPPD
License:        GPL-2.0-or-later
URL:            https://dianne.skoll.ca/projects/%{name}
Source0:        https://dianne.skoll.ca/projects/%{name}/download/%{name}-%{version}.tar.gz
Source1:        %{_name}-connect
Source2:        %{_name}-setup
Source3:        %{_name}-start
Source4:        %{_name}-status
Source5:        %{_name}-stop
Source6:        %{_name}.service
Source7:        %{_name}-server.service
Patch0:         %{name}-3.14-docdir.patch
Patch1:         %{name}-3.14-nonrfc-modems.patch
Patch2:         %{name}-3.14-release-buildsystem.patch
Patch3:         %{name}-3.14-resolve-conf.patch
Patch4:         %{name}-3.14-config.patch
Patch5:         %{name}-3.14-init.patch
Patch6:         %{name}-3.14-pie.patch
Patch7:         %{name}-3.14-strip.patch
BuildRequires:  pkgconfig
BuildRequires:  ppp
BuildRequires:  pkgconfig(systemd)
Requires:       group(%{_group})
Requires:       iproute2
Requires:       ppp
Requires(post): permissions
Requires(pre):  group(%{_group})

%description
%{name} is a user-space redirector which permits the use of PPPoE
(Point-to-Point Protocol Over Ethernet) with Linux. PPPoE is used by
many ADSL service providers.

%prep
%autosetup -p1

%build
cd src
%configure
%make_build
cd ../gui
%make_build

%install
%make_install -C src
%make_install -C gui
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_unitdir}
install -p %{SOURCE1} %{buildroot}%{_sbindir}
install -p %{SOURCE2} %{buildroot}%{_sbindir}
install -p %{SOURCE3} %{buildroot}%{_sbindir}
install -p %{SOURCE4} %{buildroot}%{_sbindir}
install -p %{SOURCE5} %{buildroot}%{_sbindir}
install -pm0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{_name}.service
install -pm0644 %{SOURCE7} %{buildroot}%{_unitdir}/%{_name}-server.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{_name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{_name}-server
ln -s %{_name}-stop %{buildroot}%{_sbindir}/adsl-stop
ln -s %{_name}-start %{buildroot}%{_sbindir}/adsl-start
install -Dpm0644 %{buildroot}%{_sysconfdir}/ppp/plugins/README %{buildroot}%{_defaultdocdir}/%{name}/README.plugins
rm -r %{buildroot}%{_initddir} \
      %{buildroot}%{_sysconfdir}/ppp/plugins \
      %{buildroot}%{_sysconfdir}/ppp/%{_name}.conf \
      %{buildroot}%{_defaultdocdir}/%{name}/LICENSE

%pre
%service_add_pre %{_name}.service
%service_add_pre %{_name}-server.service

%preun
%service_del_preun %{_name}.service
%service_del_preun %{_name}-server.service

%post
%service_add_post %{_name}.service
%service_add_post %{_name}-server.service
%set_permissions %{_sbindir}/%{_name}-wrapper

%postun
%service_del_postun %{_name}.service
%service_del_postun %{_name}-server.service

%verifyscript
%verify_permissions -e %{_sbindir}/%{_name}-wrapper

%files
%license doc/LICENSE
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/ppp/firewall-*
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/ppp/%{_name}-server-options
%{_bindir}/tkpppoe
%{_sbindir}/%{_name}
%{_sbindir}/%{_name}-*
%attr(4750,root,%{_group}) %{_sbindir}/%{_name}-wrapper
%{_mandir}/man?/*%{?ext_man}
%{_sbindir}/adsl-st*
%{_sbindir}/rc%{_name}
%{_sbindir}/rc%{_name}-server
%{_unitdir}/%{_name}.service
%{_unitdir}/%{_name}-server.service
%dir %{_sysconfdir}/ppp/%{name}-gui
%dir %{_datarootdir}/tk%{_name}
%{_datarootdir}/tk%{_name}/*
%verify(not mode caps) %attr(4750,root,%{_group}) %{_sbindir}/%{_name}-wrapper

%changelog
