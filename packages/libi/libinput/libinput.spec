#
# spec file for package libinput
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


%global flavor @BUILD_FLAVOR@%nil
%if "%flavor" == ""
%bcond_without  completion
%bcond_with     documentation
%bcond_with     debug_gui
%endif

%if "%flavor" == "extra"
%define xsuffix -extra
%bcond_with     completion
# no python3-recommonmark
%bcond_with     documentation
%bcond_without  debug_gui
%endif

# no python3-libevdev available
%bcond_without python3_libevdev

%define lname	libinput10
%define pname	libinput
Name:           libinput%{?xsuffix}
Version:        1.26.0
Release:        0
Summary:        Input device and event processing library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://www.freedesktop.org/wiki/Software/libinput/

#Git-Web:	https://gitlab.freedesktop.org/libinput/libinput/
#DL-URL:        https://gitlab.freedesktop.org/libinput/libinput/-/releases
Source:         https://gitlab.freedesktop.org/libinput/libinput/-/archive/%version/libinput-%version.tar.gz
Source3:        baselibs.conf
Source5:        libinput-rpmlintrc
Patch1:         kill-env.diff

BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{with documentation}
BuildRequires:  doxygen
BuildRequires:  graphviz >= 2.26
BuildRequires:  python3-Sphinx
BuildRequires:  python3-recommonmark
%endif
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkg-config
%if %{with debug_gui}
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(wayland-protocols)
%endif
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
%if %{with python3_libevdev}
Requires:       python3-libevdev
%endif

%description tools
This tool lists the locally recognised devices and their respective
configuration options and configuration defaults.

%package -n %pname-debug-gui
Summary:        Graphical libinput debug tool
Group:          Hardware/Other
Requires:       libinput-tools = %version

%description -n %pname-debug-gui
This tool allows graphical libinput debugging. It visualizes
all events processed by libinput.

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
%autosetup -p1 -n %pname-%version

%build
%meson \
	--includedir="%_includedir/%pname" \
	--datadir="%_datadir/%pname-%version" \
	-Dzshcompletiondir="%{?with_completion:%_datadir/zsh/site-functions}%{!?with_completion:no}" \
	-Dudev-dir="%_prefix/lib/udev" \
	-Dtests=false \
	-Ddebug-gui=%{?with_debug_gui:true}%{!?with_debug_gui:false} \
	-Ddocumentation=%{?with_documentation:true}%{!?with_documentation:false} \
	%nil
%meson_build

%install
%meson_install

%if %{without python3_libevdev}
for i in libinput-measure-fuzz libinput-measure-touch-size libinput-measure-touchpad-pressure libinput-measure-touchpad-tap libinput-replay; do
	rm -fv "%buildroot/%_libexecdir/libinput/$i"
	rm -fv "%buildroot/%_mandir/man1/$i".1*
done
%endif

%if "%flavor" == "extra"
	find "%buildroot/" \( -type f -o -type l \) -not -iname \*libinput-debug-gui\* -delete
	find "%buildroot/" -type d -empty -delete
%endif

%fdupes %buildroot/%_prefix
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{_libexecdir}/libinput/*
%endif

%ldconfig_scriptlets -n %lname

%post udev
[ -x /usr/bin/udevadm ] && /usr/bin/udevadm hwdb --update || :

%if "%flavor" == ""
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
%dir %_datadir/zsh
%_datadir/zsh/site-functions

%files devel
%_includedir/%pname/
%_libdir/pkgconfig/libinput.pc
%_libdir/libinput.so
%endif

%if "%flavor" == "extra"
%files -n %pname-debug-gui
%dir %_libexecdir/libinput/
%_libexecdir/libinput/libinput-debug-gui
%_mandir/man1/libinput-debug-gui*
%endif

%changelog
