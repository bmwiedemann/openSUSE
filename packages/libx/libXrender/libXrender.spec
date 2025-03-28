#
# spec file for package libXrender
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libXrender
%define lname	libXrender1
Version:        0.9.12
Release:        0
Summary:        X Rendering Extension library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://cgit.freedesktop.org/xorg/lib/libXrender/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXrender
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXrender/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(renderproto) >= 0.9
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The Xrender library is designed as a lightweight library interface to
the Render extension.

%package -n %lname
Summary:        X Rendering Extension library
# O/P added for 12.2
Group:          System/Libraries
Provides:       xorg-x11-libXrender = 7.6_%version-%release
Obsoletes:      xorg-x11-libXrender < 7.6_%version-%release

%description -n %lname
The Xrender library is designed as a lightweight library interface to
the Render extension.

%package devel
Summary:        Development files for the X11 Render Extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
# O/P added for 12.2
Provides:       xorg-x11-libXrender-devel = 7.6_%version-%release
Obsoletes:      xorg-x11-libXrender-devel < 7.6_%version-%release

%description devel
The Xrender library is designed as a lightweight library interface to
the Render extension.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXrender.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXrender.so
%_libdir/pkgconfig/xrender.pc
%_docdir/%name

%changelog
