#
# spec file for package hpx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Christoph Junghans
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


Name:           hpx
Version:        1.2.1
Release:        0
Summary:        General Purpose C++ Runtime System
License:        BSL-1.0
Group:          Productivity/Networking/Other
URL:            http://stellar.cct.lsu.edu/tag/hpx/
Source0:        http://stellar.cct.lsu.edu/files/%{name}_%{version}.tar.gz
#PATCH-FIX-UPSTREAM boo#1100677 avoid compile-time CPU-detection https://github.com/STEllAR-GROUP/hpx/pull/3585
Patch2:         reproducible.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  gperftools-devel
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%ifarch aarch64 %arm
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_context-devel
BuildRequires:  libboost_thread-devel
%endif
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hwloc-devel
BuildRequires:  openmpi-macros-devel

%description
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

%package devel
Summary:        Development headers and libraries for hpx
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-devel-static = %{version}-%{release}

%description devel
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

This package contains development headers and libraries for hpx

%package -n libhpx1
Summary:        Libraries for the hpx package
Group:          System/Libraries
%openmpi_requires

%description -n libhpx1
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

This package contains libraries for the hpx package.

%package devel-static
Summary:        Static development libraries for the hpx package
Group:          Development/Libraries/C and C++

%description devel-static
HPX is a general purpose C++ runtime system for parallel and distributed applications of any scale.

This package contains static development libraries for the hpx package.

%prep
%setup -n %{name}_%{version} -q
%patch2 -p1

%build
%ifarch aarch64 %arm
%define cmake_opts -DHPX_WITH_GENERIC_CONTEXT_COROUTINES=ON
%endif

# add lib atomic for s390x and ppc64
%ifarch s390x ppc64
%define cmake_opts -DCMAKE_SHARED_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic" -DCMAKE_EXE_LINKER_FLAGS="$RPM_OPT_FLAGS -latomic"
%endif

%setup_openmpi
%{cmake} -DLIB=%{_lib} %{?cmake_opts:%{cmake_opts}} -DHPX_WITH_BUILD_BINARY_PACKAGE=ON
make # no _smp_mflags to save memory

%install
make -C build install DESTDIR=%{buildroot}
rm %{buildroot}/%{_datadir}/%{name}/LICENSE_1_0.txt
%fdupes %{buildroot}%{_prefix}

sed -i '1s@env @@' %{buildroot}/%{_bindir}/{hpx*.py,hpxcxx}

%check
# full testsuite takes too much memory just run tests.examples in 1.2.0
%setup_openmpi
LD_LIBRARY_PATH="%{buildroot}/%{_libdir}:${LD_LIBRARY_PATH}" make -C build tests.examples

%post -n libhpx1 -p /sbin/ldconfig
%postun -n libhpx1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE_1_0.txt
%{_bindir}/*

%files -n libhpx1
%defattr(-,root,root,-)
%license LICENSE_1_0.txt
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib*.so.*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib*.so
%{_libdir}/%{name}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/HPX
%{_libdir}/bazel

%files devel-static
%license LICENSE_1_0.txt
%{_libdir}/lib*.a

%changelog
