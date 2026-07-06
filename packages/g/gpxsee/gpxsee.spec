#
# spec file for package gpxsee
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           gpxsee
Version:        16.11
Release:        1
Summary:        GPS log file visualization and analysis tool
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
Url:            http://www.gpxsee.org
Source0:        https://github.com/tumic0/GPXSee/archive/%{version}/GPXSee-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  desktop-file-utils
%if 0%{?fedora_version}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtpositioning-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-qtmultimedia-devel
BuildRequires:  zlib-devel
BuildRequires:  qt6-linguist
Recommends: qt6-qtimageformats
%else
%if 0%{?suse_version}
BuildRequires:  qt6-core-devel
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-gui-devel
BuildRequires:  qt6-widgets-devel
BuildRequires:  qt6-network-devel
BuildRequires:  qt6-printsupport-devel
BuildRequires:  qt6-openglwidgets-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-serialport-devel
BuildRequires:  qt6-positioning-devel
BuildRequires:  qt6-multimedia-devel
BuildRequires:  qt6-multimediawidgets-devel
BuildRequires:  zlib-devel
BuildRequires:  qt6-tools-linguist
Recommends: qt6-sql-sqlite
Recommends: qt6-imageformats
%else
# Mageia
BuildRequires:  libqt6core-devel
BuildRequires:  libqt6gui-devel
BuildRequires:  libqt6concurrent-devel
BuildRequires:  libqt6widgets-devel
BuildRequires:  libqt6network-devel
BuildRequires:  libqt6printsupport-devel
BuildRequires:  libqt6openglwidgets-devel
BuildRequires:  libqt6sql-devel
BuildRequires:  libqt6svg-devel
BuildRequires:  libqt6positioning-devel
BuildRequires:  libqt6serialport-devel
BuildRequires:  libqt6multimedia-devel
BuildRequires:  libqt6multimediawidgets-devel
BuildRequires:  lib64zlib-devel
BuildRequires:  qttools6
Recommends: qtimageformats6
Recommends: libqt6-database-plugin-sqlite
%endif
%endif

%description
GPXSee is a Qt-based tool for visualizing and analyzing GPX, TCX, FIT, KML,
IGC, CUP, NMEA, SLF, SML, LOC, OziExplorer (PLT, RTE, WPT), Garmin GPI&CSV,
TomTom OV2&ITN, ONmove OMD/GHP and geotagged JPEG files.

%prep
%setup -q -n GPXSee-%{version}

%build
%if 0%{?suse_version}
%if 0%{?suse_version} > 1600
lrelease-pro6 gpxsee.pro
%else
lrelease6 gpxsee.pro
%endif
%{qmake6} PREFIX=%{_prefix} gpxsee.pro
%else
%if 0%{?fedora_version} > 44
lrelease-pro-qt6 gpxsee.pro
%else
lrelease-qt6 gpxsee.pro
%endif
%{qmake_qt6} PREFIX=%{_prefix} gpxsee.pro
%endif
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post
%mime_database_post
%desktop_database_post

%postun
%mime_database_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%dir %{_datadir}/gpxsee
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/*

%changelog
