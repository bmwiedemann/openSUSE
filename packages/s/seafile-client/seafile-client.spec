#
# spec file for package seafile-client
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        9.0.21
Release:        0
Summary:        Cloud storage client
License:        GPL-3.0-only
URL:            https://github.com/haiwen/seafile-client/
Source0:        https://github.com/haiwen/%{name}/archive/v%{version}.tar.gz
Source1:        seafile.appdata.xml
Patch0:         01-fix-no-return-in-nonvoid.patch
Patch1:         issue1611.patch
Patch2:         fix-cmake-name.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
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
Requires:       hicolor-icon-theme
Requires:       python3-pysearpc
Requires:       seafile = %{version}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(sqlite3)
# Qt6 WebEngine is not available on 32-bit architectures
ExcludeArch:    %{ix86} %{arm}

%description
Seafile is an open source cloud storage system with features on privacy protection and teamwork. Collections of files are
called libraries, and each library can be synced separately. A library can also be encrypted with a user chosen password.
Seafile also allows users to create groups and easily sharing files into groups.

%prep
%autosetup -p1

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
%{_datadir}/applications/com.seafile.seafile-applet.desktop
%{_datadir}/icons/hicolor/*/apps/seafile.png
%{_datadir}/icons/hicolor/scalable/apps/seafile.svg
%{_datadir}/pixmaps/seafile.png
%{_datadir}/appdata/seafile.appdata.xml

%changelog
