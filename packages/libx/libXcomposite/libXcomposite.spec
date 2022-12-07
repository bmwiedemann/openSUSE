#
# spec file for package libXcomposite
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


Name:           libXcomposite
%define lname	libXcomposite1
Version:        0.4.6
Release:        0
Summary:        X11 protocol Composite extension client library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://wiki.freedesktop.org/wiki/Software/CompositeExt

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXcomposite
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXcomposite/
Source0:        http://xorg.freedesktop.org/archive/individual/lib/%name-%version.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(compositeproto) >= 0.4
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
The Composite extension causes a entire sub-tree of the window
hierarchy to be rendered to an off-screen buffer. Applications can
then take the contents of that buffer and do whatever they like. The
off-screen buffer can be automatically merged into the parent window
or merged by external programs, called compositing managers.

%package -n %lname
Summary:        X11 protocol Composite extension client library
Group:          System/Libraries

%description -n %lname
The Composite extension causes a entire sub-tree of the window
hierarchy to be rendered to an off-screen buffer. Applications can
then take the contents of that buffer and do whatever they like. The
off-screen buffer can be automatically merged into the parent window
or merged by external programs, called compositing managers.

%package devel
Summary:        Development files for the X11 Composite extension library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The composite extension provides several related mechanisms:
- Per-hierarchy storage: The rendering of an entire hierarchy of
  windows is redirected to off-screen storage.
- Automatic shadow update: When a hierarchy is rendered off-screen,
  the X server provides an automatic mechanism for presenting those
  contents within the parent window.
- Composite overlay window: provides compositing managers with a
  surface on which to draw without interference.
- Parent window clipping: modifies the semantics of parent window
  clipping in the presence of manual redirected children.

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
%_libdir/libXcomposite.so.1*

%files devel
%defattr(-,root,root)
%_includedir/X11/*
%_libdir/libXcomposite.so
%_libdir/pkgconfig/xcomposite.pc
%_mandir/man3/*

%changelog
