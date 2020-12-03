#
# spec file for package libmodbus
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libmodbus
Url:            https://www.libmodbus.org/
Summary:        Modbus Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Version:        3.1.6
Release:        0
# WARNING: tarballs from GitHub are different!
Source:         http://libmodbus.org/releases/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  pkg-config
BuildRequires:  xmlto
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%configure\
	--docdir=%{_docdir}/%{name}\
	--disable-static
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
# Installed by %%doc
rm %{buildroot}%{_docdir}/%{name}/{MIGRATION,README.md}

%post -n libmodbus5 -p /sbin/ldconfig

%postun -n libmodbus5 -p /sbin/ldconfig

%files -n libmodbus5
%defattr(-,root,root)
%doc AUTHORS MIGRATION NEWS README.md
%license COPYING.LESSER
%{_libdir}/*.so.*
%{_mandir}/man7/*.*

%files devel
%defattr(-,root,root)
%doc doc/*.txt
%{_includedir}/modbus
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.*

%changelog
