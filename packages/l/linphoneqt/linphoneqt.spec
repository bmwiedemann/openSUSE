#
# spec file for package linphoneqt
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


%define _name   linphone
Name:           linphoneqt
Version:        4.2.1
Release:        0
Summary:        Qt interface for Linphone
License:        GPL-3.0-or-later
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/linphone-desktop/-/archive/%{version}/%{_name}-desktop-%{version}.tar.bz2
Source1:        %{_name}.appdata.xml
# PATCH-FIX-OPENSUSE linphoneqt-fix-no-git.patch -- Fix building out-of-git.
Patch0:         linphoneqt-fix-no-git.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(linphone) >= 4.4.0
BuildRequires:  pkgconfig(mediastreamer) >= 4.4.0

%description
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%package -n %{_name}
Summary:        Web Phone
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
%autosetup -n %{_name}-desktop-%{version} -p1
cp %{SOURCE1} linphone.appdata.xml
touch linphone-sdk/CMakeLists.txt
mkdir -p build/linphone-sdk/desktop/{bin,share}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DLINPHONE_OUTPUT_DIR="$PWD" \
  -DENABLE_UPDATE_CHECK=OFF \
  -DENABLE_STRICT=OFF       \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install
install -Dpm 0644 linphone.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/org.linphone.appdata.xml

rm %{buildroot}%{_bindir}/qt.conf

%files -n %{_name}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/linphone
%{_datadir}/linphone/
%{_datadir}/applications/linphone.desktop
%{_datadir}/icons/hicolor/*/apps/linphone.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.linphone.appdata.xml

%changelog
