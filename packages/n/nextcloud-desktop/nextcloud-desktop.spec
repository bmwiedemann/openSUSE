#
# spec file for package nextcloud-desktop
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


%define soname  libnextcloudsync
%define sover   0

%ifarch x86_64 aarch64 riscv64
%define with_qtwebengine 1
%endif

Name:           nextcloud-desktop
Version:        4.0.0
Release:        0
Summary:        Nextcloud desktop synchronisation client
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://nextcloud.com/
Source:         https://github.com/nextcloud/desktop/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysctl-sync-inotify.conf
Source2:        README.vfs.md
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  rsvg-convert
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
%if 0%{?with_qtwebengine}
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
%endif
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libp11)
BuildRequires:  pkgconfig(openssl) >= 1.1
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
#
Recommends:     cloudproviders-extension-nextcloud = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       nextcloud-cli = %{version}
Requires:       qt6-declarative-imports
Requires:       qt6-multimedia-imports
Requires:       qt6-qt5compat-imports
Provides:       nextcloud-client = %{version}
Obsoletes:      nextcloud-client < %{version}
Provides:       nextcloud-client-lang = %{version}
Obsoletes:      nextcloud-client-lang < %{version}

%description
The Nextcloud Desktop Client is a tool to synchronise files from
the Nextcloud Server with your computer.

Nextcloud Desktop enables you to connect to your private
Nextcloud Server. With it you can create directories in your home
directory, and keep the contents of those directories synced with
the server. Simply copy a file into the directory and the desktop
synchronisation client does the rest.

%lang_package

%package -n %{soname}%{sover}
Summary:        The Nextcloud synchronisation library
Group:          Productivity/Networking/File-Sharing

%description -n %{soname}%{sover}
The Nextcloud Desktop Client synchronisation library.

%package -n %{soname}-devel
Summary:        Development files for the Nextcloud synchronisation library
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description -n %{soname}-devel
Development files for the Nextcloud Desktop Client synchronisation
library.

%package -n nautilus-extension-nextcloud
Summary:        Nautilus overlay icons
Group:          Productivity/Networking/File-Sharing
Requires:       %{name} = %{version}
Requires:       nautilus
Requires:       python3-nautilus
Supplements:    (%{name} and nautilus)
BuildArch:      noarch

%description -n nautilus-extension-nextcloud
This package provides overlay icons to visualise the
synchronisation state in the Nautilus file manager.

%if 0%{?is_opensuse}
%package -n caja-extension-nextcloud
Summary:        Caja overlay icons
Group:          Productivity/Networking/File-Sharing
Requires:       %{name} = %{version}
Requires:       caja
Requires:       python-caja
Supplements:    (%{name} and caja)
BuildArch:      noarch

%description -n caja-extension-nextcloud
This package provides overlay icons to visualise the
synchronisation state in the Caja file manager.

%package -n nemo-extension-nextcloud
Summary:        Nemo overlay icons
Group:          Productivity/Networking/File-Sharing
Requires:       %{name} = %{version}
Requires:       nemo
Requires:       python-nemo
Supplements:    (%{name} and nemo)
BuildArch:      noarch

%description -n nemo-extension-nextcloud
This package provides overlay icons to visualise the
synchronisation state in the Nemo file manager.

%package -n cloudproviders-extension-nextcloud
Summary:        Libcloudproviders integration for nextcloud-desktop
Group:          Productivity/Networking/File-Sharing
Requires:       %{name} = %{version}
BuildArch:      noarch

%description -n cloudproviders-extension-nextcloud
This package provides libcloudproviders integration for the
nextcloud desktop client.

%package -n %{name}-dolphin
Summary:        Dolphin overlay icons
Group:          Productivity/Networking/File-Sharing
Requires:       %{name} = %{version}
Requires:       dolphin
Supplements:    (%{name} and dolphin)

%description -n %{name}-dolphin
This package provides the necessary plugin libraries for the
Dolphin filemanager to display overlay icons.
%endif

%package -n nextcloud-cli
Summary:        Nextcloud sync client - Command-line utility

%description -n nextcloud-cli
The Nextcloud Desktop Client is a tool to synchronise files from
the Nextcloud Server with your computer.

This package provides Nextcloud's command-line sync utility.

%package -n nextcloud-desktop-vfs-plugin
Summary:        Early experimental virtual file system plugin for nextcloud client
Requires:       %{name} = %{version}
# nextcloud_vfs_*.so plugins were incorrectly a part of devel package
Conflicts:      %{soname}-devel < %{version}

%description -n nextcloud-desktop-vfs-plugin
The Nextcloud Desktop Client is a tool to synchronise files from
the Nextcloud Server with your computer.

This package provides the files needed to enable virtual file system on
nextcloud-desktop. Note that virtual file system support on Linux is very
experimental, so use at your own risk.

%prep
%autosetup -p1 -n desktop-%{version}
cp -a %{SOURCE1} sysctl-sync-inotify.conf
cp %{SOURCE2} ./

%build
# Set SOURCE_DATE_EPOCH to set __DATE__/__TIME__ based on tarball creation date and make build reproducible
export SOURCE_DATE_EPOCH=`date -r VERSION.cmake +"%s"`
%cmake_qt6 \
%if !0%{?with_qtwebengine}
  -DBUILD_WITH_WEBENGINE=FALSE
%endif
%{nil}

%qt6_build

