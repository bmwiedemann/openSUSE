#
# spec file for package netdiscover
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define 				pkgver 0.3-pre-beta7
Name:           netdiscover
Version:        0.3_beta7
Release:        0
Summary:        A network address discovering/monitoring tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
Url:            https://sourceforge.net/projects/netdiscover/?source=directory
Source0:        https://sourceforge.net/projects/netdiscover/files/netdiscover/%{pkgver}-LINUXONLY/netdiscover-%{pkgver}-LINUXONLY.tar.gz
# PATCH-FIX-OPENSUSE netdiscover-update-oui.patch -- alows us updating oui
# database from hwdata
Patch0:         netdiscover-update-oui.patch
# Patches from debian
Patch1:         netdiscover-fix-makefile.patch
Patch2:         netdiscover-fix-spelling-binary.patch
Patch3:         netdiscover-fix-manpage.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  hwdata
BuildRequires:  libnet-devel
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
%setup -q -n netdiscover-%{pkgver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoreconf -fiv
%configure
cp %{_datadir}/hwdata/oui.txt ./
sh update-oui-database.sh
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc

%files
%license COPYING
%doc ChangeLog README AUTHORS NEWS TODO
%{_sbindir}/netdiscover
%{_mandir}/man8/netdiscover.8%{ext_man}

%changelog
