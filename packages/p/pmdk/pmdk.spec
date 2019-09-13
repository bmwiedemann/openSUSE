#
# spec file for package pmdk
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{suse_version} > 1315
%define with_fabric 1
%endif

%define min_libfabric_ver 1.4.2
%define min_ndctl_ver 60.1

Name:           pmdk
Version:        1.6
Release:        0
Summary:        Persistent Memory Development Kit
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://pmem.io/pmdk/

Source:         https://github.com/pmem/pmdk/archive/%version.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  man
BuildRequires:  pkg-config
%if 0%{?with_fabric}
BuildRequires:  libfabric-devel >= %min_libfabric_ver
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# NVML was renamed upstream to PMDK between 1.3 and 1.3.1
Obsoletes:      nvml < %version-%release
Provides:       nvml = %version-%release
BuildRequires:  libndctl-devel >= %{min_ndctl_ver}

# By design, NVML does not support any 32-bit architecture.
# Due to dependency on xmmintrin.h and some inline assembly, it can be
# compiled only for x86_64 at the moment.
# Other 64-bit architectures could also be supported, if only there is
# a request for that, and if somebody provides the arch-specific
# implementation of the low-level routines for flushing to persistent
# memory.
ExclusiveArch:  x86_64

# Debug variants of the libraries should be filtered out of the provides.
%global __provides_exclude_from ^%_libdir/pmdk_debug/.*\\.so.*$

%description
The Persistent Memory Development Kit (PMDK), formerly known as NVML
(Non-Volatile Memory Library), is a collection of libraries and tools
built on the DAX (Direct Access) feature of the Linux kernel which
allows applications to access persistent memory as memory-mapped
files, as described in the SNIA NVM Programming Model.

%package tools
Summary:        Utilities for Persistent Memory
Group:          System/Base
Obsoletes:      nvml-tools < %version-%release
Provides:       nvml-tools = %version-%release

%description tools
The Persistent Memory Development Kit (PMDK) is a collection of
libraries and tools built on the DAX (Direct Access) feature of the
Linux kernel which allows applications to access persistent memory as
memory-mapped files, as described in the SNIA NVM Programming Model.

* pmempool: utility for administration and diagnosis  of PMDK pools
* pmreorder: Python scripts to parse and replay operations logged by pmemcheck
* daxio: utility to perform I/O on DAX devices

%package -n libpmem1
Summary:        Low-level persistent memory support library
Group:          System/Libraries
Recommends:     %name

%description -n libpmem1
libpmem provides low level persistent memory support, in particular,
support for the persistent memory instructions for flushing changes
to pmem.

%package -n libpmem-devel
Summary:        Development files for the low-level persistent memory library
Group:          Development/Libraries/C and C++
Requires:       libpmem1 = %version

%description -n libpmem-devel
libpmem provides low level persistent memory support. In particular,
support for the persistent memory instructions for flushing changes
to pmem is provided.

This library is provided for software which tracks every store to
pmem and needs to flush those changes to durability. Most developers
will find higher level libraries like libpmemobj to be much more
convenient.

%package -n libpmemblk1
Summary:        Persistent Memory Resident Block library
Group:          System/Libraries

%description -n libpmemblk1
libpmemblk implements a pmem-resident array of blocks, all the same
size, where a block is updated atomically with respect to power
failure or program interruption (no torn blocks).

%package -n libpmemblk-devel
Summary:        Development files for the Persistent Memory Resident Block library
Group:          Development/Libraries/C and C++
Requires:       libpmemblk1 = %version

%description -n libpmemblk-devel
libpmemblk implements a pmem-resident array of blocks, all the same
size, where a block is updated atomically with respect to power
failure or program interruption (no torn blocks).

For example, a program keeping a cache of fixed-size objects in pmem
might find this library useful. This library is provided for cases
requiring large arrays of objects at least 512 bytes each. Most
developers will find higher level libraries like libpmemobj to be
more generally useful.

%package -n libpmemlog1
Summary:        Persistent Memory Resident Log File library
Group:          System/Libraries

%description -n libpmemlog1
The libpmemlog library provides a pmem-resident log file. This is
useful for programs like databases that append frequently to a log
file.

%package -n libpmemlog-devel
Summary:        Development files for the Persistent Memory Resident Log File library
Group:          Development/Libraries/C and C++
Requires:       libpmemlog1 = %version

%description -n libpmemlog-devel
The libpmemlog library provides a pmem-resident log file. This
library is provided for cases requiring an append-mostly file to
record variable length entries. Most developers will find higher
level libraries like libpmemobj to be more generally useful.

