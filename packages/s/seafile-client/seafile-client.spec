#
# spec file for package seafile-client
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


Name:           seafile-client
Version:        7.0.10
Release:        0
Summary:        Cloud storage client
License:        GPL-3.0-only
URL:            https://github.com/haiwen/seafile-client/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz
Source1:        seafile.appdata.xml
Patch0:         01-fix-no-return-in-nonvoid.patch
Patch1:         fix_qpainterpath.patch
Patch2:         fix-cmake-name.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libseafile0 = %{version}
BuildRequires:  libsearpc-devel
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  seafile-devel = %{version}
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_core)
BuildRequires:  pkgconfig(libevent_extra)
BuildRequires:  pkgconfig(libevent_openssl)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(uuid)
Requires:       python3-pysearpc
Requires:       seafile = %{version}
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  jansson-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtconnectivity-devel
BuildRequires:  qt5-qtwebkit
BuildRequires:  sqlite-devel
%else
BuildRequires:  libqt5-linguist-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineCore)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(sqlite3)
%endif

%description
Seafile is an open source cloud storage system with features on privacy protection and teamwork. Collections of files are
called libraries, and each library can be synced separately. A library can also be encrypted with a user chosen password.
Seafile also allows users to create groups and easily sharing files into groups.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p0

%build
export CFLAGS="%{optflags} -fPIE -pie"
export CXXFLAGS="%{optflags} -fPIE -pie"
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_SHIBBOLETH_SUPPORT=ON ..
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datarootdir}/appdata/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/seafile.appdata.xml

%files
%doc README.md
%license LICENSE
%{_bindir}/seafile-applet
%{_datadir}/applications/seafile.desktop
%{_datadir}/icons/hicolor/128x128
%{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/seafile.png
%{_datadir}/icons/hicolor/16x16
%{_datadir}/icons/hicolor/16x16/apps
%{_datadir}/icons/hicolor/16x16/apps/seafile.png
%{_datadir}/icons/hicolor/22x22
%{_datadir}/icons/hicolor/22x22/apps
%{_datadir}/icons/hicolor/22x22/apps/seafile.png
%{_datadir}/icons/hicolor/24x24
%{_datadir}/icons/hicolor/24x24/apps
%{_datadir}/icons/hicolor/24x24/apps/seafile.png
%{_datadir}/icons/hicolor/32x32
%{_datadir}/icons/hicolor/32x32/apps
%{_datadir}/icons/hicolor/32x32/apps/seafile.png
%{_datadir}/icons/hicolor/48x48
%{_datadir}/icons/hicolor/48x48/apps
%{_datadir}/icons/hicolor/48x48/apps/seafile.png
%{_datadir}/icons/hicolor/scalable
%{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/seafile.svg
%{_datadir}/pixmaps/seafile.png
%{_datadir}/appdata/seafile.appdata.xml

%changelog
