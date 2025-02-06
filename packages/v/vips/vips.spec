#
# spec file for package vips
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


%define _typelibdir %(pkg-config --variable=typelibdir gobject-introspection-1.0)
%define _girdir %(pkg-config --variable=girdir gobject-introspection-1.0)
%define libname lib%{name}
%define short_version  8.0
%define short_version_ 8.0
%define somajor 42
Name:           vips
Version:        8.16.0
Release:        0
Summary:        C/C++ library for processing large images
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://www.libvips.org/
Source0:        https://github.com/libvips/libvips/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Based on https://github.com/libvips/libvips/commit/f0ed595021786f70dbcb145abbe8301e8a2fb331.patch with the Changelog chunk removed
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  giflib-devel
BuildRequires:  libarchive-devel
BuildRequires:  libjxl-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(imagequant)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2) >= 2.4
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(matio)
BuildRequires:  pkgconfig(openslide)
BuildRequires:  pkgconfig(orc-0.4) >= 0.4
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(zlib)

%description
VIPS is an image processing system. It is good with large images
(images larger than the amount of RAM you have available), with many CPUs,
for working with colour, for scientific analysis and for general
research and development.

%package     -n %{libname}%{somajor}
Summary:        C/C++ library for processing large images
Group:          System/Libraries
Requires:       vips-modules-%{short_version} >= %{version}

%description -n %{libname}%{somajor}
VIPS is an image processing system. It is good with large images
(images larger than the amount of RAM you have available), with many CPUs,
for working with colour, for scientific analysis and for general
research and development.

%package     -n typelib-1_0-Vips-%{short_version_}
Summary:        C/C++ library for processing large images
Group:          System/Libraries

%description -n typelib-1_0-Vips-%{short_version_}
VIPS is an image processing system. It is good with large images
(images larger than the amount of RAM you have available), with many CPUs,
for working with colour, for scientific analysis and for general
research and development.

%package     -n %{libname}-devel
Summary:        Development files for the VIPS library
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{somajor} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(gobject-2.0)
Requires:       pkgconfig(libjpeg)
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(zlib)

%description -n %{libname}-devel
This package contains the development files for developing applications that
want to make use of the VIPS library.

%package        tools
Summary:        Command line tools for VIPS library
Group:          Productivity/Graphics/Other
Requires:       %{libname}%{somajor} = %{version}

%description    tools
This package contains command line tools for processing large images using
the VIPS library.

%package        modules-%{short_version}
Summary:        Additional modules for libvips
Group:          Productivity/Graphics/Other
Requires:       %{libname}%{somajor} = %{version}

%description    modules-%{short_version}
Additional modules for libvips.

%package        doc
Summary:        Documentation for VIPS library
Group:          Documentation/Other
Requires:       %{libname}%{somajor} = %{version}
BuildArch:      noarch

%description    doc
This package contains documentation about the VIPS library in HTML and PDF
formats.

%prep
%autosetup -p1

%build
%meson \
  -Dcgif=disabled \
  -Dspng=disabled \
  -Dpdfium=disabled \
  -Dnifti=disabled
%meson_build

%install
%meson_install
%find_lang %{name} --all-name
%fdupes %{buildroot}%{python_sitearch}/

%check
%meson_test

%ldconfig_scriptlets -n %{libname}%{somajor}

%files -n %{libname}%{somajor} -f vips.lang
%license LICENSE
%{_libdir}/*.so.%{somajor}*

%files modules-%{short_version}
%license LICENSE
%{_libdir}/vips-modules-8.16/

%files -n typelib-1_0-Vips-%{short_version_}
%license LICENSE
%{_typelibdir}/Vips-%{short_version}.typelib

%files -n %{libname}-devel
%license LICENSE
%{_libdir}/*.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*
%{_girdir}/Vips-%{short_version}.gir

%files tools
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%files doc
%license LICENSE
%doc README.md ChangeLog doc

%changelog
