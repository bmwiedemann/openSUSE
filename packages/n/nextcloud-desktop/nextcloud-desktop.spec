#
# spec file for package nextcloud-desktop
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


%define soname  libnextcloudsync
%define sover   0
Name:           nextcloud-desktop
Version:        3.6.4
Release:        0
Summary:        Nextcloud desktop synchronisation client
License:        GPL-2.0-or-later AND LGPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://nextcloud.com/
Source:         https://github.com/nextcloud/desktop/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        sysctl-sync-inotify.conf
# PATCH-FIX-OPENSUSE nextcloud-desktop-remove-datetime.patch sor.alexei@meowr.ru -- Remove __TIME__ and __DATE__.
Patch1:         nextcloud-desktop-remove-datetime.patch
BuildRequires:  AppStream
BuildRequires:  cmake >= 3.2
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  inkscape >= 1.0
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  qtkeychain-qt5-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5KIO) >= 5.16
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
Recommends:     cloudproviders-extension-nextcloud = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols2
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

%prep
%autosetup -p1 -n desktop-%{version}
cp -a %{SOURCE1} sysctl-sync-inotify.conf

%build

%cmake \
%if 0%{?is_opensuse}
  -DWITH_DOC=ON \
  -DNO_SHIBBOLETH=1
%endif
%cmake_build

%install
%cmake_install

%if 0%{?is_opensuse}
mkdir -p %{buildroot}%{_docdir}/%{name}-doc/
mv -f %{buildroot}%{_datadir}/doc/client/nextcloud-client/html/ \
  %{buildroot}%{_docdir}/%{name}-doc/html/
%else
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

%suse_update_desktop_file com.nextcloud.desktopclient.nextcloud
%fdupes %{buildroot}%{_datadir}/

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING*
%config %{_sysconfdir}/Nextcloud/
#%%config %%{_sysconfdir}/sysctl.d/99-%%{name}-sync-inotify.conf
%{_bindir}/nextcloud*
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
%doc %{_docdir}/%{name}-doc/
%endif

%files -n %{soname}%{sover}
%license COPYING*
%{_libdir}/%{soname}.so.*
%{_libdir}/libnextcloud_csync.so.*

%files -n %{soname}-devel
%{_includedir}/nextcloudsync/
%{_libdir}/%{soname}.so
%{_libdir}/libnextcloud_csync.so
%{_libdir}/nextcloudsync_vfs_*.so

%files -n nautilus-extension-nextcloud
%dir %{_datadir}/nautilus-python/
%dir %{_datadir}/nautilus-python/extensions/
%dir %{_datadir}/nautilus-python/extensions/__pycache__
%{_datadir}/nautilus-python/extensions/syncstate-Nextcloud.py*
%{_datadir}/nautilus-python/extensions/__pycache__/syncstate-Nextcloud*

%if 0%{?is_opensuse}
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
%dir %{_datadir}/cloud-providers/
%{_datadir}/cloud-providers/com.nextcloudgmbh.Nextcloud.ini
%{_datadir}/dbus-1/services/com.nextcloudgmbh.Nextcloud.service

%files dolphin
%{_libdir}/libnextclouddolphinpluginhelper.so
%{_libdir}/qt5/plugins/nextclouddolphinactionplugin.so
%dir %{_libdir}/qt5/plugins/kf5/overlayicon/
%{_libdir}/qt5/plugins/kf5/overlayicon/nextclouddolphinoverlayplugin.so
%{_datadir}/kservices5/nextclouddolphinactionplugin.desktop
%endif

%changelog
