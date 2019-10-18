#
# spec file for package opae
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define git_ver 1.0.4ec6dc67e795
%define lib_opae_major 1
%define lib_hssi_major 1
%define lib_bmc_major 1
%define lib_ase_major 1
%define lib_bitstream_major 1
%define lib_fpgad_major 1

Name:           opae
Version:        1.3.2
Release:        0
Summary:        Open Programmable Acceleration Engine
License:        Intel OR MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/OPAE/opae-sdk
Source0:        %{name}-%{version}%{git_ver}.tar.bz2
Patch0:         opae-add-missing-lpthread.patch
Patch1:         opae-missing-shebang.patch
Patch3:         opae-fix-python-packaging.patch
Patch4:         opae-fix-support-for-hwloc-2.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  hwloc-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
#Currently *only* builds on x86_64
ExclusiveArch:  x86_64
Requires:       libhssi-io%{lib_hssi_major} = %{version}
Requires:       libopae-c%{lib_opae_major} = %{version}

%description
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

The OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.

%package        devel
Summary:        Development files for OPAE SDK
Group:          Development/Libraries/C and C++
Requires:       opae = %{version}

%description    devel
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

The OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
This package contains the development files.

%package -n libopae-c%{lib_opae_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libopae-c%{lib_opae_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%package -n libhssi-io%{lib_hssi_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libhssi-io%{lib_hssi_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%package -n libbmc%{lib_bmc_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libbmc%{lib_bmc_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%package ase
Summary:        OPAE AFU Simulation Environment
Group:          System/Base

%description ase
This package contains OPAE AFU Simulation Environment

%package -n libase%{lib_ase_major}
Summary:        OPAE Simulation Environment Libraries
Group:          System/Libraries

%description -n libase%{lib_ase_major}
Libraries for the OPAE Simulation environment.

%package -n libbitstream%{lib_bitstream_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libbitstream%{lib_bitstream_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%package -n libfpgad-api%{lib_fpgad_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libfpgad-api%{lib_fpgad_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%prep
%setup -q -n %{name}-%{version}%{git_ver}
%patch0
%patch1
%patch3
%patch4

%build
export RPM_OPT_FLAGS
%cmake	 -DCMAKE_BUILD_TYPE=Release \
		 -DPYTHON_EXECUTABLE=/usr/bin/python3 \
		 -DCMAKE_C_FLAGS="-Wno-format-truncation -Wno-address-of-packed-member" \
		 -DBUILD_ASE=ON

make VERBOSE=1 all %{?_smp_mflags}

%install
%cmake_install VERBOSE=1 V=1
rm -f %{buildroot}%{_libdir}/libsafestr.a
rm -Rf %{buildroot}%{_includedir}/safe_string
# Fix install path for opae samples
mkdir -p %{buildroot}%{_datarootdir}/opae/
mv  %{buildroot}/usr/src/opae/samples %{buildroot}%{_datarootdir}/opae/
# Fix path for cmake macros
mkdir -p %{buildroot}%{_datarootdir}/cmake/Modules
mv  %{buildroot}/usr/src/opae/cmake/modules %{buildroot}%{_datarootdir}/cmake/Modules/OPAE
chmod -x %{buildroot}%{_datarootdir}/cmake/Modules/OPAE/*
# For some reason, ASE packages its own sources... Remove them
rm -Rf %{buildroot}%{_datarootdir}/opae/ase/sw/*.[ch]
# Drop hidden travis file from python json
rm -f %{buildroot}%{_datarootdir}/opae/python/jsonschema-*/.travis.yml
%fdupes %{buildroot}/%{_prefix}
# Direct install to sysconfig is forbidden
mkdir -p %{buildroot}/%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/fpgad.conf %{buildroot}/%{_fillupdir}/sysconfig.fpgad
# For some unfathomable reason with_ase script is installed twice through a hardlink.
# Use some sed voodoo to force the files to be 'unlinked'
sed -i ';' %{buildroot}/%{_bindir}/with_ase

%pre
%service_add_pre fpgad.service
%post
%service_add_post fpgad.service
%{fillup_only -n fpgad}
%preun
%service_del_preun fpgad.service
%postun
%service_del_postun fpgad.service

%post   -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%postun -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%post   -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig
%postun -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig
%post   -n libase%{lib_ase_major} -p /sbin/ldconfig
%postun -n libase%{lib_ase_major} -p /sbin/ldconfig
%post   -n libbmc%{lib_bmc_major} -p /sbin/ldconfig
%postun -n libbmc%{lib_bmc_major} -p /sbin/ldconfig
%post   -n libbitstream%{lib_bitstream_major} -p /sbin/ldconfig
%postun -n libbitstream%{lib_bitstream_major} -p /sbin/ldconfig
%post   -n libfpgad-api%{lib_fpgad_major} -p /sbin/ldconfig
%postun -n libfpgad-api%{lib_fpgad_major} -p /sbin/ldconfig

%files
%{_bindir}/*
%exclude %{_bindir}/afu_sim_setup
%exclude %{_bindir}/with_ase
%license COPYING
%doc RELEASE_NOTES.md
%dir %{_datarootdir}/opae
%{_datarootdir}/opae/python
%dir %{_sysconfdir}/opae
%config(noreplace) %{_sysconfdir}/opae/fpgad.cfg
%{_fillupdir}/sysconfig.fpgad
%{_unitdir}/fpgad.service

%files devel
%{_includedir}/opae
%{_libdir}/*.so
%dir %{_datarootdir}/opae
%{_datarootdir}/opae/samples/
%{_datarootdir}/opae/platform
%{_datarootdir}/cmake/Modules/OPAE

%files -n libopae-c%{lib_opae_major}
%{_libdir}/libopae-c.so.%{lib_opae_major}
%{_libdir}/libopae-c.so.%{lib_opae_major}.*
%{_libdir}/libopae-c++*.so.%{lib_opae_major}
%{_libdir}/libopae-c++*.so.%{lib_opae_major}.*

%files -n libhssi-io%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}.*

%files -n libbmc%{lib_bmc_major}
%{_libdir}/libbmc*.so.%{lib_bmc_major}
%{_libdir}/libbmc*.so.%{lib_bmc_major}.*

%files -n libase%{lib_ase_major}
%{_libdir}/libase*.so.%{lib_ase_major}
%{_libdir}/libase*.so.%{lib_ase_major}.*

%files -n libbitstream%{lib_hssi_major}
%{_libdir}/libbitstream.so.%{lib_hssi_major}
%{_libdir}/libbitstream.so.%{lib_hssi_major}.*

%files -n libfpgad-api%{lib_bmc_major}
%{_libdir}/libfpgad-api.so.%{lib_bmc_major}
%{_libdir}/libfpgad-api.so.%{lib_bmc_major}.*

%files ase
%{_bindir}/afu_sim_setup
%{_bindir}/with_ase
%license COPYING
%dir %{_datarootdir}/opae
%{_datarootdir}/opae/ase

%changelog
