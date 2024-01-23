#
# spec file for package arpwatch
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           arpwatch
Version:        3.6
Release:        0
Summary:        Tool to keep track of Ethernet<->IP address pairings
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://ee.lbl.gov/nrg.html
Source:         https://ee.lbl.gov/downloads/arpwatch/%{name}-%{version}.tar.gz
Source10:       arpwatch@.service
Source11:       sysconfig.arpwatch
Source12:       arpwatch.service
Patch0:         arpwatch-2.1a11-chrootbuild.diff
Patch1:         arpwatch-no-source-zero.dif
Patch2:         arpwatch.ETHERCODES.patch
Patch5:         arpwatch-2.1a11-drop-privs-manpage.dif
Patch6:         arpwatch-2.1a11-drop-privs.dif
# PATCH-Fix-Upstream -- https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=625796#20 -- seife+obs@b1-systems.com
Patch10:        0001-Ignore-802.1Q-frames.patch
Patch11:        report-iface.patch
Patch13:        arpwatch-exit.patch
Patch14:        arp2ethers.patch
Patch15:        arpwatch-3.4-include-time.patch
BuildRequires:  libpcap-devel
BuildRequires:  postfix
BuildRequires:  systemd-rpm-macros
Requires:       arpwatch-ethercodes
Requires(post): %fillup_prereq
Requires(post): coreutils

%description
Arpwatch keeps track of Ethernet and IP address pairings. It logs
activity to syslog and reports certain changes via e-mail.

%package ethercodes-build
Summary:        Tool to create ethercodes.dat from IEEE.org meta data
Group:          Productivity/Networking/Diagnostic

%description ethercodes-build
Tool and required files to create the ethercodes.dat file from the OUI
and company ID data as provided by IEEE.org.  This package is only
needed if you want to build the arpwatch-ethercodes package.

%prep
%autosetup -p1

%build
%configure
%make_build \
	ARPDIR=%{_localstatedir}/lib/arpwatch \
	ETHERCODES=%{_datadir}/arpwatch/ethercodes.dat \
	%{nil}

%install
mkdir -p \
    %{buildroot}/%{_tmpfilesdir} \
    %{buildroot}/%{_sbindir} \
    %{buildroot}/%{_datadir}/arpwatch \
    %{buildroot}/%{_mandir}/man8 \
    %{buildroot}%{_fillupdir}
%make_install
# ethercodes.dat is in the arpwatch-ethercodes package
rm -f %{buildroot}/%{_datadir}/arpwatch/ethercodes.dat
for file in euppertolower.awk duplicates.awk p.awk; do
	cp -p ${file} %{buildroot}/%{_datadir}/arpwatch
done
install -Dm 0644 %{SOURCE10} %{buildroot}/%{_unitdir}/arpwatch@.service
install -Dm 0644 %{SOURCE12} %{buildroot}/%{_unitdir}/arpwatch.service
ln -s service %{buildroot}%{_sbindir}/rcarpwatch
install -Dm 0644 %{SOURCE11} \
    %{buildroot}%{_fillupdir}/sysconfig.arpwatch
# own the database files
cat > %{buildroot}%{_tmpfilesdir}/arpwatch.conf <<EOF
# See tmpfiles.d(5) for details
d %{_localstatedir}/lib/arpwatch - - - -
f %{_localstatedir}/lib/arpwatch/arp.dat - - - -
EOF
mkdir %{buildroot}%{_bindir}
install -m 0755 arp2ethers %{buildroot}%{_bindir}

%pre
%service_add_pre arpwatch.service

%preun
%service_del_preun arpwatch.service

%post
%fillup_only
%tmpfiles_create %{_tmpfilesdir}/arpwatch.conf
%service_add_post arpwatch.service

%postun
%service_del_postun arpwatch.service

%files
%{_unitdir}/arpwatch.service
%{_unitdir}/arpwatch@.service
%{_tmpfilesdir}/arpwatch.conf
%{_sbindir}/rcarpwatch
%{_sbindir}/arpsnmp
%{_sbindir}/arpwatch
%{_bindir}/arp2ethers
%ghost %dir %{_localstatedir}/lib/arpwatch
%ghost %{_localstatedir}/lib/arpwatch/arp.dat
%{_fillupdir}/sysconfig.arpwatch
%{_mandir}/man8/arpsnmp.8%{?ext_man}
%{_mandir}/man8/arpwatch.8%{?ext_man}
%doc CHANGES FILES README

%files ethercodes-build
%{_datadir}/arpwatch

%changelog
