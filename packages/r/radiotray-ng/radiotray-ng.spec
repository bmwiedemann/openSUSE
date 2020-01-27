#
# spec file for package radiotray-ng
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


Name:           radiotray-ng
Version:        0.2.7
Release:        0
Summary:        An Internet radio player
License:        GPL-3.0-or-later
URL:            https://github.com/ebruck/radiotray-ng
Source:         %{name}-%{version}.tar.xz
Patch0:         radiotray-ng-openSUSE.patch
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(appindicator3-0.1)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  pkgconfig(glibmm-2.4)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libbsd)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxdg-basedir)
Provides:       radiotray = 0.8
Obsoletes:      radiotray < 0.8

%description
Radio Tray is an online radio streaming player that runs on a Linux system
tray. Its goal is to have the minimum interface possible, making it very
straightforward to use.

Radiotray-NG is a rewrite of the classical radiotray application, but based
on modern technologies (gstreamer 1.0, python3 and c++)

%prep
%autosetup -p1

%build
%cmake \
    -DLSB_RELEASE_EXECUTABLE="lsb_release" \
    -DDISTRIBUTOR_ID="openSUSE"
%cmake_build

%install
%cmake_install


%files
%license COPYING
%{_sysconfdir}/xdg/autostart/radiotray-ng.desktop
%{_bindir}/radiotray-ng
%{_bindir}/rt2rtng
%{_bindir}/rtng-bookmark-editor
%{_datadir}/applications/radiotray-ng.desktop
%{_datadir}/applications/rtng-bookmark-editor.desktop
%{_datadir}/icons/Yaru/
%{_datadir}/icons/breeze/
%{_datadir}/icons/hicolor/24x24/apps/radiotray-ng-off.png
%{_datadir}/icons/hicolor/24x24/apps/radiotray-ng-on.png
%{_datadir}/icons/hicolor/256x256/apps/radiotray-ng-notification.png
%{_datadir}/icons/hicolor/256x256/apps/radiotray-ng-off.png
%{_datadir}/icons/hicolor/256x256/apps/radiotray-ng-on.png
%{_datadir}/metainfo/radiotray-ng.appdata.xml
%{_datadir}/radiotray-ng/

%changelog
