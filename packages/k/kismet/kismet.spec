#
# spec file for package kismet
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define realver 2016-07-R1
Name:           kismet
Version:        2016_07_R1
Release:        0
Summary:        An 802.11 Wireless Network Sniffer
License:        GPL-2.0+
Group:          Productivity/Networking/Diagnostic
Url:            https://www.kismetwireless.net/
Source:         https://www.kismetwireless.net/code/%{name}-%{realver}.tar.xz
Patch0:         kismet-2011-03-R2-makefile.diff
BuildRequires:  ImageMagick-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libexpat-devel
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
BuildRequires:  wget
BuildRequires:  wireshark-devel
BuildRequires:  xz
Requires:       wget
Requires:       wireless-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(libnl-3.0) >= 3.0
%else
BuildRequires:  libnl-devel
%endif

%description
Kismet is an 802.11 wireless network sniffer. This is different from a
normal network sniffer (such as Ethereal or tcpdump) because it
separates and identifies different wireless networks in the area.
Kismet works with any 802.11b wireless card that is capable of
reporting raw packets (rfmon support), which include any Prism2-based
cards (Linksys, D-Link, Rangelan, and more), Cisco Aironet cards, and
Orinoco-based cards. Kismet also supports the WSP100 802.11b remote
sensor by Network Chemistry and is able to monitor 802.11a networks
with cards that use the ar5k chipset.

%prep
%setup -q -n %{name}-%{realver}
%patch0

%build
%if 0%{?suse_version} >= 1220
#This is needed as apcupsd doesn't recognize ppc64 correctly
cp %{_datadir}/automake-*/config.* .
%endif
export CFLAGS="%{optflags} -Wall -fstack-protector -fno-strict-aliasing `ncurses5-config --cflags`"
export CXXFLAGS="%{optflags} -Wall -fstack-protector -fno-strict-aliasing `ncurses5-config --cflags`"
export LDFLAGS="-Wl,--as-needed"
%configure --enable-ipv6 --disable-setuid
make %{?_smp_mflags} dep
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-, root, root)
%doc CHANGELOG README docs/
%{_mandir}/man?/*
%config %{_sysconfdir}/kismet.conf
%config %{_sysconfdir}/kismet_drone.conf
%{_datadir}/kismet
%{_bindir}/*

%changelog
