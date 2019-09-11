#
# spec file for package libusb-1_0
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _name libusb
%define debug_package_requires libusb-1_0-0 = %{version}-%{release}
Name:           libusb-1_0
Version:        1.0.22
Release:        0
Summary:        USB Library
License:        LGPL-2.1-or-later
Group:          System/Hardware
URL:            http://libusb.info/
Source:         https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  dos2unix
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)

%description
Libusb is a library that allows userspace access to USB devices.

%package -n libusb-1_0-0
Summary:        USB Library
Group:          System/Libraries

%description -n libusb-1_0-0
Libusb is a library that allows userspace access to USB devices.

%package devel
Summary:        USB Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libusb-1_0-0 = %{version}

%description devel
Libusb is a library that allows userspace access to USB devices.

%prep
%setup -q -n %{_name}-%{version}
dos2unix NEWS

%build
%configure \
    --with-pic \
    --disable-silent-rules \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libusb-1_0-0 -p /sbin/ldconfig
%postun -n libusb-1_0-0 -p /sbin/ldconfig

%files -n libusb-1_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc PORTING
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
