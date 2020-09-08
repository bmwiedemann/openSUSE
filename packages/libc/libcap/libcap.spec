#
# spec file for package libcap
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


Name:           libcap
Version:        2.43
Release:        0
Summary:        Library for Capabilities (linux-privs) Support
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://sites.google.com/site/fullycapable/
Source:         https://www.kernel.org/pub/linux/libs/security/linux-privs/libcap2/libcap-%{version}.tar.xz
Source2:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  glibc-devel-static
BuildRequires:  pkgconfig

%description
Capabilities are a measure to limit the omnipotence of the superuser.
Currently a program started by root or setuid root has the power to do
anything. Capabilities (Linux-Privs) provide a more fine-grained access
control. Without kernel patches, you can use this library to drop
capabilities within setuid binaries. If you use patches, this can be
done automatically by the kernel.

%package -n libcap2
Summary:        Library for Capabilities (linux-privs) Support
Group:          System/Libraries

%description -n libcap2
Capabilities are a measure to limit the omnipotence of the superuser.
Currently a program started by root or setuid root has the power to do
anything. Capabilities (Linux-Privs) provide a more fine-grained access
control. Without kernel patches, you can use this library to drop
capabilities within setuid binaries. If you use patches, this can be
done automatically by the kernel.

%package devel
Summary:        Development files for libcap
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcap2 = %{version}

%description devel
Development files (Headers, libraries for static linking, etc) for
libcap.

libcap is a library for getting and setting POSIX.1e (formerly POSIX 6)
draft 15 capabilities.

Install libcap-devel if you want to develop or compile applications
using libcap.

%package progs
Summary:        Libcap utility programs
Group:          System/Filesystems

%description progs
This package contains utility programs handling capabilities via
libcap.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
make prefix=%{_prefix} lib=%{_lib} LIBDIR=%{_libdir} SBINDIR=%{_sbindir} \
     INCDIR=%{_includedir} MANDIR=%{_mandir} DYNAMIC=yes DEBUG="-g %{optflags}"

%install
make install RAISE_SETFCAP=no \
             DESTDIR=%{buildroot} \
             LIBDIR=/%{_libdir} \
             SBINDIR=/%{_sbindir} \
             INCDIR=/%{_includedir} \
             MANDIR=/%{_mandir}/ \
             PKGCONFIGDIR=%{_libdir}/pkgconfig/
find %{buildroot} -type f -name "*.la" -delete -print
# do not provide static libs
rm %{buildroot}%{_libdir}/libcap.a

%fdupes -s %{buildroot}

%check
make test

%post -n libcap2 -p /sbin/ldconfig
%postun -n libcap2 -p /sbin/ldconfig

%files -n libcap2
%license License
%{_libdir}/libcap.so.*

%files progs
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_sbindir}/*

%files devel
%license License
%doc README CHANGELOG
%{_includedir}/sys/capability.h
%{_includedir}/sys/psx_syscall.h
%{_libdir}/*.so
%{_libdir}/libpsx.a
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/libpsx.pc
%{_mandir}/man3/*

%changelog
