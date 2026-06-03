#
# spec file for package OpenImageDenoise
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2021 LISA GmbH, Bingen, Germany.
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


%bcond_with hip

%define sover 2
%define sub_library_sover %(echo %{version} | tr '.' '_')
%define main_library lib%{name}%{sover}
%define core_library lib%{name}_core%{sub_library_sover}
%define device_cpu_library lib%{name}_device_cpu%{sub_library_sover}
%define device_hip_library libOpenImageDenoise_device_hip%{sub_library_sover}

%define __builder ninja

%define pkgname oidn
Name:           OpenImageDenoise
Version:        2.5.0
Release:        0
Summary:        Open Image Denoise library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://openimagedenoise.github.io/
Source:         https://github.com/%{name}/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.src.tar.gz
Source99:       series
Patch1:         add-parallel-jobs.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  ninja
%if %{with hip}
BuildRequires:  clang
BuildRequires:  hipcc
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  ispc >= 1.30.0
BuildRequires:  tbb-devel
ExclusiveArch:  x86_64 aarch64

%description
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

%package -n %{main_library}
Summary:        Shared library for Open Image Denoise library
Group:          System/Libraries
Requires:       %{core_library} = %{version}-%{release}
Requires:       %{device_cpu_library} = %{version}-%{release}

%description -n %{main_library}
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

This package holds the main shared library.

%package -n %{core_library}
Summary:        Shared library for Open Image Denoise library
Group:          System/Libraries

%description -n %{core_library}
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

This package holds the core sub shared library.

%package -n %{device_hip_library}
Summary:        Shared library for Open Image Denoise library
Group:          System/Libraries

%description -n %{device_hip_library}
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

This package holds the device hip sub shared library.

%package -n %{device_cpu_library}
Summary:        Shared library for Open Image Denoise library
Group:          System/Libraries

%description -n %{device_cpu_library}
Intel Open Image Denoise is an open source library of high-performance,
high-quality denoising filters for images rendered with ray tracing.

This package holds the device cpu sub shared library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{main_library} = %{version}

%description	devel
This package contains the C++ header files and symbolic links to the shared
libraries for %{name}. If you would like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%build
%cmake \
  %if %{with hip}
  -DOIDN_DEVICE_HIP=ON \
  -DOIDN_DEVICE_HIP_COMPILER=%{_bindir}/hipcc \
  -DROCM_PATH=%{_libdir}/libhsa-runtime64.so.1 \
  -DROCM_PATH=%{_libdir} \
  %endif
  %{nil}
%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/doc

%ldconfig_scriptlets -n %{main_library}
%ldconfig_scriptlets -n %{core_library}
%ldconfig_scriptlets -n %{device_cpu_library}

%files
%license LICENSE.txt
%{_bindir}/oidn*

%files -n %{main_library}
%license LICENSE.txt
%{_libdir}/lib%{name}.so.*

%files -n %{core_library}
%license LICENSE.txt
%{_libdir}/lib%{name}_core.so.*

%files -n %{device_cpu_library}
%license LICENSE.txt
%{_libdir}/lib%{name}_device_cpu.so.*

%if %{with hip}
%files -n %{device_hip_library}
%license LICENSE.txt
%{_libdir}/libOpenImageDenoise_device_hip.so.%{version}
%endif

%files devel
%license LICENSE.txt
%doc CHANGELOG.md README.md readme.pdf
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}-%{version}
%{_libdir}/lib%{name}*.so

%changelog
