#
# spec file for package i2c-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           i2c-tools
Version:        4.1
Release:        0
Summary:        A heterogeneous set of I2C tools for Linux
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
Requires:       udev
Recommends:     modules
Url:            https://i2c.wiki.kernel.org/index.php/I2C_Tools
Source0:        https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.xz
Source1:        https://www.kernel.org/pub/software/utils/i2c-tools/%{name}-%{version}.tar.sign
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x

%description
This package contains a heterogeneous set of I2C tools for Linux: a bus
probing tool, a chip dumper, register-level access helpers, EEPROM
decoding scripts, and more.

%package -n libi2c0
Summary:        I2C/SMBus bus access library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libi2c0
libi2c offers a way for applications to interact with the devices
connected to the I2C or SMBus buses of the system.

%package -n libi2c0-devel
Summary:        Development files for the I2C/SMBus bus access library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libi2c0 = %{version}
Provides:       /usr/include/i2c/smbus.h

%description -n libi2c0-devel
libi2c offers a way for applications to interact with the devices
connected to the I2C or SMBus buses of the system.

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CC="%{__cc}" BUILD_STATIC_LIB:=0

%install
%make_install PREFIX=/usr libdir=%{_libdir} BUILD_STATIC_LIB:=0
# cleanup
rm -f "%{buildroot}/usr/bin/decode-edid"

%post -n libi2c0 -p /sbin/ldconfig

%postun -n libi2c0 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/man1/*.1.gz
%{_mandir}/man8/*.8.gz

%files -n libi2c0
%{_libdir}/libi2c.so.0*

%files -n libi2c0-devel
%{_libdir}/libi2c.so
%dir %{_includedir}/i2c
%{_includedir}/i2c/smbus.h

%changelog
