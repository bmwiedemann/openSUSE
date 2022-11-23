#
# spec file for package ipset
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


%define lname	libipset13
%if 0%{?suse_version} && 0%{?suse_version} < 1330
# Factory gets new kernels, old releases don't.
# Always build KMPs for all versions older than Factory.
%define ipset_build_kmp 1
%else
%define ipset_build_kmp 0
%endif
Name:           ipset
Version:        7.16
Release:        0
Summary:        Netfilter ipset administration utility
License:        GPL-2.0-only
Group:          Productivity/Networking/Security
URL:            https://ipset.netfilter.org/
#Git-Clone:	git://git.netfilter.org/ipset
#Git-Web:	http://git.netfilter.org/
Source:         http://ipset.netfilter.org/%name-%version.tar.bz2
Source3:        %name-preamble
Patch1:         ipset-destdir.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  linux-glibc-devel >= 2.6.24
BuildRequires:  pkg-config >= 0.21
BuildRequires:  pkgconfig(libmnl) >= 1
%if 0%{?ipset_build_kmp}
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-devel >= 2.6.39
BuildRequires:  kmod-compat
%kernel_module_package -p %name-preamble
%endif

%description
IP sets are a framework inside the Linux kernel, which can be
administered by the ipset utility. Depending on the type, currently
an IP set may store IP addresses, (TCP/UDP) port numbers or IP
addresses with MAC addresses in a way, which ensures lightning speed
when matching an entry against a set.

ipset can:
* store multiple IP addresses or port numbers and match against the
  collection by iptables in one swoop;
* dynamically update iptables rules against IP addresses or ports
  without performance penalty;
* express complex IP address and ports based rulesets with one single
  iptables rule and benefit from the speed of IP sets

%package KMP
Summary:        Netfilter ipset kernel modules
Group:          System/Kernel

%description KMP
IP sets are a framework inside the Linux kernel, which can be
administered by the ipset utility. Depending on the type, currently
an IP set may store IP addresses, (TCP/UDP) port numbers or IP
addresses with MAC addresses in a way, which ensures lightning speed
when matching an entry against a set.

This package contains a version update to the in-kernel ipset modules.

%package -n %lname
Summary:        Userspace library for the in-kernel Netfilter ipset interface
Group:          System/Libraries

%description -n %lname
IP sets are a framework inside the Linux kernel, which can be
administered by the ipset utility. Depending on the type, currently
an IP set may store IP addresses, (TCP/UDP) port numbers or IP
addresses with MAC addresses in a way, which ensures lightning speed
when matching an entry against a set.

%package devel
Summary:        Development files for ipset extensions
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
IP sets are a framework inside the Linux kernel, which can be
administered by the ipset utility. Depending on the type, currently
an IP set may store IP addresses, (TCP/UDP) port numbers or IP
addresses with MAC addresses in a way, which ensures lightning speed
when matching an entry against a set.

%prep
%autosetup -p1

%build
# build wants to call modinfo at some point
export PATH="$PATH:%_sbindir"
autoreconf -fi
%if 0%{?ipset_build_kmp}
for flavor in %flavors_to_build; do
	cp -a . "../%name-$flavor-%version"
	pushd "../%name-$flavor-%version/"
	# ksource: it just checks for a header
	%configure --disable-static \
		--with-kbuild="%_prefix/src/linux-obj/%_target_cpu/$flavor" \
		--with-ksource="%_prefix/src/linux" \
		--includedir="%_includedir/%name"
	%make_build all modules
	popd
done
%endif
%configure --disable-static --with-kmod=no \
	--includedir="%_includedir/%name"
%make_build

%install
export PATH="$PATH:%_sbindir"
b="%buildroot"
%if 0%{?ipset_build_kmp}
for flavor in %flavors_to_build; do
	pushd "../%name-$flavor-%version/"
	make %{?_smp_mflags} install modules_install \
		DESTDIR="$b" INSTALL_MOD_PATH="$b" V=1
	popd
done
%endif
%make_install
find "$b/%_libdir" -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_sbindir/ipset*
%_mandir/man*/*

%files -n %lname
%_libdir/libipset.so.13*

%files devel
%_libdir/libipset.so
%_libdir/pkgconfig/libipset.pc
%_includedir/%name/

%changelog
