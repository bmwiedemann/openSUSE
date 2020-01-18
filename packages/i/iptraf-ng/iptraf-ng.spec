#
# spec file for package iptraf-ng
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


Name:           iptraf-ng
Version:        1.1.4
Release:        0
Summary:        TCP/IP Network Monitor
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/iptraf-ng/iptraf-ng/

Source:         https://github.com/iptraf-ng/iptraf-ng/archive/v%version.tar.gz
Patch1:         iptraf-ng-1.1.4-fix-Floating-point-exception-in-tcplog_flowra.patch
Patch2:         build-use-wide-version-of-lpanel-when-needed.patch
Patch3:         0001-ifstats-make-sort-by-ifname-the-only-mode-of-operati.patch
Obsoletes:      iptraf < 4
# Just pick a number that is >3
Provides:       iptraf = 4
BuildRequires:  automake
BuildRequires:  ncurses-devel
BuildRequires:  xz

%description
IPTraf-ng is a console-based network statistics utility. It gathers a
variety of information such as TCP connection packet and byte counts,
interface statistics and activity indicators, TCP/UDP traffic
breakdowns, and LAN station packet and byte counts.

%prep
%autosetup -n %name-%version -p1

%build
if [ ! -e configure ]; then autoreconf -fi; fi
%configure
make %{?_smp_mflags}

%install
%make_install
b="%buildroot"
install -dm 0755 "$b/%_localstatedir/lib/iptraf-ng"
ln -s iptraf-ng "$b/%_sbindir/iptraf"
ln -s iptraf-ng.8 "$b/%_mandir/man8/iptraf.8"

%files
%_sbindir/iptraf*
%_sbindir/rvnamed*
%_mandir/man8/iptraf*
%_mandir/man8/rvnamed*
%_localstatedir/lib/iptraf-ng

%changelog
