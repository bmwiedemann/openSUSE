#
# spec file for package gmic
#
# Copyright (c) 2022 SUSE LLC
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


%if %{pkg_vcmp krita >= 5}
%bcond_without krita5
%else
%bcond_with    krita5
%endif

%if %{pkg_vcmp gimp >= 2.99}
%define gimp_suffix 3
%global _gimpplugindir %(gimptool-2.99 --gimpplugindir)/plug-ins/
%else
%global _gimpplugindir %(gimptool-2.0 --gimpplugindir)/plug-ins/
%endif

%if %{with krita5}
%define hostapps gimp%{?gimp_suffix}
%else
%define hostapps gimp%{?gimp_suffix} krita
%endif

%define gmic_qt_options -DENABLE_SYSTEM_GMIC=OFF -DENABLE_DYNAMIC_LINKING=ON

%define gmic_datadir %{_datadir}/gmic

Name:           gmic
Version:        3.1.6
Release:        0
Summary:        GREYC's Magick for Image Computing (denoise and others)
# gmic-qt is GPL-3.0-or-later, zart is CECILL-2.0, libgmic and cli program are
# CECILL-2.1
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://gmic.eu
# Git URL:      https://github.com/dtschump/gmic
Source0:        https://gmic.eu/files/source/gmic_%{version}.tar.gz
# PATCH-FIX-UPSTREAM krita.patch - Will be sent upstream soon. For now https://github.com/darix/gmic-qt/tree/krita5
Patch0:         krita5.patch
# PATCH-FEATURE-OPENSUSE
Patch1:         0001-Find-the-local-gmic-library.patch
#
# SECTION pkg_vcmp
#
# Those 2 are used for the pkg_vcmp conditionals above and also the rich expressions in the BuildRequires below
#
BuildRequires:  gimp
BuildRequires:  krita
#
# /SECTION
#
BuildRequires:  cmake >= 3.14.0
BuildRequires:  dos2unix
BuildRequires:  fftw3-threads-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
BuildRequires:  (krita-devel if krita >= 5)
BuildRequires:  (pkgconfig(gimp-2.0) if gimp < 2.99)
BuildRequires:  (pkgconfig(gimp-3.0) if gimp >= 2.99)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(zlib)
# gmic first looks for opencv 4 and falls back to opencv 3 if not found.
# opencv 4 in not available in leap <= 15.3
%if 0%{suse_version} == 1500 && 0%{?sle_version} < 150400
BuildRequires:  pkgconfig(opencv)
%else
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig(zlib)
%endif
Requires:       gmic-data = %{version}

%description
G'MIC is a framework for image processing, providing
several different user interfaces to convert/manipulate/filter/visualize
generic image datasets, from 1d scalar signals to 3d+t sequences of
multi-spectral volumetric images.

%package -n libgmic3
Summary:        Shared library that belongs to gmic
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors

%package -n libgmic-devel
Summary:        Header and library from gmic for use in other C++ projects
License:        CECILL-2.1
Group:          Development/Libraries/C and C++
Requires:       libgmic3 = %{version}

%description -n libgmic3
Shared library allows you to use gmic functionality from other
programs.

%description -n libgmic-devel
Header and library from gmic to needed to develop C++ code that
uses the gmic functionality provided by the gmic library.

%package -n gimp-plugin-gmic
Summary:        GMIC plugin for gimp
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
Requires:       gmic-data = %{version}
%requires_eq    gimp
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
Requires:       gmic-data = %{version}
%requires_eq    krita

%description -n  krita-plugin-gmic
This is a plugin for krita to provide gmic features.

%package bash-completion
Summary:        Bash completion for gmic
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
This package contains the bash completion command for gmic.

%package data
Summary:        Shared data files for the various gmic frontends
License:        CECILL-2.1
Group:          Productivity/Graphics/Bitmap Editors
BuildArch:      noarch

%description data
This package contains shared data files for the various gmic frontends.

%prep
%setup -q
dos2unix src/{gmic_libc.*,use_libcgmic.c}
%autopatch -p1

