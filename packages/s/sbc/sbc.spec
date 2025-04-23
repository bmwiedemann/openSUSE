#
# spec file for package sbc
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012 B1 Systems GmbH, Vohburg, Germany.
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


%define sonum 1
Name:           sbc
Version:        2.1
Release:        0
Summary:        Bluetooth Low-Complexity, Sub-Band Codec Utilities
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://www.kernel.org/pub/linux/bluetooth
Source:         https://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sndfile)

%description
The package contains utilities for using the SBC codec.

%package -n libsbc%{sonum}
Summary:        Bluetooth Low-Complexity, Sub-Band Codec Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libsbc%{sonum}
The package contains libraries for using the SBC codec.

%package devel
Summary:        Development files for libsbc%{sonum}
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
Requires:       libsbc%{sonum} = %{version}

%description devel
Development files for the SBC library.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm -v %{buildroot}/%{_libdir}/libsbc.la

%ldconfig_scriptlets -n libsbc%{sonum}

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/sbcdec
%{_bindir}/sbcenc
%{_bindir}/sbcinfo

%files -n libsbc%{sonum}
%license COPYING.LIB
%{_libdir}/libsbc.so.%{sonum}*

%files devel
%dir %{_includedir}/sbc
%{_includedir}/sbc/sbc.h
%{_libdir}/libsbc.so
%{_libdir}/pkgconfig/sbc.pc

%changelog
