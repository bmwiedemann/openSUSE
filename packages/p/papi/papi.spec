#
# spec file
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


%global flavor @BUILD_FLAVOR@%{nil}

%define pname papi
%define ver 7.0.0
%define _ver 7_0_0

%if "%flavor" == ""
ExclusiveArch:  do_not_build
%define package_name %pname
%endif

# Magic for OBS Staging. Only build the flavors required by
# other packages in the ring.
%if %{with ringdisabled}
 %if "%flavor" != "standard"
ExclusiveArch:  do_not_build
 %endif
%endif

%if "%flavor" == "standard"
%{bcond_with hpc}
%endif

%if "%flavor" == "hpc"
%{bcond_without hpc}
%endif

%if %{without hpc}
%define package_name %{pname}
%define libname() lib%{pname}%{?with_mpi:-%{mpi_family}}
%define p_bindir %_bindir
%define p_libdir %_libdir
%define p_datadir %_datadir
%define p_includedir %_includedir
%define p_mandir %_mandir
%else
%{hpc_init %{?ext:-e %{ext}}}

%define libname() lib%{pname}%{expand:%%{hpc_package_name_tail %{**}}}
%define package_name %{hpc_package_name %_ver}
%define p_bindir %hpc_bindir
%define p_libdir %hpc_libdir
%define p_datadir %hpc_datadir
%define p_includedir %hpc_includedir
%define p_mandir %hpc_mandir
%endif

Name:           %{package_name}
Version:        %ver
Release:        0
Summary:        Performance Application Programming Interface
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            http://icl.cs.utk.edu/papi/index.html
Source:         http://icl.cs.utk.edu/projects/papi/downloads/%{pname}-%{version}.tar.gz
Source1:        %{pname}-rpmlintrc
Patch1:         python3.patch

BuildRequires:  autoconf >= 2.61
BuildRequires:  automake
BuildRequires:  chrpath
BuildRequires:  gcc-fortran
BuildRequires:  libpfm-devel >= 4.3.0
BuildRequires:  libpfm-devel-static >= 4.3.0
BuildRequires:  libsensors4-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
%if %{with hpc}
BuildRequires:  lua-lmod
BuildRequires:  suse-hpc
Requires:       lua-lmod
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%if %{with hpc}
Requires:       %{libname %_ver} = %version
%endif

%description

PAPI aims to provide the tool designer and application engineer with a
consistent interface and methodology for use of the performance counter
hardware found in most major microprocessors. PAPI enables software
engineers to see, in near real time, the relation between software
performance and processor events.

%{?with_hpc:%{hpc_master_package -L}}

%package        devel
Summary:        Software Development Kit for PAPI
Group:          Development/Libraries/C and C++
Requires:       %{libname %_ver} = %version
Requires:       %{name} = %{version}
Requires:       linux-kernel-headers

%description    devel
This package includes the C header files that specify the PAPI userspace
libraries and interfaces. This is required for rebuilding any program
that uses PAPI.

%{?with_hpc:%{hpc_master_package -a devel}}

%package        devel-static
Summary:        Static PAPI libraries
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       linux-kernel-headers

%description    devel-static
This package includes the static PAPI libraries.

%package -n     %{libname %_ver}
Summary:        PAPI runtime library
Group:          System/Libraries

%description -n %{libname %_ver}
This package contains the PAPI runtime library.

%{?with_hpc:%{hpc_master_package  -l -L}}

%prep
%setup -q -n %{pname}-%{version}
%autopatch -p1

# Create baselibs.conf dynamically (non-HPC build only).
%if %{without hpc}
cat > %{_sourcedir}/baselibs.conf  <<EOF
%{libname %_ver}
%{name}-devel
  requires -%{name}-<targettype>
  requires "%{libname %_ver}-<targettype> = <version>"
EOF
%endif

%build
%define _lto_cflags %{nil}
cd src
mv configure.in configure.ac
autoreconf -fi
export CFLAGS="%{optflags} -Wno-unused-parameter"

%if %{without hpc}
    %configure \
%else
    %hpc_configure \
%endif
	--with-perf-events --with-pthread-mutexes  \
	--with-shared-lib=yes --with-shlib \
	--with-pfm-incdir=%{_includedir} --with-pfm-libdir=%{_libdir}

