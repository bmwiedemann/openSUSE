#
# spec file for package ppp
#
# Copyright (c) 2020 SUSE LLC
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


%define _group dialout
Name:           ppp
Version:        2.4.7
Release:        0
Summary:        The Point to Point Protocol for Linux
License:        BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Networking/PPP
URL:            https://ppp.samba.org
Source0:        https://download.samba.org/pub/%{name}/%{name}-%{version}.tar.gz
# config for pam
Source1:        ppp.pamd
# templates for secrets
Source2:        pap-secrets.template
Source3:        chap-secrets.template
# options and filters files
Source5:        options
Source6:        filters
# several peers file
Source7:        modem-peers
Source8:        pppoe-peers
Source9:        pppoe-rp-peers
Source10:       pppoatm-peers
Source11:       ppp-peers
Source12:       pptp-peers
Source13:       pppoe-discovery.8.gz
# modem files
Source14:       modem.chat
Source15:       modem@.service
Source16:       modem.rules
# https://www.kernel.org/doc/wot/paulus.html
Source17:       %{name}.keyring
Source18:       https://download.samba.org/pub/%{name}/%{name}-%{version}.tar.gz.asc
# Makefile changes
Patch0:         ppp-2.4.6-make.diff
# replacedefaultroute option
Patch2:         ppp-2.4.2-cifdefroute.diff
# misc tiny stuff
Patch3:         ppp-2.4.6-misc.diff
# more log output for smpppd
Patch4:         ppp-2.4.2-smpppd.diff
# allow higher serial speeds
Patch5:         ppp-2.4.1-higher-speeds.diff
# fixed use of libpcap including dial on demand
Patch6:         ppp-2.4.3-filter.diff
# option to rename ppp interface
Patch8:         ppp-2.4.6-ifname.diff
# Don't use __P from glibc (pppd uses it wrong)
Patch9:         ppp-2.4.2-__P.diff
Patch10:        ppp-2.4.3-pppoatm.diff
Patch11:        ppp-2.4.7-fix-bashisms.patch
Patch12:        ppp-2.4.2-pie.patch
Patch14:        ppp-2.4.3-fork-fix.diff
Patch17:        ppp-2.4.3-strip.diff
Patch18:        ppp-2.4.3-winbind-setuidfix.patch
Patch19:        ppp-2.4.4-strncatfix.patch
Patch21:        ppp-2.4.6-lib64.patch
Patch22:        ppp-2.4.4-var_run_resolv_conf.patch
Patch23:        ppp-send-padt.patch
# PATCH-FIX-UPSTREAM -- Patch for CVE-2015-3310
Patch24:        ppp-CVE-2015-3310.patch
Patch25:        fix-header-conflict.patch
Patch26:        ppp-2.4.7-DES-openssl.patch
Patch27:        ppp-CVE-2020-8597.patch
BuildRequires:  libpcap-devel
BuildRequires:  linux-atm-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
%if 0%{?suse_version} >= 1330
Requires:       group(%{_group})
Requires(pre):  group(%{_group})
%else
Requires(pre):  shadow
%endif

%description
The ppp package contains the PPP (Point-to-Point Protocol) daemon,
pppd, additional PPP utilities, documentation, and sample files. PPP
provides a method for transmitting IP and IPX datagrams over serial
point-to-point links, for example over a modem. The PPP daemon handles
the details of setting up a PPP link including configuring the network
interface and performing the PPP negotiations.

%package devel
Summary:        Header Files Required for Developing Plugins for pppd
Group:          Development/Libraries/C and C++
Requires:       ppp = %{version}

%description devel
The package ppp-devel contains C header files required for developing
plugins for the pppd.

%package modem
Summary:        Automatic redial for any USB modem supported by the kernel
Group:          System/Kernel
Requires:       ppp
Requires:       udev
Requires:       group(dialout)
BuildArch:      noarch

%description modem
This package contains peer, chat script, systemd unit and udev rule for
automatic redial when connecting any USB modem supported by the kernel.
For disable automatic redial (by default enabled for all), run
sudo systemctl mask modem@0.service
For enable again automatic redial, run
sudo systemctl unmask modem@0.service
"0" after "@" is the serial number of the modem, if you have more than one,
you can disable unnecessary or disable everything.

