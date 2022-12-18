#
# spec file for package libindi
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


%define so_ver 1
%define _udevdir %(pkg-config --variable udevdir udev)
Name:           libindi
Version:        1.9.9
Release:        0
Summary:        Instrument Neutral Distributed Interface
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GPL-3.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            https://www.indilib.org/
Source0:        https://github.com/indilib/indi/archive/v%{version}.tar.gz#/indi-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%if 0%{?suse_version} > 1590
BuildRequires:  cfitsio-devel
%else
BuildRequires:  libcfitsio-devel
%endif
BuildRequires:  libnova-devel
BuildRequires:  libev-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(websocketpp)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(zlib)
Requires:       libindi-plugins = %{version}

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
Requires:       libindiclient%{so_ver} = %{version}
Requires:       libindiclientqt%{so_ver} = %{version}

%description devel
This package contains development files for libindi.

%package plugins
Summary:        Plugins for libindi
Group:          Productivity/Scientific/Astronomy

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

%package -n libindiclient%{so_ver}
Summary:        Instrument Neutral Distributed Interface
Group:          System/Libraries

%description -n libindiclient%{so_ver}
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%package -n libindiclientqt%{so_ver}
Summary:        Instrument Neutral Distributed Interface
Group:          System/Libraries

%description -n libindiclientqt%{so_ver}
INDI is an Instrument Neutral Distributed Interface control protocol
for astronomical devices, which provides a framework that decouples low
level hardware drivers from high level front end clients. Clients that
use the device drivers are completely unaware of the device
capabilities and communicate with the device drivers and build a
completely dynamic GUI based on the services provided by the device.

%prep
%setup -q -n indi-%{version}
%autopatch -p1

%build
%define _lto_cflags %{nil}

export CFLAGS="%(echo %{optflags}) -Wno-stringop-truncation"
export CXXFLAGS="$CFLAGS"

%cmake \
    -DINDI_BUILD_STATIC=OFF \
    -DUDEVRULES_INSTALL_DIR=%{_udevdir}/rules.d \
    -DINDI_BUILD_QT5_CLIENT=ON \
    -DINDI_BUILD_WEBSOCKET=ON \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"

%cmake_build

%install
%cmake_install

%post -n libindiAlignmentDriver%{so_ver} -p /sbin/ldconfig
%postun -n libindiAlignmentDriver%{so_ver} -p /sbin/ldconfig
%post -n libindidriver%{so_ver} -p /sbin/ldconfig
%postun -n libindidriver%{so_ver} -p /sbin/ldconfig
%post -n libindilx200-%{so_ver} -p /sbin/ldconfig
%postun -n libindilx200-%{so_ver} -p /sbin/ldconfig
%post -n libindiclient%{so_ver} -p /sbin/ldconfig
%postun -n libindiclient%{so_ver} -p /sbin/ldconfig
%post -n libindiclientqt%{so_ver} -p /sbin/ldconfig
%postun -n libindiclientqt%{so_ver} -p /sbin/ldconfig

%files
%license COPYING.* COPYRIGHT LICENSE
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/indi*
%{_datadir}/indi/
%{_udevdir}/rules.d/*.rules

%files devel
%license COPYING.* LICENSE
%{_includedir}/libindi/
%{_libdir}/pkgconfig/libindi.pc
%{_libdir}/libindi*.so
%{_libdir}/libindi*.a

%files plugins
%license COPYING.* LICENSE
%{_libdir}/indi/

%files -n libindiclient%{so_ver}
%{_libdir}/libindiclient.so.1
%{_libdir}/libindiclient.so.1.9.9

%files -n libindiclientqt%{so_ver}
%{_libdir}/libindiclientqt.so.1
%{_libdir}/libindiclientqt.so.1.9.9

%files -n libindiAlignmentDriver%{so_ver}
%{_libdir}/libindiAlignmentDriver.so.%{so_ver}*

%files -n libindidriver%{so_ver}
%{_libdir}/libindidriver.so.%{so_ver}*

%files -n libindilx200-%{so_ver}
%{_libdir}/libindilx200.so.%{so_ver}*

%changelog
