#
# spec file for package libXaw
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


Name:           libXaw
Version:        1.0.15
Release:        0
Summary:        The X Athena Widget Set
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXaw
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXaw/
Source:         http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#git#BuildRequires:	autoconf >= 2.60, automake, libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xextproto)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.12
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xt)

%description
The X Window System Athena widget set implements simple user
interfaces based upon the X Toolkit Intrinsics (Xt) library.

%package -n libXaw6
Summary:        The X Athena Widget Set
Group:          System/Libraries
%ifarch ppc64 s390x x86_64 sparc64
Provides:       libXaw6.so.6()(64bit)
%else
Provides:       libXaw6.so.6
%endif

%description -n libXaw6
The X Window System Athena widget set implements simple user
interfaces based upon the X Toolkit Intrinsics (Xt) library.

%package -n libXaw7
Summary:        The X Athena Widget Set
Group:          System/Libraries
%ifarch ppc64 s390x x86_64 sparc64
Provides:       libXaw7.so.7()(64bit)
%else
Provides:       libXaw7.so.7
%endif

%description -n libXaw7
The X Window System Athena widget set implements simple user
interfaces based upon the X Toolkit Intrinsics (Xt) library.

%package -n libXaw8
Summary:        The X Athena Widget Set
Group:          System/Libraries
Requires:       libXaw7 = %version
%ifarch ppc64 s390x x86_64 sparc64
Provides:       libXaw.so.8()(64bit)
Provides:       libXaw8.so.8()(64bit)
%else
Provides:       libXaw.so.8
Provides:       libXaw8.so.8
%endif

%description -n libXaw8
The X Window System Athena widget set implements simple user
interfaces based upon the X Toolkit Intrinsics (Xt) library.

%package devel
Summary:        Development files for the X Athena Widget Set
Group:          Development/Libraries/C and C++
Requires:       libXaw6 = %version
Requires:       libXaw7 = %version
Requires:       libXaw8 = %version

%description devel
The X Window System Athena widget set implements simple user
interfaces based upon the X Toolkit Intrinsics (Xt) library.

This package contains the development headers for the library found
in libXaw6/libXaw7/libXaw8.

%prep
%setup -q

%build
%configure --docdir=%_docdir/%name --disable-static
make %{?_smp_mflags}

%install
b="%buildroot";
make install DESTDIR="$b"
rm -f "$b/%_libdir"/*.la

# For compatibility reasons
ln -s libXaw7.so.7 "$b/%_libdir/libXaw8.so.8";
ln -s libXaw.so.7 "$b/%_libdir/libXaw.so.8";

%post -n libXaw6 -p /sbin/ldconfig

%postun -n libXaw6 -p /sbin/ldconfig

%post -n libXaw7 -p /sbin/ldconfig

%postun -n libXaw7 -p /sbin/ldconfig

%post -n libXaw8 -p /sbin/ldconfig

%postun -n libXaw8 -p /sbin/ldconfig

%files -n libXaw6
%defattr(-,root,root)
%_libdir/libXaw6.so.6*
%_libdir/libXaw.so.6*

%files -n libXaw7
%defattr(-,root,root)
%_libdir/libXaw7.so.7*
%_libdir/libXaw.so.7*

%files -n libXaw8
%defattr(-,root,root)
%_libdir/libXaw8.so.8*
%_libdir/libXaw.so.8*

%files devel
%defattr(-,root,root)
%_includedir/X11/Xaw
%_libdir/libXaw*.so
%_libdir/pkgconfig/xaw*.pc
%_mandir/man3/Xaw.3*
%_docdir/%name

%changelog
