#
# spec file for package pptpd
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


Name:           pptpd
Version:        1.4.0
Release:        0
Summary:        PoPToP - PPTP Daemon, Linux as Microsoft VPN Server
License:        GPL-2.0-or-later
Group:          Productivity/Networking/PPP
URL:            https://www.poptop.org/
Source:         https://downloads.sourceforge.net/project/poptop/pptpd/pptpd-%{version}/pptpd-%{version}.tar.gz
Source3:        pptp-install.tar.bz2
Source4:        pptpd.conf
Source5:        options.ppp0
Source7:        README.SUSE
Source9:        pptpd.service
Patch0:         makefile.diff
Patch1:         pptpd-cflags.patch
Patch2:         ppp-2.5.0.patch
Patch3:         pptpd-stringcompare.patch
Patch4:         bcrelay-iflog-size-limit.patch
Patch5:         gcc-14-fix.patch
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  ppp-devel
BuildRequires:  pkgconfig(udev)
Requires:       ppp
%{?systemd_ordering}

%description
PoPToP is a PPTP(Point-to-Point Tunneling Protocol) server solution for
Linux, it allows Linux servers to function seamlessly in the PPTP VPN
environment. This release supports Windows 95/98/NT/2000 PPTP clients
and PPTP Linux clients.

%prep
%setup -q -a 3
%patch -P 0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3
%patch -P 4 -p1
%patch -P 5 -p1
rm plugins/patchlevel.h
cp -p %{SOURCE5} %{SOURCE7} .

%build
autoreconf -i -f
%configure
%make_build OPTFLAGS="%{optflags}"

%install
%make_install
install -m 0755 pptpd			%{buildroot}%{_sbindir}/pptpd
install -m 0755 pptpctrl		%{buildroot}%{_sbindir}/pptpctrl

install -D -m 0644 %{SOURCE9} %{buildroot}%{_unitdir}/`basename %{SOURCE9}`
mkdir -p %{buildroot}%{_modulesloaddir}
echo "ppp_mppe" > %{buildroot}%{_prefix}/lib/modules-load.d/pptpd.conf
install -Dm 0644 %{SOURCE4}			%{buildroot}%{_sysconfdir}/pptpd.conf
find {samples,PPTP-Installation,pptp-server} -type f -exec chmod -x {} +
chmod -x AUTHORS COPYING ChangeLog INSTALL NEWS README* TODO

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc README.SUSE options.ppp0
%doc ChangeLog NEWS README* TODO
%doc samples PPTP-Installation pptp-server
%config %{_sysconfdir}/pptpd.conf
%{_mandir}/*/pptp*
%{_mandir}/man8/bcrelay.8%{?ext_man}
%{_sbindir}/pptpctrl
%{_sbindir}/pptpd
%{_sbindir}/bcrelay
%{_prefix}/lib/pptpd
%{_unitdir}/%{name}.service
%{_modulesloaddir}/pptpd.conf

%changelog
