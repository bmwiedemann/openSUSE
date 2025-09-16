#
# spec file for package tkimg
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tkimg
Version:        2.1.0
Release:        0
Summary:        More Image Formats for Tk
Group:          Development/Libraries/Tcl
License:        BSD-3-Clause
URL:            https://sourceforge.net/projects/tkimg
Source0:        https://sourceforge.net/projects/tkimg/files/tkimg/2.1/tkimg%%20%{version}/Img-%{version}.tar.gz
Patch0:         tests-add-destdir-tcllibpath.patch
Patch1:         tkimg-CVE-2025-9165.patch
BuildRequires:  dos2unix
BuildRequires:  tcllib
BuildRequires:  tk-devel
BuildRequires:  xorg-x11-fonts
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(x11)
#!BuildIgnore:  tcl-bundled-extensions

%description
This package contains a collection of image format handlers for the Tk
photo image type, and a new image type, pixmaps.

The provided format handlers include bmp, gif, ico, jpeg, pcx, png,
ppm, ps, sgi, sun, tga, tiff, xbm, and xpm.

%package devel
Summary:        Header Files and C API Documentation for tkimg
Group:          Development/Libraries/Tcl

%description devel
Files needed to compile/link C code against tkimg.

%prep
%autosetup -p0 -n Img-%{version}
# Source archive is likly created on Windows, so fix some issues
# 1. Fix file permissions: Executable bit is set on every file, fix that
find . -type f -not -name configure -exec chmod 0644 \{\} +
# 2. Fix line ending
dos2unix README.md license.terms base/pkgIndex.tcl.in

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
CONFOPTS="\
        --libdir=%tcl_archdir \
        --with-tcl=%_libdir \
        --with-tk=%_libdir"
%configure $CONFOPTS
%make_build
mkdir html
dtplite -ext html -o html -exclude '*.inc' html doc

%install
make INSTALL_ROOT=%buildroot install-libraries install-man
# Fix file permissions
chmod a-x %buildroot%tcl_archdir/*/*.a

%check
TCLLIBPATH=`pwd` xvfb-run make test

%files
%doc README.md
%license license.terms
%doc %_mandir/*/*
%doc html
%tcl_archdir/*
%exclude %tcl_archdir/*/*.a

%files devel
%_includedir/*
%tcl_archdir/*/*.a

%changelog
