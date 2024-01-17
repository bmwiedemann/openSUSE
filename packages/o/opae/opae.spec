#
# spec file for package opae
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


%define with_ase 0
%define with_tests 0
%define with_legacy 0

%define git_ver 1.0.776b2b2718f7
%define lib_opae_major 2
%define lib_hssi_major 1
%define lib_ase_major 1
%define lib_bitstream_major 2
%define lib_fpgad_major 1
%define lib_board_major 1

Name:           opae
Version:        2.0.0
Release:        0
Summary:        Open Programmable Acceleration Engine
License:        Intel OR MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/OPAE/opae-sdk
Source0:        %{name}-%{version}%{git_ver}.tar.bz2
Patch0:         opae-missing-shebang.patch
Patch1:         opae-fix-linking-issue.patch
Patch2:         opae-support-OBS-build.patch
Patch3:         opae-libs-fix-macro-indentation.patch
Patch4:         opae-libs-xfpga-fix-strnlen-argument.patch
Patch5:         opae-fix-support-with-newer-spdlog.patch
Patch6:         opae-disable-FORTIFY_SOURCE.patch
Patch7:         Gcc-13-2858.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  boost-devel
BuildRequires:  cli11-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  hwloc-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  python-pybind11-common-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
BuildRequires:  spdlog-devel >= 1.0
BuildRequires:  tbb-devel
#Currently *only* builds on x86_64
ExclusiveArch:  x86_64
%if 0%{?with_legacy}
Requires:       libhssi-io%{lib_hssi_major} = %{version}
%endif
Requires:       libopae-c%{lib_opae_major} = %{version}

%description
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
It provides a library implementing the OPAE C API for presenting a
streamlined and easy-to-use interface for software applications to
discover, access, and manage FPGA devices and accelerators using
the OPAE software stack.

%package        devel
Summary:        Development files for OPAE SDK
Group:          Development/Libraries/C and C++
Requires:       opae = %{version}

%description    devel
OPAE is the Open Programmable Acceleration Engine, a software framework for
managing and accessing programmable accelerators (FPGAs).

OPAE SDK is a collection of libraries and tools to facilitate the
development of software applications and accelerators using OPAE.
It provides a library implementing the OPAE C API for presenting a
streamlined and easy-to-use interface for software applications to
discover, access, and manage FPGA devices and accelerators using
the OPAE software stack.

