#
# spec file for package netdiscover
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


Name:           netdiscover
Version:        0.10
Release:        0
Summary:        A network address discovering/monitoring tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/netdiscover-scanner/netdiscover
Source0:        https://github.com/netdiscover-scanner/netdiscover/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  hwdata
BuildRequires:  libnet-devel >= 1.1.2
BuildRequires:  libpcap-devel

%description
Netdiscover is an active/passive address reconnaissance tool, mainly developed
for those wireless networks without dhcp server, when you are wardriving. It
can be also used on hub/switched networks.

Built on top of libnet and libpcap, it can passively detect online hosts, or
search for them, by actively sending arp requests, it can also be used to
inspect your network arp traffic, and find network addresses using auto scan
mode, which will scan for common local networks.

%prep
%autosetup

%build
autoreconf -fiv
%configure
cp -p %{_datadir}/hwdata/oui.txt ./oui.txt-$(date +%Y%m%d)
sh update-oui-database.sh --no-download
%make_build

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc ChangeLog README AUTHORS NEWS TODO
%{_sbindir}/netdiscover
%{_mandir}/man8/netdiscover.8%{?ext_man}

%changelog
