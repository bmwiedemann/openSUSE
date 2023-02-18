#
# spec file for package hackrf
#
# Copyright (c) 2022 SUSE LLC
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
%define libname lib%{name}%{sover}
%define hackrf_group  hackrf
Name:           hackrf
Version:        2023.01.1
Release:        0
Summary:        Support programs for the open source SDR hardware
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://greatscottgadgets.com/hackrf/
#Git-Clone:     https://github.com/greatscottgadgets/hackrf.git
Source:         https://github.com/greatscottgadgets/hackrf/releases/download/v%{version}/hackrf-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Tools for HackRF, an open source hardware project to build a Software
Defined Radio (SDR) peripheral.

%package -n %{libname}
Summary:        Driver for HackRF
Group:          Hardware/Other
Requires:       %{name}-udev

%description -n %{libname}
Library to run HackRF, an open source hardware project to build a Software
Defined Radio (SDR) peripheral.

%package udev
Summary:        Udev rules for HackRF
Group:          Hardware/Other
Requires(pre):  shadow

%description udev
Udev rules for HackRF.

%package devel
Summary:        Development files for HackRF
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Library headers for the hackrf driver.

%package firmware
Summary:        Firmware for the hackRF board
Group:          Hardware/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description firmware
Firmare files for the hackRF board.

%prep
%setup -q -n %{name}-%{version}/host

%build
%cmake \
  -DINSTALL_UDEV_RULES=ON \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
  -DUDEV_RULES_GROUP=%{hackrf_group}
%make_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libhackrf.a

# install firmware
cd ..
mkdir -p %{buildroot}%{_datadir}/hackrf/firmware/
install -m644 firmware-bin/* %{buildroot}%{_datadir}/hackrf/firmware

%pre udev
getent group %{hackrf_group} >/dev/null || groupadd -r %{hackrf_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%license ../COPYING
%doc ../RELEASENOTES ../Readme.md
%{_bindir}/hackrf_clock
%{_bindir}/hackrf_cpldjtag
%{_bindir}/hackrf_debug
%{_bindir}/hackrf_info
%{_bindir}/hackrf_operacake
%{_bindir}/hackrf_spiflash
%{_bindir}/hackrf_sweep
%{_bindir}/hackrf_transfer

%files -n %{libname}
%{_libdir}/libhackrf.so.%{sover}*

%files udev
%{_udevrulesdir}/53-hackrf.rules

%files devel
%{_libdir}/libhackrf.so
%{_includedir}/libhackrf
%{_libdir}/pkgconfig/libhackrf.pc

%files firmware
%dir %{_datadir}/hackrf
%{_datadir}/hackrf/firmware

%changelog
