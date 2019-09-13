#
# spec file for package libuna
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


Name:           libuna
%define lname	libuna1
%define timestamp 20190102
Version:        0~%timestamp
Release:        0
Summary:        Library to support Unicode and ASCII (byte string) conversions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/libyal/libuna/wiki
Source:         https://github.com/libyal/libuna/releases/download/%timestamp/%{name}-alpha-%timestamp.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdatetime)
BuildRequires:  pkgconfig(libcerror) >= 20150101
BuildRequires:  pkgconfig(libcfile) >= 20120526
BuildRequires:  pkgconfig(libclocale) >= 20120425
BuildRequires:  pkgconfig(libcnotify) >= 20121224
# Using versions from OBS fails, tested 1/8/2015
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libuna is a library to support Unicode and ASCII (byte string)
conversions. It currently supports: 7-bit ASCII, ISO 8859-{1..15},
Windows 874, 932, 936, 949, 950, 1250, 1251, 1252, 1253, 1254, 1255,
1256, 1257, 1258, KOI8-R, KOI8-U, UTF-7, UTF-8, UTF-16, UTF-32.

%package -n %lname
Summary:        Library to support Unicode and ASCII (byte string) conversions
Group:          System/Libraries

%description -n %lname
libuna is a library to support Unicode and ASCII (byte string)
conversions.

%package tools
Summary:        Utilities from libuna for Unicode/ASCII Byte Stream conversions
Group:          Development/Tools/Other

%description tools
Several tools for converting Unicode and ASCII (byte stream) based text.

%package devel
Summary:        Development files for libuna, a library to support Unicode/ASCII conversions
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
libuna is a library to support Unicode and ASCII (byte string)
conversions.

This subpackage contains libraries and header files for developing
applications that want to make use of libuna.

%prep
%setup -qn libuna-%timestamp

%build
%configure --disable-static --enable-wide-character-type --enable-python
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog ABOUT-NLS
%{_libdir}/libuna.so.1*

%files tools
%defattr(-,root,root)
%{_bindir}/una*
%{_mandir}/man1/unaexport.1*

%files devel
%defattr(-,root,root)
%{_includedir}/libuna*
%{_libdir}/libuna.so
%{_libdir}/pkgconfig/libuna.pc
%{_mandir}/man3/libuna.3*

%changelog
