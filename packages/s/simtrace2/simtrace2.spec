#
# spec file for package simtrace2
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           simtrace2
Version:        0.7.1
Release:        0
Summary:        Osmocom SIMtrace host utility
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/Utilities
URL:            https://osmocom.org/projects/simtrace2/wiki
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libosmocore)
BuildRequires:  pkgconfig(libosmosim)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libosmousb) >= 0.0.0
BuildRequires:  pkgconfig(udev)

%description
Osmocom SIMtrace 2 is a software and hardware system for passively
tracing SIM-ME communication between the SIM card and the mobile phone,
and remote SIM operation.

This package contains SIMtrace 2 host utility.

%package -n libosmo-simtrace2-0
Summary:        Driver functions for Osmocom SIMtrace2 and compatible firmware
Group:          System/Libraries

%description -n libosmo-simtrace2-0
This library contains core "driver" functionality to interface with the
Osmocom SIMtrace2 (and compatible) USB device firmware.  It enables
applications to implement SIM card / smart card tracing as well as
SIM / smart card emulation functions.

%package -n libosmo-simtrace2-devel
Summary:        Development files for the Osmocom SIMtrace2 library
Group:          Development/Libraries/C and C++
Requires:       libosmo-simtrace2-0 = %{version}

%description -n libosmo-simtrace2-devel
Osmocom SIMtrace2 (and compatible) USB device firmware.  It enables
applications to implement SIM card / smart card tracing as well as
SIM / smart card emulation functions.

This subpackage contains libraries and header files for developing
applications that want to make use of libosmo-simtrace2.

%prep
%setup -q

%build
cd host
echo "%{version}" >.tarball-version
autoreconf -fiv
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install -C host
install -Dm0644 host/contrib/99-simtrace2.rules %{buildroot}/%{_udevrulesdir}/99-simtrace2.rules
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libosmo-simtrace2-0 -p /sbin/ldconfig
%postun -n libosmo-simtrace2-0 -p /sbin/ldconfig

%files
%license host/COPYING
%doc README.md
%{_bindir}/simtrace2-remsim
%{_bindir}/simtrace2-remsim-usb2udp
%{_bindir}/simtrace2-list
%{_bindir}/simtrace2-sniff
%{_udevrulesdir}/99-simtrace2.rules

%files -n libosmo-simtrace2-0
%{_libdir}/libosmo-simtrace2.so.0*

%files -n libosmo-simtrace2-devel
%dir %{_includedir}/osmocom/
%dir %{_includedir}/osmocom/simtrace2/
%{_includedir}/osmocom/simtrace2/*.h
%{_libdir}/libosmo-simtrace2.so
%{_libdir}/pkgconfig/libosmo-simtrace2.pc

%changelog
