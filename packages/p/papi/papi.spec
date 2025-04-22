#
# spec file for package papi
#
# Copyright (c) 2025 SUSE LLC
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


Name:           papi
Version:        7.2.0b2
Release:        0
Summary:        Performance Application Programming Interface
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://icl.cs.utk.edu/papi/index.html
Source:         http://icl.cs.utk.edu/projects/papi/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc

BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc-fortran
BuildRequires:  libpfm-devel >= 4.13.0
BuildRequires:  libpfm-devel-static >= 4.13.0
BuildRequires:  libsensors4-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
#PAPI doesn't support the s390 architecture
ExcludeArch:    s390 s390x
%ifarch %ix86 x86_64 ia64
%if 0%{?suse_version} > 1201
BuildRequires:  libquadmath0
%else
%if 0%{?suse_version} == 1201
BuildRequires:  libquadmath46
%endif
%endif
%endif
%ifarch ppc64
BuildRequires:  gcc-32bit
BuildRequires:  gcc-fortran-32bit
BuildRequires:  glibc-devel-32bit
%endif
#BuildRequires:  libibmad-devel

%description

PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter
hardware found in most major microprocessors. PAPI enables software
engineers to see, in near real time, the relation between software
performance and processor events.

%package        devel
Summary:        Software Development Kit for PAPI
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       lib%{name} = %version
Requires:       linux-kernel-headers

%description    devel
This package includes the C header files that specify the PAPI userspace
libraries and interfaces. This is required for rebuilding any program
that uses PAPI.

%package        devel-static
Summary:        Static PAPI libraries
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       linux-kernel-headers

%description    devel-static
This package includes the static PAPI libraries.

%package -n     lib%{name}
Summary:        PAPI runtime library
Group:          System/Libraries

%description -n lib%{name}
This package contains the PAPI runtime library.

%prep
%setup -q -n %{name}-%{version}

# Create baselibs.conf dynamically
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname %_ver}
%{name}-devel
  requires -%{name}-<targettype>
  requires "%{libname %_ver}-<targettype> = <version>"
EOF

%build
%define _lto_cflags %{nil}
cd src
mv configure.in configure.ac
autoreconf -fi
export CFLAGS="%{optflags} -Wno-unused-parameter"

    %configure \
	--with-perf-events --with-pthread-mutexes  \
	--with-shared-lib=yes --with-shlib \
	--with-pfm-incdir=%{_includedir} --with-pfm-libdir=%{_libdir}

make DOCDIR=%{_defaultdocdir}/%{name} %{?_smp_mflags}

# Remove env usage from shebangs on every *.py file
find . -name "*.py" -exec sed -i 's"#!/usr/bin/env python3"#!/usr/bin/python3"g' {} +

%install
# for some reason this isn't being created by install before cp of
# papi_hl_output_writer.py occurs, which results in %{_bindir} as regular file
mkdir -p %{buildroot}/%{_bindir}
cd src
make DESTDIR=%{buildroot} install %{?_smp_mflags} DOCDIR=%{_defaultdocdir}/%{name} LDCONFIG=/bin/true
ls -lR %{buildroot}
chrpath --delete %{buildroot}%{_libdir}/*.so*

%post -n lib%{name} -p /sbin/ldconfig

%postun -n lib%{name}
/sbin/ldconfig

%files
%license LICENSE.txt
%defattr(-,root,root)
%{_bindir}/papi_clockres
%{_bindir}/papi_command_line
%{_bindir}/papi_cost
%{_bindir}/papi_decode
%{_bindir}/papi_event_chooser
%{_bindir}/papi_mem_info
%{_bindir}/papi_native_avail
%{_bindir}/papi_version
%{_bindir}/papi_xml_event_info
%{_bindir}/papi_component_avail
%{_bindir}/papi_error_codes
%{_bindir}/papi_multiplex_cost
%{_bindir}/papi_hardware_avail
%{_bindir}/papi_hl_output_writer.py
%{_datadir}/%{name}
%{_bindir}/papi_avail
%doc ChangeLog*.txt README.md RELEASENOTES.txt

%files devel
%defattr(-,root,root)
%{_includedir}/f77papi.h
%{_includedir}/f90papi.h
%{_includedir}/fpapi.h
%{_includedir}/papi.h
%{_includedir}/papiStdEventDefs.h
%{_includedir}/sde_lib.h
%{_includedir}/sde_lib.hpp
%doc %{_mandir}/man3/*.gz
%doc %{_mandir}/man1/*
%{_libdir}/libpapi.so
%{_libdir}/libsde.so
%{_libdir}/pkgconfig/*.pc

%files devel-static
%defattr(-,root,root)
%{_libdir}/lib*.a

%files -n lib%{name}
%defattr(-,root,root)
%{_libdir}/libpapi.so.*
%{_libdir}/libsde.so.*

%changelog
