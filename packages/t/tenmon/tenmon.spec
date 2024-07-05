#
# spec file for package tenmon
#
# Copyright (c) 2024 SUSE LLC
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

Name:           tenmon
Version:        20240617
Release:        0
Summary:        FITS and XISF image viewer, converter and indexer
License:        GPL-3.0-or-later
URL:            https://gitea.nouspiro.space/nou/tenmon/
Source:         https://gitea.nouspiro.space/nou/tenmon/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         use_system_libxisf.patch
# PATCH-FIX-UPSTREAM
Patch1:         fix-libxisf-include.patch
BuildRequires:  gcc%{?force_gcc_version}-c++ >= 12
BuildRequires:  libXISF-devel >= 0.2.12+git5.d00de20
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel >= 6.2.0
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Sql)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(wcslib)

%description
RAW/FITS/XISF image viewer with multithreaded image loading.
Features included, but not limited to:
* FITS 8, 16 bit integer and 32 bit float
* XISF 8, 16 bit integer and 32 bit float
* JPEG and PNG images
* NEF, CR2 and DNG raw files
* Using same stretch function as PixInsight
* OpenGL accelerated drawing
* Index and search FITS XISF header data
* Quick mark images and then copy/move marked files
* Convert FITS <-> XISF
* Convert FITS/XISF -> JPEG/PNG
* Image statistics mean, media, min, max

%prep
%autosetup -p1 -n %{name}

%build
export CFLAGS=$(echo "$CFLAGS -Wno-switch -Wno-catch-value")
export  CXXFLAGS=$(echo "$CXXFLAGS -Wno-switch -Wno-catch-value")
%cmake \
 -DRELEASE_BUILD=ON \
%if 0%{?force_gcc_version}
    -DCMAKE_CXX_COMPILER=%{_bindir}/g++-%{?force_gcc_version} \
%endif

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/64x64/apps
%{_bindir}/tenmon
%{_datadir}/applications/space.nouspiro.tenmon.desktop
%{_datadir}/icons/hicolor/128x128/apps/space.nouspiro.tenmon.png
%{_datadir}/icons/hicolor/64x64/apps/space.nouspiro.tenmon.png
%{_datadir}/metainfo/space.nouspiro.tenmon.metainfo.xml

%changelog
