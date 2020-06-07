#
# spec file for package gasnet
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


%define _buildshell /bin/bash

Name:           gasnet
Version:        1.32.0
Release:        0
%define libver	1_32_0
Summary:        A Communication Layer for GAS Languages
License:        PostgreSQL
Group:          Productivity/Networking/Other
URL:            https://gasnet.lbl.gov
Source0:        https://gasnet.lbl.gov/download/GASNet-%{version}.tar.gz
Patch0:         gasnet-date-time.patch
# PATCH-FIX-OPENSUSE -- have constant BUILD_ID to fix build-compare
Patch2:         gasnet-build-id.patch
# PATCH-FIX-OPENSUSE https://bitbucket.org/berkeleylab/gasnet/pull-requests/253/allow-to-not-store-build-date-user-and/diff
Patch3:         gasnet-build-hostname.patch
Patch4:         gasnet-fix-multiple-definitions.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libibverbs-devel
%ifarch x86_64 %{ix86}
BuildRequires:  libfabric-devel
%endif
%ifarch x86_64
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  libtool
BuildRequires:  openmpi-macros-devel

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GASNet (Global Address Space Networking) is a language-independent,
low-level networking layer that provides network-independent
communication primitives tailored for implementing parallel global
address space SPMD languages such as UPC, Titanium, and Co-Array
Fortran.

%package devel
Summary:        Development files for GASNet
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       lib%{name}-%{libver}

%description devel
GASNet is a language-independent, low-level networking layer that provides
network-independent communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

The interface is primarily intended as a compilation target and for
use by runtime library writers (as opposed to end users).

Development package for GASNet. Including header files and libraries.

%package -n libgasnet-%{libver}
Summary:        Runtime libraries for GASNet
Group:          System/Libraries
%openmpi_requires

%description -n libgasnet-%{libver}
GASNet is a language-independent, low-level networking layer that provides
network-independent communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

This package contains the libraries for GASNet.

%package doc
Summary:        Documentation for GASNet
Group:          Documentation/Other
BuildArch:      noarch

%description doc
GASNet is a language-independent, low-level networking layer that provides
network-independent communication primitives tailored for
implementing parallel global address space SPMD languages
such as UPC, Titanium, and Co-Array Fortran.

This package contains the documentation for GASNet.

%prep
%setup -q -n GASNet-%{version}
%patch0
%patch2 -p1
%patch3 -p1
%patch4

# Avoid unnecessary rebuilds of the package
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M:%%S')
sed -i -e "s/__DATE__/\"$FAKE_BUILDDATE\"/" -e "s/__TIME__/\"$FAKE_BUILDTIME\"/" gasnet_tools.c gasnet_trace.c tests/test.h

%build
%setup_openmpi
%configure --enable-udp --enable-mpi --enable-par --enable-ibv --disable-aligned-segments  --enable-segment-fast --with-segment-mmap-max=4GB --disable-debug --enable-force-posix-realtime --enable-smp \
%ifarch x86_64 %{ix86}
    --enable-ofi \
%endif
%ifarch x86_64
    --enable-psm \
%endif
%ifarch s390 s390x
  --enable-force-compiler-atomicops \
%endif

 CC="gcc -fPIC" CXX="g++ -fPIC"

make %{?_smp_mflags} MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC"

%check
%setup_openmpi
make %{?_smp_mflags} check MANUAL_CFLAGS="%optflags -fPIC" MANUAL_MPICFLAGS="%optflags -fPIC" MANUAL_CXXFLAGS="%optflags -fPIC"

%install
%setup_openmpi
make %{?_smp_mflags} DESTDIR=%{buildroot} install
%fdupes %{buildroot}/%{_prefix}
chmod +x %{buildroot}/%{_bindir}/*.pl

#Upstream doesn't want to support shared libs: https://bitbucket.org/berkeleylab/gasnet/pull-requests/36
#mind the order for link deps, libgasnet-smp-par first then libam* then the rest
for l in %{buildroot}/%{_libdir}/lib{gasnet-smp-par,am*,*}.a; do \
    [[ -f $l ]] || continue; \
    soname=`basename $l .a`; \
    libdir=`dirname $l`; \
	linker=`which g++`
    libs= ; \
    [[ ${soname} = libgasnet-*-par* ]] && libs+=" -lpthread"; \
    [[ ${soname} = libgasnet_*-par* ]] && libs+=" -lpthread"; \
    [[ ${soname} = libgasnet-psm-seq ]] && libs+=" -lpthread"; \
    [[ ${soname} = libamudp ]] && libs+=" -L${libdir} -lgasnet-smp-par"; \
    [[ ${soname} = libammpi ]] && libs+=" $(mpicc --showme:link) -L${libdir} -lgasnet-smp-par"; \
    [[ ${soname} = libgasnet-udp-* ]] && libs+=" -L${libdir} -lamudp"; \
    [[ ${soname} = libgasnet-mpi-* ]] && libs+=" -L${libdir} -lammpi"; \
    [[ ${soname} = libgasnet-ibv-* ]] && libs+=" -L${libdir} -libverbs -lpthread" &&
          linker=`which mpic++`; \
    [[ ${soname} = libgasnet-psm-* ]] && libs+=" -L${libdir} -lpsm2" &&
	   linker=`which mpic++`; \
    [[ ${soname} = libgasnet-ofi-* ]] && libs+=" -L${libdir} -lfabric" &&
	   linker=`which mpic++`; \
    [[ ${soname} = libgasnet-*-* ]] && libs+=" -lrt"; \
    (${linker} -shared -Wl,-soname=${soname}-%{version}.so \
        -Wl,--as-needed -Wl,-z,defs -Wl,--rpath-link=. \
        -Wl,--whole-archive ${l} -Wl,--no-whole-archive \
        ${libs} -o ${libdir}/${soname}-%{version}.so && \
    ln -s ${soname}-%{version}.so ${libdir}/${soname}.so && \
    rm ${l}) || exit 1 ; \
done

%post -n libgasnet-%{libver} -p /sbin/ldconfig
%postun -n libgasnet-%{libver} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*

%files -n libgasnet-%{libver}
%defattr(-,root,root)
%{_libdir}/lib*-%{version}.so

%files doc
%defattr(-,root,root)
%{_datadir}/doc/GASNet

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/lib*[a-z].so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/valgrind

%changelog
