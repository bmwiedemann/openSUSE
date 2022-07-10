#
# spec file for package libxmp
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


Name:           libxmp
%define lname	libxmp4
Version:        4.5.0+g613.8e4a5e15
Release:        0
Summary:        Module Player library for MOD, S3M, IT and others
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            http://xmp.sf.net/

#Git-Clone:	https://github.com/libxmp/libxmp
#Source:         https://github.com/libxmp/libxmp/releases/download/%name-%version/%name-%version.tar.gz
Source:         %name-%version.tar.xz
BuildRequires:  c_compiler
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

%package -n %lname
Summary:        Module Player library for MOD, S3M, IT and others
Group:          System/Libraries

%description -n %lname
libxmp is a module player library which supports many module formats,
including Protacker MOD, ScreamTracker S3M and ImpulseTracker IT.

%package devel
Summary:        Development files for libxmp, a MOD/S3M/IT/etc. module player library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libxmp is a module player library which supports many module formats,
including MOD, S3M and IT. Possible applications for libxmp include
standalone module players, module player plugins for other players,
module information extractors, background music replayers for games
and other applications, converters, etc.

This subpackage contains headers and library development files for
libxmp.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
b="%buildroot"
%make_install
mkdir -p "$b/%_mandir/man3" "$b/%_docdir/%name"
cp -av docs/Changelog docs/[a-z]* "$b/%_docdir/%name/"
# Remove file due to bnc#808655, and because they are hardware-specific
# and should not have much relevance for developers anyhow.
rm -fv "$b/%_docdir/%name"/{adlib*,ay*.txt}

%check
%make_build check

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libxmp.so.4*
%license docs/COPYING.LIB

%files devel
%_includedir/xmp.h
%_libdir/libxmp.so
%_libdir/pkgconfig/libxmp.pc
%_docdir/%name/

%changelog
