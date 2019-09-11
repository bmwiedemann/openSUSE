#
# spec file for package libindi
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


%define so_ver 1
%define _udevdir %(pkg-config --variable udevdir udev)
Name:           libindi
Version:        1.7.9
Release:        0
Summary:        Instrument Neutral Distributed Interface
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://www.indilib.org/
Source0:        https://github.com/indilib/indi/archive/v%{version}.tar.gz#/indi-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-warnings.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  libcfitsio-devel
BuildRequires:  libcurl-devel
BuildRequires:  libnova-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(websocketpp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(udev)
Requires:       libindi-plugins = %{version}
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%endif

%description
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%package devel
Summary:        Development files for libindi
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libindiAlignmentDriver%{so_ver} = %{version}
Requires:       libindidriver%{so_ver} = %{version}
Requires:       libindilx200-%{so_ver} = %{version}

%description devel
This package contains development files for libindi.

%package plugins
Summary:        Plugins for libindi
# libindi1 was last used at version 1.3.1
Group:          Productivity/Scientific/Astronomy
Obsoletes:      libindi1 < %{version}

%description plugins
This package contains plugins for libindi.

%package -n libindiAlignmentDriver%{so_ver}
Summary:        Instrument Neutral Distributed Interface
Group:          System/Libraries

%description -n libindiAlignmentDriver%{so_ver}
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%package -n libindidriver%{so_ver}
Summary:        Instrument Neutral Distributed Interface
Group:          System/Libraries

%description -n libindidriver%{so_ver}
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%package -n libindilx200-%{so_ver}
Summary:        Instrument Neutral Distributed Interface
Group:          System/Libraries

%description -n libindilx200-%{so_ver}
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%prep
%setup -q -n indi-%{version}
%autopatch -p1

# Cleanup
rm -fr debian docker macosx travis-ci
# Also remove blobs
rm -fr 3rdparty

%build
%define _lto_cflags %{nil}
pushd libindi

# libindi doesn't check whether CMAKE_INSTALL_LIBDIR is relative or not...
sed -i 's|${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}|${CMAKE_INSTALL_LIBDIR}|' libs/indibase/alignment/CMakeLists.txt

%if 0%{?suse_version} < 1330
export CC=gcc-7
export CXX=g++-7
%endif

%cmake -DUDEVRULES_INSTALL_DIR=%{_udevdir}/rules.d \
  -DINDI_BUILD_QT5_CLIENT=ON \
%if 0%{?suse_version} >= 1330
  -DINDI_BUILD_WEBSOCKET=ON \
%endif
  -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"

%make_jobs
popd

%install
pushd libindi
%cmake_install
popd

%post -n libindiAlignmentDriver%{so_ver} -p /sbin/ldconfig
%postun -n libindiAlignmentDriver%{so_ver} -p /sbin/ldconfig
%post -n libindidriver%{so_ver} -p /sbin/ldconfig
%postun -n libindidriver%{so_ver} -p /sbin/ldconfig
%post -n libindilx200-%{so_ver} -p /sbin/ldconfig
%postun -n libindilx200-%{so_ver} -p /sbin/ldconfig

%files
%license libindi/COPYING.* libindi/COPYRIGHT libindi/LICENSE
%doc libindi/AUTHORS libindi/ChangeLog libindi/NEWS libindi/README
%{_bindir}/indi*
%{_datadir}/indi/
%{_udevdir}/rules.d/*.rules

%files devel
%license libindi/COPYING.* libindi/LICENSE
%{_includedir}/libindi/
%{_libdir}/pkgconfig/libindi.pc
%{_libdir}/libindi*.so
%{_libdir}/libindi*.a

%files plugins
%license libindi/COPYING.* libindi/LICENSE
%{_libdir}/indi/

%files -n libindiAlignmentDriver%{so_ver}
%{_libdir}/libindiAlignmentDriver.so.%{so_ver}*

%files -n libindidriver%{so_ver}
%{_libdir}/libindidriver.so.%{so_ver}*

%files -n libindilx200-%{so_ver}
%{_libdir}/libindilx200.so.%{so_ver}*

%changelog
