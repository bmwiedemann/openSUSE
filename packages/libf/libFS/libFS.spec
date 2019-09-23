#
# spec file for package libFS
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libFS
%define lname	libFS6
Version:        1.0.8
Release:        0
Summary:        X Font Service client library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libFS
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libFS/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xtrans)

%description
This library is used by clients of X Font Servers (xfs), such as
xfsinfo, xfslsfonts, and the X servers themselves.

%package -n %lname
Summary:        X Font Service client library
Group:          System/Libraries

%description -n %lname
This library is used by clients of X Font Servers (xfs), such as
xfsinfo, xfslsfonts, and the X servers themselves.

%package devel
Summary:        Development files for the X Font Service client library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
This library is used by clients of X Font Servers (xfs), such as
xfsinfo, xfslsfonts, and the X servers themselves.

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
%_libdir/libFS.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libFS.so
%_libdir/pkgconfig/libfs.pc
%_docdir/%name

%changelog