%package -n libpmemobj1
Summary:        Persistent Memory Transactional Object Store library
Group:          System/Libraries

%description -n libpmemobj1
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming.

%package -n libpmemobj-devel
Summary:        Development files for the Persistent Memory Transactional Object Store library
Group:          Development/Libraries/C and C++
Requires:       libpmemobj1 = %version

%description -n libpmemobj-devel
The libpmemobj library provides a transactional object store,
providing memory allocation, transactions, and general facilities for
persistent memory programming. Developers new to persistent memory
probably want to start with this library.

%package -n libvmem1
Summary:        Volatile Memory Pool library
Group:          System/Libraries

%description -n libvmem1
The libvmem library turns a pool of persistent memory into a volatile
memory pool, similar to the system heap but kept separate and with
its own malloc-style API.

%package -n libvmem-devel
Summary:        Development files for the Volatile Memory library
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

%package -n libpmempool1
Summary:        Persistent Memory pool management library
Group:          System/Libraries

%description -n libpmempool1
The libpmempool library provides a set of utilities for off-line administration,
analysis, diagnostics and repair of persistent memory pools created
by libpmemlog, libpemblk and libpmemobj libraries.

%package -n libpmempool-devel
Summary:        Development files for Persistent Memory pool management library
Group:          Development/Libraries/C and C++
Requires:       libpmempool1 = %version

%description -n libpmempool-devel
The libpmempool library provides a set of utilities for off-line administration,
analysis, diagnostics and repair of persistent memory pools created
by libpmemlog, libpemblk and libpmemobj libraries.

%package -n librpmem1
Summary:        Remote Access to Persistent Memory library
#Manual dependency to make sure libfabric is at least in this version
Group:          System/Libraries
Requires:       libfabric >= %min_libfabric_ver
Requires:       openssh

%description -n librpmem1
The librpmem library provides low-level support for remote access
to persistent memory utilizing RDMA-capable NICs. It can be used
to replicate persistent memory regions over RDMA protocol.

%package -n librpmem-devel
Summary:        Development files for the Remote Access to Persistent Memory library
Group:          Development/Libraries/C and C++
Requires:       librpmem1 = %version

%description -n librpmem-devel
The librpmem library provides low-level support for remote access
to persistent memory utilizing RDMA-capable NICs. It can be used
to replicate persistent memory regions over RDMA protocol.

This sub-package contains libraries and header files for developing
applications that want to specifically make use of librpmem.

%package -n rpmemd
Summary:        Target node process executed by librpmem
#Manual dependency to make sure libfabric is at least in this version
Group:          System/Base
Requires:       libfabric >= %min_libfabric_ver

%description -n rpmemd
The rpmemd process is executed on a target node by librpmem library
and facilitates access to persistent memory over RDMA.

%package devel-doc
Summary:        Man pages for the libpmem C API
Group:          Documentation/Man

%description devel-doc
Documentation for the pmem library interface.

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
EXTRA_CFLAGS_RELEASE="%optflags" \
EXTRA_CFLAGS_DEBUG="%optflags -Wp,-U_FORTIFY_SOURCE -O0" \
EXTRA_CXXFLAGS="%optflags" \
make %{?_smp_mflags} BINDIR="%_bindir" EXTRA_CFLAGS="-Wno-error" \
%if 0%{?with_fabric}
  BUILD_RPMEM=y \
%endif
  NORPATH=1

# Override LIB_AR with empty string to skip installation of static libraries
%install
b="%buildroot"
make install DESTDIR="$b" LIB_AR= \
	prefix="%_prefix" \
	libdir="%_libdir" \
	includedir="%_includedir" \
	mandir="%_mandir" \
	bindir="%_bindir" \
	sysconfdir="%_sysconfdir" \
	docdir="%_docdir"
mkdir -p "$b/%_datadir/pmdk"
cp utils/pmdk.magic "$b/%_datadir/pmdk/"
%fdupes %buildroot/%_prefix

%check
cp src/test/testconfig.sh.example src/test/testconfig.sh
#make check

