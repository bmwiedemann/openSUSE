#
# spec file for package nanosvg
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


%define fltktag fltk_2022-12-22
%define sover 0
Name:           nanosvg
Version:        2022.12.22
Release:        0
Summary:        Simple single-header-file SVG parse
License:        Zlib
# fltk fork required by PrusaSlicer (addition of nsvgRasterizeXY())
URL:            https://github.com/fltk/nanosvg
Source0:        https://github.com/fltk/nanosvg/archive/refs/tags/%{fltktag}.tar.gz#/nanosvg-%{fltktag}.tar.gz
# PATCH-FIX-UPSTREAM fix-cname-dest.patch gh#memononen/nanosvg#245 -- originally by mike.chikov@gmail.com, fix cmake install library directory
Patch0:         fix-cname-dest.patch
# PATCH-FEATURE-UPSTREAM nanosvg-add-soversion.patch gh#memononen/nanosvg#242, gh#memononen/nanosvg#246
Patch1:         nanosvg-add-soversion.patch
BuildRequires:  cmake
BuildRequires:  fdupes

%description
NanoSVG is a simple SVG parser.
The output of the parser is a list of cubic bezier shapes.

The shapes in the SVG images are transformed by the viewBox
and converted to specified units. That is, you should get
the same looking data as your designed in your favorite app.

NanoSVG can return the paths in few different units. For
example if you want to render an image, you may choose to
get the paths in pixels, or if you are feeding the data into
a CNC-cutter, you may want to use millimeters.

The units passed to NanoSVG should be one of:
'px', 'pt', 'pc' 'mm', 'cm', or 'in'.
DPI (dots-per-inch) controls how the unit conversion is done.

Note that this package builds shared libraries libnanosvg and
libnanosvgrast from the source code in the .h header files.

%package -n libnanosvg%{sover}
Summary:        Simple SVG parse

%description -n libnanosvg%{sover}
Shared library built from the code in the nanosvg.h header file

A simple SVG parser. The output of the parser is a list of cubic bezier shapes.

%package -n libnanosvgrast%{sover}
Summary:        Simple SVG parse

%description -n libnanosvgrast%{sover}
Shared library built from the code in the nanosvgrast. header file

Provides functions to rasterize SVG image,
returns RGBA image (non-premultiplied alpha)

%package devel
Summary:        Development files for %{name}
Requires:       libnanosvg%{sover} = %{version}
Requires:       libnanosvgrast%{sover} = %{version}

%description devel
NanoSVG is a simple SVG parser.
The output of the parser is a list of cubic bezier shapes.

The shapes in the SVG images are transformed by the viewBox
and converted to specified units. That is, you should get
the same looking data as your designed in your favorite app.

NanoSVG can return the paths in few different units. For
example if you want to render an image, you may choose to
get the paths in pixels, or if you are feeding the data into
a CNC-cutter, you may want to use millimeters.

The units passed to NanoSVG should be one of:
'px', 'pt', 'pc' 'mm', 'cm', or 'in'.
DPI (dots-per-inch) controls how the unit conversion is done.

The library can be used by copying the .h files into the
consuming package or through shared libraries installed by
the CMake build process.

%prep
%autosetup -p1 -n nanosvg-%{fltktag}

%build
%cmake
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}/%{_prefix}

%post   -n libnanosvg%{sover} -p /sbin/ldconfig
%postun -n libnanosvg%{sover} -p /sbin/ldconfig
%post   -n libnanosvgrast%{sover} -p /sbin/ldconfig
%postun -n libnanosvgrast%{sover} -p /sbin/ldconfig

%files -n libnanosvg%{sover}
%{_libdir}/libnanosvg.so.%{sover}

%files -n libnanosvgrast%{sover}
%{_libdir}/libnanosvgrast.so.%{sover}

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/%{name}
%{_libdir}/libnanosvg.so
%{_libdir}/libnanosvgrast.so
%{_libdir}/cmake/NanoSVG

%changelog
