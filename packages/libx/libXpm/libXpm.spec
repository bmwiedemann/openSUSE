#
# spec file for package libXpm
#
# Copyright (c) 2023 SUSE LLC
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


%define lname	libXpm4
Name:           libXpm
Version:        3.5.16
Release:        0
Summary:        X Pixmap image file format library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://xorg.freedesktop.org/
#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXpm
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXpm/
Source:         https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        https://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz.sig
Source2:        libXpm.keyring
Source9:        baselibs.conf
BuildRequires:  /usr/bin/gzip
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)

%description
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

%package -n %{lname}
Summary:        X Pixmap image file format library
Group:          System/Libraries
# Invokes 'gzip' and 'uncompress' at runtime.
Requires:       /usr/bin/gzip
Requires:       /usr/bin/uncompress
# 'compress' (ncompress package) is not available on SLE
Suggests:       /usr/bin/compress

%description -n %{lname}
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

%package devel
Summary:        Development files for the X Pixmap image file format library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
# O/P added for 12.2
Provides:       xorg-x11-libXpm-devel = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libXpm-devel < 7.6_%{version}-%{release}

%description devel
libXpm facilitates working with XPM (X PixMap), a format for
storing/retrieving X pixmaps to/from files.

This package contains the development headers for the library found
in %{lname}.

%package tools
Summary:        Conversion utilities for X Pixmap (XPM) files
# O/P added for 12.2
Group:          Productivity/Graphics/Convertors
Provides:       xorg-x11-libXpm = 7.6_%{version}-%{release}
Obsoletes:      xorg-x11-libXpm < 7.6_%{version}-%{release}

%description tools
The spxm tool converts XPM1/XPM2 files to XPM version 3.
The cxpm tool will check whether an XPM file is correct or not with
regard to its format.

%prep
%autosetup -p1

%build
autoreconf -fi
export XPM_PATH_COMPRESS=%{_bindir}/compress
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%{_libdir}/libXpm.so.4*

%files devel
%{_includedir}/X11/*
%{_libdir}/libXpm.so
%{_libdir}/pkgconfig/xpm.pc
%{_mandir}/man3/*.3%{?ext_man}

%files tools
%{_bindir}/cxpm
%{_bindir}/sxpm
%{_mandir}/man1/cxpm.1%{?ext_man}
%{_mandir}/man1/sxpm.1%{?ext_man}

%changelog
