#
# spec file for package ndpi
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2024, Martin Hauke <mardnh@gmx.de>
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


%define sover 4
%ifarch %{ix86} x86_64
%bcond_without hyperscan
%endif
Name:           ndpi
Version:        4.12
Release:        0
Summary:        Extensible deep packet inspection library
# wireshark/ndpi.lua is GPL-3.0-or-later
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/ntop/nDPI
Source:         https://github.com/ntop/nDPI/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-makefile.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libnuma-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(json-c)
%if 0%{with hyperscan}
BuildRequires:  pkgconfig(libhs)
%endif

%description
nDPI is a ntop-maintained superset of the OpenDPI library. It extends
the original library by adding new protocols that are otherwise
available only on the paid version of OpenDPI.

%package -n libndpi%{sover}
Summary:        Extensible deep packet inspection library
Group:          System/Libraries
Requires:       ndpi-common

%description -n libndpi%{sover}
nDPI is a ntop-maintained superset of the OpenDPI library. It extends
the original library by adding new protocols that are otherwise
available only on the paid version of OpenDPI. nDPI was modified to
be more suitable for traffic monitoring applications, by disabling
specific features that slow down the DPI engine while being them
un-necessary for network traffic monitoring.

%package -n libndpi-devel
Summary:        Development headers for nNDPI
Group:          Development/Libraries/C and C++
Requires:       libndpi%{sover} = %{version}
%if 0%{with hyperscan}
Requires:       pkgconfig(libhs)
%endif

%description -n libndpi-devel
nDPI is a ntop-maintained superset of the OpenDPI library. It extends
the original library by adding new protocols that are otherwise
available only on the paid version of OpenDPI.

This package contains the Development headers for libndpi.

%package -n ndpi-tools
Summary:        Tools for nNDPI
Group:          Development/Libraries/C and C++

%description -n ndpi-tools
nDPI is a ntop-maintained superset of the OpenDPI library. It extends
the original library by adding new protocols that are otherwise
available only on the paid version of OpenDPI.

This package contains the ndpiReader binary.

%package -n ndpi-common
Summary:        Common files used by nDPI
Group:          Development/Libraries/C and C++
# version 3 rpm did not yet follow rules correctly
Conflicts:      libndpi3

%description -n ndpi-common
nDPI is a ntop-maintained superset of the OpenDPI library. It extends
the original library by adding new protocols that are otherwise
available only on the paid version of OpenDPI.

This package contains common files used by nDPI.

%prep
%autosetup -p1 -n nDPI-%{version}

%build
autoreconf -fiv
%configure \
%if 0%{with hyperscan}
    --with-hyperscan \
%endif
    %{nil}
%make_build

%install
%make_install
rm %{buildroot}/%{_libdir}/libndpi.a

%post   -n libndpi%{sover} -p /sbin/ldconfig
%postun -n libndpi%{sover} -p /sbin/ldconfig

%files -n libndpi%{sover}
%{_libdir}/libndpi.so.%{sover}*

%files -n libndpi-devel
%{_includedir}/ndpi
%{_libdir}/libndpi.so
%{_libdir}/pkgconfig/libndpi.pc

%files -n ndpi-tools
%{_bindir}/ndpiReader
%doc wireshark

%files -n ndpi-common
%license COPYING
%doc CHANGELOG.md README.md
%doc doc/guide/nDPI_QuickStartGuide.pdf
%{_datadir}/%{name}

%changelog
