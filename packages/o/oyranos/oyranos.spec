#
# spec file for package oyranos
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011-2017 Kai-Uwe Behrmann <ku.b@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define syscolordir     %{_datadir}/color
%define usercolordir    ~/.config/color
%define usercolordata   ~/.local/share/color
%define iccdirname      icc
%define cmmsubpath      color/modules
%define metasubpath     oyranos-meta
%define settingsdirname settings
%define targetdirname   target
%define pixmapdir       %{_datadir}/pixmaps
%define icondir         %{_datadir}/icons
%define desktopdir      %{_datadir}/applications
Name:           oyranos
Version:        0.9.6
Release:        0
Summary:        Color Management System
License:        BSD-3-Clause AND GPL-2.0
Group:          Development/Libraries/C and C++
Url:            http://www.oyranos.org
Source0:        oyranos_%{version}.orig.tar.bz2
Source1:        oyranos_%{version}-1.debian.tar.gz
Source2:        oyranos-rpmlintrc
Patch0:         0001-Use-GNUInstallDirs.patch
Patch1:         0002-mv-src-examples-oforms-src-tools-oforms.patch
Patch2:         0003-Make-tests-optional.patch
Patch3:         0004-Make-examples-optional.patch
Patch4:         0005-Make-static-libs-optional.patch
Patch5:         0006-Use-FindFLTK-shipped-by-cmake.patch
Patch6:         0007-No-undefined.patch
# PATCH-FIX-UPSTREAM -- https://github.com/oyranos-cms/oyranos/commit/ac7bdc35ea376f938ad223b0156a04a2af6d2eff
Patch7:         exmpl-update-GLee.h-to-Mesa-18.3.1.patch
# PATCH-FIX-UPSTREAM -- https://github.com/oyranos-cms/oyranos/pull/52
Patch8:         reproducible.patch
BuildRequires:  cmake
BuildRequires:  color-filesystem
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
BuildRequires:  libjpeg-devel
BuildRequires:  libltdl-devel
BuildRequires:  libyajl-devel
BuildRequires:  netpbm
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(elektra)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sane-backends)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcm) >= 0.5.4
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
Requires:       oyranos-monitor
Requires:       oyranos-profile-graph
Recommends:     oyranos-qcmsevents

%package      -n lib%{name}0
Summary:        Color Management System Libraries
# assume users want the device modules
# we need rgb, lab, xyz gray and cmyk profiles
# the proper names: sRGB.icc, XYZ.icc, Lab.icc are in the OpenICC-data package
Group:          System/Libraries
Requires:       icc-profiles
Requires:       lib%{name}0-cups = %{version}
Requires:       lib%{name}0-lraw = %{version}
Requires:       lib%{name}0-monitor = %{version}
# for mount-openicc we need the cli
Requires(post): elektra

%package      -n lib%{name}-devel
Summary:        Development files for oyranos, a color management system
Group:          Development/Libraries/C and C++
Requires:       lib%{name}0 = %{version}
Requires:       libyajl-devel
Requires:       pkgconfig(libxml-2.0)

%package      -n lib%{name}-alpha-devel
Summary:        Alpha and Pre Alpha Headers for Oyranos
Group:          Development/Libraries/Other
Requires:       lib%{name}-devel = %{version}

%package      -n lib%{name}0-monitor
Summary:        Oyranos monitor-dependent libraries
Group:          System/Libraries
Requires:       xcalib

%package      monitor
Summary:        Oyranos Monitor Tools
Group:          System/X11/Utilities
Requires:       lib%{name}0-monitor >= %{version}

%package      profile-graph
Summary:        Profile 2D graph tool
Group:          System/X11/Utilities

%package      -n lib%{name}0-cups
Summary:        CUPS device support for Oyranos
Group:          System/Libraries
Requires:       cups

%package      -n lib%{name}0-lraw
Summary:        LibRaw device support for Oyranos
Group:          System/Libraries

%package      -n lib%{name}0-sane
Summary:        SANE device support for Oyranos
Group:          System/Libraries

%package      ui-fltk
Summary:        Example Configuration Panel and Image Viewer
Group:          System/GUI/Other

%package      qcmsevents
Summary:        Xorg Color management Event observer applet
Group:          System/Monitoring
Requires:       oyranos-monitor

%description
Oyranos is a color management system.
Features:
* configuration for cross application color agreement
* plugable and selectable modules (known as CMMs)
* pixel conversions
* profile handling
* named colors
* device profile assignment

