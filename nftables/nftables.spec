#
# spec file for package nftables
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


Name:           nftables
Version:        0.9.0
Release:        0
Summary:        Userspace utility to access the nf_tables packet filter
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
Url:            http://netfilter.org/projects/nftables/

#Git-Clone:	git://git.netfilter.org/nftables
Source:         http://ftp.netfilter.org/pub/nftables/nftables-%version.tar.bz2
Source2:        http://ftp.netfilter.org/pub/nftables/nftables-%version.tar.bz2.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  docbook2x
BuildRequires:  flex
BuildRequires:  gmp-devel
BuildRequires:  pkg-config >= 0.21
BuildRequires:  readline-devel
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(libmnl) >= 1.0.3
BuildRequires:  pkgconfig(libnftnl) >= 1.1.1
BuildRequires:  pkgconfig(xtables) >= 1.6.1

%description
nf_tables is a firewalling mechanism in the Linux kernel, running
independently of, and thus parallel to, ip_tables, ip6_tables,
arp_tables and ebtables. nftables is the corresponsing userspace
frontend.

nftables features support for sets and dictionaries of arbitrary
types, support for different protocols, meta data types, access to
connection tracking and NAT, logging, atomic incremental and full
ruleset updates.

%package -n libnftables0
Summary:        nftables firewalling command interface
Group:          System/Libraries

%description -n libnftables0
libnftables is the nftables command line interface placed into a
library.

%package devel
Summary:        Development files for the nftables command line interface
Group:          Development/Libraries/C and C++
Requires:       libnftables0 = %version

%description devel
libnftables is the nftables command line interface placed into a
library.

This package contains the header files for the library.

%prep
%setup -q

%build
mkdir bin
ln -s "%_bindir/docbook-to-man" bin/docbook2x-man
export PATH="$PATH:$PWD/bin"
mkdir obj
pushd obj/
%define _configure ../configure
%configure --disable-silent-rules --disable-static --docdir="%_docdir/%name" \
	--includedir="%_includedir/%name"
make %{?_smp_mflags}
popd

%install
b="%buildroot"
%make_install -C obj
rm -f "%buildroot/%_libdir"/*.la
mkdir -p "$b/%_docdir/%name/examples"
mv "$b/%_sysconfdir/nftables"/* "$b/%_docdir/%name/examples/"

%post   -n libnftables0 -p /sbin/ldconfig
%postun -n libnftables0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%_sbindir/nft
%_mandir/man8/nft*
%_docdir/%name/

%files -n libnftables0
%_libdir/libnftables.so.*

%files devel
%_includedir/%name/
%_libdir/libnftables.so
%_libdir/pkgconfig/*.pc

%changelog
