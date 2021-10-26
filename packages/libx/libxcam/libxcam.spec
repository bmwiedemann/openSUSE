#
# spec file for package libxcam
#
# Copyright (c) 2021 SUSE LLC
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
BuildRequires:  pkgconfig(opencv)
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
%setup -q -n %{name}-release_%{version}

%build
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
