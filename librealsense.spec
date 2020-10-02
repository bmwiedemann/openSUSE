#
# spec file for package librealsense
#
# Copyright (c) 2020 SUSE LLC
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


%define libver 2
Name:           librealsense
Version:        2.38.1
Release:        0
Summary:        Library for Intel RealSense depth cameras
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/IntelRealSense/librealsense
Source:         https://github.com/IntelRealSense/librealsense/archive/v%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM - https://github.com/IntelRealSense/librealsense/pull/6321
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(glfw3) >= 3.3
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(x11)

%description
The SDK allows depth and color streaming, and provides intrinsic and extrinsic
calibration information. The library also offers synthetic streams (pointcloud,
depth aligned to color and vise-versa), and a built-in support for record and
playback of streaming sessions.

%package -n %{name}%{libver}
Summary:        Library for librealsense
Group:          Development/Libraries/C and C++

%description -n %{name}%{libver}
Library for librealsense applications.

%package devel
Summary:        Headers and library for librealsense
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Headers and cmake project files for developing librealsense applications.

%package examples
Summary:        Examples for librealsense
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description examples
Examples from the librealsense library.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
	-DOpenGL_GL_PREFERENCE=GLVND
%cmake_build

%install
%cmake_install

rm -f %{buildroot}/%{_libdir}/*.a

install -d %{buildroot}/%{_udevrulesdir}
install -m 644 -t %{buildroot}/%{_udevrulesdir} config/99-realsense-libusb.rules

%fdupes %{buildroot}/%{_libdir}/cmake/

%post -n %{name}%{libver} -p /sbin/ldconfig
%postun -n %{name}%{libver} -p /sbin/ldconfig

%files
%doc readme.md CONTRIBUTING.md code-of-conduct.md NOTICE
%{_bindir}/realsense-viewer
%{_udevrulesdir}/99-realsense-libusb.rules

%files -n %{name}%{libver}
%license LICENSE
%{_libdir}/librealsense*.so.*

%files devel
%{_includedir}/librealsense2
%{_includedir}/librealsense2-gl
%{_libdir}/librealsense*.so
%dir %{_libdir}/cmake/realsense2
%dir %{_libdir}/cmake/realsense2-gl
%{_libdir}/cmake/realsense2/*.cmake
%{_libdir}/cmake/realsense2-gl/*.cmake
%{_libdir}/pkgconfig/realsense2*.pc

%files examples
%{_bindir}/rs-*

%changelog
