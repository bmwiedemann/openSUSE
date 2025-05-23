#
# spec file for package libmfx
#
# Copyright (c) 2024 SUSE LLC
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


%global sover 1
Name:           libmfx
%define lname   libmfx%{sover}
Version:        23.2.2
Release:        0
Summary:        The Intel Media SDK
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/Intel-Media-SDK/MediaSDK
Source0:        %{url}/archive/intel-mediasdk-%{version}.tar.gz
Source1:        supplements.inc
Source2:        generate-supplements.sh
Patch0:         cmake-sle12.patch
Patch1:         gcc13-fix.patch
BuildRequires:  cmake
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(wayland-client)
ExclusiveArch:  x86_64

%description
The Intel Media SDK provides a plain C API to access hardware-accelerated
video decode, encode and filtering on Intel Gen graphics hardware
platforms. The implementation is written in C++11, with parts in C-for-Media
(CM).

%package -n %lname
Summary:        The Intel Media SDK
Group:          System/Libraries
%include %{S:1}

%description -n %lname
The Intel Media SDK provides a plain C API to access hardware-accelerated
video decode, encode and filtering on Intel Gen graphics hardware
platforms. The implementation is written in C++11, with parts in C-for-Media
(CM).

%package devel
Summary:        Development files Intel Media SDK
Group:          Development/Languages/C and C++
Requires:       %lname = %version

%description devel
This package contains the development headers and pkgconfig files for
the Intel Media SDK.

%package samples
Summary:        Examples for the Intel Media SDK
Group:          Development/Languages/C and C++

%description samples
This package contains example applications for the Intel Media SDK.

%prep
%autosetup -p1 -n MediaSDK-intel-mediasdk-%{version}

%build
mkdir -p build
pushd build
# libITT and cm compiler not available on openSUSE
cmake \
%if 0%{?suse_version} < 1500
-DCMAKE_CXX_COMPILER="%{_bindir}/g++-7" \
%endif
-DCMAKE_INSTALL_PREFIX="%{_prefix}" \
-DENABLE_X11_DRI3:BOOL=ON \
-DENABLE_WAYLAND:BOOL=ON \
-DENABLE_TEXTLOG:BOOL=ON \
-DENABLE_STAT:BOOL=ON \
-DBUILD_TESTS:BOOL=OFF \
-DBUILD_TOOLS:BOOL=OFF \
-DENABLE_ITT:BOOL=OFF \
-DCMAKE_SYSTEM_VERSION=6.14.0 \
-DBUILD_KERNELS:BOOL=OFF \
-DBUILD_TUTORIALS:BOOL=OFF \
-DBUILD_SAMPLES:BOOL=OFF \
..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
#mkdir -p %{buildroot}/%{_libdir}/mfx/samples
#mv %{buildroot}/%{_datadir}/mfx/samples/* \
#   %{buildroot}/%{_libdir}/mfx/samples
#rmdir %{buildroot}/%{_datadir}/mfx/samples

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%doc CHANGELOG.md CODEOWNERS README.rst
%exclude %{_bindir}/asg-hevc
%exclude %{_bindir}/hevc_fei_extractor
%exclude %{_bindir}/mfx-tracer-config

%files -n %lname
%license LICENSE
%exclude %{_libdir}/libmfx.so.%{sover}
%exclude %{_libdir}/libmfx.so.%{sover}.*
%{_libdir}/libmfxhw64.so.%{sover}
%{_libdir}/libmfxhw64.so.%{sover}.*
%exclude %{_libdir}/libmfx-tracer.so.%{sover}
%exclude %{_libdir}/libmfx-tracer.so.%{sover}.*
%dir %{_libdir}/mfx
%{_libdir}/mfx/libmfx_*_hw64.so
%dir %{_datadir}/mfx
%{_datadir}/mfx/plugins.cfg

#%files samples
%exclude %{_libdir}/mfx/samples/

#%files devel
%exclude %{_includedir}/mfx/
%exclude %{_libdir}/libmfx.so
%exclude %{_libdir}/libmfxhw64.so
%exclude %{_libdir}/libmfx-tracer.so
%exclude %{_libdir}/pkgconfig/*.pc

%changelog
