#
# spec file for package gmic
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


# Disable LTO as it removes important symbols
#
# g++ use_libgmic.cpp -o use_gmic -L/tmp/local/gmic/lib64 -lgmic
# use_libgmic.cpp:function main: error: undefined reference to 'cimg_library::CImgList<float>::assign(unsigned int)'
#
# https://discuss.pixls.us/t/gmic-lookup-symbol-err-on-opensuse-darktable-master-build/15827
#
%define _lto_cflags %{nil}

%global _gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%bcond_without digikam_plugin
%else
%bcond_with digikam_plugin
%endif
# opencv3 is not available for ppc
%ifnarch ppc64 ppc64le
%bcond_without opencv
%else
%bcond_with opencv
%endif
Name:           gmic
Version:        2.9.2
Release:        0
Summary:        GREYC's Magick for Image Computing (denoise and others)
# gmic-qt is GPL-3.0-or-later, zart is CECILL-2.0, libgmic and cli program are
# CECILL-2.1
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://gmic.eu
# Git URL:      https://framagit.org/dtschump/gmic
Source0:        https://gmic.eu/files/source/gmic_%{version}.tar.gz
Source1:        gmic_qt.png
# PATCH-FIX-UPSTREAM
Patch:          0001-Don-t-use-CMake-commands-not-available-in-CMake-3.9.patch
BuildRequires:  cmake >= 3.9.4
BuildRequires:  fftw3-threads-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if %{with digikam_plugin}
BuildRequires:  cmake(DigikamCore) >= 6.3.0
%endif
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gimp-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
%if %{with opencv}
# gmic first looks for opencv 4 first and falls back to opencv 3 if not found.
# opencv in not available in leap <= 15.2
%if 0%{?suse_version} <= 1500
BuildRequires:  pkgconfig(opencv)
%else
BuildRequires:  pkgconfig(opencv4)
%endif
%endif

%description
G'MIC is a framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

%package -n libgmic1
Summary:        Shared library that belongs to gmic
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors

%package -n libgmic-devel
Summary:        Header and library from gmic for use in other C++ projects
License:        CECILL-2.1
Group:          Development/Libraries/C and C++
Requires:       libgmic1 = %{version}

%description -n libgmic1
Shared library allows you to use gmic functionality from other
programs.

%description -n libgmic-devel
Header and library from gmic to needed to develop C++ code that
uses the gmic functionality provided by the gmic library.

%package -n gimp-plugin-gmic
Summary:        GMIC plugin for gimp
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
Requires:       gimp
# This package was only available in the 'graphics' repo
Provides:       gmic-gimp = %{version}
Obsoletes:      gmic-gimp < %{version}

%description -n gimp-plugin-gmic
This is a plugin for gimp that exposes many of the nice gmic features
for interactive use in gimp.

%package -n krita-plugin-gmic
Summary:        GMIC plugin for krita
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
Requires:       krita

%description -n  krita-plugin-gmic
This is a plugin for krita to provide gmic features.

%if %{with digikam_plugin}
%package -n digikam-plugin-gmic
Summary:        GMIC plugin for digikam
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
Requires:       digikam

%description -n  digikam-plugin-gmic
This is a plugin for digikam to provide gmic features.
%endif

%package zart
Summary:        GMIC GUI for video streams
License:        CECILL-2.0
Group:          Productivity/Graphics/Bitmap Editors

%description zart
ZArt is a computer program whose purpose is to demonstrate the possibilities of
the G'MIC image processing language by offering the choice of several
manipulations on a video stream acquired from a webcam. In other words, ZArt is
a GUI for G'MIC real-time manipulations on the output of a webcam.

%package bash-completion
Summary:        Bash completion for gmic
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
This package contain de bash completion command for gmic.

%prep
%autosetup -p1

# Generated file that should not be there
rm -f zart/.qmake.stash

%build
# Build gmic
%cmake \
    -DENABLE_DYNAMIC_LINKING=ON \
    -DBUILD_LIB_STATIC=OFF
%cmake_build

cd ..

# Create link for zart dynamic linking
ln -s ../build/libgmic.so src/libgmic.so

# Build gmic{_gimp|_krita|_digikam}_qt
pushd gmic-qt
%cmake \
    -DENABLE_DYNAMIC_LINKING=ON \
    -DGMIC_PATH=%{_builddir}/%{name}-%{version}/src \
    -DGMIC_LIB_PATH=%{_builddir}/%{name}-%{version}/build \
    -DGMIC_QT_HOST=gimp
