#
# spec file for package grubby
#
# Copyright (c) 2021 SUSE LLC
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


Name:           grubby
Version:        20200210.99d10a3
Release:        0
Summary:        Command line tool for updating bootloader configs
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/rhboot/grubby
Source0:        %{name}-%{version}.tar.xz
# for make test / getopt:
BuildRequires:  grub2
BuildRequires:  pkgconfig
BuildRequires:  util-linux
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(popt)
%ifarch s390 s390x
Requires:       s390-tools
%endif
%ifarch %{arm}
Requires:       u-boot-tools
%endif

%description
grubby is a command line tool for updating and displaying information about
the configuration files for the grub, lilo, elilo (ia64), yaboot (powerpc)
and zipl (s390) boot loaders. It is primarily designed to be used from scripts
which install new kernels and need to find information about the current boot
environment.

%prep
%autosetup -p1

%build
sed -i~ '
/^LDFLAGS/d
/^CFLAGS/d
/^grubby_LIBS/d
/^VERBOSE_TEST/d
' Makefile
diff -u "$_"~ "$_" && exit 1
CFLAGS="%{optflags} -std=gnu99 $(pkg-config --cflags blkid popt)"
LDFLAGS=
grubby_LIBS="$(pkg-config --libs blkid popt)"
%make_build CFLAGS="${CFLAGS}" LDFLAGS="${LDFLAGS}" grubby_LIBS="${grubby_LIBS}" VERSION='%{version}'

%check
%ifnarch aarch64
sed -i~ '
s@/vmlinuz-foo@/boot/vmlinuz-foo@
' test/results/add/g2-1.16
diff -u "$_"~ "$_" && exit 1
%make_build test VERBOSE_TEST="-b grub2"
%endif

%install
make install DESTDIR=%{buildroot} mandir="%{_mandir}"
# Remove installkernel as it is provided with mkinitrd package
rm %{buildroot}/sbin/installkernel
rm %{buildroot}/%{_mandir}/man8/installkernel.8

%files
%license COPYING
/sbin/new-kernel-pkg
/sbin/grubby
%{_mandir}/man8/*.8%{?ext_man}

%changelog
