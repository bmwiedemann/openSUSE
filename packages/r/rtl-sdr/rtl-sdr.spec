#
# spec file for package rtl-sdr
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


%define sover 0
%define libname librtlsdr%{sover}
%define rtlsdr_group rtlsdr

Name:           rtl-sdr
Version:        2.0.2
Release:        0
Summary:        Support programs for RTL2832
License:        GPL-2.0-or-later
URL:            http://sdr.osmocom.org/trac/wiki/rtl-sdr
#Git-Clone:     https://git.osmocom.org/rtl-sdr
Source:         https://github.com/steve-m/librtlsdr/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Better-udev-handling.patch
BuildRequires:  cmake >= 3.7.2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Programs that controls Realtek RTL2832 based DVB dongle in raw mode, so
it can be used as a SDR receiver.

%package -n %{libname}
Summary:        SDR driver for RTL2832
Requires:       %{name}-udev
Conflicts:      librtlsdr2

%description -n %{libname}
Library to run Realtek RTL2832 based DVB dongle as a SDR receiver.

%package udev
Summary:        Udev rules for RTL2832
Requires(pre):  shadow

%description udev
Udev rules for rtl-sdr driver

%package devel
Summary:        Development files for rtl-sdr
Requires:       %{libname} = %{version}

%description devel
Library headers for rtl-sdr driver.

%prep
%autosetup -p1

%build
%cmake \
  -DINSTALL_UDEV_RULES=ON \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
  -DUDEV_RULES_GROUP=%{rtlsdr_group} \
  -DDETACH_KERNEL_DRIVER=ON \
  -DENABLE_ZEROCOPY=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/librtlsdr.a

%ldconfig_scriptlets -n %{libname}

%pre udev
getent group %{rtlsdr_group} >/dev/null || groupadd -r %{rtlsdr_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/rtl_adsb
%{_bindir}/rtl_biast
%{_bindir}/rtl_eeprom
%{_bindir}/rtl_fm
%{_bindir}/rtl_power
%{_bindir}/rtl_sdr
%{_bindir}/rtl_tcp
%{_bindir}/rtl_test

%files -n %{libname}
%{_libdir}/librtlsdr.so.%{sover}*
%{_libdir}/librtlsdr.so.2*

%files udev
%{_udevrulesdir}/rtl-sdr.rules

%files devel
%{_libdir}/librtlsdr.so
%{_includedir}/rtl-sdr.h
%{_includedir}/rtl-sdr_export.h
%{_libdir}/pkgconfig/librtlsdr.pc
%{_libdir}/cmake/rtlsdr

%changelog
