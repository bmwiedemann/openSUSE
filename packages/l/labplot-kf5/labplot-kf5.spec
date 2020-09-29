#
# spec file for package labplot-kf5
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


%if "%{?_kf5_appstreamdir}" == ""
# it's not defined in Leap 42.1, so define it appropriately in that case
%define _kf5_appstreamdir %{_kf5_sharedir}/appdata
%endif
Name:           labplot-kf5
Version:        2.8.0
Release:        0
Summary:        KDE Framework 5 data analysis and visualization application
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://labplot.kde.org/
Source:         https://download.kde.org/stable/labplot/%{version}/labplot-%{version}.tar.xz
# PATCH-FIX-UPSTREAM fix_labplot_assumption_cantor_version.patch andythe_great@pm.me -- Fix Labplot 2.8.0 wrong assumption that Cantor 20.08.1 has a new interface.
Patch0:         fix_labplot_assumption_cantor_version.patch
BuildRequires:  bison
BuildRequires:  cantor-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hdf5-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Service)
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120300
# only available since Leap 42.3
BuildRequires:  cmake(KF5SyntaxHighlighting)
%endif
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5SerialPort)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(zlib)
Provides:       labplot = %{version}
Obsoletes:      labplot < 2.3.0
%lang_package

%description
LabPlot is a KDE application for interactive graphing and analysis
of scientific data. LabPlot provides an easy way to create, manage
and edit plots. It allows you to produce plots based on data from a
spreadsheet or on data imported from external files. Plots can be
exported to several pixmap and vector graphic formats.

This version is based on KDE Frameworks 5

%prep
%setup -q -n labplot-%{version}
%patch0 -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%find_lang labplot2 --with-man %{?no_lang_C}

%fdupes -s %{buildroot}

%kf5_post_install

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_kf5_bindir}/labplot2
%{_kf5_appsdir}/labplot2/
%{_kf5_applicationsdir}/org.kde.labplot2.desktop
%dir %{_kf5_iconsdir}/hicolor/512x512/
%dir %{_kf5_iconsdir}/hicolor/512x512/apps/
%{_kf5_iconsdir}/hicolor/scalable/apps/labplot-*
%{_kf5_iconsdir}/hicolor/*/apps/labplot2.*
%{_kf5_kxmlguidir}/labplot2/
%{_kf5_sharedir}/mime/packages/labplot2.xml
%dir %{_kf5_appstreamdir}
%{_kf5_appstreamdir}/org.kde.labplot2.appdata.xml
%{_kf5_htmldir}/en/labplot2/
%{_kf5_mandir}/man1/labplot2.1%{?ext_man}

%files lang -f labplot2.lang
%{_kf5_htmldir}/*/labplot2/
## These belong in the main package
%exclude %{_kf5_htmldir}/en/labplot2/

%changelog
