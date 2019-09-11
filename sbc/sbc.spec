#
# spec file for package sbc
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 B1 Systems GmbH, Vohburg, Germany.
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
Version:        1.4
Release:        0
Summary:        Bluetooth Low-Complexity, Sub-Band Codec Utilities
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
Url:            http://www.kernel.org/pub/linux/bluetooth
Source:         https://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  libsndfile-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The package contains utilities for using the SBC codec.

%package -n libsbc%{sonum}
Summary:        Bluetooth Low-Complexity, Sub-Band Codec Library
License:        LGPL-2.1-or-later
Group:          Hardware/Mobile

%description -n libsbc%{sonum}
The package contains libraries for using the SBC codec.

%package devel
Summary:        Development files for libsbc%{sonum}
License:        GPL-2.0-or-later
Group:          Development/Sources
Requires:       libsbc%{sonum} = %{version}

%description devel
Development files for the SBC library

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
rm %{buildroot}/%{_libdir}/libsbc.la

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post -n libsbc%{sonum} -p /sbin/ldconfig

%postun -n libsbc%{sonum} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
/usr/bin/sbc*

%files -n libsbc%{sonum}
%defattr(-,root,root)
%{_libdir}/libsbc.so.%{sonum}
%{_libdir}/libsbc.so.%{sonum}.*

%files devel
%defattr(-,root,root)
%dir /usr/include/sbc
/usr/include/sbc/sbc.h
%{_libdir}/pkgconfig/sbc.pc
%{_libdir}/libsbc.a
%{_libdir}/libsbc.so

%changelog
