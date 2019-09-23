#
# spec file for package hidapi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 0

Name:           hidapi
Version:        0.9.0
Release:        0
Summary:        Simple library for communicating with USB and Bluetooth HID devices
License:        GPL-3.0-or-later OR BSD-3-Clause
Group:          System/Libraries
Url:            https://github.com/libusb/hidapi
Source:         https://github.com/libusb/hidapi/archive/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE do_not_install_docs.patch -- don't let make install put files into /usr/share/doc/packages
Patch0:         do_not_install_docs.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  make
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks, it is most useful when used with custom (Vendor-Defined) HID devices.

%package -n libhidapi-devel
Summary:        Development libraries and header files for hidapi
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libhidapi-hidraw%{sover} = %{version}
Requires:       libhidapi-libusb%{sover} = %{version}
Requires:       libudev-devel
Requires:       libusb-1_0-devel

%description -n libhidapi-devel
This package contains the header files and libraries for building
programs using the hidapi library.

%package -n libhidapi-hidraw%{sover}
Summary:        Simple library for communicating with USB and Bluetooth HID devices
Group:          System/Libraries

%description -n libhidapi-hidraw%{sover}
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks, it is most useful when used with custom (Vendor-Defined) HID devices.

%package -n libhidapi-libusb%{sover}
Summary:        Simple library for communicating with USB and Bluetooth HID devices
Group:          System/Libraries

%description -n libhidapi-libusb%{sover}
HIDAPI is a library which allows an application to interface with USB and Bluetooth HID-Class devices.
While it can be used to communicate with standard HID devices like keyboards, mice, and Joysticks, it is most useful when used with custom (Vendor-Defined) HID devices.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

%build
./bootstrap
%configure --disable-static --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
make install DESTDIR=%{?buildroot}
find %{buildroot}%{_libdir} -type f -name '*.la' -delete -print

%post -n libhidapi-libusb%{sover} -p /sbin/ldconfig
%post -n libhidapi-hidraw%{sover} -p /sbin/ldconfig

%postun -n libhidapi-libusb%{sover} -p /sbin/ldconfig
%postun -n libhidapi-hidraw%{sover} -p /sbin/ldconfig

%files -n libhidapi-devel
%defattr(-,root,root)
%doc README.md AUTHORS.txt HACKING.txt
%{_includedir}/hidapi
%{_libdir}/pkgconfig/*
%{_libdir}/libhidapi-*.so

%files -n libhidapi-hidraw%{sover}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libhidapi-hidraw.so.%{sover}*

%files -n libhidapi-libusb%{sover}
%defattr(-,root,root)
%license LICENSE*
%{_libdir}/libhidapi-libusb.so.%{sover}*

%changelog
