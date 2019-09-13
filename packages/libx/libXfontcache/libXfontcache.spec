#
# spec file for package libXfontcache
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libXfontcache
%define lname	libXfontcache1
Version:        1.0.5
Release:        0
Summary:        X TrueType font cache extension client library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXfontcache
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXfontcache/
Source:         http://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontcacheproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.3

%description
FontCache is an extension that is used by X TrueType to cache
information about fonts.

%package -n %lname
Summary:        X TrueType font cache extension client library
Group:          System/Libraries

%description -n %lname
FontCache is an extension that is used by X TrueType to cache
information about fonts.

%package devel
Summary:        Development files for the X TrueType font cache library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
FontCache is an extension that is used by X TrueType to cache
information about fonts.

This package contains the development headers for the library found
in %lname.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_prefix

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libXfontcache.so.1*

%files devel
%defattr(-,root,root)
%_libdir/libXfontcache.so
%_libdir/pkgconfig/xfontcache.pc
%_mandir/man3/*

%changelog
