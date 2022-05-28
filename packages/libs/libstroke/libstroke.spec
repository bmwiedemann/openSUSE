#
# spec file for package libstroke
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


Name:           libstroke
Version:        0.5.1
Release:        0
Summary:        A Stroke Translation Library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.etla.net/libstroke/
Source0:        http://www.etla.net/libstroke/libstroke-%{version}.tar.bz2
Patch:          libstroke-0.4.dif
Patch1:         no-gtk1.patch
Patch2:         fix-implicit-declarations.patch
# PATCH-FIX-UPSTREAM Fix quoting of AC_DEFUN args (bnc#794807) (2013-01-07)
Patch3:         libstroke-quote_m4_definitions.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)

%description
LibStroke is a stroke interface library.  Strokes are motions of the
mouse that can be interpreted by a program as a command.  Strokes are
used extensively in CAD programs.

%package -n libstroke0
Summary:        A Stroke Translation Library
Group:          System/Libraries
Obsoletes:      libstroke
Provides:       libstroke = %{version}-%{release}

%description -n libstroke0
LibStroke is a stroke interface library.  Strokes are motions of the
mouse that can be interpreted by a program as a command.  Strokes are
used extensively in CAD programs.

%package devel
Summary:        Development package for libstroke
Group:          Development/Libraries/C and C++
Requires:       libstroke0 = %{version}-%{release}
Requires:       pkgconfig(x11)

%description devel
This package is needed if you want to program or compile applications
that use libstroke.

%prep
%setup -q
%patch
%patch1 -p1
%patch2 -p1
%patch3

%build
rm -f config.cache
# update config.{guess,sub}
autoreconf --force --install
%configure --disable-static --with-pic
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post   -n libstroke0 -p /sbin/ldconfig
%postun -n libstroke0 -p /sbin/ldconfig

%files -n libstroke0
%{_libdir}/libstroke.so.*
%license COPY*

%files -n libstroke-devel
%doc AUTHORS CREDITS ChangeLog INSTALL NEWS README* TODO
%{_libdir}/libstroke.so
/usr/include/*.h
/usr/share/aclocal/*.m4

%changelog
