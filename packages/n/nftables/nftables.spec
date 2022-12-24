#
# spec file for package nftables
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


Name:           nftables
Version:        1.0.6
Release:        0
Summary:        Userspace utility to access the nf_tables packet filter
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/nftables/

#Git-Clone:	git://git.netfilter.org/nftables
Source:         http://ftp.netfilter.org/pub/%name/%name-%version.tar.xz
Source2:        http://ftp.netfilter.org/pub/%name/%name-%version.tar.xz.sig
Source3:        %name.keyring
BuildRequires:  asciidoc
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.21
BuildRequires:  python3-base
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libmnl) >= 1.0.4
BuildRequires:  pkgconfig(libnftnl) >= 1.2.4
BuildRequires:  pkgconfig(xtables) >= 1.6.1

%description
nf_tables is a firewalling mechanism in the Linux kernel, running
independently of and parallel to ip_tables, ip6_tables,
arp_tables and ebtables. nftables is the corresponsing userspace
frontend.

The nftables frontend features support for sets and dictionaries of arbitrary
types, meta data types, atomic incremental and full ruleset updates, and,
similar to iptables, support for different protocols, access to connection
tracking and NAT and logging.

%package -n libnftables1
Summary:        nftables firewalling command interface
Group:          System/Libraries

%description -n libnftables1
libnftables is the nftables command line interface placed into a
library.

%package devel
Summary:        Development files for the nftables command line interface
Group:          Development/Libraries/C and C++
Requires:       libnftables1 = %version

%description devel
libnftables is the nftables command line interface placed into a
library.

This package contains the header files for the library.

%package -n python3-nftables
Summary:        Python interface for nftables
Group:          Development/Languages/Python

%description -n python3-nftables
A Python module for nftables.

%prep
%autosetup -p1

%build
autoreconf -fi
mkdir bin
ln -s "%_bindir/docbook-to-man" bin/docbook2x-man
export PATH="$PATH:$PWD/bin"
mkdir obj
pushd obj/
%define _configure ../configure
%configure --disable-silent-rules --disable-static --docdir="%_docdir/%name" \
	--includedir="%_includedir/%name" --with-json \
	--enable-python --with-python-bin="$(which python3)"
%make_build
popd

%install
b="%buildroot"
%make_install -C obj
rm -f "%buildroot/%_libdir"/*.la
mkdir -p "$b/%_docdir/%name/examples"
mv -v "$b/%_datadir/nftables"/*.nft "$b/%_docdir/%name/examples/"

%post   -n libnftables1 -p /sbin/ldconfig
%postun -n libnftables1 -p /sbin/ldconfig

%files
%license COPYING
%_sysconfdir/nftables/
%_sbindir/nft
%_mandir/man5/*.5*
%_mandir/man8/nft*
%_docdir/%name/

%files -n libnftables1
%_libdir/libnftables.so.1*

%files devel
%_includedir/%name/
%_libdir/libnftables.so
%_libdir/pkgconfig/*.pc
%_mandir/man3/*.3*

%files -n python3-nftables
%python3_sitelib/nftables*

%changelog
