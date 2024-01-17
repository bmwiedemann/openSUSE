#
# spec file for package libxcam
#
# Copyright (c) 2022 SUSE LLC
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


%define sover   1
%define libname %{name}%{sover}
Name:           libxcam
Version:        1.5.0
Release:        0
Summary:        Image processing library for extended camera features and video analysis
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/01org/libxcam
Source0:        https://github.com/01org/libxcam/archive/release_%{version}.tar.gz
# PATCH-FIX-UPSTREAM OpenCV 4.x support, part 1
Patch0:         https://github.com/intel/libxcam/commit/b40c249bcfbf85da66fba416c6480d5ac6ff2ecb.patch#/0001-gl-stitch_support_EGL_initialize_by_GBM.patch
# PATCH-FIX-UPSTREAM OpenCV 4.x support, part 2
Patch1:         https://github.com/intel/libxcam/commit/6a20559b402493ff29eac7368b5d7b4569a64884.patch#/0001-New_features_camera_tunning_and_fixes.patch
# PATCH-FIX-UPSTREAM OpenCV 4.x support, part 3
Patch2:         https://github.com/intel/libxcam/commit/ea99d89082c2473c2e22c848bff4f9f537af3fde.patch#/0001-pkg_config_check_opencv_module_version.patch
# PATCH-FIX-UPSTREAM Fix ODR violation
Patch3:         0001-Fix-multiple-definitions-of-XCam-ShaderID-ODR-violat.patch
# PATCH-FIX-UPSTREAM Fix build with GCC 12
Patch4:         https://github.com/intel/libxcam/pull/802/commits/d13b69e6332277a4a59cd736439e17851fe8be74.patch#/libxcam-1.5.0-gcc-12.patch
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libtool
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libdrm_intel)
%endif
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(opencv4)
%else
BuildRequires:  pkgconfig(opencv)
%endif
BuildRequires:  pkgconfig(vulkan)

%description
libXCam is a project for extended camera features and focus on image quality
improvement and video analysis. There are lots features supported in image
pre-processing, image post-processing and smart analysis. This library makes
GPU/CPU/ISP working together to improve image quality. OpenCL is used to improve
performance in different platforms.

%package -n %{libname}
Summary:        Image processing library for extended camera features and video analysis
Group:          System/Libraries

%description -n %{libname}
libXCam is a project for extended camera features and focus on image quality
improvement and video analysis. There are lots features supported in image
pre-processing, image post-processing and smart analysis. This library makes
GPU/CPU/ISP working together to improve image quality. OpenCL is used to improve
performance in different platforms.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-release_%{version}

%build
%ifarch ppc64le
export CXXFLAGS="$CXXFLAGS -std=gnu++11"
%endif

autoreconf -fiv
%configure \
   --disable-static \
   --with-package-name="Libxcam (openSUSE)" \
   --with-package-origin="http://www.opensuse.org/" \
%ifarch %{ix86} x86_64
   --enable-drm \
%endif
   --disable-aiq \
   --enable-gst \
   --enable-gles \
   --enable-libcl \
   --enable-vulkan \
   --enable-opencv \
   --enable-capi \
   --disable-3alib \
   --enable-smartlib
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README.md NOTICE
%license COPYING
%{_libdir}/%{name}_capi.so.%{sover}*
%{_libdir}/%{name}_core.so.%{sover}*
%{_libdir}/%{name}_gles.so.%{sover}*
%{_libdir}/%{name}_ocl.so.%{sover}*
%{_libdir}/%{name}_soft.so.%{sover}*
%{_libdir}/%{name}_vulkan.so.%{sover}*
%{_libdir}/gstreamer-1.0/libgstxcamsrc.so
%{_libdir}/gstreamer-1.0/libgstxcamfilter.so

%files devel
%{_includedir}/xcam
%{_libdir}/pkgconfig/libxcam.pc
%{_libdir}/libxcam_capi.so
%{_libdir}/libxcam_core.so
%{_libdir}/libxcam_gles.so
%{_libdir}/libxcam_ocl.so
%{_libdir}/libxcam_soft.so
%{_libdir}/libxcam_vulkan.so

%changelog
