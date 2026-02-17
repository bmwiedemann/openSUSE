#
# spec file for package ddcutil
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ddcutil
Version:        2.2.5
Release:        0
Summary:        Utility to query and update monitor settings
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/rockowitz/ddcutil
Source:         https://github.com/rockowitz/ddcutil/archive/refs/tags/v%{version}.tar.gz

# PATCH-FIX-UPSTREAM 0001-fix-freezes-on-laptops.patch <sfalken@opensuse.org>
Patch0:         0001-fix-freezes-on-laptops.patch

BuildRequires:  autoconf
BuildRequires:  automake
# Directory not owned by package error
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libi2c0-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
Recommends:     ddcutil-i2c-udev-rules

%description
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

A particular use case for ddcutil is as part of color profile management.
Monitor calibration is relative to the monitor color settings currently in
effect, e.g. red gain.  ddcutil allows color related settings to be saved at
the time a monitor is calibrated, and then restored when the calibration is
applied.

%package -n libddcutil5
Summary:        Shared library to query and update monitor settings
Group:          System/Libraries
Suggests:       ddcutil-i2c-udev-rules
# libddcutil.so.4 was wrongly packaged as libddcutil3 after the 1.x upgrade
Conflicts:      libddcutil3 >= 1.0

%description -n libddcutil5
Shared library version of ddcutil, exposing a C API.

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package -n libddcutil-devel
Summary:        Development files for libddcutil
Group:          Development/Libraries/C and C++
Requires:       libddcutil5 = %{version}

%description -n libddcutil-devel
Header files and pkgconfig control file for libddcutil.

%package -n ddcutil-i2c-udev-rules
Summary:        Udev rules to grant logged in users DDC/CI access
Group:          Hardware/Other
Requires:       libddcutil5 = %{version}
Provides:       ddcutil:%{_udevrulesdir}/60-ddcutil.rules
BuildArch:      noarch

%description -n ddcutil-i2c-udev-rules
ddcutil allows to control monitor settings like brightness or
color settings.

This sub-package contains udev rules granting access to the
DDC/CI bus of connected displays for regular (non-root) users
who are currently logged in.

%prep
%autosetup -p1

%build
./autogen.sh --prefix=%{_prefix}
%configure \
	--enable-lib=yes \
	--enable-drm=yes \
	--enable-usb=yes \
	--docdir="%{_defaultdocdir}/%{name}" \
	--disable-build-timestamp \
	%{nil}
%make_build

%install
%make_install

%check
%make_build check

%ldconfig_scriptlets -n libddcutil5

%files
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*rules
%{_datadir}/%{name}/data/90-nvidia-i2c.conf
%{_datadir}/%{name}/data/nvidia-i2c.conf
%{_mandir}/man1/ddcutil.1%{?ext_man}
%{_bindir}/ddcutil

%files -n ddcutil-i2c-udev-rules
%license COPYING
%{_udevrulesdir}/60-ddcutil-i2c.rules
%{_modulesloaddir}*

%files -n libddcutil5
%license COPYING
%{_libdir}/libddcutil.so.5*

%files -n libddcutil-devel
%license COPYING
%{_includedir}/ddcutil_types.h
%{_includedir}/ddcutil_c_api.h
%{_includedir}/ddcutil_macros.h
%{_includedir}/ddcutil_status_codes.h
%{_libdir}/pkgconfig/ddcutil.pc
%{_libdir}/cmake/%{name}/
%{_libdir}/libddcutil.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data/

%changelog
