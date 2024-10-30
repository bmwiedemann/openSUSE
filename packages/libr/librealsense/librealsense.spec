#
# spec file for package librealsense
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


%define libver %(echo %version|sed 's@^\\([0-9]*\\)\\.\\([0-9]*\\).*@\\1_\\2@')

Name:           librealsense
Version:        2.56.1
Release:        0
Summary:        Library for Intel RealSense depth cameras
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://github.com/IntelRealSense/librealsense
Source:         https://github.com/IntelRealSense/librealsense/archive/v%{version}.tar.gz
Patch0:         presets_path.patch
Patch1:         disable-pedantic.patch
Patch2:         0001-third-party-use-nlohmann_json-from-system.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  cmake(FreeGLUT)
BuildRequires:  cmake(glfw3) >= 3.3
BuildRequires:  cmake(nlohmann_json) >= 3.11.3
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libglvnd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)

%description
The SDK allows depth and color streaming, and provides intrinsic and extrinsic
calibration information. The library also offers synthetic streams (pointcloud,
depth aligned to color and vise-versa), and a built-in support for record and
playback of streaming sessions.

%package -n %{name}%{libver}
Summary:        Library for Intel RealSense depth cameras
Group:          System/Libraries

%description -n %{name}%{libver}
Library for Intel RealSense depth cameras applications.

%package devel
Summary:        Headers and library for librealsense
Group:          Development/Libraries/C and C++
Requires:       %{name}%{libver} = %{version}-%{release}

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
# there is a *lot* of those warnings
export CXXFLAGS='%optflags -Wno-reorder -Wno-unused-variable -Wno-sign-compare -Wno-unknown-pragmas'
sed -i "s/‘\|\’/\'/g" %{_builddir}/%{name}-%{version}/src/libusb/libusb.h
%cmake \
	-DOpenGL_GL_PREFERENCE=GLVND \
	-DCHECK_FOR_UPDATES=OFF \
	-DIMPORT_DEPTH_CAM_FW=OFF
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
%doc readme.md CONTRIBUTING.md code-of-conduct.md NOTICE.md Security.md
%{_bindir}/realsense-viewer
%dir %{_datadir}/librealsense2/
%dir %{_datadir}/librealsense2/presets/
%{_datadir}/librealsense2/presets/*.preset
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
