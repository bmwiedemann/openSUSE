#
# spec file for package memkind
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           memkind
Summary:        User Extensible Heap Manager
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Version:        1.6.0
Release:        0
Url:            http://memkind.github.io/memkind
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
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

# x86_64 is the only arch memkind will build due to its
# current dependency on SSE4.2 CRC32 instruction which
# is used to compute thread local storage arena mappings
# with polynomial accumulations via GCC's intrinsic _mm_crc32_u64
# For further info check:
# - /lib/gcc/<target>/<version>/include/smmintrin.h
# - https://gcc.gnu.org/bugzilla/show_bug.cgi?id=36095
# - http://en.wikipedia.org/wiki/SSE4
ExclusiveArch:  x86_64

# default values if version is a tagged release on github
%{!?commit: %define commit %{version}}
%{!?buildsubdir: %define buildsubdir %{namespace}-%{commit}}
Source0:        https://github.com/%{namespace}/%{namespace}/archive/v%{commit}/%{buildsubdir}.tar.gz
Patch0:         memkind-fix-build.diff

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
%patch0 -p1

%build

# It is required that we configure and build the jemalloc subdirectory
# before we configure and start building the top level memkind directory.
# To ensure the memkind build step is able to discover the output
# of the jemalloc build we must create an 'obj' directory, and build
# from within that directory.
cd %{_builddir}/%{buildsubdir}/jemalloc/
echo %{version} > %{_builddir}/%{buildsubdir}/jemalloc/VERSION
test -f configure || %{__autoconf}
mkdir %{_builddir}/%{buildsubdir}/jemalloc/obj
ln -s %{_builddir}/%{buildsubdir}/jemalloc/configure %{_builddir}/%{buildsubdir}/jemalloc/obj/
cd %{_builddir}/%{buildsubdir}/jemalloc/obj
../configure --enable-autogen --with-jemalloc-prefix=jemk_ --enable-memkind --enable-cc-silence --prefix=%{_prefix} --includedir=%{_includedir} --libdir=%{_libdir} --bindir=%{_bindir} --docdir=%{_docdir} --mandir=%{_mandir}
%{__make} %{?_smp_mflags} 

# Build memkind lib and tools
cd %{_builddir}/%{buildsubdir}
echo %{version} > %{_builddir}/%{buildsubdir}/VERSION
test -f configure || ./autogen.sh
./configure CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" --prefix=%{_prefix} --libdir=%{_libdir} --includedir=%{_includedir} --sbindir=%{_sbindir} --enable-cxx11 --mandir=%{_mandir} --docdir=%{_docdir}/%{namespace} --disable-static
%{__make} %{?_smp_mflags}

%install
cd %{_builddir}/%{buildsubdir}
%{__make} DESTDIR=%{buildroot} install
rm -f %{buildroot}/libautohbw.*
rm -f %{buildroot}/%{_libdir}/lib%{namespace}.la
rm -f %{buildroot}/%{_libdir}/lib{numakind,autohbw}.*

%post -n libmemkind0 -p /sbin/ldconfig

%postun -n libmemkind0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license %{_docdir}/%{namespace}/COPYING
%doc %{_docdir}/%{namespace}/README
%doc %{_docdir}/%{namespace}/VERSION
%dir %{_docdir}/%{namespace}
%{_bindir}/%{namespace}-hbw-nodes

%files -n libmemkind0
%{_libdir}/lib%{namespace}.so.*

%define internal_include memkind/internal

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/memkind
%dir %{_includedir}/%{internal_include}
%{_includedir}/hbwmalloc.h
%{_includedir}/hbw_allocator.h
%{_includedir}/memkind_deprecated.h
%{_libdir}/lib%{namespace}.so
%{_includedir}/%{namespace}.h
%{_includedir}/%{internal_include}/%{namespace}*.h
%{_includedir}/%{internal_include}/heap_manager.h
%{_includedir}/%{internal_include}/tbb_mem_pool_policy.h
%{_includedir}/%{internal_include}/tbb_wrapper.h
%{_mandir}/man3/hbwmalloc.3.*
%{_mandir}/man3/hbwallocator.3.*
%{_mandir}/man3/%{namespace}*.3.*

%changelog
