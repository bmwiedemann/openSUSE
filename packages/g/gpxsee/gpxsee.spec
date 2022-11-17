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
Version:        11.9
Release:        1
Summary:        GPS log file visualization and analysis tool
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
Url:            http://www.gpxsee.org
Source0:        GPXSee-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  make
%if 0%{?centos_version} >= 800
BuildRequires:  gdb-headless
%endif
%if 0%{?fedora_version} || 0%{?centos_version} >= 800
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-linguist
Recommends: qt5-qtimageformats
Recommends: qt5-qtserialport
Recommends: qt5-qtpbfimageformat
%else
%if 0%{?suse_version}
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5Concurrent-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5PrintSupport-devel
BuildRequires:  libQt5OpenGL-devel
BuildRequires:  libQt5Sql-devel
BuildRequires:  libQt5Svg-devel
BuildRequires:  libqt5-qtlocation-devel
BuildRequires:  libqt5-linguist
Recommends: libQt5Sql5-sqlite
Recommends: libQt5SerialPort5
Recommends: libqt5-qtimageformats
Recommends: libqt5-qtpbfimageformat
%else
# Mageia
BuildRequires:  libqt5core-devel
BuildRequires:  libqt5gui-devel
BuildRequires:  libqt5concurrent-devel
BuildRequires:  libqt5widgets-devel
BuildRequires:  libqt5network-devel
BuildRequires:  libqt5printsupport-devel
BuildRequires:  libqt5opengl-devel
BuildRequires:  libqt5sql-devel
BuildRequires:  libqt5svg-devel
BuildRequires:  libqt5location-devel
BuildRequires:  qttools5
Recommends: qtimageformats5
Recommends: libqt5-qtserialport
Recommends: libqt5-database-plugin-sqlite
Recommends: libqt5-qtpbfimageformat
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
lrelease-qt5 gpxsee.pro
%{qmake5} gpxsee.pro
%else
%if 0%{?fedora_version} || 0%{?centos_version} >= 800
lrelease-qt5 gpxsee.pro
%{qmake_qt5} gpxsee.pro
%else
lrelease gpxsee.pro
%{qmake_qt5} gpxsee.pro
%endif
%endif
make %{?_smp_mflags}

%install
install -d 755 %{buildroot}/%{_bindir}
install -d 755 %{buildroot}/%{_datadir}/applications
install -d 755 %{buildroot}/%{_datadir}/icons/hicolor
install -d 755 %{buildroot}/%{_datadir}/mime/packages
install -d 755 %{buildroot}/%{_datadir}/%{name}
install -d 755 %{buildroot}/%{_datadir}/%{name}/maps
install -d 755 %{buildroot}/%{_datadir}/%{name}/csv
install -d 755 %{buildroot}/%{_datadir}/%{name}/translations
install -d 755 %{buildroot}/%{_datadir}/%{name}/symbols
install -m 755 gpxsee %{buildroot}/%{_bindir}/%{name}
install -m 644 pkg/maps/* %{buildroot}/%{_datadir}/%{name}/maps
install -m 644 pkg/csv/* %{buildroot}/%{_datadir}/%{name}/csv
install -m 644 lang/*.qm %{buildroot}/%{_datadir}/%{name}/translations
install -m 644 icons/symbols/*.png %{buildroot}/%{_datadir}/%{name}/symbols
cp -r icons/app/hicolor/* %{buildroot}/%{_datadir}/icons/hicolor
install -m 644 pkg/gpxsee.desktop %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -m 644 pkg/gpxsee.xml %{buildroot}/%{_datadir}/mime/packages/%{name}.xml

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
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/*

%changelog
