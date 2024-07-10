#
# spec file for package linphoneqt
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


%define ispell_commit_hash 05574fe160222c3d0b6283c1433c9b087271fad1

%define _name   linphone
Name:           linphoneqt
Version:        5.2.4
Release:        0
Summary:        Qt interface for Linphone
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/SIP/Clients
URL:            https://linphone.org/technical-corner/linphone
Source:         https://gitlab.linphone.org/BC/public/linphone-desktop/-/archive/%{version}/%{_name}-desktop-%{version}.tar.bz2
Source1:        %{_name}.appdata.xml
# ispell with Linphone-specific patches from the Linphone developers
Source2:        https://gitlab.linphone.org/BC/public/external/ispell/-/archive/%{ispell_commit_hash}/ispell-%{ispell_commit_hash}.tar.gz
# PATCH-FIX-OPENSUSE linphoneqt_fix_gcc12_error.patch -- Fix building with gcc12
Patch0:         linphoneqt_fix_gcc12_error.patch
# Fix spelling mistakes in library detection, add missing include directory and missing install.
Patch1:         fix_cmakelists.patch
# Fix gcc complaining about methods without a return value.
Patch2:         fix_ispell_return_type_error.patch

BuildRequires:  Mesa-libGLESv2-devel
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist-devel
BuildRequires:  lime-devel >= 5.3.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bctoolbox) >= 5.3.0
BuildRequires:  pkgconfig(belcard) >= 5.3.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(linphone) >= 5.3.0
BuildRequires:  pkgconfig(mediastreamer) >= 5.3.0
Provides:       linphone = %{version}-%{release}
Obsoletes:      linphone < %{version}-%{release}

%description
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%package -n %{_name}-desktop
Summary:        Web Phone
Group:          Productivity/Telephony/SIP/Clients
Requires:       liblinphone-data
Recommends:     %{_name}-cli
Obsoletes:      %{_name}-lang < %{version}
Provides:       %{_name} = %{version}-%{release}
Obsoletes:      %{_name} < %{version}-%{release}

%description -n %{_name}-desktop
Linphone is a Web phone with a Qt interface. It lets you make
two-party calls over IP networks such as the Internet. It uses the IETF
protocols SIP (Session Initiation Protocol) and RTP (Realtime TransporT
Protocol) to make calls, so it should be able to communicate with other
SIP-based Web phones. With several codecs available, it can be used
with high speed connections as well as 28k modems.

%package -n %{_name}-devel
Summary:        Web Phone
Group:          Productivity/Telephony/SIP/Clients
BuildArch:      noarch
Provides:       linphone-devel = %{version}-%{release}
Obsoletes:      linphone-devel < %{version}-%{release}

%description -n %{_name}-devel
Devel package for %{_name}.

%prep
%setup -n %{_name}-desktop-%{version} -q -a2
cp %{SOURCE1} linphone.appdata.xml
touch linphone-sdk/CMakeLists.txt
%patch -P0 -p1
%patch -P1 -p1

rm -r external/ispell
mv ispell-%{ispell_commit_hash} external/ispell
cd external/ispell
%patch -P2 -p1
cd ../..

# linphone-desktop wants to be built with liblinphone as a git submodule and includes its CMakeLists.txt, even though the submodule is not present during the build. Creating this file tricks cmake, while the dependencies are included from system packages instead.
touch linphone-sdk/CMakeLists.txt

# These files shadow the Config files installed by the respective devel packages and let the build fail since they expect to find the libraries in git submodules, which are not part of the archive.
rm linphone-app/cmake/FindMediastreamer2.cmake \
   linphone-app/cmake/FindLibLinphone.cmake \
   linphone-app/cmake/FindLinphoneCxx.cmake

%build
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags} -fpic -ffat-lto-objects -fpermissive" \
  -DCMAKE_BUILD_TYPE=Release \
  -DLINPHONE_OUTPUT_DIR="$PWD" \
  -DLINPHONEAPP_VERSION=%{version} \
  -DENABLE_QT_KEYCHAIN=OFF \
  -DENABLE_UPDATE_CHECK=OFF
%cmake_build

%install
%cmake_install
install -Dpm 0644 linphone.appdata.xml  %{buildroot}%{_datadir}/metainfo/org.linphone-desktop.appdata.xml

rm %{buildroot}%{_bindir}/qt.conf
chmod a-x %{buildroot}%{_datadir}/applications/linphone.desktop
mv %{buildroot}%{_datadir}/applications/linphone.desktop %{buildroot}%{_datadir}/applications/linphone-desktop.desktop

chrpath -d %{buildroot}%{_bindir}/linphone %{buildroot}%{_libdir}/libapp-plugin.so

%files -n %{_name}-desktop
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/linphone
%{_libdir}/libapp-plugin.so
%{_libdir}/libISpell.so
%{_datadir}/linphone/
%{_datadir}/applications/linphone-desktop.desktop
%{_datadir}/icons/hicolor/*/apps/linphone.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.linphone-desktop.appdata.xml

%files -n %{_name}-devel
%{_includedir}/LinphoneApp/

%changelog
