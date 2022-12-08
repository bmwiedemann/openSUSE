#
# spec file for package hmcfgusb
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Andreas Vetter
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


%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           hmcfgusb
Version:        0.103+git23.g7157286
Release:        0
Summary:        Hmland and utilities to use the HM-CFG-USB(2)
License:        MIT AND SUSE-Public-Domain
Group:          System/Monitoring
URL:            https://git.zerfleddert.de/cgi-bin/gitweb.cgi/hmcfgusb
Source:         %{name}-%{version}.tar.gz
Source1:        hmland.service
Source2:        sysconfig.hmland
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkgconfig(systemd)
Requires:       logrotate
Requires(pre):  %fillup_prereq

%description
This package contains, amongst others, hmland an application, which emulates the
HomeMatic LAN configuration adapter-protocol to make it possible to use the
HM-CFG-USB in Fhem or as a lan configuration tool for the CCU or the
HomeMatic windows configuration software, also supporting devices using
AES-signing like KeyMatic.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 flash-hmcfgusb  %{buildroot}%{_bindir}
install -m 755 flash-hmmoduart %{buildroot}%{_bindir}
install -m 755 flash-ota       %{buildroot}%{_bindir}
install -m 755 hmsniff         %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_sbindir}
install -m 755 hmland          %{buildroot}%{_sbindir}

install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 debian/hmland.logrotate  %{buildroot}%{_sysconfdir}/logrotate.d/hmland

mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %{_sourcedir}/sysconfig.hmland %{buildroot}%{_fillupdir}/sysconfig.hmland
install -D -m 0644 %{_sourcedir}/hmland.service %{buildroot}/%{_unitdir}/hmland.service
ln -s service %{buildroot}%{_sbindir}/rchmland

%pre
%service_add_pre hmland.service

%post
%service_add_post hmland.service
%{fillup_only -ans hmland}

%preun
%service_del_preun hmland.service

%postun
%service_del_postun hmland.service

%files
%defattr (-,root,root,755)
%config /%{_sysconfdir}/logrotate.d/hmland
%{_bindir}/flash-hmcfgusb
%{_bindir}/flash-hmmoduart
%{_bindir}/flash-ota
%{_bindir}/hmsniff
%{_sbindir}/hmland
%{_sbindir}/rchmland
%{_fillupdir}/sysconfig.hmland
%{_unitdir}/hmland.service
%doc README.md debian/changelog
%license LICENSE

%changelog
