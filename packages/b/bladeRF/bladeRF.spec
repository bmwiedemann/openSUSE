#
# spec file for package bladeRF
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013-2015 Wojciech Kazubski, wk@ire.pw.edu.pl
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


%define sover 2
%define libname lib%{name}%{sover}
%define libversion 2.5.0
%define release_name 2023.02
%define bladerf_group bladerf
%define use_syslog 0
Name:           bladeRF
Version:        2023.02
Release:        0
Summary:        SDR radio receiver
License:        AGPL-3.0-or-later AND GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://nuand.com/
#Git-Clone:     https://github.com/Nuand/bladeRF.git
Source0:        https://github.com/Nuand/bladeRF/archive/%{release_name}.tar.gz#/%{name}-%{release_name}.tar.xz
Source1:        ad9361.tar.xz
Patch0:         bladeRF-doxygen-no-timestamp.patch
BuildRequires:  cmake >= 2.8.4
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  help2man
BuildRequires:  pkgconfig
BuildRequires:  tecla-devel
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
The software for bladeRF USB 3.0 Superspeed Software Defined Radio.

%package -n %{libname}
Summary:        SDR radio receiver library
Group:          System/Libraries
Version:        %{libversion}
Release:        0
Requires:       %{name}-udev

%description -n %{libname}
Library for bladeRF, an SDR transceiver.

%package -n %{libname}-doc
Summary:        Documentation for libbladeRF
Group:          Documentation/HTML
Version:        %{libversion}
Release:        0

%description -n %{libname}-doc
HTML documentation files for libbladeRF.

%package udev
Summary:        Udev rules for bladeRF
Group:          Hardware/Other
Requires(pre):  shadow

%description udev
Udev rules for bladeRF.

%package devel
Summary:        Development files for libbladeRF
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{libversion}

%description devel
Libraries and header files for developing applications that want to make
use of libbladerf.

%prep
%setup -q -n %{name}-%{release_name}
%patch0 -p1
ls
pushd thirdparty/analogdevicesinc/no-OS
tar -xJf %{SOURCE1}
popd

%build
cd host
%cmake \
  -DVERSION_INFO_EXTRA="" \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
  -DBLADERF_GROUP=%{bladerf_group} \
%if 0%{?use_syslog}
  -DENABLE_LIBBLADERF_SYSLOG=ON \
%endif
  -DBUILD_DOCUMENTATION=ON
%cmake_build

%install
cd host
%cmake_install

#move docs
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}/%{_datadir}/doc/libbladeRF %{buildroot}%{_docdir}

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig

%pre udev
getent group %{bladerf_group} >/dev/null || groupadd -r %{bladerf_group}

%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license COPYING
%doc README.md CONTRIBUTORS
%{_bindir}/bladeRF-cli
%{_bindir}/bladeRF-fsk
%{_mandir}/man1/bladeRF-cli.1%{?ext_man}

%files udev
%{_udevrulesdir}/88-nuand-*.rules

%files -n %{libname}
%{_libdir}/libbladeRF.so.%{sover}*

%files -n %{libname}-doc
%{_docdir}/libbladeRF

%files devel
%{_libdir}/libbladeRF.so
%{_includedir}/bladeRF1.h
%{_includedir}/bladeRF2.h
%{_includedir}/libbladeRF.h
%{_libdir}/pkgconfig/libbladeRF.pc

%changelog
