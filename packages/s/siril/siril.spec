#
# spec file for package siril
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


Name:           siril
Version:        1.2.6
Release:        0
Summary:        An astronomical image processing software for Linux. (IRIS clone)
License:        BSL-1.0 AND GPL-3.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://www.siril.org/
Source:         https://gitlab.com/free-astro/siril/-/archive/%{version}/siril-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM - extracted from https://gitlab.com/free-astro/siril/-/commit/763079de767df0e3ae42f51b65f2f25d7ea7b8b8
Patch0:         fix_C_linkage.patch
# PATCH-FIX-UPSTREAM
Patch1:         https://gitlab.com/free-astro/siril/-/commit/1041f25fd1d04330626601185907373c2e69e709.patch#/fix_glib_284_compat.patch
# PATCH-FIX-UPSTREAM
Patch2:         https://gitlab.com/free-astro/siril/-/commit/241b4b17d83285eb4bf4151dd77198427ac9fde4.patch#/fix_odr_violation.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libheif-devel
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(exiv2) >= 0.25
BuildRequires:  pkgconfig(ffms2)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil) >= 55.20
BuildRequires:  pkgconfig(libconfig++) >= 1.4
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(opencv4) >= 4.4.0
BuildRequires:  pkgconfig(rtprocess)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(wcslib)

%description
Siril is meant to be Iris for Linux (sirI-L). It is an astronomical image
processing tool, able to convert, pre-process images, help aligning them
automatically or manually, stack them and enhance final images.

%prep
%autosetup -p1

%build
# override build directory, the default "build" is a regular source directory
%define _vpath_builddir builddir
%meson  \
    -Drelocatable-bundle=no \
    %{nil}
%meson_build

%install
%meson_install
rm %{buildroot}/%{_datadir}/doc/siril/*
%find_lang %{name}
install -m 0644 -D platform-specific/linux/org.siril.Siril.desktop %{buildroot}%{_datadir}/applications/org.siril.Siril.desktop
install -m 0644 -D platform-specific/linux/siril.xml %{buildroot}%{_datadir}/mime/packages/siril.xml

%fdupes %{buildroot}/%{_datadir}

%files -f %{name}.lang
%doc ChangeLog NEWS README.md AUTHORS
%license LICENSE.md LICENSE_sleef.txt
%{_bindir}/siril
%{_bindir}/siril-cli
%{_mandir}/man1/siril.1%{?ext_man}
%{_mandir}/man1/siril-cli.1%{?ext_man}
%{_datadir}/siril/
%{_datadir}/metainfo/org.siril.Siril.appdata.xml
%{_datadir}/applications/org.siril.Siril.desktop
%{_datadir}/mime/packages/siril.xml
%{_datadir}/icons/hicolor/scalable/mimetypes/text-x-seq.svg
%{_datadir}/icons/hicolor/scalable/apps/org.siril.Siril.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.siril.Siril-symbolic.svg

%changelog
