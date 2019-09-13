#
# spec file for package libcec
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guillaume GARDET <guillaume@opensuse.org>
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


%define sover   4
%define libname	%{name}%{sover}
%bcond_with enable_rpi_build
Name:           libcec
Version:        4.0.4
Release:        0
Summary:        Library to control devices with TV remote control via HDMI
License:        GPL-2.0-or-later
Group:          Hardware/TV
URL:            https://github.com/Pulse-Eight/libcec
Source:         https://github.com/Pulse-Eight/libcec/archive/libcec-%{version}.tar.gz
Patch1:         libcec-cmake_install_lib_dir.patch
Patch123:       libcec-build-compare.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(lockdev)
BuildRequires:  pkgconfig(p8-platform)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(xrandr)
%ifarch armv6l armv6hl
%if %{with enable_rpi_build}
BuildRequires:  raspberrypi-gfx-devel
%endif
%endif

%description
In combination with the right hardware, libcec allows to control
a device with a TV remote control utilizing existing HDMI
cabling.

libCEC is an enabling platform for the CEC bus in HDMI. It allows
developers to interact with other HDMI devices without having to
worry about the communication overhead, handshaking, and the various
ways of sending a message for each vendor.

%package -n cec-client
Summary:        Control your device with your TV remote control via HDMI
Group:          Hardware/TV
Requires:       %{libname} = %{version}

%description -n cec-client
In combination with the right hardware, libcec allows to control
a device with a TV remote control utilizing existing HDMI
cabling.

libCEC is an enabling platform for the CEC bus in HDMI, it allows
developers to interact with other HDMI devices without having to
worry about the communication overhead, handshaking, and the various
ways of sending a message for each vendor.

This package contains the client applications.

%package -n python3-%{name}
Summary:        Python bindings for %{name}
Group:          Hardware/TV

%description -n python3-%{name}
In combination with the right hardware, libcec allows to control
a device with a TV remote control utilizing existing HDMI
cabling.

libCEC is an enabling platform for the CEC bus in HDMI, it allows
developers to interact with other HDMI devices without having to
worry about the communication overhead, handshaking, and the various
ways of sending a message for each vendor.

This package contains the Python bindings.

%package -n %{libname}
Summary:        USB CEC adapter communication library
Group:          System/Libraries

%description -n %{libname}
In combination with the right hardware, libcec allows to control
a device with a TV remote control utilizing existing HDMI
cabling.

%package devel
Summary:        Development files for the USB CEC adapter communication library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libCEC is an enabling platform for the CEC bus in HDMI, it allows
developers to interact with other HDMI devices without having to
worry about the communication overhead, handshaking, and the various
ways of sending a message for each vendor.

This subpackage contains the headers for libcec.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch1 -p1
%patch123 -p1

%build
%cmake \
  -Wno-dev
%make_jobs

%install
%cmake_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n cec-client
%defattr(755,root,root)
%{_bindir}/cec-client
%{_bindir}/cec-client-%{version}
%{_bindir}/cecc-client
%{_bindir}/cecc-client-%{version}

%files -n python3-%{name}
%{_bindir}/pyCecClient
%{python3_sitearch}/*

%files -n %{libname}
%{_libdir}/libcec.so.%{sover}*

%files devel
%{_includedir}/libcec
%{_libdir}/pkgconfig/libcec.pc
%{_libdir}/libcec.so

%changelog
