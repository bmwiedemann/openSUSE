#
# spec file for package liboldX
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


Name:           liboldX
%define lname	liboldX6
Version:        1.0.1
Release:        0
Summary:        X version 10 backwards compatibility library
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://cgit.freedesktop.org/xorg/lib/liboldX/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/liboldX
Source:         http://xorg.freedesktop.org/releases/X11R7.0/src/lib/%{name}-X11R7.0-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.57, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)

%description
(Upstream has not provided a description)

%package -n %lname
Summary:        X version 10 backwards compatibility library
Group:          System/Libraries

%description -n %lname
(Upstream has not provided a description)

%package devel
Summary:        Development files for the X version 10 compatibility library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
(Upstream has not provided a description)

This package contains the development headers for the library found
in %lname.

%prep
%setup -qn %name-X11R7.0-%version

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
rm -f "%buildroot/%_libdir"/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/liboldX.so.6*

%files devel
%defattr(-,root,root)
%_includedir/X11/X10.h
%_libdir/liboldX.so
%_libdir/pkgconfig/oldx.pc

%changelog
