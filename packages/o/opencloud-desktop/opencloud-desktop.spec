#
# spec file for package opencloud-desktop
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


# LibreGraph version to build against (statically):
%define libregraph_version 1.0.7
%global __requires_exclude qt6qmlimport\\(eu\\.OpenCloud\\.*
Name:           opencloud-desktop
Version:        3.0.3
Release:        0
Summary:        The OpenCloud synchronization client
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/opencloud-eu/desktop
Source0:        https://github.com/opencloud-eu/desktop/archive/refs/tags/v%{version}.tar.gz#/desktop-%{version}.tar.gz
Source1:        opencloud.conf
Source2:        https://github.com/opencloud-eu/libre-graph-api-cpp-qt-client/archive/refs/tags/v%{libregraph_version}.tar.gz#/libre-graph-api-cpp-qt-client-%{libregraph_version}.tar.gz
BuildRequires:  cmake >= 2.8.11
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain) >= 0.12.0
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
# We want to build against a static LibreGraphAPI library; this is required to prevent
# having a LibreGraphAPI shared library installed in the build root:
BuildConflicts: cmake(LibreGraphAPI)
Requires:       libopencloudsync0 = %{version}
Requires:       opencloud-extensions-resources
Requires:       qt6-sql-sqlite
Suggests:       caja-extension-opencloud
Suggests:       nautilus-extension-opencloud
Suggests:       nemo-extension-opencloud
Suggests:       opencloud-dolphin
Supplements:    (%{name} and nautilus)
Obsoletes:      libLibreGraphAPI
%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
BuildRequires:  kf6-extra-cmake-modules
%else
BuildRequires:  extra-cmake-modules
%endif

%description
With OpenCloud Desktop files can be continously kept in sync between a local
workstation and the OpenCloud server.

%package -n %{name}-doc
Summary:        Documentation for OpenCloud
Group:          Development/Libraries/C and C++

%description -n %{name}-doc
Documentation for the OpenCloud desktop application.

%package -n libopencloudsync0
Summary:        The OpenCloud synchronization library
Group:          Development/Libraries/C and C++

%description -n libopencloudsync0
The OpenCloud synchronization library. It implements the OpenCloud
sync algorithm that keeps a local directory in sync with the
content on your cloud.

%package -n libopencloudsync-devel
Summary:        Development files for the OpenCloud synchronization library
Group:          Development/Libraries/C and C++
Requires:       libopencloudsync0 = %{version}

%description -n libopencloudsync-devel
Development files for the OpenCloud synchronization library. It
implements the OpenCloud sync algorithm that keeps a local directory
in sync with the content on your cloud.

%prep
%autosetup -p1 -n desktop-%{version} -a 2

%build
pushd "./libre-graph-api-cpp-qt-client-%{libregraph_version}/client"
%{cmake_qt6} -DBUILD_SHARED_LIBS=OFF
%{qt6_build}
install -d "${PWD}/.install"
DESTDIR="${PWD}/.install/" \
cmake --build build -v -t install
popd

export CMAKE_PREFIX_PATH="./libre-graph-api-cpp-qt-client-%{libregraph_version}/client/.install%{_libdir}/cmake${CMAKE_PREFIX_PATH+:}${CMAKE_PREFIX_PATH}"
%{cmake_qt6} -DKDE_SKIP_RPATH_SETTINGS=ON -DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%{qt6_build}

%install
export CMAKE_PREFIX_PATH="./libre-graph-api-cpp-qt-client-%{libregraph_version}/client/.install%{_libdir}/cmake${CMAKE_PREFIX_PATH+:}${CMAKE_PREFIX_PATH}"
%{qt6_install}

# do not allow to call home
install -m 0644 -D %{SOURCE1} -t %{buildroot}%{_sysconfdir}/opencloud/

# we don't need these any more, and we do not intend to ship them either:
rm -rf \
"%{buildroot}%{_includedir}/OpenAPI" \
"%{buildroot}%{_libdir}/libLibreGraphAPI.a" \
"%{buildroot}%{_libdir}/cmake/LibreGraphAPI"

%suse_update_desktop_file -n opencloud

%ldconfig_scriptlets -n libopencloudsync0

%files
%doc CHANGELOG.md PACKAGING.md README.md
%license COPYING
%{_bindir}/opencloud
%{_bindir}/opencloudcmd
%{_datadir}/applications/opencloud.desktop
%{_datadir}/applications/opencloudcmd.desktop
%{_libdir}/qt6/plugins/OpenCloud_vfs_*.so
%{_libdir}/libOpenCloudGui.so
%dir %{_libdir}/qt6/qml/eu
%{_libdir}/qt6/qml/eu/OpenCloud
%{_datadir}/icons/hicolor/*/apps/opencloud.*
%dir %{_sysconfdir}/opencloud
# old rpm without /usr/etc
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
%config(noreplace) %{_sysconfdir}/opencloud/opencloud.conf
%else
%{_sysconfdir}/opencloud/opencloud.conf
%endif

%files -n libopencloudsync0
%{_libdir}/libOpenCloudLibSync.so.0
%{_libdir}/libOpenCloudLibSync.so.3.*
%{_libdir}/libOpenCloudResources.so.0
%{_libdir}/libOpenCloudResources.so.3.*

%files -n libopencloudsync-devel
%{_libdir}/libOpenCloudLibSync.so
%{_libdir}/libOpenCloudResources.so
%dir %{_libdir}/cmake/OpenCloud
%{_libdir}/cmake/OpenCloud/OpenCloud*.cmake
%{_includedir}/OpenCloud

%changelog
