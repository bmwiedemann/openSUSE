#
# spec file for package nheko
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           nheko
Version:        0.12.1
Release:        0
Summary:        Desktop client for the Matrix protocol
License:        Apache-2.0 AND GPL-3.0-or-later AND CC-BY-4.0
Group:          Productivity/Networking/Talk/Clients
URL:            https://github.com/Nheko-Reborn/%{name}
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix_scrolling.patch
Patch1:         fix_reply_rendering.patch
# PATCH-FIX-UPSTREAM -- Qt 6.10 compat
Patch2:         nheko-qt610.patch
BuildRequires:  appstream-glib
BuildRequires:  asciidoc
BuildRequires:  cmake >= 3.13.0
BuildRequires:  cmark-devel
BuildRequires:  desktop-file-utils
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  kdsingleapplication-qt6-devel
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  kf6-kirigami-devel
BuildRequires:  kf6-kirigami-imports
BuildRequires:  libappstream-glib8
BuildRequires:  libboost_atomic-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_regex-devel
%if 0%{?suse_version} < 1600
BuildRequires:  libboost_system-devel
%endif
BuildRequires:  libboost_thread-devel
BuildRequires:  lmdb-devel
BuildRequires:  lmdbxx-devel
BuildRequires:  memory-constraints
BuildRequires:  mpark-variant-devel
BuildRequires:  ninja
BuildRequires:  nlohmann_json-devel >= 3.2.0
BuildRequires:  olm-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-qml-private-devel
BuildRequires:  spdlog-devel >= 1.0.0
BuildRequires:  zlib-devel
BuildRequires:  cmake(MatrixClient) >= 0.10.0
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(re2)
BuildRequires:  pkgconfig(coeurl)
BuildRequires:  pkgconfig(gstreamer-webrtc-1.0)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-ewmh)
Requires:       kf6-kirigami-imports
Requires:       qt6-multimedia-imports
Recommends:     qt-jdenticon
# Workaround https://github.com/Nheko-Reborn/nheko/issues/391
Provides:       bundled(blurhash) = 0.0.1
Provides:       bundled(cpp-httplib) = 0.5.12

%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app.

%package zsh-completion
Summary:        Zsh completion for %{name}
Group:          System/Management
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
This package contain the zsh completion command for the %{name} matrix client.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%limit_build -m 1800
%define __builder ninja

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCOMPILE_QML=OFF \
    -DHUNTER_ENABLED=OFF \
    -DCI_BUILD=OFF \
    -DASAN=OFF \
    -DUSE_BUNDLED_SPDLOG=OFF \
    -DUSE_BUNDLED_OLM=OFF \
    -DQML_DEBUGGING=OFF \
    -DBUILD_DOCS=OFF \
    -DUSE_BUNDLED_GTEST=OFF \
    -DUSE_BUNDLED_CMARK=OFF \
    -DUSE_BUNDLED_LMDBXX=OFF \
    -DUSE_BUNDLED_MTXCLIENT=OFF \
    -DUSE_BUNDLED_LMDB=OFF \
    -DUSE_BUNDLED_QTKEYCHAIN=OFF \
    -DUSE_BUNDLED_JSON=OFF \
    -DUSE_BUNDLED_COEURL=OFF \
    -DUSE_BUNDLED_LIBEVENT=OFF \
    -DUSE_BUNDLED_QTKEYCHAIN=OFF \
    -DUSE_BUNDLED_SPDLOG=OFF \
    -DUSE_BUNDLED_OPENSSL=OFF
%cmake_build

%install
%cmake_install

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*
%{_mandir}/man1/nheko.1%{?ext_man}

%files zsh-completion
%{_datadir}/zsh/site-functions/_nheko

%changelog
