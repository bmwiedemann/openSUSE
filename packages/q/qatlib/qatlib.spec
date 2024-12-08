#
# spec file for package qatlib
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


Name:           qatlib
Version:        24.09.0
Release:        0
Summary:        Intel QuickAssist Technology Library
License:        BSD-3-Clause
Group:          Hardware/Other
URL:            https://github.com/intel/qatlib
Source:         https://github.com/intel/qatlib/archive/refs/tags/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(numa)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# This package can be built on all archs, but is useful only on enterprise-class intel.
ExclusiveArch:  x86_64

%package -n libusdm0
Summary:        QuickAssist memory management library

%description -n libusdm0
User space library for memory management.

%package -n libqat4
Summary:        QuickAssist device access library

%description -n libqat4
User space library for accessing Intel QAT devices.

%package devel
Summary:        Development files for qatlib
Group:          Hardware/Other
Requires:       libqat4 = %{version}-%{release}
Requires:       libusdm0 = %{version}-%{release}

%description
This package provides user space libraries that allow access to Intel
QuickAssist devices for hardware-accelerated cryptography.
The QuickAssist APIs allow for finer control over the qat_4xxx devices
than the more general libkcapi.

%description devel
Header files for using the Intel QuickAssist C APIs.
These APIs allow for finer control over the qat_4xxx devices
than the more general libkcapi.

%prep
%autosetup
autoreconf -iv

%build
%configure --disable-static --enable-legacy-algorithms
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/*.so.[0-9]

%ldconfig_scriptlets -n libusdm0
%ldconfig_scriptlets -n libqat4

%files
%license LICENSE
%doc README.md
%{_mandir}/man8/qat*
%{_unitdir}/qat*
%{_sbindir}/qat*

%files -n libusdm0
%{_libdir}/libusdm.so.0*

%files -n libqat4
%{_libdir}/libqat.so.4*

%files devel
%{_includedir}/qat
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/libqat.pc
%{_libdir}/pkgconfig/libusdm.pc
%{_libdir}/pkgconfig/qatlib.pc

%changelog
