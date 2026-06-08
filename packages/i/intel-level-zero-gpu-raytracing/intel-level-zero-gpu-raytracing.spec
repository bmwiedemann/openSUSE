#
# spec file for package intel-level-zero-gpu-raytracing
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define realname level-zero-raytracing-support

Name:           intel-level-zero-gpu-raytracing
Version:        1.2.4+0
Release:        0
Summary:        Intel GPU support for oneAPI level zero raytracing
License:        MIT
URL:            https://github.com/intel/level-zero-raytracing-support
Source0:        %{realname}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  pkgconfig(tbb)

%description
The oneAPI Level Zero Ray Tracing Support library implements high performance CPU
based construction algorithms for 3D acceleration structures that are compatible
with the ray tracing hardware of Intel GPUs. This library is used by Intel(R)
oneAPI Level Zero to implement part of the RTAS builder extension. This library
should not get used directly but only through Level Zero.

%package -n libze_intel_gpu_raytracing
Summary:        Intel GPU support for oneAPI level zero raytracing
Requires:       level-zero

%description -n libze_intel_gpu_raytracing
The oneAPI Level Zero Ray Tracing Support library implements high performance CPU
based construction algorithms for 3D acceleration structures that are compatible
with the ray tracing hardware of Intel GPUs. This library is used by Intel(R)
oneAPI Level Zero to implement part of the RTAS builder extension. This library
should not get used directly but only through Level Zero.
%prep
%autosetup -n %{realname}-%{version}

%build
%cmake -DZE_RAYTRACING_TBB_STATIC=OFF \
       -DCMAKE_INSTALL_PREFIX=/usr \
       -DCMAKE_BUILD_TYPE=Release ..

%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n libze_intel_gpu_raytracing
%license LICENSE.txt
%license third-party-programs*
%{_libdir}/libze_intel_gpu_raytracing.so

%changelog

