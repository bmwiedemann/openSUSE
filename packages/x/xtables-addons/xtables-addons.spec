#
# spec file for package xtables-addons
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


Name:           xtables-addons
Version:        3.11
Release:        0
Summary:        IP Packet Filter Administration Extensions
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://xtables-addons.sf.net/

#Git-Clone:	git://git.inai.de/xtables-addons
Source:         https://inai.de/files/%name/%name-%version.tar.xz
Source2:        https://inai.de/files/%name/%name-%version.tar.asc
Source3:        %name-preamble
Source4:        %name.keyring
BuildRequires:  %kernel_module_package_buildreqs
BuildRequires:  kernel-syms >= 4.15
BuildRequires:  pkg-config >= 0.21
BuildRequires:  xz
BuildRequires:  pkgconfig(xtables) >= 1.6.0
Requires:       perl(Getopt::Long)
Requires:       perl(Net::CIDR::Lite)
Requires:       perl(Socket)
Requires:       perl(Text::CSV_XS)
Requires:       perl(strict)
Requires:       perl(warnings)
Recommends:     %name-kmp
Recommends:     xtables-geoip

%define xtlibdir %(pkg-config xtables --variable=xtlibdir)

%kernel_module_package -p %name-preamble

%description
Xtables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.

Xtables-addons is the successor to patch-o-matic(-ng). Likewise, it
contains extensions that were not, or are not yet, accepted in the
main kernel/iptables packages.

%package KMP
Summary:        IP Packet Filter Administration Extensions
Group:          System/Kernel

%description KMP
Xtables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.

Xtables-addons is the successor to patch-o-matic(-ng). Likewise, it
contains extensions that were not, or are not yet, accepted in the
main kernel/iptables packages.

%prep
%autosetup -p1

%build
pushd ../
for flavor in %flavors_to_build; do
	cp -a "%name-%version" "%name-$flavor-%version"
	pushd "%name-$flavor-%version/"
	%configure --with-kbuild="/usr/src/linux-obj/%_target_cpu/$flavor"
	make %{?linux_make_arch} %{?_smp_mflags} V=1
	popd
done

%install
b="%buildroot"
pushd ../
for flavor in %flavors_to_build; do
	pushd "%name-$flavor-%version/"
	make %{?linux_make_arch} install DESTDIR="$b"
	popd
done
# There is no -devel package. So no need for these files.
find "$b/%_prefix" -iname "*.la" -delete
find "$b/%_libdir" -maxdepth 1 -type l -iname "*.so" -delete

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%_bindir/xt_geoip_fetch
%_mandir/man*/*
%_sbindir/*
%_libdir/*.so.*
%xtlibdir/
%_libexecdir/xtables-addons/
%license LICENSE

%changelog