%build
# Build gmic
# Starting with gmic 3.1.0, the gmic dev replaced their CMake build system with a non-configurable Makefile...
sed -i 's#LIB = lib#LIB = %{_lib}#' src/Makefile

# Breaks compilation for a couple archs
sed -i 's#-mtune=generic##' src/Makefile

# Broken rpath
sed -i 's# -Wl,-rpath,.##' src/Makefile

# The file is moved post-install in a directory not owned by gimp
sed -i 's#/usr/lib/gimp/2.0/plug-ins#%{gmic_datadir}#' src/gmic_stdlib.gmic

EXTRA_CFLAGS='%{optflags}' NOSTRIP=1 make lib cli_shared

# Build gmic{_gimp|_krita}_qt
pushd gmic-qt

%cmake %{gmic_qt_options} -DGMIC_QT_HOST=none
%cmake_build

cd ..

for hostapp in %{hostapps} ; do
%cmake %{gmic_qt_options} -DGMIC_QT_HOST=${hostapp}
%cmake_build

cd ..
done

%if %{with krita5}
%cmake_kf5 -d plugin-build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir} %{gmic_qt_options} -DGMIC_QT_HOST=krita-plugin -DCMAKE_BUILD_TYPE=RelWithDebInfo

%cmake_build

cd ..
%endif
popd

%install
DESTDIR=%{buildroot} make install

# As planned, only providing a Makefile partially works...
install -m 0644 src/CImg.h %{buildroot}%{_includedir}

# Install icons
for size in 16 32 48 64; do
    install -Dm 0644 gmic-qt/icons/application/${size}-gmic_qt.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/gmic_qt.png
done
install -Dm 0644 gmic-qt/icons/application/gmic_qt.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/gmic_qt.svg

%if %{with krita5}
DESTDIR=%{buildroot} cmake --install gmic-qt/plugin-build
%else
# krita plugin
install -m 0755 gmic-qt/build/gmic_krita_qt %{buildroot}%{_bindir}/gmic_krita_qt
%endif

%suse_update_desktop_file -c gmic_qt "G'Mic Qt" "G'MIC Qt GUI" "gmic_qt %%F" gmic_qt "Qt;Graphics;Photography;"

# Film color lookup tables
install -d -m 0755 \
    %{buildroot}%{_gimpplugindir} \
    %{buildroot}%{gmic_datadir}/

# Move gmic plugins out of the gimp plugin dir
for file in gmic_cluts.gmz gmic_denoise_cnn.gmz ; do
    mv %{buildroot}%{_libdir}/gimp/2.0/plug-ins/${file} %{buildroot}%{gmic_datadir}/
done

# This manpage isn't translated
rm %{buildroot}%{_mandir}/fr/man1/gmic.1*

# qt_gmic
pushd gmic-qt
install -m 0755 build/gmic_qt %{buildroot}%{_bindir}/gmic_qt

# gimp plugin
install -m 0755 build/gmic_gimp_qt %{buildroot}%{_gimpplugindir}/gmic_gimp_qt
popd

%post -n libgmic3 -p /sbin/ldconfig
%postun -n libgmic3 -p /sbin/ldconfig

%files
%doc README gmic-qt/README.md
%{_bindir}/gmic
%{_bindir}/gmic_qt
%{_mandir}/man1/gmic.1%{?ext_man}
%{_datadir}/applications/gmic_qt.desktop
%{_datadir}/icons/hicolor/*/apps/gmic_qt.png
%{_datadir}/icons/hicolor/scalable/apps/gmic_qt.svg

%files data
%{gmic_datadir}/

%files -n gimp-plugin-gmic
%{_gimpplugindir}/

%files -n krita-plugin-gmic
%if %{with krita5}
%{_kf5_libdir}/kritaplugins/krita_gmic_qt.so
%else
%{_bindir}/gmic_krita_qt
%endif

%files -n libgmic3
%license COPYING
%{_libdir}/libgmic.so.*

%files -n libgmic-devel
%{_includedir}/CImg.h
%{_includedir}/gmic.h
%{_includedir}/gmic_libc.h
%{_libdir}/libgmic.so

%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/gmic

%changelog
