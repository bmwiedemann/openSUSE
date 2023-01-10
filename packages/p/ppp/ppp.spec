#
# spec file for package ppp
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2.4.9
Release:        0
Summary:        The Point to Point Protocol for Linux
License:        BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Productivity/Networking/PPP
URL:            https://ppp.samba.org
Source0:        https://download.samba.org/pub/ppp/ppp-%{version}.tar.gz
Source1:        https://download.samba.org/pub/ppp/ppp-%{version}.tar.gz.asc
# templates for secrets
Source2:        pap-secrets.template
Source3:        chap-secrets.template
# config for pam
Source4:        ppp.pamd
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
# PATCH-FEATURE-OPENSUSE ppp-smpppd.patch -- Add more log output for smpppd (move from debug to info log)
Patch0:         ppp-smpppd.patch
# PATCH-FIX-OPENSUSE ppp-pie.patch -- Build position independent code
Patch1:         ppp-pie.patch
# PATCH-FIX-OPENSUSE ppp-lib64.patch -- Install into lib64 on 64bit systems
Patch2:         ppp-lib64.patch
# PATCH-FIX-UPSTREAM ppp-var_run_resolv_conf.patch -- Move resolv.conf to /var/run
Patch3:         ppp-var_run_resolv_conf.patch
# PATCH-FIX-UPSTREAM ppp-fix-bashisms.patch -- Remove bashism from posix shell interpreted script https://github.com/ppp-project/ppp/issues/348
Patch4:         ppp-fix-bashisms.patch
# PATCH-FIX-UPSTREAM ppp-fork-fix.patch -- fix safe_fork to not close needed file descriptors
Patch5:         ppp-fork-fix.patch
# misc tiny stuff
Patch6:         ppp-misc.patch
# PATCH-FIX-UPSTREAM ppp-fork-fix.patch -- fix E: executable-stack (Badness: 10000) /usr/sbin/pppd
Patch7:         ppp-compiling-with-clang-encounters-an-error-in-eap-tls..patch
# Of cause any other compatible libc would work, like musl, but 2.24 required for SOL_NETLINK
BuildRequires:  glibc-devel >= 2.24
BuildRequires:  libpcap-devel
BuildRequires:  linux-atm-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
Requires:       group(%{_group})
Requires(pre):  group(%{_group})

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
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6
%patch7 -p1

%if "%{_lib}" == "lib64"
%patch2 -p1
%endif

sed -i -e '1s/local\///' scripts/secure-card
find scripts -type f | xargs chmod a-x
find -type f -name '*.orig' | xargs rm -f

# Have to patch this in the Makefile, because setting it on the make
# command line only is not enough.
sed -i '/#HAVE_LIBATM/s/#//' pppd/plugins/pppoatm/Makefile.linux

%build
%configure --cflags "%{optflags} -fno-strict-aliasing -fPIC $SP"
%make_build CHAPMS=y CBCP=y HAS_SHADOW=y USE_PAM=y FILTER=y HAVE_INET6=y HAVE_LOGWTMP=y

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
%if 0%{?suse_version} > 1500
install -d 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE4} %{buildroot}%{_pam_vendordir}/ppp
%else
install -d 755 %{buildroot}%{_sysconfdir}/pam.d
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/pam.d/ppp
%endif
install -m 644 %{SOURCE13} %{buildroot}%{_mandir}/man8/pppoe-discovery.8.gz
install -Dm 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/ppp/chatscripts/modem.chat
install -Dm 644 %{SOURCE15} %{buildroot}%{_unitdir}/modem@.service
install -Dm 644 %{SOURCE16} %{buildroot}%{_udevrulesdir}/90-modem.rules

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/ppp ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/ppp ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files
%attr(0750,root,root) %dir %{_sysconfdir}/ppp
%dir %{_sysconfdir}/ppp/peers
%config(noreplace) %{_sysconfdir}/ppp/options
%config(noreplace) %{_sysconfdir}/ppp/filters
%config(noreplace) %{_sysconfdir}/ppp/pap-secrets
%config(noreplace) %{_sysconfdir}/ppp/chap-secrets
%config(noreplace) %{_sysconfdir}/ppp/peers/p*
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/ppp
%else
%config(noreplace) %{_sysconfdir}/pam.d/ppp
%endif
%doc FAQ README* SETUP scripts PLUGINS
%{_mandir}/man?/*.?%{ext_man}
%attr(-,root,%{_group}) %{_sbindir}/pppd
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
