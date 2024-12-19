#
# spec file for package owncloud-client
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


# The minimum required version of qtkeychain
%define keychain_version 0.12.0
# old rpm without /usr/etc
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
%global _distconfdir /etc
%endif

Name:           owncloud-client
Version:        5.3.1
Release:        0
Summary:        The ownCloud synchronization client
License:        GPL-2.0-only AND GPL-3.0-only
Group:          Productivity/Networking/Other
URL:            https://owncloud.com/desktop-app
Source0:        ownCloud_os-%{version}.tar.xz
Source2:        69-sync-inotify.conf
Source3:        README.source
Source4:        ownCloud.conf
# PATCH-FIX-UPSTREAM
Patch0:         owncloud-qt68.patch

BuildRequires:  cmake >= 2.8.11
BuildRequires:  extra-cmake-modules

BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-core-private-devel
BuildRequires:  qt6-gui-private-devel
BuildRequires:  qt6-widgets-private-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(LibreGraphAPI)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain) >= %{keychain_version}
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       libowncloudsync0 = %{version}
Requires:       owncloud-extensions-resources
Requires:       qt6-sql-sqlite
Suggests:       %{name}-nautilus
Suggests:       %{name}-nemo
Suggests:       owncloud-dolphin
Supplements:    (%{name} and nautilus)
Obsoletes:      libocsync-devel
Obsoletes:      libocsync-devel-doc
Obsoletes:      libocsync-doc
Obsoletes:      libocsync-plugin-owncloud
Obsoletes:      libocsync0
Obsoletes:      owncloud-client-l10n

%description
The ownCloud sync client - github.com/owncloud/client

ownCloud client enables you to connect to your private
ownCloud Server. With it you can create folders in your home
directory, and keep the contents of those folders synced with your
ownCloud server. Simply copy a file into the directory and the
ownCloud Client does the rest.

ownCloud gives you anytime and anywhere access to the files you
need, whether through this desktop application, our mobile apps,
the web interface, or other WebDAV clients. With it, you can
easily view and share documents and information in a secure,
flexible and controlled architecture. You can extend ownCloud
with plug-ins from the community, or that you build yourself.

%package -n %{name}-doc
Summary:        Documentation for ownCloud
Group:          Development/Libraries/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-doc
Documentation for the ownCloud desktop application.

%package -n libowncloudsync0
Summary:        The ownCloud synchronization library
Group:          Development/Libraries/C and C++
Requires:       libqt6keychain1 >= %{keychain_version}

%description -n libowncloudsync0
The ownCloud synchronization library. It implements the ownCloud
sync algorithm that keeps a local directory in sync with the
content on your cloud.

%package -n libowncloudsync-devel
Summary:        Development files for the ownCloud synchronization library
Group:          Development/Libraries/C and C++
Requires:       libowncloudsync0 = %{version}

%description -n libowncloudsync-devel
Development files for the ownCloud synchronization library. It
implements the ownCloud sync algorithm that keeps a local directory
in sync with the content on your cloud.

%prep
%autosetup -p1 -n ownCloud_os-%{version}

%build
%cmake_qt6 -DKDE_SKIP_RPATH_SETTINGS=ON -DKDE_INSTALL_SYSCONFDIR=%{_distconfdir}
%{qt6_build}

%install
%{qt6_install}

# Copy the source README here to be picked up by doc macro
cp %{SOURCE3} .

# https://github.com/owncloud/client/issues/4107
install -m 0644 -D %{SOURCE2} %{buildroot}/%{_sysctldir}/69-sync-inotify.conf
# do not allow to call home
install -m 0644 -D %{SOURCE4} -t %{buildroot}%{_distconfdir}/ownCloud/

# remove the icons that this version of the source tarball still contains
rm %{buildroot}%{_datadir}/icons/hicolor/*/apps/ownCloud_*png

%suse_update_desktop_file -n owncloud

%ldconfig_scriptlets -n libowncloudsync0

%files
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/applications/owncloudcmd.desktop
%{_datadir}/mime/packages/owncloud.xml
%{_libdir}/qt6/plugins/owncloudsync_vfs_*.so
%{_datadir}/icons/hicolor/*/apps/owncloud.png

%doc CONTRIBUTING.md README.md
%license COPYING COPYING.documentation

%config %{_distconfdir}/ownCloud
# https://github.com/owncloud/client/issues/4107
%{_sysctldir}/69-sync-inotify.conf

%files -n libowncloudsync0
%{_libdir}/libowncloudsync.so.*
%{_libdir}/libowncloud_csync.so.*
%{_libdir}/libowncloudResources.so.*

%files -n libowncloudsync-devel
%{_libdir}/libowncloudsync.so
%{_libdir}/libowncloud_csync.so
%{_libdir}/libowncloudResources.so
%dir %{_libdir}/cmake/ownCloud
%{_libdir}/cmake/ownCloud/ownCloud*.cmake
%{_includedir}/ownCloud

%changelog
