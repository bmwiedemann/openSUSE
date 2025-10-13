#
# spec file for package LuminanceHDR
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} && 0%{?suse_version} < 1590
%global force_gcc_version 12
%endif

%define _lto_cflags %{nil}
%define liblcms2_name liblcms2-2

Name:           LuminanceHDR
Version:        2.6.0+git313.634b489
Release:        0
Summary:        Complete workflow for HDR imaging
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/LuminanceHDR/LuminanceHDR
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE use-system-rtprocess.patch
Patch0:         use-system-rtprocess.patch
# PATCH-FIX-UPSTREAM
Patch1:         fix-boost_system.patch
# PATCH-FIX-UPSTREAM
Patch2:         clamp.patch
Patch3:         fix-version.patch
Patch4:         fix-boost-1.87.0.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-openmp-devel
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_program_options-devel
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libboost_thread-devel
BuildRequires:  libexiv2-devel >= 0.27.0
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  librtprocess-devel
BuildRequires:  openexr-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
Requires:       %{liblcms2_name} >= 2.6
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Luminance HDR is a graphical user interface (based on the Qt5 toolkit) that provides a complete workflow for HDR imaging.
Supported HDR formats:
  * OpenEXR (extension: exr)
  * Radiance RGBE (extension: hdr)
  * Tiff formats: 16bit, 32bit (float) and LogLuv (extension: tiff)
  * Raw image formats (extension: various)
  * PFS native format (extension: pfs)

Supported LDR formats:
  * JPEG, PNG, PPM, PBM, TIFF, FITS

Supported features:
  * Create an HDR file from a set of images (JPEG, TIFF 8bit and 16bit, RAW) of the same scene taken at different exposure setting
  * Save and load HDR files
  * Rotate and resize HDR files
  * Tonemap HDR images
  * Projective Transformations
  * Copy EXIF data between sets of images
  * Supports internationalization

%package doc
Summary:        This package provides documentation for %{name}
BuildArch:      noarch

%description doc
This package contains the documentation for Luminance HDR.

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++%{?force_gcc_version:-%force_gcc_version}
%cmake_build

%install
%cmake_install

%files
%{_bindir}/luminance-hdr
%{_bindir}/luminance-hdr-cli
%dir %{_datadir}/appdata
%dir %{_datadir}/applications
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/luminance-hdr
%dir %{_datadir}/luminance-hdr/doc
%{_datadir}/appdata/net.sourceforge.qtpfsgui.LuminanceHDR.appdata.xml
%{_datadir}/applications/net.sourceforge.qtpfsgui.LuminanceHDR.desktop
%{_datadir}/icons/hicolor/48x48/apps/luminance-hdr.png
%{_datadir}/luminance-hdr/doc/AUTHORS
%{_datadir}/luminance-hdr/doc/Changelog
%{_datadir}/luminance-hdr/doc/LICENSE
%{_datadir}/luminance-hdr/doc/README.md

%files doc
%dir %{_datadir}/luminance-hdr
%dir %{_datadir}/luminance-hdr/hdrhtml
%dir %{_datadir}/luminance-hdr/help
%dir %{_datadir}/luminance-hdr/help/en
%dir %{_datadir}/luminance-hdr/i18n
%{_datadir}/luminance-hdr/hdrhtml/*
%{_datadir}/luminance-hdr/hdrhtml/hdrhtml_default_templ/*
%{_datadir}/luminance-hdr/help/en/*
%{_datadir}/luminance-hdr/i18n/*

%changelog
