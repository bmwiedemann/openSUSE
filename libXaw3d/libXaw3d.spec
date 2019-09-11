#
# spec file for package libXaw3d
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libXaw3d
Version:        1.6.3
Release:        0
Summary:        The 3D Athena Widget Set
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://xorg.freedesktop.org/

#Git-Clone:	git://anongit.freedesktop.org/xorg/lib/libXaw3d
#Git-Web:	http://cgit.freedesktop.org/xorg/lib/libXaw3d/
#Freecode-URL:	http://freecode.com/projects/xaw3d
Source:         http://xorg.freedesktop.org/releases/individual/lib/%name-%version.tar.bz2
Source2:        README.SuSE
Source3:        baselibs.conf
Patch1:         xaw3d-secure.patch
Patch2:         xaw3d-thumb.patch
Patch3:         xaw3d-hsbar.patch
Patch4:         xaw3d-3dlabel.patch
Patch5:         xaw3d-fontset.patch
Patch6:         xaw3d-elf.patch
Patch7:         xaw3d.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf >= 2.60
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)

%description
Xaw3d is a general-purpose replacement for the Athena toolkit which
adds a 3D appearance and support for XPM images.

This is a library that can be used instead of the standard
Athena Widget Library. It has tried to keep the standard of the
libXaw library. There are also programs which explicitly use this
library (this is the reason why the library was included).

NOTE: Do NOT replace /usr/lib/libXaw.so.6.1!

%package -n libXaw3d6
Summary:        The 3D Athena Widget Set
Group:          System/Libraries

%description -n libXaw3d6
Xaw3d is a general-purpose replacement for the Athena toolkit which
adds a 3D appearance and support for XPM images.

%package -n libXaw3d7
Summary:        The 3D Athena Widget Set
Group:          System/Libraries

%description -n libXaw3d7
Xaw3d is a general-purpose replacement for the Athena toolkit which
adds a 3D appearance and support for XPM images.

%package -n libXaw3d8
Summary:        The 3D Athena Widget Set
Group:          System/Libraries
Provides:       Xaw3d = %version-%release
# bug437293
%ifarch ppc64
Obsoletes:      xaw3d-64bit
%endif
# Added for 13.1
Obsoletes:      xaw3d < %version-%release
Provides:       xaw3d = %version-%release

%description -n libXaw3d8
Xaw3d is a general-purpose replacement for the Athena toolkit which
adds a 3D appearance and support for XPM images.

%package devel
Summary:        Development files for the X Athena Widget Set
Group:          Development/Libraries/C and C++
Requires:       libXaw3d6 = %version
Requires:       libXaw3d7 = %version
Requires:       libXaw3d8 = %version
Provides:       xaw3d:/usr/include/X11/Xaw3d/Xaw3dP.h
# bug437293
%ifarch ppc64
Obsoletes:      xaw3d-devel-64bit
%endif
# O/P added for 13.2
Provides:       xaw3d-devel = %version-%release
Obsoletes:      xaw3d-devel < %version-%release

%description devel
Xaw3d is a general-purpose replacement for the Athena toolkit which
adds a 3D appearance and support for XPM images.

This package contains the development headers for the library found
in libXaw3d6/libXaw3d7/libXaw3d8.

%package -n xaw3dd
Summary:        Select 3D Athena Widgets as a replacement for Athena Widgets
Group:          System/Libraries
Requires:       libXaw3d6 = %version
Requires:       libXaw3d7 = %version
Requires:       libXaw3d8 = %version

%description -n xaw3dd
Installation of this package will cause programs utilizing the Athena
Widget Toolkit to instead use the 3D Athena Widget set.

If any problems arise using or starting X Window System programs,
remove this package.

%prep
%setup -q
%patch1 -p1 -b .p1
%patch2 -p1 -b .p2
%patch3 -p1 -b .p3
%patch4 -p1 -b .p4
%patch5 -p1 -b .p5
%patch6 -p1 -b .p6
%patch7 -p1 -b .p7

%build
autoreconf -fi
%configure --docdir=%_docdir/%name --disable-static	\
	--enable-internationalization			\
	--enable-multiplane-bitmaps			\
	--enable-gray-stipples				\
	--enable-arrow-scrollbars			\
	--with-pic					\
	--with-gnu-ld					\

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%buildroot
find %{buildroot} -type f -name "*.la" -print -delete

# Copy README here and then gobble it up via %%doc
mkdir -p %{buildroot}%_docdir/xaw3dd
cp %_sourcedir/README.SuSE %{buildroot}/%_docdir/xaw3dd/README.SUSE
ln -s %_docdir/xaw3dd/README.SUSE %{buildroot}%_libdir/Xaw3d/NOTE

# Create /etc/ld.so.conf.d/xaw3dd.conf                                          
mkdir -p %{buildroot}%_sysconfdir/ld.so.conf.d
echo %_libdir/Xaw3d > %{buildroot}%_sysconfdir/ld.so.conf.d/xaw3dd.conf

%post   -n libXaw3d6 -p /sbin/ldconfig
%postun -n libXaw3d6 -p /sbin/ldconfig
%post   -n libXaw3d7 -p /sbin/ldconfig
%postun -n libXaw3d7 -p /sbin/ldconfig
%post   -n libXaw3d8 -p /sbin/ldconfig
%postun -n libXaw3d8 -p /sbin/ldconfig
%post   -n xaw3dd -p /sbin/ldconfig
%postun -n xaw3dd -p /sbin/ldconfig

%files -n libXaw3d6
%defattr(-,root,root)
%_libdir/libXaw3d.so.6*

%files -n libXaw3d7
%defattr(-,root,root)
%_libdir/libXaw3d.so.7*

%files -n libXaw3d8
%defattr(-,root,root)
%_libdir/libXaw3d.so.8*

%files devel
%defattr(-,root,root)
%_includedir/X11/Xaw3d/
%_libdir/libXaw3d.so
%_libdir/pkgconfig/xaw3d.pc
%_docdir/%name/

%files -n xaw3dd
%defattr(-,root,root)
%config %_sysconfdir/ld.so.conf.d/xaw3dd.conf
%_libdir/Xaw3d/
%doc %_libdir/Xaw3d/NOTE
%_docdir/xaw3dd/

%changelog
