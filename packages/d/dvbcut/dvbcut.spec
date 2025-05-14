#
# spec file for package dvbcut
#
# Copyright (c) 2024 SUSE LLC
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


Name:           dvbcut
Version:        0.7.4
Release:        0
Summary:        Qt application for cutting parts out of DVB streams
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/bernhardu/dvbcut-deb
Source0:        https://github.com/bernhardu/dvbcut-deb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE dvbcut-use_pkgconfig.patch aloisio@gmx.com -- use pkgconfig for ffmpeg libraries
Patch1:         dvbcut-use_pkgconfig.patch
# PATCH-FIX-OPENSUSE dvbcut-a52.patch aloisio@gmx.com -- Support new version of liba52
Patch2:         dvbcut-a52.patch
# PATCH-FIX-OPENSUSE dvbcut-appicon-patch aloisio@gmx.com -- install icon in the proper path
Patch3:         dvbcut-appicon.patch
# PATCH-FIX-OPENSUSE dvbcut-locale.patch aloisio@gmx.com -- also install .qm locale files
Patch4:         dvbcut-locale.patch
# PATCH-FIX-OPENSUSE dvbcut-autoconf269.patch aloisio@gmx.com -- autoconf 2.71 is not really necessary
Patch5:         dvbcut-autoconf269.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(liba52)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libavcodec) < 60.31.102
BuildRequires:  pkgconfig(libavformat) < 60.16.100
BuildRequires:  pkgconfig(libavutil) < 58.29.100
BuildRequires:  pkgconfig(libswscale) < 7.5.100
%else
BuildRequires:  pkgconfig(libavcodec) >= 58.7.100
BuildRequires:  pkgconfig(libavformat) >= 58.0.102
BuildRequires:  pkgconfig(libavutil) >= 56.6.100
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
%endif
BuildRequires:  pkgconfig(mad)

%description
DVBcut is a Qt application that allows you to select certain parts of an MPEG
transport stream (as received via Digital Video Broadcasting, DVB) and save
these parts into a single MPEG output file. It follows a `keyhole surgery''
approach where the input video and audio data is mostly kept unchanged, and
only very few frames at the beginning and/or end of the selected range are re-
encoded in order to obtain a valid MPEG file.

%prep
%autosetup -p1 -n %{name}-deb-%{version}

%build
%if %{pkg_vcmp liba52 <= 0.7.9}
EXTRA_CXXFLAGS="-DLIBA52_07"
%endif
export CXXFLAGS="-std=c++11 %{optflags} $EXTRA_CXXFLAGS"
export CPPFLAGS=-DDVBCUT_VERSION=\\\"%{version}\\\"
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}%{_datadir}

%files
%doc ChangeLog README README.icons
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
