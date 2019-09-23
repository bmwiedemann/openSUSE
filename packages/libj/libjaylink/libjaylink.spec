#
# spec file for package libjaylink
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


Name:           libjaylink
Version:        0.1.0
Release:        0
Url:            http://git.zapb.de/libjaylink.git
Summary:        USB interface library for J-Link
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Source:         libjaylink-%{version}.tar.xz
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): udev
Requires(postun): udev
%define _udevdir %(pkg-config --variable udevdir udev)
Provides:       libjaylink0:%{_udevdir}/rules.d/99-libjaylink.rules

%description
Library for accessing Segger J-Link USB devices.

%package -n libjaylink0
Summary:        USB interface library for J-Link
Group:          System/Libraries
Recommends:     libjaylink

%description -n libjaylink0
Library for accessing Segger J-Link USB devices.

%package devel
Summary:        USB interface library for J-Link -- development files
Group:          Development/Libraries/C and C++
Requires:       libjaylink0 = %{version}

%description devel
Library for accessing Segger J-Link USB devices.

This sub-package contains the development files.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libjaylink.la
mkdir -p %{buildroot}%{_udevdir}/rules.d
sed -e 's/GROUP="plugdev"/GROUP="users"/' <contrib/99-libjaylink.rules >%{buildroot}%{_udevdir}/rules.d/99-libjaylink.rules

%post
%udev_rules_update

%postun
%udev_rules_update

%post -n libjaylink0 -p /sbin/ldconfig

%postun -n libjaylink0 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_udevdir}/rules.d/99-libjaylink.rules

%files -n libjaylink0
%defattr(-,root,root,-)
%{_libdir}/libjaylink.so.0*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libjaylink/
%{_libdir}/libjaylink.so
%{_libdir}/pkgconfig/libjaylink.pc

%changelog
