#
# spec file for package openocd
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


%if 0%{?suse_version} < 1320
%define external_jimtcl 0
%else
%define external_jimtcl 1
%endif

%define external_libjaylink 1

%define _udevdir %(pkg-config --variable udevdir udev)
Name:           openocd
Version:        0.12.0
Release:        0
Summary:        Debugging, in-system programming and boundary-scan testing for embedded devices
License:        GPL-2.0-only
Group:          Development/Tools/Debuggers
URL:            http://openocd.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2.sig
Source2:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2.sha256
Source3:        %name.keyring
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  fdupes
%if %{external_jimtcl}
BuildRequires:  jimtcl-devel
%endif
BuildRequires:  libftdi1-devel
BuildRequires:  libhidapi-devel
%if %{external_libjaylink}
BuildRequires:  libjaylink-devel >= 0.2.0
%endif
BuildRequires:  libtool
BuildRequires:  libusb-compat-devel
BuildRequires:  makeinfo
BuildRequires:  pkg-config >= 0.23
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
Requires:       %{name}-data = %{version}
Requires(post): udev
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}
Requires(postun):udev

%description
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming
and boundary-scan testing for embedded devices.  Various different boards,
targets, and interfaces are supported to ease development time.

Install OpenOCD if you are looking for an open source solution for hardware
debugging.

%package data
Summary:        Hardware Scripts for OpenOCD
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
The Open On-Chip Debugger (OpenOCD) provides debugging, in-system programming
and boundary-scan testing for embedded devices.
This package provides hardware description files and documentation.

%prep
%setup -q

%build
%if !%{external_jimtcl}
# set this explicitly, else the configure from included jimtcl
# won't find a compiler :(
export CC=gcc
%endif
%configure \
  --disable-silent-rules \
  --disable-shared \
  --enable-static \
  --disable-doxygen-html \
  --disable-werror \
  --enable-ftdi \
  --enable-stlink \
  --enable-ti-icdi \
  --enable-ulink \
  --enable-usb-blaster-2 \
  --enable-vsllink \
  --enable-osbdm \
  --enable-opendous \
  --enable-aice \
  --enable-usbprog \
  --enable-rlink \
  --enable-armjtagew \
  --enable-cmsis-dap \
  --enable-usb-blaster \
  --enable-presto \
  --enable-openjtag \
  --enable-jlink \
%ifarch %ix86 x86_64
  --enable-parport \
%endif
  --enable-amtjtagaccel \
%ifarch %arm
  --enable-bcm2835gpio \
%endif
  --enable-gw16012 \
  --enable-buspirate \
  --enable-sysfsgpio \
%if %{external_jimtcl}
  --disable-internal-jimtcl \
%endif
%if %{external_libjaylink}
  --disable-internal-libjaylink \
%endif
  --enable-remote-bitbang \

make %{?_smp_mflags} V=1

%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/libopenocd.*
rm -f %{buildroot}%{_datadir}/%{name}/contrib/openocd.udev
rm -rf %{buildroot}%{_datadir}/%{name}/contrib/libdcc
mkdir -p %{buildroot}%{_udevdir}/rules.d
cat contrib/60-openocd.rules | sed -e 's/GROUP="plugdev"/GROUP="users"/' > %{buildroot}%{_udevdir}/rules.d/60-openocd.rules
%fdupes %{buildroot}

%post
%udev_rules_update
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%udev_rules_update

%files
%defattr(-,root,root,-)
%doc contrib/libdcc README AUTHORS ChangeLog COPYING NEWS
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_infodir}/%{name}.info*.gz
%{_udevdir}/rules.d/60-openocd.rules

%files data
%defattr(-,root,root,-)
%{_datadir}/%{name}

%changelog
