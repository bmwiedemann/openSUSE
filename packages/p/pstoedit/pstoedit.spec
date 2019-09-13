#
# spec file for package pstoedit
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pstoedit
Version:        3.70
Release:        0
Summary:        PostScript and PDF Converter
License:        GPL-2.0+
Group:          Productivity/Publishing/PS
Url:            http://www.pstoedit.net/
Source:         https://sourceforge.net/projects/pstoedit/files/pstoedit/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pstoedit-pkglibdir.patch sbrabec@suse.cz -- Fix plugin search path.
Patch:          pstoedit-pkglibdir.patch
Patch1:         reproducible.patch
# pstoedit-imagemagick7.patch sent to author (wglunz35_AT_pstoedit.net) on 2017-09-20
Patch2:         pstoedit-imagemagick7.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gd-devel
BuildRequires:  ghostscript-devel
BuildRequires:  libEMF-devel
BuildRequires:  libMagick++-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libzip-devel
BuildRequires:  pkg-config
BuildRequires:  plotutils-devel
Requires:       ghostscript
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pstoedit converts PostScript and PDF files to other vector graphic
formats so that they can be edited graphically.

pstoedit supports:

* Tgif .obj format (for tgif version >= 3)
* .fig format for xfig
* pdf - Adobe's Portable Document Format
* gnuplot format
* Flattened PostScript (with or without Bezier curves)
* DXF - CAD exchange format
* LWO - LightWave 3D
* RIB - RenderMan
* RPL - Real3D
* Java 1 or Java 2 applet
* Idraw format (in fact a special form of EPS that idraw can read)
* Tcl/Tk
* HPGL
* AI (Adobe Illustrator) (based on ps2ai.ps - not a real pstoedit driver - see notes below and manual)
* Windows Meta Files (WMF) (Windows only)
* Enhanced Windows Meta Files (EMF) (Windows, but also Linux/Unix if libemf is available)
* OS/2 meta files (OS/2 only)
* PIC format for troff/groff
* MetaPost format for usage with TeX/LaTeX
* LaTeX2e picture
* Kontour
* GNU Metafile (plotutils / libplot)
* Skencil ( http://www.skencil.org )
* Mathematica
* via ImageMagick to any format supported by ImageMagick
* SWF
* CNC G code
* VTK files for ParaView and similar visualization tools

%package devel
Summary:        PostScript and PDF converter (development files)
Group:          Productivity/Publishing/PS
Requires:       %{name} = %{version}
Requires:       ImageMagick-devel
Requires:       libMagick++-devel
Requires:       libpng-devel
Requires:       libzip-devel

%description devel
PostScript and PDF converter development headers and library files.

%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
chmod -x examples/*.ps examples/Makefile* doc/*.* copying

%build
# we are patching configure.ac
sh autogen.sh
# --without-swf: lacking libming package
%configure \
	--disable-static \
	--with-emf \
	--with-magick \
	--with-libplot \
	--with-pptx \
	--without-swf

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
# doc cleanup
rm -rf examples/Makefile*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc copying
%doc examples
%doc doc/*.htm
%{_bindir}/pstoedit
%{_libdir}/*.so.*
%dir %{_libdir}/pstoedit
%{_libdir}/pstoedit/*.so
%{_libdir}/pstoedit/*.so.*
%{_datadir}/%{name}
%doc %{_mandir}/man?*/*.*

%files devel
%defattr(-, root, root)
%{_libdir}/*.so
%{_includedir}/pstoedit
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4

%changelog
