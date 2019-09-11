#
# spec file for package usbredir
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands.
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


Name:           usbredir
Version:        0.8.0
Release:        0
Summary:        A protocol for redirection USB traffic
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Url:            https://www.spice-space.org/usbredir.html
Source:         https://www.spice-space.org/download/usbredir/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libusb-1.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%package -n libusbredirhost1
Summary:        A protocol for redirection USB traffic
Group:          System/Libraries

%description -n libusbredirhost1
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%package -n libusbredirparser1
Summary:        A protocol for redirection USB traffic
Group:          System/Libraries
Obsoletes:      libusbredirparser0 < %{version}
Provides:       libusbredirparser0 = %{version}

%description -n libusbredirparser1
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine then the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%package devel
Summary:        A protocol for redirection USB traffic - Development files
Group:          Development/Languages/C and C++
Requires:       libusbredirhost1 = %{version}
Requires:       libusbredirparser1 = %{version}

%description devel
usbredir is a protocol for redirection USB traffic from a single USB device,
to a different (virtual) machine than the one to which the USB device is
attached. See usb-redirection-protocol.txt for the description / definition
of this protocol.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install LIBDIR=%{_libdir} PREFIX=%{_prefix}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libusbredirhost1 -p /sbin/ldconfig
%postun -n libusbredirhost1 -p /sbin/ldconfig
%post -n libusbredirparser1 -p /sbin/ldconfig
%postun -n libusbredirparser1 -p /sbin/ldconfig
%files
%defattr(-,root,root)
%doc ChangeLog README
%license COPYING
%{_mandir}/man1/usbredirserver.1.gz
%{_sbindir}/usbredirserver

%files -n libusbredirhost1
%defattr(-, root, root)
%{_libdir}/libusbredirhost.so.*

%files -n libusbredirparser1
%defattr(-, root, root)
%{_libdir}/libusbredirparser.so.*

%files devel
%defattr(-, root, root)
%doc README.multi-thread
%{_includedir}/usbredirhost.h
%{_includedir}/usbredirfilter.h
%{_includedir}/usbredirparser.h
%{_includedir}/usbredirproto.h
%{_libdir}/libusbredirhost.so
%{_libdir}/libusbredirparser.so
%{_libdir}/pkgconfig/libusbredirhost.pc
%{_libdir}/pkgconfig/libusbredirparser-0.5.pc

%changelog
