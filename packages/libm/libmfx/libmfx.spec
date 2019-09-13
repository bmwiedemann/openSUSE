#
# spec file for package libmfx
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


Name:           libmfx
%define lname   libmfx1
Version:        19.1.0
Release:        0
Summary:        The Intel Media SDK
License:        MIT
Group:          Development/Languages/C and C++
URL:            https://github.com/Intel-Media-SDK/MediaSDK
Source0:        https://github.com/Intel-Media-SDK/MediaSDK/archive/intel-mediasdk-%{version}.tar.gz
Patch0:         cmake-sle12.patch
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
Requires:       %{name}

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

%prep
%setup -q -n MediaSDK-intel-mediasdk-%{version}
%if 0%{?suse_version} < 1500
%patch0 -p1
%endif

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
-DBUILD_TESTS:BOOL=ON \
-DBUILD_TOOLS:BOOL=ON \
-DENABLE_ITT:BOOL=OFF \
-DBUILD_KERNELS:BOOL=OFF \
..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
mkdir -p %{buildroot}/%{_libdir}/mfx/samples
mv %{buildroot}/%{_datadir}/mfx/samples/* \
   %{buildroot}/%{_libdir}/mfx/samples
rmdir %{buildroot}/%{_datadir}/mfx/samples

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%doc CHANGELOG.md CODEOWNERS README.md
%license LICENSE 
%{_bindir}/asg-hevc
%{_bindir}/hevc_fei_extractor

%files -n %lname
%{_libdir}/libmfx.so.*
%{_libdir}/libmfxhw64.so.*
%dir %{_libdir}/mfx
%{_libdir}/mfx/libmfx_*_hw64.so
%dir %{_libdir}/mfx/samples/
%{_libdir}/mfx/samples/*
%exclude %{_libdir}/mfx/samples/libvpp_plugin.a
%dir %{_datadir}/mfx
%{_datadir}/mfx/plugins.cfg

%files devel
%{_includedir}/mfx/
%{_libdir}/libmfx.so
%{_libdir}/libmfxhw64.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/mfx/samples/libvpp_plugin.a

%changelog
