#
# spec file for package qatlib
#
# Copyright (c) 2021 SUSE LLC
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
Version:        20.10.20201116T163433.0257eb1
Release:        0
Summary:        Intel QuickAssist Technology Library
License:        BSD-3-clause
Group:          Hardware/Other
URL:            https://github.com/intel/qatlib
Source:         %{name}-%{version}.tar.xz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(zlib)
# This package can be built on all archs, but is useful only on enterprise-class intel.
ExclusiveArch:  x86_64

%package devel
Summary:        Development files for qatlib
Requires:       %{name}

%description
This package provides user space libraries that allow access to Intel(R)
QuickAssist devices for hardware-accelerated cryptography.
The QuickAssist APIs allow for finer control over the qat_4xxx devices
than the more general libkcapi.

%description devel
Header files for using the Intel(R) QuickAssist C APIs.
These APIs allow for finer control over the qat_4xxx devices
than the more general libkcapi.

%prep
%setup -q
autoreconf -iv

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/*.so.[0-9]

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_mandir}/man8/qat*
%{_unitdir}/qat*
%{_libdir}/lib*.so.0.*
%{_sbindir}/qat*

%files devel
%{_includedir}/qat
%{_libdir}/lib*.so

%changelog
