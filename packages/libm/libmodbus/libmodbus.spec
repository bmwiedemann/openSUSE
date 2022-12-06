#
# spec file for package libmodbus
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


Name:           libmodbus
Version:        3.1.8
Release:        0
Summary:        Modbus Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.libmodbus.org/
Source:         https://github.com/stephane/libmodbus/releases/download/v%{version}/libmodbus-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  pkgconfig
BuildRequires:  xmlto

%description
libmodbus is a free software library to send/receive data with a device which
respects the Modbus protocol. This library can use a serial port or an Ethernet
connection.

The functions included in the library have been derived from the Modicon Modbus
Protocol Reference Guide which can be obtained from Schneider.

%package -n libmodbus5
Summary:        Modbus Library
Group:          System/Libraries

%description -n libmodbus5
libmodbus is a free software library to send/receive data with a device which
respects the Modbus protocol. This library can use a serial port or an Ethernet
connection.

The functions included in the library have been derived from the Modicon Modbus
Protocol Reference Guide which can be obtained from Schneider.

%package devel
Summary:        Development Files for Modbus Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libmodbus5 = %{version}

%description devel
libmodbus is a free software library to send/receive data with a device which
respects the Modbus protocol. This library can use a serial port or an Ethernet
connection.

The functions included in the library have been derived from the Modicon Modbus
Protocol Reference Guide which can be obtained from Schneider.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%configure\
	--docdir=%{_docdir}/%{name}\
	--disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Installed by %%doc
rm %{buildroot}%{_docdir}/%{name}/{AUTHORS,MIGRATION,NEWS,README.md}

%post -n libmodbus5 -p /sbin/ldconfig
%postun -n libmodbus5 -p /sbin/ldconfig

%files -n libmodbus5
%license COPYING.LESSER
%doc AUTHORS MIGRATION NEWS README.md
%{_libdir}/*.so.*

%files devel
%{_includedir}/modbus
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
