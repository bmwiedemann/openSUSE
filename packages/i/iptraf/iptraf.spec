#
# spec file for package iptraf
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           iptraf
Version:        1.1.4
Release:        0
Summary:        TCP/IP Network Monitor
License:        GPL-2.0+
Group:          Productivity/Networking/Diagnostic
Url:            https://fedorahosted.org/iptraf-ng/

#Git-Clone:	git://git.fedorahosted.org/git/iptraf-ng
#DL-URL:	http://fedorahosted.org/releases/i/p/iptraf-ng/iptraf-ng-%version.tar.gz
Source:         %name-ng-%version.tar.xz
Patch1:         iptraf-ng-1.1.4-fix-Floating-point-exception-in-tcplog_flowra.patch
Patch2:         build-use-wide-version-of-lpanel-when-needed.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ncurses-devel
BuildRequires:  xz

%description
IPTraf-ng is a console-based network statistics utility. It gathers a
variety of information such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic
breakdowns, and LAN station packet and byte counts.

%package ng
# 2010-04: We really want to have a iptraf-ng binrpm so that Obsoletes can
# easily work (and make the user somewhat aware of the change by seeing a
# new install in zypper). puzel wanted to keep the iptraf name in OBS however,
# so we now have this nifty construct with an empty main package.
Summary:        TCP/IP Network Monitor
Group:          Productivity/Networking/Diagnostic
# Just pick a number that is >3
Provides:       iptraf = 4
Obsoletes:      iptraf < 4

%description ng
IPTraf-ng is a console-based network statistics utility. It gathers a
variety of information such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic
breakdowns, and LAN station packet and byte counts.

%prep
%setup -qn %name-ng-%version
%patch1 -p1
%patch2 -p1

%build
%configure
make %{?_smp_mflags};

%install
b="%buildroot";
make install DESTDIR="$b";
install -dm 0755 "$b/%_localstatedir/lib/iptraf-ng";
ln -s iptraf-ng "$b/%_sbindir/iptraf";
ln -s iptraf-ng.8 "$b/%_mandir/man8/iptraf.8";

%files ng
%defattr(-,root,root)
%_sbindir/iptraf*
%_sbindir/rvnamed*
%_mandir/man8/iptraf*
%_mandir/man8/rvnamed*
%_localstatedir/lib/iptraf-ng

%changelog
