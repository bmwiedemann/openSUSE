#
# spec file for package ASL
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver  0
Name:           ASL
Version:        0.1.7
Release:        0
Summary:        Hardware-accelerated multiphysics simulation platform
License:        AGPL-3.0
Group:          Productivity/Scientific/Physics
Url:            http://asl.org.il/features/
Source:         https://github.com/AvtechScientific/ASL/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         vtk-version.patch
BuildRequires:  cmake >= 3.0.2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libmatio-devel
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  netcdf-devel
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers-1_2
BuildRequires:  vtk-devel >= 7
Recommends:     beignet
Recommends:     freeocl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel >= 1.58.0
%endif

%description
Advanced Simulation Library (ASL) is a hardware-accelerated
multiphysics simulation platform (and an extensible general purpose
tool for solving Partial Differential Equations). Its computational
engine is written in OpenCL and utilizes matrix-free solution
techniques which enable high performance, memory efficiency and
deployability on a variety of massively parallel architectures.

Mesh-free immersed boundary approach allows to move from CAD
directly to simulation, reducing pre-processing efforts and amount of
potential errors. ASL can be used to model various coupled physical
and chemical phenomena and is employed in computational fluid
dynamics, virtual sensing, industrial process data validation and
reconciliation, image-guided surgery, computer-aided engineering,
design space exploration, and crystallography.

%package        devel
Summary:        Development files for the Advanced Simulation Library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libaslcommon%{so_ver} = %{version}

%description    devel
Advanced Simulation Library (ASL) is a hardware-accelerated
multiphysics simulation platform (and an extensible general purpose
tool for solving Partial Differential Equations). Its computational
engine is written in OpenCL and utilizes matrix-free solution
techniques which enable high performance, memory efficiency and
deployability on a variety of massively parallel architectures.

This package contains the header files.

%package        doc
Summary:        API documentation for the Advanced Simulation Library
Group:          Documentation/Man
Requires:       %{name} = %{version}

%description    doc
Advanced Simulation Library (ASL) is a hardware-accelerated
multiphysics simulation platform (and an extensible general purpose
tool for solving Partial Differential Equations). Its computational
engine is written in OpenCL and utilizes matrix-free solution
techniques which enable high performance, memory efficiency and
deployability on a variety of massively parallel architectures.

This package contains the API documentation.

%package     -n libaslcommon%{so_ver}
Summary:        C++ Library for asl
Group:          System/Libraries

%description -n libaslcommon%{so_ver}
Advanced Simulation Library (ASL) is a hardware-accelerated
multiphysics simulation platform (and an extensible general purpose
tool for solving Partial Differential Equations). Its computational
engine is written in OpenCL and utilizes matrix-free solution
techniques which enable high performance, memory efficiency and
deployability on a variety of massively parallel architectures.

This package contains the shared libraries.

%prep
%setup -q
%patch0 -p1
sed -i 's/HTML_TIMESTAMP         = YES/HTML_TIMESTAMP         = NO/' doc/Developer-Guide/Doxyfile.in

%build
%cmake \
  -DWITH_MATIO=yes \
  -DWITH_API_DOC=yes
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%post   -n libaslcommon%{so_ver} -p /sbin/ldconfig
%postun -n libaslcommon%{so_ver} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE README.org
%{_bindir}/asl-hardware
%{_bindir}/asl-acousticWaves
%{_bindir}/asl-bus_wind
%{_bindir}/asl-compressor
%{_bindir}/asl-cubeGravity
%{_bindir}/asl-cubeIncompressibleGravity
%{_bindir}/asl-cubePoroelasticGravity
%{_bindir}/asl-flow
%{_bindir}/asl-flow2
%{_bindir}/asl-flow3
%{_bindir}/asl-flowKDPGrowth
%{_bindir}/asl-flowRotatingCylinders
%{_bindir}/asl-jumpingBox
%{_bindir}/asl-levelSetBasic
%{_bindir}/asl-levelSetFacetedGrowth
%{_bindir}/asl-levelSetNormalGrowth
%{_bindir}/asl-locomotive
%{_bindir}/asl-locomotive_laminar
%{_bindir}/asl-locomotive_stability
%{_bindir}/asl-multicomponent_flow
%{_bindir}/asl-multiphase_flow
%{_bindir}/asl-pitot_tube_ice
%{_bindir}/asl-poroelastic
%{_bindir}/asl-surfaceFlux
%{_bindir}/asl-testSMDiff
%{_bindir}/asl-testSMDiff3C
%{_bindir}/asl-testSMPhi
%{_bindir}/asl-testSMPhiBV
%{_datadir}/%{name}/

%files -n libaslcommon%{so_ver}
%defattr(-,root,root)
%{_libdir}/libasl.so.*
%{_libdir}/libaslacl.so.*
%{_libdir}/libaslcommon.so.*
%{_libdir}/libaslmatio.so.*
%{_libdir}/libaslnum.so.*
%{_libdir}/libaslnumext.so.*
%{_libdir}/libaslvtk.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/libasl.so
%{_libdir}/libaslacl.so
%{_libdir}/libaslcommon.so
%{_libdir}/libaslmatio.so
%{_libdir}/libaslnum.so
%{_libdir}/libaslnumext.so
%{_libdir}/libaslvtk.so
%{_includedir}/ASL/
%{_libdir}/cmake/ASL/
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%{_datadir}/doc/ASL/

%changelog
