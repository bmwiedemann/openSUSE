#
# spec file for package osmo-fl2k
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


%define sover	0
%define libname libosmo-fl2k%{sover}
Name:           osmo-fl2k
Version:        0.1.1+git.20200602
Release:        0
Summary:        SDR driver for FL2000 based USB 3.0 to VGA adapters
License:        GPL-2.0-or-later
Group:          Productivity/Hamradio/Other
URL:            https://osmocom.org/projects/osmo-fl2k/wiki
#Git-Clone:     https://git.osmocom.org/osmo-fl2k
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  git-core
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Osmo-fl2k allows to use USB 3.0 to VGA adapters based on the
Fresco Logic FL2000 chip as general purpose DACs and SDR transmitter
generating a continuous stream of samples by avoiding the HSYNC and
VSYNC blanking intervals.

%package -n %{libname}
Summary:        SDR driver for FL2000 based USB to VGA adapters
Group:          System/Libraries
Requires:       %{name}-udev

%description -n %{libname}
Osmo-fl2k allows to use USB 3.0 to VGA adapters based on the
Fresco Logic FL2000 chip as general purpose DACs and SDR transmitter
generating a continuous stream of samples by avoiding the HSYNC and
VSYNC blanking intervals.

%package udev
Summary:        Udev rules for osmo-fl2k
Group:          Hardware/Other

%description udev
Udev rules for osmo-fl2k.

%package devel
Summary:        Development files for osmo-fl2k
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Library headers for osmo-fl2k driver.

%prep
%setup -q

%build
%cmake \
    -DINSTALL_UDEV_RULES=ON \
    -DUDEV_RULES_PATH=%{_udevrulesdir}
make %{?_smp_mflags}

%install
%cmake_install
rm %{buildroot}%{_libdir}/libosmo-fl2k.a

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/fl2k_file
%{_bindir}/fl2k_fm
%{_bindir}/fl2k_tcp
%{_bindir}/fl2k_test

%files -n %{libname}
%{_libdir}/libosmo-fl2k.so.%{sover}*

%files udev
%{_udevrulesdir}/osmo-fl2k.rules

%files devel
%{_libdir}/libosmo-fl2k.so
%{_includedir}/osmo-fl2k.h
%{_includedir}/osmo-fl2k_export.h
%{_libdir}/pkgconfig/libosmo-fl2k.pc

%changelog
