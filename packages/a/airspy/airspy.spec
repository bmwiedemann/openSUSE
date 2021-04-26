#
# spec file for package airspy
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2014 Wojciech Kazubski, wk@ire.pw.edu.pl
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


%define sover   0
%define airspy_group    airspy
%define libname lib%{name}%{sover}
Name:           airspy
Version:        1.0.10
Release:        0
Summary:        Support programs for Airspy
License:        GPL-2.0-or-later
URL:            http://www.airspy.com
#Git-Clone:     https://github.com/airspy/airspyone_host.git
Source:         https://github.com/airspy/airspyone_host/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
A tiny and efficient software defined radio.

%package -n %{libname}
Summary:        Driver for Airspy
Requires:       %{name}-udev

%description -n %{libname}
Library to run Airspy SDR receiver.

%package udev
Summary:        Udev rules for Airspy SDR
Requires(pre):  shadow

%description udev
Udev rules for Airspy SDR

%package devel
Summary:        Development files for airspy
Requires:       %{libname} = %{version}

%description devel
Library headers for airspy driver.

%prep
%setup -q -n airspyone_host-%{version}

# HACK: set udev group to airspy
sed -i "s/plugdev/airspy/g" airspy-tools/52-airspy.rules

%build
%define __builder ninja
%cmake \
  -DINSTALL_UDEV_RULES=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libairspy.a

mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspy.rules %{buildroot}%{_udevrulesdir}

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig

%pre udev
getent group %{airspy_group} >/dev/null || groupadd -r %{airspy_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license airspy-tools/LICENSE.md
%doc README.md
%{_bindir}/airspy_gpio
%{_bindir}/airspy_gpiodir
%{_bindir}/airspy_info
%{_bindir}/airspy_lib_version
%{_bindir}/airspy_r820t
%{_bindir}/airspy_rx
%{_bindir}/airspy_si5351c
%{_bindir}/airspy_spiflash

%files -n %{libname}
%license libairspy/LICENSE.md
%{_libdir}/libairspy.so.*

%files udev
%{_udevrulesdir}/52-airspy.rules

%files devel
%{_libdir}/libairspy.so
%{_includedir}/libairspy
%{_libdir}/pkgconfig/libairspy.pc

%changelog
