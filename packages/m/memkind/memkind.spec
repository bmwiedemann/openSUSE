#
# spec file for package memkind
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


Name:           memkind
Summary:        User Extensible Heap Manager
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        1.14.0
Release:        0
URL:            http://memkind.github.io/memkind
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  unzip
%if %{defined suse_version}
BuildRequires:  libnuma-devel
%else
BuildRequires:  numactl-devel
%endif

%define namespace memkind

%if %{defined suse_version}
%define docdir %{_defaultdocdir}/%{namespace}
%else
%define docdir %{_defaultdocdir}/%{namespace}-%{version}
%endif

ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le s390x

# default values if version is a tagged release on github
%{!?commit: %define commit %{version}}
%{!?buildsubdir: %define buildsubdir %{namespace}-%{commit}}
Source0:        https://github.com/%{namespace}/%{namespace}/archive/v%{commit}/%{buildsubdir}.tar.gz
Patch0:         memkind-fix-build.diff
Patch1:         memkind-dont-redefine-fortify.diff

%description
The memkind library is an user extensible heap manager built on top
of jemalloc which enables control of memory characteristics and a
partitioning of the heap between kinds of memory.

%package -n libmemkind0
Summary:        User Extensible Heap Manager shared library
Group:          System/Libraries

%description -n libmemkind0
The memkind library is an user extensible heap manager built on top
of jemalloc which enables control of memory characteristics and a
partitioning of the heap between kinds of memory. The kinds of memory
are defined by operating system memory policies that have been
applied to virtual address ranges. Memory characteristics supported
by memkind without user extension include control of NUMA and page
size features. The jemalloc non-standard interface has been extended
to enable specialized arenas to make requests for virtual memory from
the operating system through the memkind partition interface. Through
the other memkind interfaces, the user can control and extend memory
partition features and allocate memory while selecting enabled
features.

%package devel
Summary:        Development files for the "memkind" user extensible heap manager
Group:          Development/Libraries/C and C++
Requires:       libmemkind0 = %{version}-%{release}

%description devel
Header files for building applications with libmemkind.

%prep
%setup -q -n memkind-%{version}
%patch0
%patch1

%build

export JE_PREFIX=jemk_

# Build memkind lib and tools
cd %{_builddir}/%{buildsubdir}
echo %{version} > %{_builddir}/%{buildsubdir}/VERSION
test -f configure || ./autogen.sh
%configure --docdir=%{_docdir}/%{namespace} --disable-static
%{__make} %{?_smp_mflags}

%install
cd %{_builddir}/%{buildsubdir}
%{__make} DESTDIR=%{buildroot} install
# remove unwanted libs
rm -f %{buildroot}/libautohbw.*
rm -f %{buildroot}/%{_libdir}/lib%{namespace}.la
rm -f %{buildroot}/%{_libdir}/lib{numakind,autohbw,memtier}.*
rm -f %{buildroot}/%{_mandir}/man7/autohbw.*
rm -f %{buildroot}/%{_mandir}/man7/memtier.*

%post -n libmemkind0 -p /sbin/ldconfig

%postun -n libmemkind0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license %{_docdir}/%{namespace}/COPYING
%doc %{_docdir}/%{namespace}/README
%doc %{_docdir}/%{namespace}/VERSION
%dir %{_docdir}/%{namespace}
%{_bindir}/%{namespace}-hbw-nodes
%{_bindir}/%{namespace}-auto-dax-kmem-nodes
%{_bindir}/memtier
%{_mandir}/man1/memkind-hbw-nodes.1.*
%{_mandir}/man1/memkind-auto-dax-kmem-nodes.1.*
%{_mandir}/man1/memtier.1.*
%{_mandir}/man7/libmemtier.7.*

%files -n libmemkind0
%{_libdir}/lib%{namespace}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/hbwmalloc.h
%{_includedir}/hbw_allocator.h
%{_includedir}/memkind_deprecated.h
%{_includedir}/memkind_allocator.h
%{_includedir}/pmem_allocator.h
%{_includedir}/memkind_memtier.h
%{_includedir}/fixed_allocator.h
%{_libdir}/lib%{namespace}.so
%{_libdir}/pkgconfig/memkind.pc
%{_includedir}/%{namespace}.h
%{_mandir}/man3/hbwmalloc.3.*
%{_mandir}/man3/hbwallocator.3.*
%{_mandir}/man3/%{namespace}*.3.*
%{_mandir}/man3/pmemallocator.3.*
%{_mandir}/man3/fixedallocator.3.*
%{_mandir}/man3/libmemtier.3.*

%changelog
