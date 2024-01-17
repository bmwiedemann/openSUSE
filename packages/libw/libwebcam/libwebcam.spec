#
# spec file for package libwebcam
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libwebcam
Version:        0.2.5
%define so_ver  0
Release:        0
Summary:        A library for user-space configuration of the uvcvideo driver
License:        GPL-3.0+
Url:            http://sourceforge.net/projects/libwebcam/
Source0:        http://downloads.sourceforge.net/%name/%name-src-%version.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  systemd-rpm-macros

%description
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%package     -n %name%so_ver
License:        LGPL-3.0+
Summary:        A library for user-space configuration of the uvcvideo driver

%description -n %name%so_ver
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%package        devel
Summary:        Development files for libwebcam
License:        LGPL-3.0+
Requires:       %name%so_ver = %version

%description    devel
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

This package contains development files for libwebcam.

%package     -n uvcdynctrl
Summary:        Command line interface to libwebcam
License:        GPL-3.0+
Requires:       udev

%description -n uvcdynctrl
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

This package contains command line interface to libwebcam.

%prep
%autosetup -p1

%build
tee uvcdynctrl/udev/rules/80-uvcdynctrl.rules <<__EOR__
ACTION=="add", SUBSYSTEM=="video4linux", DRIVERS=="uvcvideo", RUN+="%_libexecdir/uvcdynctrl.sh"
__EOR__
%cmake
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_libdir/*.a
# fix up after dirty tarball
find %buildroot -name '*~' -exec rm -fv '{}' +
mkdir -vp %buildroot%_libexecdir %buildroot%_udevrulesdir
mv -t %buildroot%_udevrulesdir %buildroot/lib/udev/rules.d/*.rules
mv %buildroot/lib/udev/uvcdynctrl %buildroot%_libexecdir/uvcdynctrl.sh
rm -rfv %buildroot/lib

%ldconfig_scriptlets -n %name%so_ver

%post -n uvcdynctrl
%udev_rules_update

%postun -n uvcdynctrl
%udev_rules_update

%files -n uvcdynctrl
%license uvcdynctrl/COPYING
%doc uvcdynctrl/README
%_bindir/uvcdynctrl*
%_datadir/uvcdynctrl
%_datadir/man/man1/*
%_libexecdir/uvcdynctrl.sh
%_udevrulesdir/*.rules

%files -n %name%so_ver
%license libwebcam/COPYING libwebcam/COPYING.LESSER
%doc libwebcam/README
%_libdir/*.so.*

%files devel
%_includedir/*.h
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
