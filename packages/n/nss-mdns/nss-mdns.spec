#
# spec file for package nss-mdns
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


Name:           nss-mdns
Version:        0.15.1
Release:        0
Summary:        Host Name Resolution Via Multicast DNS (Zeroconf) for glibc
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/lathiat/nss-mdns
Source0:        https://github.com/lathiat/nss-mdns/releases/download/v%{version}/nss-mdns-%{version}.tar.gz
Source1:        nss-mdns-config
Source2:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(check)
Requires:       avahi
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         grep
# needed by nss-mdns-config
PreReq:         sed

%description
nss-mdns is a plug-in for the GNU Name Service Switch (NSS)
functionality of the GNU C Library (glibc) providing a hostname
resolution via Multicast DNS (aka Zeroconf, aka Apple Rendezvous, aka
Apple Bonjour), and effectively allowing name resolution by common
Unix/Linux programs in the ad-hoc mDNS domain .local.

nss-mdns provides only client functionality, which means that you have
to run a mDNS responder daemon separately from nss-mdns if you want to
register the local hostname via mDNS. I recommend Avahi.

By default, nss-mdns tries to contact a running avahi-daemon to resolve
hostnames and addresses and makes use of its superior record cacheing.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
install -D -m0755 %{SOURCE1} %{buildroot}%{_sbindir}/nss-mdns-config

%check
make %{?_smp_mflags} check || (cat ./test-suite.log; false)

%post
/sbin/ldconfig
if [ "$1" -eq 1 ] ; then
    # Only enable on first install, to not overwrite changes done by users
    nss-mdns-config --enable
fi

%preun
if [ "$1" -eq 0 ] ; then
    # Completely disable when not upgrading (ie, fully uninstalling)
    nss-mdns-config --disable
fi

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md NEWS.md ACKNOWLEDGEMENTS.md
%{_sbindir}/nss-mdns-config
%{_libdir}/libnss_mdns.so.2
%{_libdir}/libnss_mdns_minimal.so.2
%{_libdir}/libnss_mdns4.so.2
%{_libdir}/libnss_mdns4_minimal.so.2
%{_libdir}/libnss_mdns6.so.2
%{_libdir}/libnss_mdns6_minimal.so.2

%changelog
