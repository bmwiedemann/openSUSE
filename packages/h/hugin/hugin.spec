#
# spec file for package hugin
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with hsi
%bcond_with system_flann
%bcond_without lapack

Name:           hugin
BuildRequires:  Mesa-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  cmake >= 3.1.0
BuildRequires:  desktop-file-utils
BuildRequires:  exiftool
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
%if %{with system_flann}
BuildRequires:  flann-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
%if %{with lapack}
BuildRequires:  lapack-devel
%endif
BuildRequires:  libexiv2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpano-devel >= 2.9.19
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
%if %{with hsi}
BuildRequires:  python-wxWidgets >= 3
BuildRequires:  swig
%endif
BuildRequires:  pkg-config
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  vigra-devel
BuildRequires:  wxGTK3-devel >= 3
%define mversion 2019.2
Version:        2019.2.0
Release:        0
Summary:        Toolchain for Stitching of Images and Creating Panoramas
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://hugin.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/%{name}/%{name}/%{name}-%{mversion}/%{name}-%{version}.tar.bz2
Patch0:         hugin.appdata.patch
Requires:       enblend-enfuse >= 3.2
# needed for photo stiching (bnc#822775)
Requires:       make
Recommends:     autopano-sift-C
Recommends:     exiftool

%description
Hugin can be used to stitch multiple images together. The resulting
image can span 360 degrees. Another common use is the creation of very
high resolution pictures by combining multiple images.

Other tools in this package can correct lens distortion, vignetting and
chromatic abberation, create HDR images, provide automatic feature
detection and extraction of key points.

%prep
%setup -q
%patch0

chmod -x AUTHORS authors.txt Changes.txt README COPYING.txt

# Rename Czech in Czech Republic to Czech.
mv src/translations/cs_CZ.po src/translations/cs.po
#sed -i "s/ca_ES/ca/;s/cs_CZ/cs/" src/hugin/po/LINGUAS

%build
%cmake \
	-DENABLE_LAPACK=%{?with_lapack:ON}%{!?with_lapack:OFF} \
	-DBUILD_HSI=%{?with_hsi:ON}%{!?with_hsi:OFF} \
	-DCMAKE_SKIP_RPATH:BOOL=OFF \
	..

%cmake_build

%install
pushd .
%cmake_install

popd
%suse_update_desktop_file hugin 2DGraphics
%suse_update_desktop_file PTBatcherGUI 2DGraphics
%suse_update_desktop_file calibrate_lens_gui 2DGraphics
# locales
%{find_lang} %{name}

# Use better place for MIME icon.
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
mv -f %{buildroot}%{_datadir}/icons/{gnome/48x48/mimetypes/gnome-mime-,hicolor/48x48/mimetypes/}application-x-ptoptimizer-script.png
rmdir -p --ignore-fail-on-non-empty %{buildroot}%{_datadir}/icons/gnome/48x48/mimetypes

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
%dir %{_datadir}/appdata
%{_datadir}/appdata/*xml
%dir %{_libdir}/hugin
%{_libdir}/hugin/*.so.*
%doc %{_mandir}/man?/*.*

%changelog