%prep
%setup -q
%patch0
%patch2
%patch3
%patch4
%patch5
%patch6 -p1
%patch8
%patch9
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch14
%patch17
%patch18
%patch19 -p1
%if %{_lib} == lib64
%patch21
%endif
%patch22
%patch23 -p1
%patch24
%patch25 -p1
%patch26 -p1
%patch27
sed -i -e '1s/local\///' scripts/secure-card
find scripts -type f | xargs chmod a-x
find -type f -name '*.orig' | xargs rm -f

# Have to patch this in the Makefile, because setting it on the make
# command line only is not enough.
sed -i '/#HAVE_LIBATM/s/#//' pppd/plugins/pppoatm/Makefile.linux

%build
export MY_CFLAGS="%{optflags} -fno-strict-aliasing -fPIC $SP"
%configure
make %{?_smp_mflags} CHAPMS=y CBCP=y HAS_SHADOW=y USE_PAM=y FILTER=y HAVE_INET6=y HAVE_LOGWTMP=y

%install
make install DESTDIR=%{buildroot}%{_prefix}
install -dm 750 %{buildroot}%{_sysconfdir}/ppp
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/ppp/options
install -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/ppp/filters
install -m 600 %{SOURCE2} %{buildroot}%{_sysconfdir}/ppp/pap-secrets
install -m 600 %{SOURCE3} %{buildroot}%{_sysconfdir}/ppp/chap-secrets
install -d 755 %{buildroot}%{_sysconfdir}/ppp/peers
install -m 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/ppp/peers/modem
install -m 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/ppp/peers/pppoe
install -m 644 %{SOURCE9} %{buildroot}%{_sysconfdir}/ppp/peers/pppoe-rp
%ifnarch mips s390 s390x
install -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/ppp/peers/pppoatm
%endif
install -m 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/ppp/peers/ppp
install -m 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/ppp/peers/pptp
install -d 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/ppp
install -m 644 %{SOURCE13} %{buildroot}%{_mandir}/man8/pppoe-discovery.8.gz
install -Dm 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/ppp/chatscripts/modem.chat
install -Dm 644 %{SOURCE15} %{buildroot}%{_unitdir}/modem@.service
install -Dm 644 %{SOURCE16} %{buildroot}%{_udevrulesdir}/90-modem.rules

%if 0%{?suse_version} < 1330
%pre
getent group %{_group} >/dev/null || %{_sbindir}/groupadd -r %{_group}
%endif

%files
%attr(750, root, root) %dir %{_sysconfdir}/ppp
%dir %{_sysconfdir}/ppp/peers
%config(noreplace) %{_sysconfdir}/ppp/options
%config(noreplace) %{_sysconfdir}/ppp/filters
%config(noreplace) %{_sysconfdir}/ppp/pap-secrets
%config(noreplace) %{_sysconfdir}/ppp/chap-secrets
%config(noreplace) %{_sysconfdir}/ppp/peers/p*
%config(noreplace) %{_sysconfdir}/pam.d/ppp
%doc FAQ README* SETUP scripts PLUGINS
%{_mandir}/man?/*.?%{ext_man}
%attr (-, root, dialout) %{_sbindir}/pppd
%{_sbindir}/chat
%{_sbindir}/pppdump
%{_sbindir}/pppstats
%{_sbindir}/pppoe-discovery
%dir %{_libdir}/pppd
%dir %{_libdir}/pppd/%{version}
%attr(0755,root,root) %{_libdir}/pppd/%{version}/*.so

%files devel
%{_includedir}/pppd

%files modem
%dir %{_sysconfdir}/ppp/peers
%config(noreplace) %{_sysconfdir}/ppp/peers/modem
%dir %{_sysconfdir}/ppp/chatscripts
%config(noreplace) %{_sysconfdir}/ppp/chatscripts/modem.chat
%{_unitdir}/modem@.service
%dir %{_udevrulesdir}
%{_udevrulesdir}/90-modem.rules

%changelog
