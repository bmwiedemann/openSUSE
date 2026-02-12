#
# spec file for package owncloud-client
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


# The minimum required version of qtkeychain
%define keychain_version 0.13.0
# old rpm without /usr/etc
%if 0%{?suse_version} && 0%{?suse_version} <= 1500
%global _distconfdir /etc
%endif
Name:           owncloud-client
Version:        6.0.3
Release:        0
Summary:        The ownCloud synchronization client
License:        GPL-2.0-only AND GPL-3.0-only
URL:            https://owncloud.com/desktop-app
Source0:        ownCloud_os-%{version}.tar.xz
Source1:        69-sync-inotify.conf
Source2:        ownCloud.conf
Source3:        README.source
BuildRequires:  cmake >= 3.18
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules >= 6.0.0
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  cmake(KDSingleApplication-qt6)
BuildRequires:  cmake(LibreGraphAPI) >= 1.0.4
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain) >= %{keychain_version}
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       libowncloudsync0 = %{version}
Requires:       owncloud-extensions-resources
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
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %{name}-doc
Documentation for the ownCloud desktop application.

%package -n libowncloudsync0
Summary:        The ownCloud synchronization library
Requires:       libqt6keychain1 >= %{keychain_version}

%description -n libowncloudsync0
The ownCloud synchronization library. It implements the ownCloud
sync algorithm that keeps a local directory in sync with the
content on your cloud.

%package -n libowncloudsync-devel
Summary:        Development files for the ownCloud synchronization library
Requires:       libowncloudsync0 = %{version}

%description -n libowncloudsync-devel
Development files for the ownCloud synchronization library. It
implements the ownCloud sync algorithm that keeps a local directory
in sync with the content on your cloud.

%prep
%autosetup -p1 -n ownCloud_os-%{version}

cp %{SOURCE3} .

%build
%cmake_qt6 -DKDE_SKIP_RPATH_SETTINGS:BOOL=TRUE -DKDE_INSTALL_SYSCONFDIR:STRING=%{_distconfdir}

%qt6_build

%install
%qt6_install

# https://github.com/owncloud/client/issues/4107
install -m 0644 -D %{SOURCE1} %{buildroot}%{_sysctldir}/69-sync-inotify.conf

# do not allow to call home
install -m 0644 -D %{SOURCE2} -t %{buildroot}%{_distconfdir}/ownCloud/

%ldconfig_scriptlets
%ldconfig_scriptlets -n libowncloudsync0

%files
%license COPYING COPYING.documentation
%doc CHANGELOG.md CONTRIBUTING.md README.md README.source
%config %{_distconfdir}/ownCloud
%{_bindir}/owncloud
%{_bindir}/owncloudcmd
%{_datadir}/applications/owncloud.desktop
%{_datadir}/applications/owncloudcmd.desktop
%{_datadir}/icons/hicolor/*/apps/owncloud.png
%{_datadir}/mime/packages/owncloud.xml
%{_qt6_libdir}/libowncloudGui.so
%{_qt6_pluginsdir}/ownCloud_vfs_*.so
%{_qt6_qmldir}/org/ownCloud/
# https://github.com/owncloud/client/issues/4107
%{_sysctldir}/69-sync-inotify.conf

%files -n libowncloudsync0
%license COPYING
%{_qt6_libdir}/libownCloudCsync.so.*
%{_qt6_libdir}/libownCloudLibSync.so.*
%{_qt6_libdir}/libownCloudResources.so.*

%files -n libowncloudsync-devel
%{_includedir}/ownCloud
%{_qt6_cmakedir}/ownCloud/
%{_qt6_libdir}/libownCloudCsync.so
%{_qt6_libdir}/libownCloudLibSync.so
%{_qt6_libdir}/libownCloudResources.so

%changelog
