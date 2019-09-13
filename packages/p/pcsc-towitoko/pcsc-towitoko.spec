#
# spec file for package pcsc-towitoko
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           pcsc-towitoko
BuildRequires:  libtool pcsc-lite-devel pkg-config
%define _name towitoko
Version:        2.0.7
Release:        182
Group:          Productivity/Security
License:        LGPL-2.1+
Url:            http://www.geocities.com/cprados
Summary:        PCSC driver for Towitoko Smart Card Readers
Source:         %{_name}-%{version}.tar.bz2
Patch:          %{_name}-%{version}-install.diff
Patch1:         %{_name}-destdir.patch
Patch2:         towitoko-2.0.7-implicit-decls.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       pcsc-lite
Supplements:    modalias(usb:v067Bp2303d*dc*dsc*dp*ic*isc*ip*)
%define ifddir %(pkg-config libpcsclite --variable=usbdropdir)

%description
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.



Authors:
--------
    Carlos Prados <cprados@yahoo.com>
    David Corcoran <corcoran@linuxnet.com>

%package -n libtowitoko2
License:        LGPL-2.1+
Summary:        Library for PCSC driver for Towitoko Smart Card Readers
Group:          System/Libraries

%description -n libtowitoko2
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.



Authors:
--------
    Carlos Prados <cprados@yahoo.com>
    David Corcoran <corcoran@linuxnet.com>

%package devel
License:        LGPL-2.1+
Summary:        PCSC driver for Towitoko Smart Card Readers
Group:          Development/Libraries/C and C++
Requires:       libtowitoko2 = %{version}

%description devel
This package contains a driver for Towitoko Chipdrive Micro, Extern,
Extern II, Intern, and Twin and Kartenzwerg smart card readers.

This driver is meant to be used with the PCSC-Lite daemon from the
pcsc-lite package.

Please note, that many modern Towitoko readers are supported by the
openct package.



Authors:
--------
    Carlos Prados <cprados@yahoo.com>
    David Corcoran <corcoran@linuxnet.com>

%prep
%setup -q -n %{_name}-%{version}
%patch
%patch1
%patch2

%build
autoreconf -f -i
%configure\
	--includedir=%{_includedir}/PCSC/towitoko\
	--with-pcsc-lite-dir=%{ifddir}\
	--enable-win32-com\
	--enable-usb-bundle
make %{?jobs:-j%jobs}

%install
%makeinstall
mv $RPM_BUILD_ROOT%{_bindir}/tester $RPM_BUILD_ROOT%{_bindir}/towitoko-tester

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libtowitoko2 -p /sbin/ldconfig

%postun -n libtowitoko2 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/*
%{ifddir}/*

%files -n libtowitoko2
%defattr(-,root,root)
%{_libdir}/libtowitoko.so.2
%{_libdir}/libtowitoko.so.2.*

%files devel
%defattr(-,root,root)
%{_includedir}/PCSC/*
%{_libdir}/*.so
%{_libdir}/*.*a
%doc %{_mandir}/man3/*.*

%changelog
