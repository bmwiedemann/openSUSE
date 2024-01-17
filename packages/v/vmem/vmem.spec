#
# spec file for package vmem
#
# Copyright (c) 2020 SUSE LLC
# Copyright 2016, Intel Corporation
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

Name:           vmem
Version:        1.8
Release:        0
Summary:        Malloc-like volatile allocations
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://pmem.io/vmem/

Source:         https://github.com/pmem/vmem/archive/%version.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  man
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
The Persistent Memory Development Kit is a collection of libraries for
using memory-mapped persistence, optimized specifically for persistent memory.

%package -n libvmem1
Summary:        Volatile Memory allocation library
Group:          System/Libraries

%description -n libvmem1
The libvmem library turns a pool of persistent memory into a volatile
memory pool, similar to the system heap but kept separate and with
its own malloc-style API.

%package -n libvmem-devel
Summary:        Development files for the Volatile allocation library
Group:          Development/Libraries/C and C++
Requires:       libvmem1 = %version

%description -n libvmem-devel
The libvmem library turns a pool of persistent memory into a volatile
memory pool, similar to the system heap but kept separate and with
its own malloc-style API.

This subpackage contains libraries and header files for developing
applications that want to make use of libvmem.

%package -n libvmmalloc1
Summary:        Dynamic to Persistent Memory allocation translation library
Group:          System/Libraries

%description -n libvmmalloc1
The libvmmalloc library transparently converts all the dynamic memory
allocations into persistent memory allocations. This allows the use
of persistent memory as volatile memory without modifying the target
application.

The typical usage of libvmmalloc is to load it via the LD_PRELOAD
environment variable.

%package -n libvmmalloc-devel
Summary:        Development files for the Dynamic-to-Persistent allocation library
Group:          Development/Libraries/C and C++
Requires:       libvmmalloc1 = %version

%description -n libvmmalloc-devel
The libvmmalloc library transparently converts all the dynamic memory
allocations into persistent memory allocations. This allows the use
of persistent memory as volatile memory without modifying the target
application.

This subpackage contains libraries and header files for developing
applications that want to specifically make use of libvmmalloc.

%prep
%setup -q

%build
%define _lto_cflags %{nil}
# Currently, NVML makefiles do not allow to easily override CFLAGS,
# so the build flags are passed via EXTRA_CFLAGS.  For debug build
# selected flags are overriden to disable compiler optimizations.
#
# remaining issues:
# * jemalloc attempts to use __builtin_clz, this might not always work
export CFLAGS="%{optflags}"
make %{?_smp_mflags} NORPATH=1

# Override LIB_AR with empty string to skip installation of static libraries
%install
make install DESTDIR="%buildroot" LIB_AR="" \
	prefix="%_prefix" \
	libdir="%_libdir" \
	includedir="%_includedir" \
	mandir="%_mandir" \
	bindir="%_bindir" \
	sysconfdir="%_sysconfdir" \
	docdir="%_docdir" NORPATH=1
%fdupes %buildroot/%_prefix


%post   -n libvmem1 -p /sbin/ldconfig
%postun -n libvmem1 -p /sbin/ldconfig
%post   -n libvmmalloc1 -p /sbin/ldconfig
%postun -n libvmmalloc1 -p /sbin/ldconfig

%files -n libvmem1
%defattr(-,root,root)
%_libdir/libvmem.so.1*
%license LICENSE

%files -n libvmem-devel
%defattr(-,root,root)
%_libdir/libvmem.so
%_libdir/pkgconfig/libvmem.pc
%dir %_libdir/vmem_debug/
%_libdir/vmem_debug/libvmem.so*
%_includedir/libvmem.h
%{_mandir}/man7/libvmem.7.gz
%{_mandir}/man3/vmem_*.3.gz

%files -n libvmmalloc1
%defattr(-,root,root)
%_libdir/libvmmalloc.so.1*
%license LICENSE

%files -n libvmmalloc-devel
%defattr(-,root,root)
%_libdir/libvmmalloc.so
%_libdir/pkgconfig/libvmmalloc.pc
%dir %_libdir/vmem_debug/
%_libdir/vmem_debug/libvmmalloc.so*
%_includedir/libvmmalloc.h
%{_mandir}/man7/libvmmalloc.7.gz

%changelog
