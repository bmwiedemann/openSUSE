#
# spec file for package nextcloud-desktop
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


%define soname  libnextcloudsync
%define sover   0
%define __builder ninja

# For dolphin KF5/KF6 integration
%if 0%{?suse_version} < 1650
%bcond_with qt6_dolphin
%else
%bcond_without qt6_dolphin
%endif

# std=c++17 and <filesystem> now required, use GCC >= 8 for Leap
%if 0%{?suse_version} < 1650
%define gcc_ver 9
%endif
Name:           nextcloud-desktop
Version:        3.13.1
Release:        0
Summary:        Nextcloud desktop synchronisation client
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://nextcloud.com/
Source:         https://github.com/nextcloud/desktop/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysctl-sync-inotify.conf
Source2:        README.vfs.md
# PATCH-FIX-UPSTREAM nextcloud-fix-HiDPI-window-size.patch badshah400@gmail.com -- Fix huge size of the nextcloud client settings and crash-reporter windows on HiDPI systems
Patch0:         nextcloud-fix-HiDPI-window-size.patch
BuildRequires:  AppStream
BuildRequires:  cmake >= 3.8.0
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  glibc-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  rsvg-convert
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5GuiAddons)
###BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.15
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5WebSockets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(cloudproviders)
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl) >= 1.1
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
%if %{with qt6_dolphin}
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF6KIO)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  rpm_macro(_qt6_pluginsdir)
%else
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF5KIO) >= 5.16
%endif
#
Recommends:     cloudproviders-extension-nextcloud = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
Requires:       nextcloud-cli = %{version}
Provides:       nextcloud-client = %{version}
Obsoletes:      nextcloud-client < %{version}
Provides:       nextcloud-client-lang = %{version}
Obsoletes:      nextcloud-client-lang < %{version}
%if 0%{?is_opensuse}
BuildRequires:  doxygen
#BuildRequires:  python3-MarkupSafe
BuildRequires:  python3-Sphinx
#BuildRequires:  python3-importlib-metadata
Suggests:       %{name}-doc = %{version}
%endif

%description
The Nextcloud Desktop Client is a tool to synchronise files from
the Nextcloud Server with your computer.

Nextcloud Desktop enables you to connect to your private
Nextcloud Server. With it you can create directories in your home
directory, and keep the contents of those directories synced with
the server. Simply copy a file into the directory and the desktop
synchronisation client does the rest.

%lang_package

%if 0%{?is_opensuse}
%package doc
Summary:        Documentation for nextcloud-desktop
Group:          Productivity/Networking/File-Sharing
Provides:       nextcloud-client-doc = %{version}
Obsoletes:      nextcloud-client-doc < %{version}
BuildArch:      noarch

%description doc
The Nextcloud Desktop Client is a tool to synchronise files from
the Nextcloud Server with your computer.

This package contains the documentation.
%endif

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
%cmake \
  -DCMAKE_C_COMPILER=gcc%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
%if 0%{?is_opensuse}
  -DWITH_DOC=ON \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
%endif
%{nil}
%cmake_build

%install
%cmake_install

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
mkdir -p %{buildroot}%{_libqt5_plugindir}
ln -s -t %{buildroot}%{_libqt5_plugindir}/ %{_libdir}/nextcloudsync_vfs_{suffix,xattr}.so

%suse_update_desktop_file com.nextcloud.desktopclient.nextcloud
%fdupes %{buildroot}%{_datadir}/

%ldconfig_scriptlets -n %{soname}%{sover}

%posttrans -n nextcloud-desktop-vfs-plugin
echo "The virtual file system implementation of nextcloud-desktop on Linux is \
at an early experimental stage. Enable at your own risk. \
Please read %{_docdir}/nextcloud-desktop-vfs-plugin/README.vfs.md for steps \
needed to enable the plugin." || true

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

%files lang
%{_datadir}/nextcloud/i18n/

%if 0%{?is_opensuse}
%files doc
%doc %{_docdir}/%{name}/
%endif

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
%if %{with qt6_dolphin}
%dir %{_qt6_pluginsdir}/kf6/kfileitemaction
%{_qt6_pluginsdir}/kf6/kfileitemaction/nextclouddolphinactionplugin.so
%dir %{_qt6_pluginsdir}/kf6/overlayicon
%{_qt6_pluginsdir}/kf6/overlayicon/nextclouddolphinoverlayplugin.so
%else
%dir %{_libqt5_plugindir}/kf5/kfileitemaction
%{_libqt5_plugindir}/kf5/kfileitemaction/nextclouddolphinactionplugin.so
%dir %{_libqt5_plugindir}/kf5/overlayicon
%{_libqt5_plugindir}/kf5/overlayicon/nextclouddolphinoverlayplugin.so
%endif

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
%{_libqt5_plugindir}/*.so

%changelog
