#
# spec file for package liburing
#
# Copyright (c) 2023 SUSE LLC
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


%define lname   liburing2
Name:           liburing
Version:        2.3
Release:        0
Summary:        Linux-native io_uring I/O access library
License:        (GPL-2.0-only AND LGPL-2.1-or-later) OR MIT
Group:          Development/Libraries/C and C++
URL:            https://git.kernel.dk/cgit/liburing
Source:         https://git.kernel.dk/cgit/liburing/snapshot/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM: fix tests on big endian
Patch1:         0001-test-helpers-fix-socket-length-type.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  procps
# Kernel part has landed in 5.1
Conflicts:      kernel < 5.1

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package -n %{lname}
Summary:        Linux-native io_uring I/O access library
Group:          Development/Libraries/C and C++

%description -n %{lname}
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary:        Development files for Linux-native io_uring I/O access library
Group:          Development/Libraries/C and C++
# SLE/Leap 15.4+ retain liburing-devel for the inherited 0.6 API. The v2 API is:
Provides:       %{lname}-devel = %{version}
Requires:       %{lname} = %{version}
Requires:       pkgconfig

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%autosetup -p1

%build
# not autotools, so configure macro doesn't work
sh ./configure --prefix=%{_prefix} \
            --includedir=%{_includedir} \
            --libdir=/%{_libdir} \
            --libdevdir=/%{_libdir} \
            --mandir=%{_mandir} \
            --datadir=%{_datadir}
%make_build -C src

%check
# io_uring syscalls not supported as of qemu 7.0.0 and would test the host
# kernel anyway not the target kernel..
%if !0%{?qemu_user_space_build}
/usr/bin/make runtests
%endif

%install
%make_install
rm -v %{buildroot}%{_libdir}/%{name}.a

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/liburing.so.*
%license COPYING COPYING.GPL LICENSE

%files devel
%doc README
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
