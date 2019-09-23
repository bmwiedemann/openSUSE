#
# spec file for package libwebcam
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libwebcam
Version:        0.2.5
%define so_ver  0
Release:        0
Summary:        A library for user-space configuration of the uvcvideo driver
License:        GPL-3.0+
Group:          System/Libraries
Url:            http://sourceforge.net/projects/libwebcam/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  kernel-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)

%description
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%package     -n %{name}%{so_ver}
Group:          System/Libraries
License:        LGPL-3.0+
Summary:        A library for user-space configuration of the uvcvideo driver

%description -n %{name}%{so_ver}
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

%package        devel
Summary:        Development files for libwebcam
Group:          Development/Libraries
License:        LGPL-3.0+
Requires:       %{name}%{so_ver} = %{version}

%description    devel
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

This package contains development files for libwebcam.

%package     -n uvcdynctrl
Summary:        Command line interface to libwebcam
Group:          Productivity/Multimedia/Other
License:        GPL-3.0+
Requires:       udev

%description -n uvcdynctrl
Libwebcam provides a user-space library for interaction with the uvcvideo
kernel driver. One could use this library to manipulate settings for one
or many UVC-type webcams found attached on a single computer.

This package contains command line interface to libwebcam.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm -rf %{buildroot}%{_libdir}/*.a
# fix up after dirty tarball
find %{buildroot} -name '*~' -exec rm -f '{}' \;
mkdir -p %{buildroot}/%{_libexecdir}
mv %{buildroot}/lib/udev %{buildroot}/%{_libexecdir}/udev

%post -n %{name}%{so_ver} -p /sbin/ldconfig

%postun -n %{name}%{so_ver} -p /sbin/ldconfig

%files -n uvcdynctrl
%defattr(-,root,root,-)
%doc uvcdynctrl/README uvcdynctrl/COPYING
%{_bindir}/uvcdynctrl*
%{_datadir}/uvcdynctrl
%{_datadir}/man/man1/*
%{_libexecdir}/udev/uvcdynctrl
%{_libexecdir}/udev/rules.d/*.rules

%files -n %{name}%{so_ver}
%defattr(-,root,root,-)
%doc libwebcam/README libwebcam/COPYING libwebcam/COPYING.LESSER
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