%install
%qt6_install

%if 0%{!?is_opensuse}
# There's no Caja and Nemo in SLE.
rm -r %{buildroot}%{_datadir}/caja-python/
rm -r %{buildroot}%{_datadir}/nemo-python/
%endif

# Generate bytecode for extensions.
for fm in caja nautilus nemo; do
    if [ -d %{buildroot}%{_datadir}/$fm-python/ ]; then
        %py3_compile %{buildroot}%{_datadir}/$fm-python/extensions/
    fi
done

# ecsos: Comment this out, because it seems to be a security risk.
# See: https://github.com/owncloud/client/issues/4107#issuecomment-240627858
# A workaround for gh#owncloud/client#4107
#install -Dpm 0644 sysctl-sync-inotify.conf \
#  %%{buildroot}%%{_sysconfdir}/sysctl.d/99-%%{name}-sync-inotify.conf

# Needs the following symlinks for VFS support, otherwise client crashes when VFS is enabled
mkdir -p %{buildroot}%{_qt6_pluginsdir}
ln -s -t %{buildroot}%{_qt6_pluginsdir}/ %{_libdir}/nextcloudsync_vfs_{suffix,xattr}.so

%fdupes %{buildroot}%{_datadir}/

%ldconfig_scriptlets -n %{soname}%{sover}

%posttrans -n nextcloud-desktop-vfs-plugin
echo "The virtual file system implementation of nextcloud-desktop on Linux is \
at an early experimental stage. Enable at your own risk. \
Please read %{_docdir}/nextcloud-desktop-vfs-plugin/README.vfs.md for steps \
needed to enable the plugin." || true

%pre
%systemd_user_pre com.nextcloud.desktopclient.nextcloud.service

%post
%systemd_user_post com.nextcloud.desktopclient.nextcloud.service

%preun
%systemd_user_preun com.nextcloud.desktopclient.nextcloud.service

%postun
%systemd_user_postun com.nextcloud.desktopclient.nextcloud.service

%files
%license COPYING*
#%%config %%{_sysconfdir}/sysctl.d/99-%%{name}-sync-inotify.conf
%{_bindir}/nextcloud
%dir %{_datadir}/nextcloud/
%{_datadir}/applications/com.nextcloud.desktopclient.nextcloud.desktop
%dir %{_datadir}/icons/hicolor/1024x1024/
%dir %{_datadir}/icons/hicolor/1024x1024/apps/
%{_datadir}/icons/hicolor/*/apps/Nextcloud*.*
%{_datadir}/mime/packages/nextcloud.xml
%{_userunitdir}/com.nextcloud.desktopclient.nextcloud.service

%files lang
%{_datadir}/nextcloud/i18n/

%files -n %{soname}%{sover}
%license COPYING*
%{_libdir}/%{soname}.so.*
%{_libdir}/libnextcloud_csync.so.*

%files -n %{soname}-devel
%{_includedir}/nextcloudsync/
%{_libdir}/%{soname}.so
%{_libdir}/libnextcloud_csync.so

%files -n nautilus-extension-nextcloud
%dir %{_datadir}/nautilus-python/
%dir %{_datadir}/nautilus-python/extensions/
%dir %{_datadir}/nautilus-python/extensions/__pycache__
%{_datadir}/nautilus-python/extensions/syncstate-Nextcloud.py*
%{_datadir}/nautilus-python/extensions/__pycache__/syncstate-Nextcloud*

%if 0%{?is_opensuse}
# SECTION openSUSE not SLE
%files -n caja-extension-nextcloud
%dir %{_datadir}/caja-python/
%dir %{_datadir}/caja-python/extensions/
%dir %{_datadir}/caja-python/extensions/__pycache__
%{_datadir}/caja-python/extensions/syncstate-Nextcloud.py*
%{_datadir}/caja-python/extensions/__pycache__/*

%files -n nemo-extension-nextcloud
%dir %{_datadir}/nemo-python/
%dir %{_datadir}/nemo-python/extensions/
%dir %{_datadir}/nemo-python/extensions/__pycache__
%{_datadir}/nemo-python/extensions/syncstate-Nextcloud.py*
%{_datadir}/nemo-python/extensions/__pycache__/*

%files -n cloudproviders-extension-nextcloud
# When built with libcloudproviders >= 0.3.3 the .ini file is no longer required,
# see https://github.com/nextcloud/desktop/pull/6275
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} < 150600
%dir %{_datadir}/cloud-providers/
%{_datadir}/cloud-providers/com.nextcloudgmbh.Nextcloud.ini
%endif
%{_datadir}/dbus-1/services/com.nextcloudgmbh.Nextcloud.service

%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%dir %{_qt6_pluginsdir}/kf6/kfileitemaction
%{_qt6_pluginsdir}/kf6/kfileitemaction/nextclouddolphinactionplugin.so
%dir %{_qt6_pluginsdir}/kf6/overlayicon
%{_qt6_pluginsdir}/kf6/overlayicon/nextclouddolphinoverlayplugin.so

# /SECTION
%endif

%files -n nextcloud-cli
%license COPYING
%config %{_sysconfdir}/Nextcloud/
%{_bindir}/nextcloudcmd

%files -n nextcloud-desktop-vfs-plugin
%license COPYING
%doc README.vfs.md
%{_libdir}/nextcloudsync_vfs_*.so
%{_qt6_pluginsdir}/*.so

%changelog
