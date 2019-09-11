#
# spec file for package ftgl
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


%define libname libftgl2
%bcond_without ftgl_html
Name:           ftgl
Version:        2.1.3~rc5
Release:        0
Summary:        Library for Using Arbitrary Fonts in OpenGL Applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            http://ftgl.wiki.sourceforge.net/
Source0:        http://sourceforge.net/projects/ftgl/files/FTGL%%20Source/2.1.3%%7Erc5/%{name}-2.1.3-rc5.tar.bz2
Source1:        baselibs.conf
Patch0:         %{name}-autoreconf.patch
Patch1:         ftgl-pkgconfig.patch
Patch2:         ftgl-fix-no-add-needed.patch
# PATCH-FIX-OPENSUSE: install FTVectoriser.h, required by tulip-5.0; kkaempf@suse.de
Patch3:         install-FTVectoriser.h.patch
%if %{with ftgl_html}
BuildRequires:  doxygen
BuildRequires:  texlive-epstopdf
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(x11)

%description
FTGL is a C++ library using Freetype2 to render fonts in OpenGL
applications. FTGL supports bitmaps, pixmaps, texture maps, outlines,
polygon mesh, and extruded polygon rendering modes.

%package -n libftgl2
Summary:        Library for Using Arbitrary Fonts in OpenGL Applications
Group:          System/Libraries

%description -n libftgl2
FTGL is a C++ library using Freetype2 to render fonts in OpenGL
applications. FTGL supports bitmaps, pixmaps, texture maps, outlines,
polygon mesh, and extruded polygon rendering modes.

%package devel
Summary:        Development files for the FTGL OpenGL font managing library
Group:          Development/Libraries/C and C++
Requires:       libftgl2 = %{version}

%description devel
FTGL is a C++ library using Freetype2 to render fonts in OpenGL
applications. FTGL supports bitmaps, pixmaps, texture maps, outlines,
polygon mesh, and extruded polygon rendering modes.

This package provides development files.

%package demo
Summary:        Demos for FTGL OpenGL font managing library
Group:          Development/Tools/Other
Conflicts:      %{name}-devel <= 2.1.2

%description demo
FTGL is a C++ library using Freetype2 to render fonts in OpenGL
applications. FTGL supports bitmaps, pixmaps, texture maps, outlines,
polygon mesh, and extruded polygon rendering modes.

This package provides demo application showing usage of the library.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1

%build
autoreconf -fvi
%configure \
	--disable-static
make %{?_smp_mflags} documentationdir=%{_docdir}/%{name}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags} documentationdir=%{_docdir}/%{name}
mkdir -p %{buildroot}%{_defaultdocdir}/libftgl2
cp -pr AUTHORS BUGS COPYING ChangeLog NEWS README TODO %{buildroot}%{_defaultdocdir}/libftgl2
mkdir -p %{buildroot}%{_bindir}
cd demo
/bin/sh ../libtool --mode=install %{_bindir}/install -c FTGLDemo %{buildroot}%{_bindir}/FTGLDemo
/bin/sh ../libtool --mode=install %{_bindir}/install -c FTGLMFontDemo %{buildroot}%{_bindir}/FTGLMFontDemo
/bin/sh ../libtool --mode=install %{_bindir}/install -c c-demo %{buildroot}%{_bindir}/FTGL-c-demo
/bin/sh ../libtool --mode=install %{_bindir}/install -c simple %{buildroot}%{_bindir}/FTGL-simple-demo
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}-demo
cp -pr *.cpp *.c *.h %{buildroot}%{_defaultdocdir}/%{name}-demo
cd ..
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libftgl2 -p /sbin/ldconfig
%postun -n libftgl2 -p /sbin/ldconfig

%files -n libftgl2
%doc %dir %{_defaultdocdir}/libftgl2
%doc %{_defaultdocdir}/libftgl2/[ABCNRT]*
%{_libdir}/*.so.*

%files devel
%doc %dir %{_defaultdocdir}/%{name}
%if %{with ftgl_html}
%doc %{_defaultdocdir}/%{name}/html
%endif
%doc %{_defaultdocdir}/%{name}/*.txt
%{_includedir}/FTGL
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files demo
%doc %dir %{_defaultdocdir}/%{name}
%doc %{_defaultdocdir}/%{name}-demo
%{_bindir}/FTGLDemo
%{_bindir}/FTGLMFontDemo
%{_bindir}/FTGL-c-demo
%{_bindir}/FTGL-simple-demo

%changelog
