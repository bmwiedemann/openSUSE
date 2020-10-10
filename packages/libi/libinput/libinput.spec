#
# spec file for package libinput
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


%bcond_with documentation

Name:           libinput
%define lname	libinput10
Version:        1.16.2
Release:        0
Summary:        Input device and event processing library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/wiki/Software/libinput/

#Git-Web:	https://gitlab.freedesktop.org/libinput/libinput/
Source:         http://freedesktop.org/software/libinput/%name-%version.tar.xz
Source2:        http://freedesktop.org/software/libinput/%name-%version.tar.xz.sig
Source3:        baselibs.conf
Source4:        %name.keyring
Source5:        libinput-rpmlintrc
Patch1:         kill-env.diff

BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{with documentation}
BuildRequires:  doxygen
BuildRequires:  graphviz >= 2.26
%endif
BuildRequires:  grep
BuildRequires:  meson >= 0.41.0
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libevdev) >= 0.4
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom) >= 0.20
BuildRequires:  pkgconfig(mtdev) >= 1.1.0

%description
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

%package udev
Summary:        Input device and event processing library integration into udev
Group:          Hardware/Other

%description udev
The libinput udev helper rule will set the LIBINPUT_DEVICE_GROUP
variable for event devices. Device groups are a labelling system to
allow callers to identify which libinput devices are part of the same
physical device.

%package -n %lname
Summary:        Input device and event processing library
Group:          System/Libraries
Recommends:     %name-udev

%description -n %lname
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input
code the user of libinput need to provide the common set of
functionality that users expect.

%package tools
Summary:        Utilities to display libinput configuration
Group:          Hardware/Other

%description tools
This tool lists the locally recognised devices and their respective
configuration options and configuration defaults.

%package devel
Summary:        Development files for the Input Device Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

This package contains all necessary include files and libraries needed
to develop applications that require libinput.

%prep
%autosetup -p1

%build
%meson \
	--includedir="%_includedir/%name" \
	--datadir="%_datadir/%name-%version" \
	-Dudev-dir="%_prefix/lib/udev" \
	-Dtests=false \
	-Ddocumentation=%{?with_documentation:true}%{!?with_documentation:false} \
	%nil
%meson_build

%install
%meson_install
%fdupes %buildroot/%_prefix
# no python3-libevdev available
for i in libinput-measure-fuzz libinput-measure-touch-size libinput-measure-touchpad-pressure libinput-measure-touchpad-tap libinput-replay; do
	rm -fv "%buildroot/usr/lib/libinput/$i"
	rm -fv "%buildroot/%_mandir/man1/$i".1*
done

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%post udev
[ -x /usr/bin/udevadm ] && /usr/bin/udevadm hwdb --update || :

%files udev
%_prefix/lib/udev/libinput-device-group
%_prefix/lib/udev/libinput-fuzz-*
%_prefix/lib/udev/rules.d/

%files -n %lname
%license COPYING
%_libdir/libinput.so.10*
%_datadir/libinput-%version/

%files tools
%_bindir/libinput
%_libexecdir/libinput/
%_mandir/man1/*

%files devel
%_includedir/%name/
%_libdir/pkgconfig/libinput.pc
%_libdir/libinput.so

%changelog