%post   -n libpmem1 -p /sbin/ldconfig
%postun -n libpmem1 -p /sbin/ldconfig
%post   -n libpmemblk1 -p /sbin/ldconfig
%postun -n libpmemblk1 -p /sbin/ldconfig
%post   -n libpmemlog1 -p /sbin/ldconfig
%postun -n libpmemlog1 -p /sbin/ldconfig
%post   -n libpmemobj1 -p /sbin/ldconfig
%postun -n libpmemobj1 -p /sbin/ldconfig
%post   -n libvmem1 -p /sbin/ldconfig
%postun -n libvmem1 -p /sbin/ldconfig
%post   -n libvmmalloc1 -p /sbin/ldconfig
%postun -n libvmmalloc1 -p /sbin/ldconfig
%post   -n libpmempool1 -p /sbin/ldconfig
%postun -n libpmempool1 -p /sbin/ldconfig
%post   -n librpmem1 -p /sbin/ldconfig
%postun -n librpmem1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_datadir/pmdk/
%doc ChangeLog

%files tools
%defattr(-,root,root)
%config %_sysconfdir/bash_completion.d/*
%_bindir/daxio
%_bindir/pmempool
%_bindir/pmreorder
%_datadir/pmreorder/
%_mandir/man1/daxio.1*
%_mandir/man1/pmempool-*.1*
%_mandir/man1/pmempool.1*
%_mandir/man1/pmreorder.1*
%_mandir/man5/*.5*
%doc LICENSE

%files -n libpmem1
%defattr(-,root,root)
%_libdir/libpmem.so.1*

%files -n libpmem-devel
%defattr(-,root,root)
%_libdir/libpmem.so
%_libdir/pkgconfig/libpmem.pc
%dir %_libdir/pmdk_debug/
%_libdir/pmdk_debug/libpmem.so*
%_includedir/libpmem.h

%files -n libpmemblk1
%defattr(-,root,root)
%_libdir/libpmemblk.so.1*

%files -n libpmemblk-devel
%defattr(-,root,root)
%_libdir/libpmemblk.so
%_libdir/pkgconfig/libpmemblk.pc
%dir %_libdir/pmdk_debug/
%_libdir/pmdk_debug/libpmemblk.so*
%_includedir/libpmemblk.h

%files -n libpmemlog1
%defattr(-,root,root)
%_libdir/libpmemlog.so.1*

%files -n libpmemlog-devel
%defattr(-,root,root)
%_libdir/libpmemlog.so
%_libdir/pkgconfig/libpmemlog.pc
%dir %_libdir/pmdk_debug/
%_libdir/pmdk_debug/libpmemlog.so*
%_includedir/libpmemlog.h

%files -n libpmemobj1
%defattr(-,root,root)
%_libdir/libpmemobj.so.1*

%files -n libpmemobj-devel
%defattr(-,root,root)
%_libdir/libpmemobj.so
%dir %_libdir/pmdk_debug/
%_libdir/pkgconfig/libpmemobj.pc
%_libdir/pmdk_debug/libpmemobj.so*
%_includedir/libpmemobj.h
%_includedir/libpmemobj/

%files -n libvmem1
%defattr(-,root,root)
%_libdir/libvmem.so.1*

%files -n libvmem-devel
%defattr(-,root,root)
%_libdir/libvmem.so
%_libdir/pkgconfig/libvmem.pc
%dir %_libdir/pmdk_debug/
%_libdir/pmdk_debug/libvmem.so*
%_includedir/libvmem.h

%files -n libvmmalloc1
%defattr(-,root,root)
%_libdir/libvmmalloc.so.1*

%files -n libvmmalloc-devel
%defattr(-,root,root)
%_libdir/libvmmalloc.so
%_libdir/pkgconfig/libvmmalloc.pc
%dir %_libdir/pmdk_debug/
%_libdir/pmdk_debug/libvmmalloc.so*
%_includedir/libvmmalloc.h

%files -n libpmempool1
%defattr(-,root,root)
%_libdir/libpmempool.so.1*

%files -n libpmempool-devel
%defattr(-,root,root)
%_libdir/libpmempool.so
%_libdir/pkgconfig/libpmempool.pc
%dir %_libdir/pmdk_debug
%_libdir/pmdk_debug/libpmempool.so*
%_includedir/libpmempool.h

%if 0%{?with_fabric}
%files -n librpmem1
%defattr(-,root,root,-)
%_libdir/librpmem.so.*
%license LICENSE

%files -n librpmem-devel
%defattr(-,root,root,-)
%_libdir/librpmem.so
%_libdir/pkgconfig/librpmem.pc
%dir %_libdir/pmdk_debug
%_libdir/pmdk_debug/librpmem.so*
%_includedir/librpmem.h
%license LICENSE

%files -n rpmemd
%_bindir/rpmemd
%_mandir/man1/rpmemd.1*
%endif #with_fabric

%files devel-doc
%_mandir/man3/*.3*
%_mandir/man7/*.7*
%doc ChangeLog CONTRIBUTING.md README.md

%changelog
