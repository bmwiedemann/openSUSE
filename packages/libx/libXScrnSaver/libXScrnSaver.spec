#
# spec file for package libXScrnSaver
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


Name:           libXScrnSaver
%define lname	libXss1
Version:        1.2.4
Release:        0
Summary:        X11 Screen Saver extension client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXScrnSaver
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXScrnSaver/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(scrnsaverproto) >= 1.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package -n %lname
Summary:        X11 Screen Saver extension client library
Group:          System/Libraries
Provides:       %name = %version-%release

%description -n %lname
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

%package -n libXss-devel
Summary:        Development files for the X11 Screen Saver extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Provides:       libXScrnSaver-devel = 1.2.2
Obsoletes:      libXScrnSaver-devel < 1.2.2

%description -n libXss-devel
The X Window System provides support for changing the image on a
display screen after a user-settable period of inactivity to avoid
burning the cathode ray tube phosphors. This extension allows an
external "screen saver" client to detect when the alternate image is
to be displayed and to provide the graphics.

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
%_libdir/libXss.so.1*

%files -n libXss-devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXss.so
%_libdir/pkgconfig/xscrnsaver.pc
%_mandir/man3/*

%changelog
