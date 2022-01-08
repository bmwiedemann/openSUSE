#
# spec file
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


%if "@BUILD_FLAVOR@" != ""
%define pprefix @BUILD_FLAVOR@-
%define psuffix -@BUILD_FLAVOR@
%else
%define psuffix %nil
%endif
%define lname libuna1

Name:           libuna%psuffix
Version:        20220102
Release:        0
Summary:        Library to support Unicode and ASCII (byte string) conversions
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libyal/libuna/
Source:         https://github.com/libyal/libuna/releases/download/%version/libuna-alpha-%version.tar.gz
Source2:        https://github.com/libyal/libuna/releases/download/%version/libuna-alpha-%version.tar.gz.asc
Source3:        libuna.keyring
Patch1:         system-libs.patch
BuildRequires:  c_compiler
BuildRequires:  gettext-tools >= 0.18.1
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcdatetime) >= 20200510
BuildRequires:  pkgconfig(libcerror) >= 20220101
%if "@BUILD_FLAVOR@" != "mini"
BuildRequires:  pkgconfig(libcfile) >= 20201229
%endif
BuildRequires:  pkgconfig(libclocale) >= 20210526
BuildRequires:  pkgconfig(libcnotify) >= 20200913

%description
libuna is a library to support Unicode and ASCII (byte string)
conversions. It currently supports: 7-bit ASCII, ISO 8859-{1..15},
Windows 874, 932, 936, 949, 950, 1250, 1251, 1252, 1253, 1254, 1255,
1256, 1257, 1258, KOI8-R, KOI8-U, UTF-7, UTF-8, UTF-16, UTF-32.

%package -n %lname%psuffix
Summary:        Library to support Unicode and ASCII (byte string) conversions
Group:          System/Libraries
%if "@BUILD_FLAVOR@" == ""
Obsoletes:      %lname-mini
%endif

%description -n %lname%psuffix
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
Requires:       %lname%psuffix = %version
%if "@BUILD_FLAVOR@" == ""
Obsoletes:      libuna-mini-devel
%endif

%description devel
libuna is a library to support Unicode and ASCII (byte string)
conversions.

This subpackage contains libraries and header files for developing
applications that want to make use of libuna.

%prep
%autosetup -p1 -n libuna-%version

%build
autoreconf -fi
%configure \
%if "@BUILD_FLAVOR@" == "mini"
	--disable-tools \
%endif
	--disable-static --enable-wide-character-type
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname%psuffix -p /sbin/ldconfig
%postun -n %lname%psuffix -p /sbin/ldconfig

%files -n %lname%psuffix
%license COPYING
%_libdir/libuna.so.1*

%if "@BUILD_FLAVOR@" != "mini"
%files tools
%_bindir/una*
%_mandir/man1/unaexport.1*
%endif

%files devel
%_includedir/libuna*
%_libdir/libuna.so
%_libdir/pkgconfig/libuna.pc
%_mandir/man3/libuna.3*

%changelog
