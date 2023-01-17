#
# spec file for package ddcutil
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


Name:           ddcutil
Version:        1.4.0
Release:        0
Summary:        Utility to query and update monitor settings
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/rockowitz/ddcutil
Source:         https://github.com/rockowitz/ddcutil/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
# Directory not owned by package error
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libi2c0-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)

%description
ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

A particular use case for ddcutil is as part of color profile management.
Monitor calibration is relative to the monitor color settings currently in
effect, e.g. red gain.  ddcutil allows color related settings to be saved at
the time a monitor is calibrated, and then restored when the calibration is
applied.

%package -n libddcutil4
Summary:        Shared library to query and update monitor settings
Group:          System/Libraries
# libddcutil.so.4 was wrongly packaged as libddcutil3 after the 1.x upgrade
Conflicts:      libddcutil3 >= 1.0

%description -n libddcutil4
Shared library version of ddcutil, exposing a C API.

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.

%package -n libddcutil-devel
Summary:        Development files for libddcutil
Group:          Development/Libraries/C and C++
Requires:       libddcutil4 = %{version}

%description -n libddcutil-devel
Header files and pkgconfig control file for libddcutil.

%prep
%setup -q

%build
./autogen.sh --prefix=%{_prefix}
%configure --enable-lib=yes --enable-drm=yes --enable-usb=yes \
   --docdir="%{_defaultdocdir}/%{name}"
%make_build

%check
make %{?_smp_mflags} check

%install
%make_install

%post   -n libddcutil4 -p /sbin/ldconfig
%postun -n libddcutil4 -p /sbin/ldconfig

%files
%doc AUTHORS NEWS.md README.md CHANGELOG.md
%license COPYING
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%{_datadir}/%{name}/data/*rules
%{_udevrulesdir}/60-ddcutil.rules
%{_datadir}/%{name}/data/90-nvidia-i2c.conf
%{_mandir}/man1/ddcutil.1*
%{_bindir}/ddcutil

%files -n libddcutil4
%license COPYING
%{_libdir}/libddcutil.so.4*

%files -n libddcutil-devel
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