%description -n lib%{name}0
Oyranos is usable to store default profiles and paths and
query for profiles in that paths.
An internal device profile API allowes configuring of a
profile in X.
The documentation in html format is included.
The object oriented Oyranos APIs provide advanced access to
ICC profiles, allow for filtering profile lists and provide
a CMM independent color conversion API. Single color lookups
are supported.
These APIs are to be considered to change very frequently.

%description -n lib%{name}-devel
Header files, libraries and documentation for development.
Oyranos is usable to store default profiles and paths and
query for profiles in that paths.
The documentation in HTML format is included.

%description -n lib%{name}-alpha-devel
Header files and libraries for development.
The object oriented Oyranos APIs provide advanced access to
ICC profiles, allow for filtering profile lists and provide
a CMM independent color conversion API. Single color lookups
are supported.
These APIs are to be considered to change very frequently.

%description  monitor
The monitor profile configuration tool.

%description  -n lib%{name}0-monitor
The monitor support libraries of the
Oyranos color management system.

%description  profile-graph
The grapher renders a simple gamut
hull of a ICC profile in 2D.

%description  -n lib%{name}0-cups
CUPS device support for the
Oyranos color management system.

%description  -n lib%{name}0-lraw
LibRaw device support for the
Oyranos color management system.

%description  -n lib%{name}0-sane
SANE device support for the
Oyranos color management system.

%description  ui-fltk
A example configuration GUI and a image viewer.
Oyranos is a color management system.

%description  qcmsevents
the applet shows if a color server is running through a icon in
the system tray.

%prep
%setup -q
%autopatch -p1

# Remove bundled sources
rm -r libxcm yajl
# TODO: openicc

%build
%cmake \
  -DCMAKE_INSTALL_DOCDIR=share/doc/packages/lib%{name}-devel \
  -DENABLE_FLTK=ON \
  -DUSE_SYSTEM_ELEKTRA=ON \
  -DUSE_SYSTEM_LIBXCM=ON \
  -DUSE_SYSTEM_OPENICC=OFF \
  -DUSE_SYSTEM_YAJL=ON \
  -DCMAKE_DISABLE_FIND_PACKAGE_Qt4=ON \
  -DCMAKE_DISABLE_FIND_PACKAGE_Cairo=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_Cups=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_Doxygen=OFF \
  -DENABLE_EXAMPLES=ON \
  -DCMAKE_DISABLE_FIND_PACKAGE_Exif2=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_FLTK=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_JPEG=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_Qt5=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_LibRaw=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_Sane=OFF \
  -DENABLE_STATIC_LIBS=OFF \
  -DENABLE_TESTS=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_TIFF=OFF \
  -DCMAKE_DISABLE_FIND_PACKAGE_X11=OFF
make %{?_smp_mflags}

%install
%cmake_install
# remove qt4 mans
rm %{buildroot}%{_mandir}/man1/qcmsevents-qt4.1
rm -fr %{buildroot}/%{_datadir}/doc/%{name}-%{version}
cp -av src/tools/qcmsevents/qcmsevents-applet.desktop .
cp -av extras/%{name}-profile-install.desktop .
cp -av src/examples/image_display/%{name}-image-display.desktop .
echo 'X-SuSE-translate=true' >> qcmsevents-applet.desktop
echo 'X-SuSE-translate=true' >> %{name}-profile-install.desktop
echo 'X-SuSE-translate=true' >> %{name}-image-display.desktop
desktop-file-install --dir=%{buildroot}/%{desktopdir} qcmsevents-applet.desktop
desktop-file-install --dir=%{buildroot}/%{desktopdir} %{name}-profile-install.desktop
desktop-file-install --dir=%{buildroot}/%{desktopdir} %{name}-image-display.desktop