%cmake_build

cd ..

%cmake \
    -DENABLE_DYNAMIC_LINKING=ON \
    -DGMIC_PATH=%{_builddir}/%{name}-%{version}/src \
    -DGMIC_LIB_PATH=%{_builddir}/%{name}-%{version}/build \
    -DGMIC_QT_HOST=krita
%cmake_build

cd ..

%if %{with digikam_plugin}
%cmake \
    -DENABLE_DYNAMIC_LINKING=ON \
    -DGMIC_PATH=%{_builddir}/%{name}-%{version}/src \
    -DGMIC_LIB_PATH=%{_builddir}/%{name}-%{version}/build \
    -DGMIC_QT_HOST=digikam
%cmake_build

cd ..
%endif

%cmake \
    -DENABLE_DYNAMIC_LINKING=ON \
    -DGMIC_PATH=%{_builddir}/%{name}-%{version}/src \
    -DGMIC_LIB_PATH=%{_builddir}/%{name}-%{version}/build \
    -DGMIC_QT_HOST=none
%cmake_build

cd ..
popd

%if %{with opencv}
# Build zart
pushd zart
%qmake5 zart.pro \
   CONFIG+=release \
   GMIC_DYNAMIC_LINKING=on \
   GMIC_PATH=%{_builddir}/%{name}-%{version}/src
%make_jobs
popd
%endif

%install
%cmake_install

install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/gmic_qt.png

%suse_update_desktop_file -c gmic_qt "G'Mic Qt" "G'MIC Qt GUI" "gmic_qt %%F" gmic_qt "Qt;Graphics;Photography;"

# Film color lookup tables
install -d -m 0755 %{buildroot}%{_gimpplugindir}
install -m 0644 resources/gmic_cluts.gmz %{buildroot}%{_gimpplugindir}/gmic_cluts.gmz

# qt_gmic
pushd gmic-qt
install -m 0755 build/gmic_qt %{buildroot}%{_bindir}/gmic_qt

# krita plugin
install -m 0755 build/gmic_krita_qt %{buildroot}%{_bindir}/gmic_krita_qt

# gimp plugin
install -d -m 0755 %{buildroot}%{_gimpplugindir}
install -m 0755 build/gmic_gimp_qt %{buildroot}%{_gimpplugindir}/gmic_gimp_qt

%if %{with digikam_plugin}
# digikam plugin
install -d -m 0755 %{buildroot}%{_libqt5_plugindir}/digikam/editor
install -m 0755 build/Editor_GmicQt_Plugin.so %{buildroot}%{_libqt5_plugindir}/digikam/editor/Editor_GmicQt_Plugin.so
%endif
popd

%if %{with opencv}
# zart
pushd zart
install -m 0755 zart %{buildroot}%{_bindir}/zart
popd
%endif

%post -n libgmic1 -p /sbin/ldconfig
%postun -n libgmic1 -p /sbin/ldconfig

%files
%license COPYING
%doc README gmic-qt/README.md
%{_bindir}/gmic
%{_bindir}/gmic_qt
%{_mandir}/man1/gmic.1%{?ext_man}
%{_datadir}/applications/gmic_qt.desktop
%{_datadir}/pixmaps/gmic_qt.png

%if %{with opencv}
%files zart
%{_bindir}/zart
%endif

%files -n gimp-plugin-gmic
%license COPYING
%{_gimpplugindir}/gmic_gimp_qt
%{_gimpplugindir}/gmic_cluts.gmz

%files -n krita-plugin-gmic
%license COPYING
%{_bindir}/gmic_krita_qt

%if %{with digikam_plugin}
%files -n digikam-plugin-gmic
%license COPYING
%dir %{_libqt5_plugindir}/digikam
%dir %{_libqt5_plugindir}/digikam/editor
%{_libqt5_plugindir}/digikam/editor/Editor_GmicQt_Plugin.so
%endif

%files -n libgmic1
%license COPYING
%{_libdir}/libgmic.so.*

%files -n libgmic-devel
%{_includedir}/gmic.h
%{_libdir}/libgmic.so
%{_libdir}/cmake/gmic/

%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gmic

%changelog
