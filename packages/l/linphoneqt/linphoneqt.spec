#
# spec file for package linphoneqt
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


%define _name   linphone
Name:           linphoneqt
Version:        4.4.11
Release:        0
Summary:        Qt interface for Linphone
License:        GPL-3.0-or-later
Group:          Productivity/Telephony/SIP/Clients
URL:            https://linphone.org/technical-corner/linphone
Source:         https://gitlab.linphone.org/BC/public/linphone-desktop/-/archive/%{version}/%{_name}-desktop-%{version}.tar.bz2
Source1:        %{_name}.appdata.xml
# PATCH-FIX-OPENSUSE linphoneqt-fix-no-git.patch -- Fix building out-of-git.
Patch0:         linphoneqt-fix-no-git.patch
# PATCH-FIX-OPENSUSE https://aur.archlinux.org/cgit/aur.git/plain/0002-remove-bc_compute_full_version-usage.patch?h=linphone-desktop
Patch1:         linphoneqt-0002-remove-bc_compute_full_version-usage.patch
%if 0%{?suse_version}
BuildRequires:  Mesa-libGLESv2-devel
%else
BuildRequires:  mesa-libGL-devel
%endif
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  libqt5-linguist-devel
%else
BuildRequires:  boost-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qttools-devel
Requires:       qt5-qtquickcontrols
%endif
BuildRequires:  pkgconfig
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(linphone) >= 5.1.58
BuildRequires:  pkgconfig(mediastreamer) >= 5.0.0

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
Requires:       liblinphone-data
Recommends:     %{_name}-cli
Obsoletes:      %{_name}-lang < %{version}

%description -n %{_name}
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

%description -n %{_name}-devel
Devel package for %{_name}.

%prep
%autosetup -n %{_name}-desktop-%{version} -p1
cp %{SOURCE1} linphone.appdata.xml
touch linphone-sdk/CMakeLists.txt
%if 0%{?suse_version}
mkdir -p build/linphone-sdk/desktop/{bin,share}
%else
mkdir -p redhat-linux-build/linphone-sdk/desktop/{bin,share}
%endif

# Fix building out-of-git
echo '#define LINPHONE_QT_GIT_VERSION "${PROJECT_VERSION}"' >> linphone-app/src/config.h.cmake
# Hardcode linphoneqt version
echo "project(linphoneqt VERSION %{version})" > linphone-app/linphoneqt_version.cmake

%build
if [[ %version = 4.4.[0-9]* ]]; then
    sed -i '/^add_custom_command/s@${CMAKE_INSTALL_PREFIX}/include/@%{buildroot}%{_includedir}/@;/^add_custom_command/s@${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR}/@%{buildroot}%{_libdir}/@' linphone-app/CMakeLists.txt
    sed -i '/\/ui/s@${qml_dir}@${CMAKE_CURRENT_SOURCE_DIR}/../&@' linphone-app/cmake_builder/linphone_package/CMakeLists.txt
%if 0%{?suse_version}
    mkdir -p build/linphone-sdk/desktop/share/{,sounds}/linphone
%else
    mkdir -p redhat-linux-build/linphone-sdk/desktop/share/{,sounds}/linphone
%endif
fi
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags} -fpic -ffat-lto-objects -fpermissive" \
  -DCMAKE_BUILD_TYPE=Release \
  -DLINPHONE_OUTPUT_DIR="$PWD" \
  -DCMAKE_INSTALL_PREFIX=/usr \
  -DENABLE_UPDATE_CHECK=OFF \
  -DENABLE_STRICT=OFF       \
  -DENABLE_STATIC=OFF
%cmake_build

%install
%cmake_install
%if 0%{?fedora}
# for Fedora the internal call to cmake overwrites CMAKE_INSTALL_PREFIX, move...
mkdir -p %{buildroot}/usr
mv %{buildroot}/home/abuild/rpmbuild/BUILD/linphone-desktop*/redhat-linux-build/OUTPUT/* %{buildroot}/usr
rm -rf %{buildroot}/home
%endif
install -Dpm 0644 linphone.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/org.linphone.appdata.xml

rm %{buildroot}%{_bindir}/qt.conf
chmod a-x %{buildroot}%{_datadir}/applications/linphone.desktop

chrpath -d %{buildroot}%{_bindir}/linphone %{buildroot}%{_libdir}/libapp-plugin.so

%files -n %{_name}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{_bindir}/linphone
%{_libdir}/libapp-plugin.so
%{_datadir}/linphone/
%{_datadir}/applications/linphone.desktop
%{_datadir}/icons/hicolor/*/apps/linphone.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/org.linphone.appdata.xml

%files -n %{_name}-devel
%{_includedir}/LinphoneApp/

%changelog
