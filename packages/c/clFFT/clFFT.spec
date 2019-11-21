#
# spec file for package clFFT
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define sover 2
%define libclfft lib%{name}%{sover}
%define libtimer libStatTimer%{sover}
Name:           clFFT
Version:        2.12.2
Release:        0
Summary:        OpenCL FFT library
License:        Apache-2.0
Group:          Productivity/Scientific/Math
Url:            https://github.com/clMathLibraries/clFFT
#Git-Clone:     https://github.com/clMathLibraries/clFFT.git
Source:         https://github.com/clMathLibraries/clFFT/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        clFFT-client.1
Patch0:         fix-client-no-symlink.patch
Patch1:         clFFT-fix-aarm64.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)
BuildRequires:  pkgconfig(fftw3)
ExcludeArch:    %{ix86} %{arm}
%if 0%{?suse_version} > 1315
BuildRequires:  libboost_program_options-devel
%else
BuildRequires:  boost-devel
%endif

%description
The clFFT library is an OpenCL implementation of discrete
Fast Fourier Transforms which:
  * Works on CPU or GPU backends.
  * Supports in-place or out-of-place transforms.
  * Supports 1D, 2D, and 3D transforms with a batch size that can be greater
    than 1.
  * Supports planar (real and complex components in separate arrays) and
    interleaved (real and complex components as a pair contiguous in memory)
    formats.
  * Supports dimension lengths that can be any mix of powers of 2, 3, and 5.
  * Supports single and double precision floating point formats.

%package devel
Summary:        Development files for libclfft
Group:          Development/Libraries/C and C++
Requires:       %{libclfft} = %{version}
Requires:       %{libtimer} = %{version}

%description devel
Libraries and header files for developing applications that want to
make use of libclFFT.

%package -n %{libclfft}
Summary:        Library for libclfft
Group:          System/Libraries

%description -n %{libclfft}
The clFFT library is an OpenCL implementation of discrete
Fast Fourier Transforms which:
  * Works on CPU or GPU backends.
  * Supports in-place or out-of-place transforms.
  * Supports 1D, 2D, and 3D transforms with a batch size that can be greater
    than 1.
  * Supports planar (real and complex components in separate arrays) and
    interleaved (real and complex components as a pair contiguous in memory)
    formats.
  * Supports dimension lengths that can be any mix of powers of 2, 3, and 5.
  * Supports single and double precision floating point formats.

This subpackage provides shared library clFFT library

%package -n %{libtimer}
Summary:        Library for libclfft
Group:          System/Libraries

%description -n %{libtimer}
The clFFT library is an OpenCL implementation of discrete
Fast Fourier Transforms which:
  * Works on CPU or GPU backends.
  * Supports in-place or out-of-place transforms.
  * Supports 1D, 2D, and 3D transforms with a batch size that can be greater
    than 1.
  * Supports planar (real and complex components in separate arrays) and
    interleaved (real and complex components as a pair contiguous in memory)
    formats.
  * Supports dimension lengths that can be any mix of powers of 2, 3, and 5.
  * Supports single and double precision floating point formats.

This subpackage provides shared libStatTimer library

%prep
%setup -q
%patch0 -p1
%ifarch aarch64
%patch1 -p1
%endif

%build
cd src
%cmake \
  -DBoost_USE_STATIC_LIBS=OFF \
  -DBUILD_CLIENT=ON \
  -DBUILD_EXAMPLES=OFF \
  -DBUILD_LOADLIBRARIES=ON \
  -DBUILD_RUNTIME=ON \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_TEST=OFF
%cmake_build

%install
cd src
%cmake_install
install -Dpm0644 %{SOURCE1} \
  %{buildroot}%{_mandir}/man1/clFFT-client.1

%post -n %{libclfft} -p /sbin/ldconfig
%post -n %{libtimer} -p /sbin/ldconfig
%postun  -n %{libclfft} -p /sbin/ldconfig
%postun  -n %{libtimer} -p /sbin/ldconfig

%files
%{_bindir}/clFFT-client
%{_mandir}/man1/clFFT-client.1%{ext_man}

%files -n %{libclfft}
%doc CHANGELOG LICENSE NOTICE ReleaseNotes.txt
%{_libdir}/libclFFT.so.%{sover}*

%files -n %{libtimer}
%doc CHANGELOG LICENSE NOTICE ReleaseNotes.txt
%{_libdir}/libStatTimer.so.%{sover}*

%files devel
%{_libdir}/libclFFT.so
%{_libdir}/libStatTimer.so
%{_includedir}/clAmdFft*.h
%{_includedir}/clFFT*.h
%{_libdir}/pkgconfig/clFFT.pc
%{_libdir}/cmake/clFFT

%changelog