%package -n libopae-c%{lib_opae_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libopae-c%{lib_opae_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%package -n libbitstream%{lib_bitstream_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libbitstream%{lib_bitstream_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.

%if 0%{?with_legacy}
%package -n libhssi-io%{lib_hssi_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libhssi-io%{lib_hssi_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.
%endif

%if 0%{?with_ase}
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
%endif

%if 0%{?with_tests}
%package -n libfpgad-api%{lib_fpgad_major}
Summary:        Open Programmable Acceleration Engine Libraries
Group:          System/Libraries

%description -n libfpgad-api%{lib_fpgad_major}
Libraries for the Open Programmable Acceleration Engine Libraries tools.
%endif

%prep
%setup -q -n %{name}-%{version}%{git_ver}
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7

%build
export RPM_OPT_FLAGS
%cmake	 -DCMAKE_BUILD_TYPE=Release \
		 -DPYTHON_EXECUTABLE=/usr/bin/python3 \
		 -DCMAKE_C_FLAGS="-Wno-format-truncation -Wno-address-of-packed-member" \
		 -DOPAE_PRESERVE_REPOS=ON -DOPAE_OBS_BUILD=ON
%make_build all VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install VERBOSE=1 V=1
rm -f %{buildroot}%{_libdir}/libsafestr.a
rm -f %{buildroot}%{_libdir}/libargsfilter.a
rm -Rf %{buildroot}%{_includedir}/safe_string
# This is used by the other .so in libdir/opae/*.so but we do not need the static lib anymore
rm -f %{buildroot}%{_libdir}/libboard_common.a
# Fix install path for opae samples
mkdir -p %{buildroot}%{_datarootdir}/opae/
mv  %{buildroot}/usr/src/opae/samples %{buildroot}%{_datarootdir}/opae/
# Install cmake macros
mkdir -p %{buildroot}%{_datarootdir}/cmake/Modules/OPAE
for s in FindSphinx.cmake
do
  install -m0644 "cmake/${s}" %{buildroot}%{_datarootdir}/cmake/Modules/OPAE
done
for s in FindHwloc.cmake \
			 OPAE.cmake \
			 FindUUID.cmake \
			 Findjson-c.cmake \
			 OPAECompiler.cmake \
			 OPAEGit.cmake \
			 OPAEPackaging.cmake
do
	install -m0644 "opae-libs/cmake/modules/${s}" %{buildroot}%{_datarootdir}/cmake/Modules/OPAE
done

# Drop hidden travis file from python json
rm -f %{buildroot}%{_datarootdir}/opae/python/jsonschema-*/.travis.yml

%fdupes %{buildroot}/%{_prefix}

%if 0%{?with_tests}
# Direct install to sysconfig is forbidden
mkdir -p %{buildroot}/%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/fpgad.conf %{buildroot}/%{_fillupdir}/sysconfig.fpgad
# For some unfathomable reason with_ase script is installed twice through a hardlink.
# Use some sed voodoo to force the files to be 'unlinked'
sed -i ';' %{buildroot}/%{_bindir}/with_ase
%endif
%if !0%{?with_ase}
# If ASE is not built, drop trhe compat library
rm -f %{buildroot}/%{_libdir}/libopae-c-ase.so*
%endif

%post   -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%postun -n libopae-c%{lib_opae_major} -p /sbin/ldconfig
%post   -n libbitstream%{lib_bitstream_major} -p /sbin/ldconfig
%postun -n libbitstream%{lib_bitstream_major} -p /sbin/ldconfig

%if 0%{?with_legacy}
%post   -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig
%postun -n libhssi-io%{lib_hssi_major} -p /sbin/ldconfig
%endif

%if 0%{?with_tests}
%pre
%service_add_pre fpgad.service

%post
%service_add_post fpgad.service
%{fillup_only -n fpgad}

%preun
%service_del_preun fpgad.service

%postun
%service_del_postun fpgad.service

%post   -n libfpgad-api%{lib_fpgad_major} -p /sbin/ldconfig
%postun -n libfpgad-api%{lib_fpgad_major} -p /sbin/ldconfig
%endif

%if 0%{?with_ase}
%post   -n libase%{lib_ase_major} -p /sbin/ldconfig
%postun -n libase%{lib_ase_major} -p /sbin/ldconfig
%endif

%files
%{_bindir}/*
%if 0%{?with_ase}
%exclude %{_bindir}/afu_sim_setup
%exclude %{_bindir}/with_ase
%endif
%dir %{_libdir}/opae/
%{_libdir}/opae/*.so
%license COPYING LICENSE
%doc RELEASE_NOTES.md
%dir %{_datarootdir}/opae
%{_datarootdir}/opae/python
%if 0%{?with_tests}
%dir %{_sysconfdir}/opae
%config(noreplace) %{_sysconfdir}/opae/fpgad.cfg
%{_fillupdir}/sysconfig.fpgad
%{_unitdir}/fpgad.service
%endif

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
%{_libdir}/libopae-cxx-core*.so.%{lib_opae_major}
%{_libdir}/libopae-cxx-core*.so.%{lib_opae_major}.*

%files -n libbitstream%{lib_bitstream_major}
%{_libdir}/libbitstream.so.%{lib_bitstream_major}
%{_libdir}/libbitstream.so.%{lib_bitstream_major}.*

%if 0%{?with_legacy}
%files -n libhssi-io%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}
%{_libdir}/libhssi-io*.so.%{lib_hssi_major}.*
%endif

%if 0%{?with_tests}
%files -n libfpgad-api%{lib_fpgad_major}
%{_libdir}/libfpgad-api.so.%{lib_fpgda_major}
%{_libdir}/libfpgad-api.so.%{lib_fpgad_major}.*
%endif

%if 0%{?with_ase}
%files ase
%{_bindir}/afu_sim_setup
%{_bindir}/with_ase
%license COPYING
%dir %{_datarootdir}/opae

%{_datarootdir}/opae/ase

%files -n libase%{lib_ase_major}
%{_libdir}/libase*.so.%{lib_ase_major}
%{_libdir}/libase*.so.%{lib_ase_major}.*
%endif

%changelog