# Fix cmake detectors
sed -i \
    -e "s:/usr//usr:%{_prefix}:g" \
    %{buildroot}%{_libdir}/cmake/%{name}/*.cmake

%find_lang %{name}       # generate a special file list

%post -n lib%{name}0
/sbin/ldconfig
export LD_LIBRARY_PATH=%{_libdir}/elektra4/:$LD_LIBRARY_PATH
kdb mount-openicc || :

%postun -n lib%{name}0 -p /sbin/ldconfig

%files -f %{name}.lang
%doc AUTHORS.md COPYING.md ChangeLog.md README.md
%{_bindir}/%{name}-compat-gnome
%{_bindir}/%{name}-icc
%{_bindir}/%{name}-policy
%{_bindir}/%{name}-profile
%{_bindir}/%{name}-profiles
%{_bindir}/%{name}-profile-install
%{_bindir}/%{name}-xforms
%{_bindir}/%{name}-xforms-modules
%{_mandir}/man1/%{name}-policy*
%{_mandir}/man1/%{name}-profile.1*
%{_mandir}/man1/%{name}-profiles.1*
%{_mandir}/man1/%{name}-profile-install.1*
%{_mandir}/man1/%{name}-xforms.1*
%{_mandir}/man1/%{name}-xforms-modules.1*
%{pixmapdir}/oyranos_logo.*
%{pixmapdir}/lcms_logo2.png
%dir %{syscolordir}/%{settingsdirname}
%{syscolordir}/%{settingsdirname}/*.policy.xml
%{desktopdir}/%{name}-profile-install.desktop

%files -n lib%{name}0
%{_libdir}/libOyranosCore.so.*
%{_libdir}/libOyranosObject.so.*
%{_libdir}/libOyranosModules.so.*
%{_libdir}/libOyranosConfig.so.*
%{_libdir}/libOyranos.so.*
%dir %{_libdir}/color/
%dir %{_libdir}/%{cmmsubpath}/
%dir %{_libdir}/%{metasubpath}/
%{_libdir}/%{cmmsubpath}/lib%{name}_*DB_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_lcm*
%{_libdir}/%{cmmsubpath}/lib%{name}_oyra_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_oicc_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_oPNG_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_oJPG_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_trds_cmm_module*
%{_libdir}/%{metasubpath}/lib%{name}_oyIM_cmm_module*

%files -n lib%{name}-devel
%{_bindir}/%{name}-config
%{_libdir}/libOyranosCore.so
%{_libdir}/libOyranosObject.so
%{_libdir}/libOyranosModules.so
%{_libdir}/libOyranosConfig.so
%{_libdir}/libOyranos.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/icc34.h
%{_includedir}/%{name}/oy*.h
%{_libdir}/pkgconfig/*
%dir %{_libdir}/cmake/oyranos/
%{_libdir}/cmake/oyranos/*.cmake
%{_mandir}/man3/%{name}-config.3*
%{_mandir}/man3/%{name}.3%{ext_man}
%{_docdir}/lib%{name}-devel

%files -n lib%{name}-alpha-devel
%dir %{_includedir}/%{name}/alpha
%{_includedir}/%{name}/alpha/%{name}_alpha.h

%files monitor
%{_bindir}/%{name}-monitor
%{_bindir}/%{name}-monitor-daemon
%{_mandir}/man1/%{name}-monitor.1*
%{_mandir}/man1/%{name}-monitor-daemon.1*
%{_sysconfdir}/xdg/autostart/%{name}-monitor-setup.desktop

%files -n lib%{name}0-monitor
%dir %{_libdir}/color/
%dir %{_libdir}/%{cmmsubpath}/
%{_libdir}/%{cmmsubpath}/lib%{name}_oyX1_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_oydi_cmm_module*
%dir %{syscolordir}/rank-map
%{syscolordir}/rank-map/config.icc_profile.monitor.*.json

%files -n lib%{name}0-cups
%dir %{_libdir}/color/
%dir %{_libdir}/%{cmmsubpath}/
%{_libdir}/%{cmmsubpath}/lib%{name}_CUPS_cmm_module*
%dir %{syscolordir}/rank-map
%{syscolordir}/rank-map/config.icc_profile.printer.*.json

%files -n lib%{name}0-lraw
%dir %{_libdir}/color/
%dir %{_libdir}/%{cmmsubpath}/
%{_libdir}/%{cmmsubpath}/lib%{name}_lraw_cmm_module*
%{_libdir}/%{cmmsubpath}/lib%{name}_oyRE_cmm_module*
%dir %{syscolordir}/rank-map
%{syscolordir}/rank-map/config.icc_profile.raw-image.*.json

%files -n lib%{name}0-sane
%dir %{_libdir}/color/
%dir %{_libdir}/%{cmmsubpath}/
%{_libdir}/%{cmmsubpath}/lib%{name}_SANE_cmm_module*
%dir %{syscolordir}/rank-map
%{syscolordir}/rank-map/config.icc_profile.scanner.*.json

%files ui-fltk
%{_bindir}/%{name}-config-fl*
%{_bindir}/%{name}-image-display
%{_bindir}/%{name}-xforms-fltk
%{_mandir}/man1/%{name}-config-fltk.1*
%{_mandir}/man1/%{name}-image-display.1*
%{_mandir}/man1/%{name}-xforms-fltk.1*
%{desktopdir}/%{name}-image-display.desktop

%files qcmsevents
%{_bindir}/qcmsevents
%{_mandir}/man1/qcmsevents.1*
%{pixmapdir}/qcmsevents.*
%{desktopdir}/qcmsevents-applet.desktop

%files profile-graph
%{_bindir}/%{name}-profile-graph
%{_mandir}/man1/%{name}-profile-graph.1*

%changelog
