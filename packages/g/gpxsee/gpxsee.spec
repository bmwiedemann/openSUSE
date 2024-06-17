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
Version:        13.22
Release:        1
Summary:        GPS log file visualization and analysis tool
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
Url:            http://www.gpxsee.org
Source0:        https://github.com/tumic0/GPXSee/archive/%{version}/GPXSee-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
%if 0%{?fedora_version}
BuildRequires:  qt6-qtbase
BuildRequires:  qt6-qtbase-gui
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtpositioning-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qtserialport-devel
BuildRequires:  qt6-linguist
Recommends: qt6-qtimageformats
Recommends: qt6-qtpbfimageformat
%else
%if 0%{?suse_version}
BuildRequires:  qt6-core-devel
BuildRequires:  qt6-concurrent-devel
BuildRequires:  qt6-gui-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-devel
BuildRequires:  qt6-network-devel
BuildRequires:  qt6-printsupport-devel
BuildRequires:  qt6-openglwidgets-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  qt6-serialport-devel
BuildRequires:  qt6-positioning-devel
BuildRequires:  qt6-tools-linguist
Recommends: qt6-sql-sqlite
Recommends: qt6-imageformats
Recommends: qt6-qtpbfimageformat
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
BuildRequires:  qttools6
Recommends: qtimageformats6
Recommends: libqt6-database-plugin-sqlite
Recommends: libqt6-qtpbfimageformat
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
lrelease6 gpxsee.pro
%{qmake6} gpxsee.pro
%else
lrelease-qt6 gpxsee.pro
%{qmake_qt6} gpxsee.pro
%endif
make %{?_smp_mflags}

%install
install -d 755 %{buildroot}/%{_bindir}
install -d 755 %{buildroot}/%{_datadir}/applications
install -d 755 %{buildroot}/%{_datadir}/icons/hicolor
install -d 755 %{buildroot}/%{_datadir}/mime/packages
install -d 755 %{buildroot}/%{_datadir}/metainfo
install -d 755 %{buildroot}/%{_datadir}/%{name}
install -d 755 %{buildroot}/%{_datadir}/%{name}/maps
install -d 755 %{buildroot}/%{_datadir}/%{name}/CRS
install -d 755 %{buildroot}/%{_datadir}/%{name}/translations
install -d 755 %{buildroot}/%{_datadir}/%{name}/symbols
install -m 755 gpxsee %{buildroot}/%{_bindir}/%{name}
install -m 644 data/maps/* %{buildroot}/%{_datadir}/%{name}/maps
install -m 644 data/CRS/* %{buildroot}/%{_datadir}/%{name}/CRS
install -m 644 lang/*.qm %{buildroot}/%{_datadir}/%{name}/translations
install -m 644 icons/symbols/*.png %{buildroot}/%{_datadir}/%{name}/symbols
cp -r icons/app/hicolor/* %{buildroot}/%{_datadir}/icons/hicolor
install -m 644 pkg/linux/gpxsee.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -m 644 pkg/linux/gpxsee.xml %{buildroot}/%{_datadir}/mime/packages/%{name}.xml
install -m 644 pkg/linux/gpxsee.appdata.xml %{buildroot}/%{_datadir}/metainfo/%{name}.xml

%post
if [ -x /usr/bin/update-mime-database ]; then
	/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
if [ -x /usr/bin/update-desktop-database ]; then
	/usr/bin/update-desktop-database > /dev/null || :
fi

%postun
if [ -x /usr/bin/update-mime-database ]; then
	/usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
if [ -x /usr/bin/update-desktop-database ]; then
	/usr/bin/update-desktop-database > /dev/null || :
fi

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