make DOCDIR=%{_defaultdocdir}/%{pname} %{?_smp_mflags}

%install
# for some reason this isn't being created by install before cp of
# papi_hl_output_writer.py occurs, which results in %{p_bindir} as regular file
mkdir -p %{buildroot}/%{p_bindir}
cd src
make DESTDIR=%{buildroot} install %{?_smp_mflags} DOCDIR=%{_defaultdocdir}/%{pname} LDCONFIG=/bin/true
ls -lR %{buildroot}
chrpath --delete %{buildroot}%{p_libdir}/*.so*
%if %{with hpc}
%{hpc_compress_man 3}
%hpc_write_modules_files
#%%Module1.0#####################################################################

proc ModulesHelp { } {

    puts stderr " "
    puts stderr "This module loads the %{pname} library"
    puts stderr "toolchain."
    puts stderr "\nVersion %{version}\n"

}
module-whatis "Name: %{pname}"
module-whatis "Version: %{version}"
module-whatis "Category: runtime library"
module-whatis "Description: %{SUMMARY:0}"
module-whatis "URL %{url}"

set     version                     %{version}

prepend-path    PATH                %{hpc_bindir}
prepend-path    MANPATH             %{hpc_mandir}
prepend-path    LD_LIBRARY_PATH     %{hpc_libdir}

setenv          %{hpc_upcase %pname}_DIR        %{hpc_prefix}
setenv          %{hpc_upcase %pname}_BIN        %{hpc_bindir}
setenv          %{hpc_upcase %pname}_LIB        %{hpc_libdir}

if {[file isdirectory  %{hpc_includedir}]} {
prepend-path    LIBRARY_PATH        %{hpc_libdir}
prepend-path    CPATH               %{hpc_includedir}
prepend-path    C_INCLUDE_PATH      %{hpc_includedir}
prepend-path    CPLUS_INCLUDE_PATH  %{hpc_includedir}
prepend-path    INCLUDE                         %{hpc_includedir}
%hpc_modulefile_add_pkgconfig_path

setenv          %{hpc_upcase %pname}_INC        %{hpc_includedir}
}
EOF
%endif

%post -n %{libname %_ver} -p /sbin/ldconfig

%postun -n %{libname %_ver}
/sbin/ldconfig
%{?with_hpc:%{hpc_module_delete_if_default}}

%files
%defattr(-,root,root)
%if %{with hpc}
%hpc_dirs
%dir %hpc_datadir
%dir %hpc_bindir
%hpc_modules_files
%endif
%{p_bindir}/papi_clockres
%{p_bindir}/papi_command_line
%{p_bindir}/papi_cost
%{p_bindir}/papi_decode
%{p_bindir}/papi_event_chooser
%{p_bindir}/papi_mem_info
%{p_bindir}/papi_native_avail
%{p_bindir}/papi_version
%{p_bindir}/papi_xml_event_info
%{p_bindir}/papi_component_avail
%{p_bindir}/papi_error_codes
%{p_bindir}/papi_multiplex_cost
%{p_bindir}/papi_hardware_avail
%{p_bindir}/papi_hl_output_writer.py
%{p_datadir}/%{pname}
%{p_bindir}/papi_avail
%doc ChangeLog*.txt LICENSE.txt README.md RELEASENOTES.txt

%files devel
%defattr(-,root,root)
%if %{with hpc}
%dir %hpc_mandir
%dir %hpc_mandir/man1
%dir %hpc_mandir/man3
%dir %hpc_includedir
%dir %hpc_pkgconfigdir
%endif
%{p_includedir}/f77papi.h
%{p_includedir}/f90papi.h
%{p_includedir}/fpapi.h
%{p_includedir}/papi.h
%{p_includedir}/papiStdEventDefs.h
%{p_includedir}/sde_lib.h
%{p_includedir}/sde_lib.hpp
%doc %{p_mandir}/man3/*.gz
%doc %{p_mandir}/man1/*
%{p_libdir}/libpapi.so
%{p_libdir}/libsde.so
%{p_libdir}/pkgconfig/*.pc

%files devel-static
%defattr(-,root,root)
%{p_libdir}/lib*.a

%files -n %{libname %_ver}
%defattr(-,root,root)
%{p_libdir}/libpapi.so.*
%{p_libdir}/libsde.so.*

%changelog
