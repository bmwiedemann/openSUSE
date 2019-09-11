#
# spec file for package linphoneqt
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


%define _name   linphone
Name:           linphoneqt
Version:        4.1.1
Release:        0
Summary:        Qt interface for Linphone
License:        GPL-2.0-or-later
Group:          Productivity/Telephony/SIP/Clients
Url:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source1:        %{_name}.appdata.xml
# PATCH-FIX-UPSTREAM linphoneqt-fix-cmake-i18n.patch -- Support new CMake versions for translations (commit e70c077).
Patch0:         linphoneqt-fix-cmake-i18n.patch
# PATCH-FIX-UPSTREAM linphoneqt-force-default-style.patch boo#1083654 -- Force default theme style (commit 313aa68).
Patch1:         linphoneqt-force-default-style.patch
# PATCH-FIX-UPSTREAM linphoneqt-fix-qt-5.11.patch boo#1083654 -- Fix issues with Qt 5.10 and 5.11 (commits ecaab0f, d95f523, 5dd0161, 7f62ae9, 8720931, 4f908ef).
Patch2:         linphoneqt-fix-qt-5.11.patch
# PATCH-FIX-OPENSUSE linphoneqt-qt-5.9-fix-buttons.patch boo#1095273 -- Fix button invisibility with Qt 5.9.
Patch3:         linphoneqt-qt-5.9-fix-buttons.patch
# PATCH-FIX-OPENSUSE linphoneqt-fix-no-git.patch -- Fix building out-of-git.
Patch4:         linphoneqt-fix-no-git.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel >= 5.9
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
BuildRequires:  pkgconfig(Qt5DBus) >= 5.9
BuildRequires:  pkgconfig(Qt5Gui) >= 5.9
BuildRequires:  pkgconfig(Qt5Network) >= 5.9
BuildRequires:  pkgconfig(Qt5Quick) >= 5.9
BuildRequires:  pkgconfig(Qt5QuickControls2) >= 5.9
BuildRequires:  pkgconfig(Qt5Svg) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(linphone) >= 3.12.0
BuildRequires:  pkgconfig(mediastreamer) >= 2.16.0

%description
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%package -n %{_name}
Summary:        Web Phone
Group:          Productivity/Telephony/SIP/Clients
Requires:       lib%{_name}-data
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols
Requires:       libqt5-qtquickcontrols2
Recommends:     %{_name}-cli
Obsoletes:      %{_name}-lang < %{version}

%description -n %{_name}
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
cp %{SOURCE1} linphone.appdata.xml

%build
%cmake \
  -DENABLE_DBUS=ON                 \
  -DENABLE_PRECOMPILED_HEADERS=OFF \
  -DENABLE_STRICT=OFF              \
  -DENABLE_STATIC=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install
install -Dpm 0644 linphone.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/linphone.appdata.xml

%if 0%{?suse_version} < 1500
%post -n %{_name}
%desktop_database_post
%icon_theme_cache_post

%postun -n %{_name}
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files -n %{_name}
%license LICENSE
%doc README.md
%{_bindir}/linphone
%{_bindir}/linphone-tester
%{_datadir}/linphone/
%{_datadir}/applications/linphone.desktop
%{_datadir}/icons/hicolor/*/apps/linphone.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/linphone.appdata.xml

%changelog
