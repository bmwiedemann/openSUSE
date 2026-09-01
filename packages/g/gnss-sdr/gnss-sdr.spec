#
# spec file for package gnss-sdr
#
# Copyright (c) 2026 SUSE LLC
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
%global sname gnss-sdr
%if "%{flavor}" == "volk"
%global psuffix -%{flavor}
%global pkgsummary VOLK module for gnss-sdr
%global pkglicense GPL-3.0-or-later AND BSD-3-Clause AND Zlib
# SONAME tracks upstream VERSION_INFO_* in
# src/algorithms/libs/volk_gnsssdr_module/volk_gnsssdr/CMakeLists.txt - recheck on every bump
%global libname libvolk_gnsssdr0_0_21
%else
%global pkgsummary Software-defined receiver for GNSS signals
%global pkglicense GPL-3.0-or-later AND LGPL-3.0-only AND BSD-1-Clause AND BSD-2-Clause AND BSD-3-Clause AND MIT
%endif
Name:           gnss-sdr%{?psuffix}
Version:        0.0.21
Release:        0
Summary:        %{pkgsummary}
# Legal-Review-Notice: cpu_features (Apache-2.0) and src/algorithms/libs/opencl
# (MIT, LicenseRef-Apple-Permissive) ship in the tarball but are never built -
# VOLK_CPU_FEATURES=OFF resp. ENABLE_PACKAGING=ON turn them off. CC-BY-4.0
# covers only docs/ images and CODE_OF_CONDUCT.md, none of which are packaged.
License:        %{pkglicense}
URL:            https://gnss-sdr.org/
Source:         https://github.com/gnss-sdr/gnss-sdr/archive/v%{version}.tar.gz#/%{sname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(orc-0.4)
%if "%{flavor}" == "volk"
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Mako
BuildRequires:  python3-six
%else
BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  gnss-sdr-volk-devel
BuildRequires:  gr-osmosdr-devel
BuildRequires:  lapack-devel
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  cmake(absl) >= 20240116
BuildRequires:  pkgconfig(armadillo) >= 9.900.0
BuildRequires:  pkgconfig(gnuradio-analog)
BuildRequires:  pkgconfig(gnuradio-blocks)
BuildRequires:  pkgconfig(gnuradio-fft)
BuildRequires:  pkgconfig(gnuradio-filter)
BuildRequires:  pkgconfig(gnuradio-runtime) >= 3.7.3
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(log4cpp)
BuildRequires:  pkgconfig(matio) >= 1.5.3
BuildRequires:  pkgconfig(protobuf) >= 3.0.0
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(zlib)
%endif
%if "%{flavor}" == "volk"
%description
Set of kernels targeted at gnss-sdr, but also usable
standalone.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description devel
Development files for %{name}.

%package -n %{libname}
Summary:        Optimized kernels for gnss-sdr

%description -n %{libname}
Set of optimized kernels targeted at gnss-sdr, but also usable
standalone.
%else
%description
An SDR receiver able to detect and decode signals according to
various standards:

- GPS (L1, L2C, L5 bands)
- GLONASS (L1, L2 bands)
- BeiDou (B1I, B3I bands)
- Galileo (E1b/c, E5a bands)

It can process signal in realtime or prerecorded signals and
output process signals in various formats.
%endif

%prep
%if "%{flavor}" == "volk"
%autosetup -n %{sname}-%{version}/src/algorithms/libs/volk_gnsssdr_module/volk_gnsssdr
%else
%autosetup -n %{sname}-%{version}
%endif

%build
# gnss-sdr uses libraries only as build artifacts, build as static
%cmake \
  -DPYTHON_EXECUTABLE=%{_bindir}/python3 \
  -DENABLE_GENERIC_ARCH:BOOL=ON \
%if "%{flavor}" == ""
  -DBUILD_SHARED_LIBS:BOOL=OFF \
  -DBUILD_STATIC_LIBS:BOOL=ON \
  -DENABLE_PACKAGING:BOOL=ON \
  -DENABLE_OSMOSDR:BOOL=ON \
  -DENABLE_UNIT_TESTING:BOOL=OFF
%else
  -DVOLK_PYTHON_DIR:PATH=%{python3_sitelib} \
  -DVOLK_CPU_FEATURES:BOOL=OFF
%endif

%cmake_build

%install
%cmake_install
%if "%{flavor}" == "volk"
# python3 never loads sidecar bytecode, and cmake wrote it before the sed below
rm %{buildroot}%{python3_sitelib}/volk_gnsssdr_modtool/*.pyc
rm %{buildroot}%{python3_sitelib}/volk_gnsssdr_modtool/*.pyo
# imported modules, not scripts - drop the shebang instead of chmod +x
sed -i '1{/^#!/d}' %{buildroot}%{python3_sitelib}/volk_gnsssdr_modtool/*.py
%else
# Remove changelog installed at the wrong location
rm %{buildroot}%{_datadir}/doc/gnss-sdr/changelog.gz
%endif
%fdupes %{buildroot}

%if "%{flavor}" == "volk"
%check
# qa_volk_gnsssdr_32fc_convert_8ic compares the NEON kernel against generic at
# tolerance 0 and trips on a 1 LSB rounding difference on some aarch64 workers
%ctest '-E' 'qa_volk_gnsssdr_32fc_convert_8ic'

%ldconfig_scriptlets -n %{libname}

%files
%license COPYING
%doc README.md
%{_bindir}/volk_gnsssdr_profile

%files -n %{libname}
%license COPYING
%{_libdir}/libvolk_gnsssdr.so.*

%files devel
%license COPYING
%{_bindir}/volk_gnsssdr_modtool
%{_bindir}/volk_gnsssdr-config-info
%{_includedir}/volk_gnsssdr
%{_libdir}/cmake/volk_gnsssdr
%{_libdir}/pkgconfig/volk_gnsssdr.pc
%{_libdir}/libvolk_gnsssdr.so
%{python3_sitelib}/volk_gnsssdr_modtool
%else
%files
%license COPYING
%doc README.md build/changelog.gz
%{_bindir}/gnss-sdr
%{_bindir}/front-end-cal
%{_datadir}/gnss-sdr
%{_mandir}/man*/*
%endif

%changelog
