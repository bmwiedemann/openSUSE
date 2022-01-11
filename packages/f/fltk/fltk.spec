#
# spec file for package fltk
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


%define libname libfltk1_3
Name:           fltk
Version:        1.3.8
Release:        0
Summary:        C++ GUI Toolkit for the X Window System, OpenGL, and WIN32
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://www.fltk.org/
Source0:        https://www.fltk.org/pub/fltk/%{version}/fltk-%{version}-source.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM fltk-1.3.4-fltk_config.patch tchvatal@suse.com -- obey libdir and other options in fltk-config taken from Fedora
Patch0:         fltk-1.3.4-fltk_config.patch
# PATCH-FIX-OPENSUSE fltk-1.3.2-verbose_build.patch reddwarf@opensuse.org -- Make the build verbose so the post build checks can verify the CFLAGS
Patch2:         fltk-1.3.2-verbose_build.patch
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)

%description
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a C++
graphical user interface toolkit for the X Window System,
OpenGL, and Microsoft Windows NT 4.0, 95, or 98. The
installation of this package requires a 3D library such as Mesa.

%package devel
Summary:        Development files for the FLTK GUI toolkit
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(x11)
Provides:       fltk = %{version}

%description devel
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a C++
graphical user interface toolkit for the X Window System,
OpenGL, and Microsoft Windows NT 4.0, 95, or 98. The
installation of this package requires a 3D library such as Mesa.

%package -n %{libname}
Summary:        The FLTK GUI toolkit library
Group:          System/Libraries
Obsoletes:      fltk < 1.3.2

%description -n %{libname}
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a C++
graphical user interface toolkit for the X Window System,
OpenGL, and Microsoft Windows NT 4.0, 95, or 98. The
installation of this package requires a 3D library such as Mesa.

%package devel-static
Summary:        Static libraries for the FLTK GUI toolkit
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       fltk-devel = %{version}

%description devel-static
The Fast Light Tool Kit ("FLTK", pronounced "fulltick") is a C++
graphical user interface toolkit for the X Window System,
OpenGL, and Microsoft Windows NT 4.0, 95, or 98. The
installation of this package requires a 3D library such as Mesa.

%prep
%setup -q
%patch0 -p1
%patch2

%build
%configure \
  --with-optim="%{_lto_cflags} -ffat-lto-objects" \
  --enable-shared \
  --disable-localjpeg \
  --disable-localzlib \
  --disable-localpng \
  --enable-threads

%make_build
cd documentation
%make_build html

%install
make install libdir=%{buildroot}%{_libdir}/ \
	     includedir=%{buildroot}%{_includedir} \
	     bindir=%{buildroot}%{_bindir} \
	     docdir=%{buildroot}/%{_docdir}/fltk-devel/html/ \
	     mandir=%{buildroot}%{_mandir} STRIP=true
rm -r %{buildroot}%{_mandir}/cat*

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%doc examples makeinclude
%doc %{_docdir}/fltk-devel
%{_mandir}/man*/*
%{_libdir}/*.so
%{_includedir}/*
%{_bindir}/*

%files -n %{libname}
%license COPYING
%doc CHANGES README
%{_libdir}/*.so.*

%files devel-static
%{_libdir}/libfltk*.a

%changelog
