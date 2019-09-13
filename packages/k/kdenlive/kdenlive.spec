#
# spec file for package kdenlive
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define mlt_version 6.10.0
%define melt_path %(pkg-config --variable=meltbin mlt-framework)
%define mlt_soname %(pkg-config --variable=moduledir mlt-framework | sed 's/.*-\\([0-9]\\+\\)/\\1/')
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kdenlive
Version:        19.08.1
Release:        0
Summary:        Non-linear video editor
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://www.kdenlive.org/
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  knewstuff-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kplotting-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libmlt-devel
BuildRequires:  pkgconfig
BuildRequires:  purpose-devel
BuildRequires:  rttr-devel
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(mlt++) >= %{mlt_version}
BuildRequires:  pkgconfig(mlt-framework) >= %{mlt_version}
BuildRequires:  pkgconfig(x11)
# Waiting for the day all libraries have versioned symbols...
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt++.so) --qf '%%{NAME}') >= %{mlt_version}
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%%{NAME}') >= %{mlt_version}
# It requires the profiles
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%%{NAME}')-data
# Without a few of the plugins it crashes on start
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libmlt.so) --qf '%%{NAME}')-modules
Requires:       %{melt_path}
# It doesn't start without it (boo#994649)
Requires:       libqt5-qtquickcontrols
# needed for the new timeline
Requires:       libqt5-qtquickcontrols2
Recommends:     %{_bindir}/dvdauthor
Recommends:     %{_bindir}/dvgrab
Recommends:     %{_bindir}/ffmpeg
Recommends:     %{_bindir}/ffplay
Recommends:     %{_bindir}/genisoimage
Recommends:     frei0r-plugins
Recommends:     libv4l
Recommends:     mlt(%{mlt_soname})(avformat)
Obsoletes:      kdenlive5 < %{version}
Provides:       kdenlive5 = %{version}
Recommends:     %{name}-lang

%description
Kdenlive is a non-linear video editor for GNU/Linux and FreeBSD, which supports
DV, AVCHD (experimental support) and HDV editing. Kdenlive relies on several
other open source projects, such as FFmpeg and the MLT video framework. It was
designed to answer all needs, from basic video editing to semi-professional
work.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif
%fdupes -s %{buildroot}
rm -fr %{buildroot}%{_datadir}/doc/Kdenlive

%post
%icon_theme_cache_post
%mime_database_post
%desktop_database_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun

%files
%defattr(0644,root,root,0755)
%attr(0755,-,-) %{_bindir}/%{name}
%attr(0755,-,-) %{_bindir}/%{name}_render
%license COPYING
%doc AUTHORS README.md
%(config) %{_kf5_configdir}/*.knsrc
%dir %{_kf5_configkcfgdir}
%doc %lang(en) %{_kf5_htmldir}/en/kdenlive/
%{_kf5_applicationsdir}/org.kde.kdenlive.desktop
%{_kf5_appstreamdir}/
%{_kf5_configkcfgdir}/kdenlivesettings.kcfg
%{_kf5_debugdir}/kdenlive.categories
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/kdenlive/
%{_kf5_mandir}/man1/*
%{_kf5_plugindir}/mltpreview.so
%{_kf5_servicesdir}/mltpreview.desktop
%{_kf5_sharedir}/kdenlive/
%{_kf5_sharedir}/knotifications5/kdenlive.notifyrc
%{_kf5_sharedir}/mime/packages/*

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
