#
# spec file for package hugin
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


%define mversion 2024.0
%bcond_with hsi
%bcond_without system_flann
%bcond_without lapack
# Note: Build with EGL support *only* if wxwidgets supports EGL too
%if 0%{?suse_version} > 1650
%bcond_without egl
%else
%bcond_with egl
%endif
Name:           hugin
Version:        %{mversion}.1
Release:        0
Summary:        Toolchain for Stitching of Images and Creating Panoramas
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://hugin.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{mversion}/%{name}-%{version}.tar.bz2
Patch0:         hugin.appdata.patch
BuildRequires:  Mesa-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  cmake >= 3.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  exiftool
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpano-devel >= 2.9.19
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  vigra-devel
BuildRequires:  wxGTK3-devel >= 3.1.5
BuildRequires:  pkgconfig(epoxy)
Requires:       enblend-enfuse >= 3.2
# needed for photo stiching (bnc#822775)
Requires:       make
Recommends:     autopano-sift-C
Recommends:     exiftool
%if %{with system_flann}
BuildRequires:  flann-devel
%endif
%if %{with lapack}
BuildRequires:  lapack-devel
%endif
%if %{with hsi}
BuildRequires:  python3-wxPython
BuildRequires:  swig
%endif
%if %{with egl}
BuildRequires:  pkgconfig(egl)
%endif

%description
Hugin can be used to stitch multiple images together. The resulting
image can span 360 degrees. Another common use is the creation of very
high resolution pictures by combining multiple images.

Other tools in this package can correct lens distortion, vignetting and
chromatic abberation, create HDR images, provide automatic feature
detection and extraction of key points.

%prep
%autosetup -p1 -n %{name}-%{version}

chmod -x AUTHORS authors.txt Changes.txt README COPYING.txt

sed -i "s/\r$//" Changes.txt

# Rename Czech in Czech Republic to Czech.
mv src/translations/cs_CZ.po src/translations/cs.po
#sed -i "s/ca_ES/ca/;s/cs_CZ/cs/" src/hugin/po/LINGUAS

%build
# Doesn't define the ZLIB::ZLIB target needed by OpenEXR 3
rm CMakeModules/FindZLIB.cmake
%cmake \
  -DENABLE_LAPACK=%{?with_lapack:ON}%{!?with_lapack:OFF} \
  -DBUILD_HSI=%{?with_hsi:ON}%{!?with_hsi:OFF} \
  -DBUILD_WITH_EGL:BOOL=%{?with_egl:ON}%{!?with_egl:OFF} \
  -DUSE_GDKBACKEND_X11:BOOL=%{?with_egl:OFF}%{!?with_egl:ON} \
  -DBUILD_WITH_EPOXY:BOOL=ON \
	%{nil}

%cmake_build

%install
%cmake_install

# locales
%find_lang %{name}

# Install manually so it can be dedup'ed with the one in the program resources
install -m644 -D -t %{buildroot}%{_licensedir}/hugin/ COPYING.txt
%fdupes %{buildroot}

%files -f %{name}.lang
%license COPYING.txt
%doc AUTHORS authors.txt Changes.txt README
%{_bindir}/*
%{_datadir}/hugin
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/mimetypes/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/mime/packages/*.xml
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/*xml
%dir %{_libdir}/hugin
%{_libdir}/hugin/*.so.*
%{_mandir}/man?/*.*

%changelog
