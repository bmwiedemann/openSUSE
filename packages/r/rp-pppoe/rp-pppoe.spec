#
# spec file for package rp-pppoe
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


%define _name pppoe
%define _group dialout
Name:           rp-%{_name}
Version:        3.13
Release:        0
Summary:        A PPP Over Ethernet Redirector for PPPD
License:        GPL-2.0-or-later
Group:          Productivity/Networking/PPP
URL:            https://dianne.skoll.ca/projects/%{name}
Source0:        https://dianne.skoll.ca/projects/%{name}/download/%{name}-%{version}.tar.gz
Source1:        %{_name}-connect
Source2:        %{_name}-setup
Source3:        %{_name}-start
Source4:        %{_name}-status
Source5:        %{_name}-stop
Source6:        %{_name}.service
Source7:        %{_name}-server.service
Patch0:         docdir.diff
Patch1:         nonrfc-modems.diff
Patch2:         release-buildsystem.diff
Patch3:         resolve-conf.diff
Patch4:         %{name}-3.10-config.patch
Patch5:         %{name}-3.10-init.patch
Patch6:         %{name}-pie.patch
Patch7:         strip.diff
BuildRequires:  pkgconfig
BuildRequires:  ppp
BuildRequires:  pkgconfig(systemd)
Requires:       net-tools
Requires:       ppp
Requires(post): permissions
%if 0%{?suse_version} >= 1330
Requires:       group(%{_group})
Requires(pre):  group(%{_group})
%else
Requires(pre):  shadow
%endif

%description
%{name} is a user-space redirector which permits the use of PPPoE
(Point-to-Point Protocol Over Ethernet) with Linux. PPPoE is used by
many ADSL service providers.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1
%patch6
%patch7

%build
cd src
%configure
make %{?_smp_mflags}
cd ../gui
make %{?_smp_mflags}

%install
%make_install -C src
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_unitdir}
install -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE3} %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}
install -m 0755 %{SOURCE5} %{buildroot}%{_sbindir}
install -m 0644 %{SOURCE6} %{buildroot}%{_unitdir}/%{_name}.service
install -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/%{_name}-server.service
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{_name}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{_name}-server
ln -sf %{_name}-stop %{buildroot}%{_sbindir}/adsl-stop
ln -sf %{_name}-start %{buildroot}%{_sbindir}/adsl-start
rm -rf %{buildroot}%{_sysconfdir}/ppp/%{_name}.conf \
       %{buildroot}%{_sysconfdir}/rc.d/init.d/%{_name} \
       %{buildroot}%{_initddir}
%make_install -C gui
install -d  %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{_sysconfdir}/ppp/plugins/README %{buildroot}%{_defaultdocdir}/%{name}/README.plugins
rm -r %{buildroot}%{_sysconfdir}/ppp/plugins %{buildroot}%{_defaultdocdir}/%{name}/LICENSE

%pre
%if 0%{?suse_version} < 1330
getent group %{_group} >/dev/null || %{_sbindir}/groupadd -r %{_group}
%endif
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
%defattr(0644,root,root,-)
%license doc/LICENSE
%dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}/*
%attr(0750,root,root) %config(noreplace) %{_sysconfdir}/ppp/firewall-*
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/ppp/%{_name}-server-options
%attr(0755,root,root) %{_bindir}/tkpppoe
%attr(0755,root,root) %{_sbindir}/%{_name}
%attr(0755,root,root) %{_sbindir}/%{_name}-{c,r,s}*
%attr(4750,root,dialout) %{_sbindir}/%{_name}-wrapper
%{_mandir}/man?/*%{?ext_man}
%{_sbindir}/adsl-st*
%{_sbindir}/rc%{_name}
%{_sbindir}/rc%{_name}-server
%{_unitdir}/%{_name}.service
%{_unitdir}/%{_name}-server.service
%dir %{_sysconfdir}/ppp/%{name}-gui
%dir %{_datarootdir}/tk%{_name}
%{_datarootdir}/tk%{_name}/?*.{html,msg,png}
%verify(not mode caps) %attr(4750,root,dialout) %{_sbindir}/%{_name}-wrapper

%changelog
