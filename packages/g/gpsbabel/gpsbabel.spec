#
# spec file for package gpsbabel
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


%global translationdir %{_datadir}/qt5/translations
Name:           gpsbabel
Version:        1.8.0
Release:        0
Summary:        Converts GPS waypoint, route and track data from one format type to another
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://www.gpsbabel.org/
Source:         https://github.com/GPSBabel/gpsbabel/archive/refs/tags/%{name}_1_8_0.tar.gz
Source1:        http://www.gpsbabel.org/htmldoc-%{version}/%{name}-%{version}.pdf
Source2:        %{name}.png
Source21:       style3.css
# No automatic phone home by default (RHBZ 668865)
Patch4:         0004-gpsbabel-1.4.3-nosolicitation.patch
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebChannel)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(shapelib)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GPSBabel converts waypoints, tracks, and routes from one format to
another, whether that format is a common mapping format like Delorme,
Streets and Trips, or even a serial upload or download to a GPS unit
such as those from Garmin and Magellan. By flattening the Tower of
Babel that the authors of various programs for manipulating GPS data
have imposed upon us, it returns to us the ability to freely move our
own waypoint data between the programs and hardware we choose to use.

It contains extensive data manipulation abilities making it a
convenient for server-side processing or as the backend for other
tools.

It does not convert, transfer, send, or manipulate maps. We process
data that may (or may not be) placed on a map, such as waypoints,
tracks, and routes.

%package gui
Summary:        Qt GUI interface for GPSBabel
Group:          Hardware/Other
Requires:       %{name} = %{version}-%{release}
Requires(post): update-desktop-files
Requires(postun):update-desktop-files

%description gui
Qt GUI interface for GPSBabel

%prep
%autosetup -p1 -n gpsbabel-gpsbabel_1_8_0
# Use system shapelib instead of bundled partial shapelib
rm -rf shapelib

# Get rid of bundled zlib
rm -rf zlib/*

cp -p %{SOURCE21} gpsbabel.org-style3.css

# Fixup categories for .desktop file
sed -i \
    -e 's:Utility;::g' \
    gui/gpsbabel.desktop

%build
%qmake5 PREFIX=%{_prefix} WITH_LIBUSB=system WITH_SHAPELIB=pkgconfig WITH_ZLIB=pkgconfig
make %{?_smp_mflags}
cp %{SOURCE1} %{name}.pdf

pushd gui
CFLAGS="%{optflags}" \
%qmake5 PREFIX=%{_prefix}
lrelease-qt5 *.ts
make %{?_smp_mflags}
popd

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

make -C gui DESTDIR=%{buildroot} install

install -m 0755 -d %{buildroot}/%{_bindir}
install -m 0755 -p gpsbabel %{buildroot}/%{_bindir}
install -m 0755 -p gui/objects/gpsbabelfe %{buildroot}/%{_bindir}
install -m 0755 -d %{buildroot}/%{_datadir}/%{name}
install -m 0644 -p gui/gmapbase.html %{buildroot}/%{_datadir}/%{name}/
install -m 0755 -d %{buildroot}/%{translationdir}
install -m 0644 -p gui/gpsbabelfe_*.qm %{buildroot}/%{translationdir}/
install -m 0644 -p gui/coretool/gpsbabel_*.qm %{buildroot}/%{translationdir}/

install -m 0755 -d %{buildroot}/%{_datadir}/applications
install -m 0644 gui/gpsbabel.desktop %{buildroot}/%{_datadir}/applications

install -m 0755 -d            %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
install -m 0644 -p %{SOURCE2} %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/

%find_lang %{name} --with-qt --all-name

%post gui
%icon_theme_cache_post
%desktop_database_post

%postun gui
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS README* %{name}.pdf
%license COPYING
%{_bindir}/gpsbabel
%{_bindir}/gpsbabelfe
%{_datadir}/applications/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{translationdir}/
%{translationdir}/*
%dir %{_datadir}/icons/hicolor/256x256/
%dir %{_datadir}/icons/hicolor/256x256/apps/
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
