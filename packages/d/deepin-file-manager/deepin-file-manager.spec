#
# spec file for package deepin-file-manager
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


%define _name dde-file-manager
%define sover 5

Name:           deepin-file-manager
Version:        5.6.4
Release:        0
Summary:        Deepin File Manager
License:        GPL-3.0-or-later AND MIT
Group:          Productivity/File utilities
URL:            https://github.com/linuxdeepin/dde-file-manager
Source0:        https://github.com/linuxdeepin/dde-file-manager/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        deepin-file-dbus-installer.in
Source2:        deepin-file-polkit-installer.in
# PATCH-FIX-UPSTEAM fix-header-include.patch hillwood@opensuse.org - dfsearch is necessary
Patch1:         fix-header-include.patch
# PATCH-FIX-UPSTEAM gcc12.patch hillwood@opensuse.org - fix gcc 12 build
Patch2:         gcc-12.patch
# PATCH-FIX-UPSTRAM update-taglib-interface.patch hillwood@opensuse.org - fix build on new taglib
Patch3:         update-taglib-interface.patch
# PATCH-FIX-UPSTRAM fix-build-on-icu-75.patch hillwood@opensuse.org - ICU 75 needs c++17
Patch4:         fix-build-on-icu-75.patch
Patch99:        harden_dde-filemanager-daemon.service.patch
%ifarch ppc ppc64 ppc64le s390 s390x
BuildRequires:  deepin-desktop-base
%else
BuildRequires:  deepin-manual
%endif
BuildRequires:  boost-devel
BuildRequires:  deepin-gettext-tools
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5PlatformHeaders-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libmimetic-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pcre-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  udisks2-qt5-devel >= 5.0.0
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(disomaster)
BuildRequires:  pkgconfig(docparser)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(htmlcxx)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libdmr)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-util)
Requires:       deepin-shortcut-viewer
Requires:       deepin-terminal
Requires:       file-roller
Requires:       glib2-tools
Requires:       gstreamer-plugins-good
Requires:       gvfs
Requires:       libqt5-dxcbplugin
Requires:       libqt5-qdbus
Requires:       qt5integration
Requires:       samba
Requires:       xdg-user-dirs
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
Deepin File Manager is a file management tool independently  developed by Deepin
Technology, featured with searching, copying, trash, compression/decompression,
file property and other file management functions.

%package -n deepin-desktop
Summary:        Deepin Desktop
Group:          System/GUI/Other

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%package -n lib%{_name}%{sover}
Summary:        Deepin File Manager libraries
Group:          System/Libraries

%description -n lib%{_name}%{sover}
This package contains the libraries for deepin-file-manager

%package -n libdfm-extension%{sover}
Summary:        Deepin File Manager libraries
Group:          System/Libraries

%description -n libdfm-extension%{sover}
This package contains the libraries for deepin-file-manager

%package polkit
Summary:        Deepin File polkit profiles
Group:          Productivity/File utilities
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description polkit
This package provides polkit profiles for deepin-file-manager. These profiles
are not adopted by security team. If you need the polkit feature, you should
install them manually or use deepin-polkit-install package.

%package dbus
Summary:        Deepin File DBus profiles
Group:          Productivity/File utilities
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description dbus
This package provides dbus profiles for deepin-file-manager. These profiles are
not adopted by security team. If you need the dbus feature, you should install
them manually or use deepin-dbus-install package.

%package devel
Summary:        Development package for Deepin File Manager
Group:          Development/Libraries/X11
Requires:       lib%{_name}%{sover} = %{version}

%description devel
Header files and libraries for Deepin File Manager.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}

find -type f -perm 775 -exec chmod 644 {} \;
find -type f -name ".readme" -delete -print
sed -i '/target.path/s|$${PREFIX}/lib|$$LIBDIR|' src/dde-dock-plugins/disk-mount/disk-mount.pro

sed -i 's|lrelease|lrelease-qt5|' src/%{_name}/generate_translations.sh \
src/%{_name}-*/generate_translations.sh \
src/dde-desktop/translate_generation.sh

sed -i 's|lupdate|lupdate-qt5|' src/%{_name}*/update_translations.sh \
src/dde-desktop/update_translations.sh \
src/dde-dock-plugins/disk-mount/update_translations.sh

sed -i '/target.path/s|lib|%{_lib}|' src/dde-dock-plugins/disk-mount/disk-mount.pro

sed -i 's|qdbus|qdbus-qt5|g' tests/dde-file-manager-lib/dbus/ut_dbussystemInfo_test.cpp

sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|g' src/dde-file-manager-daemon/dbusservice/help.sh \
src/dde-file-manager-daemon/dbusservice/vault.sh

sed -i 's|qdbuscpp2xml|qdbuscpp2xml-qt5|g' src/dde-file-manager-daemon/dbusservice/vault.sh

# --as-needed link option
sed -i '/PKGCONFIG +=/s|$| x11 liblucene++|' src/%{_name}-lib/%{_name}-lib.pro

# sed -i 's/dframeworkdbus/dframeworkdbus liblucene++/g;s/-lKF5Codecs/-lKF5Codecs -llucene++/g' src/dde-file-manager-lib/dde-file-manager-lib.pro

cp 3rdparty/fsearch/* src/dde-file-manager-lib/search/
# sed -i 's|fsearch.h|../../../3rdparty/fsearch/fsearch.h|g' src/dde-file-manager-lib/search/dfsearch.h

%build

qmake-qt5 \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} \
        CONFIG+="DISABLE_ANYTHING" \
        IS_PLATFORM_OPENSUSE=YES \
        VERSION=%{version} \
        filemanager.pro
%make_build

%install
%qmake5_install

chmod -x %{buildroot}%{_datadir}/deepin-manual/manual-assets/application/dde-file-manager/file-manager/common/*.svg \
         %{buildroot}%{_datadir}/deepin-manual/manual-assets/application/dde-file-manager/file-manager/*/*.md

install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/deepin-file-dbus-installer
install -m0755 %{SOURCE2} %{buildroot}%{_bindir}/deepin-file-polkit-installer

# Fix values extending the format should start with "X-" rpmlint warnings
sed -i 's/OnlyShowIn=/X-DEEPIN-OnlyShowIn=/g' \
        %{buildroot}%{_datadir}/applications/dde-computer.desktop \
        %{buildroot}%{_datadir}/applications/dde-trash.desktop

# Remove zero-length files
rm -rf %{buildroot}%{_datadir}/dde-file-manager/mimetypes/audio.mimetype \
        %{buildroot}%{_datadir}/dde-file-manager/mimetypes/image.mimetype

# File all dbus service and policy profiles, workaround boo#1134132 and boo#1134131
mkdir build
pushd build
mkdir polkit
mv %{buildroot}%{_datadir}/polkit-1/actions/* polkit/
tar -cvf polkit.tar.gz polkit
install -m 0644 polkit.tar.gz %{buildroot}%{_datadir}/%{_name}/

mkdir dbus
mkdir dbus/system-services
mkdir dbus/system.d
mv %{buildroot}%{_datadir}/dbus-1/system-services/* dbus/system-services
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/* dbus/system.d
tar -cvf dbus.tar.gz dbus
install -m 0644 dbus.tar.gz %{buildroot}%{_datadir}/%{_name}/
popd

install -d %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdde-filemanager-daemon

chmod -x %{buildroot}%{_datadir}/dbus-1/services/*.service
%suse_update_desktop_file -r %{_name} System FileManager
%suse_update_desktop_file -r dde-computer System FileManager
%suse_update_desktop_file -r dde-trash System FileManager

%fdupes %{buildroot}%{_datadir}

%pre
%service_add_pre dde-filemanager-daemon.service

%post
%service_add_post dde-filemanager-daemon.service

%preun
%service_del_preun dde-filemanager-daemon.service

%postun
%service_del_postun dde-filemanager-daemon.service

%post -n lib%{_name}%{sover} -p /sbin/ldconfig
%postun -n lib%{_name}%{sover} -p /sbin/ldconfig

%post -n libdfm-extension%{sover} -p /sbin/ldconfig
%postun -n libdfm-extension%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE LICENSE.MIT
# %config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.deepin.filemanager.daemon.conf
%{_prefix}/lib/systemd/system/dde-filemanager-daemon.service
%{_bindir}/*
%exclude %{_bindir}/dde-desktop
%exclude %{_bindir}/deepin-file-dbus-installer
%exclude %{_bindir}/deepin-file-polkit-installer
%{_sbindir}/rcdde-filemanager-daemon
%dir %{_libdir}/dde-dock
%dir %{_libdir}/dde-dock/plugins
%dir %{_libdir}/dde-dock/plugins/system-trays/
%{_libdir}/dde-dock/plugins/system-trays/libdde-disk-mount-plugin.so
%{_libdir}/%{_name}/
%{_datadir}/%{_name}/
%{_datadir}/deepin-manual/manual-assets/application/%{_name}
%exclude %{_datadir}/%{_name}/*.tar.gz
%{_datadir}/icons/hicolor/scalable/apps/*.svg
# %{_datadir}/deepin/dde-file-manager
%{_datadir}/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%{_datadir}/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%{_datadir}/dbus-1/services/*.service
# %{_datadir}/dbus-1/system-services/com.deepin.filemanager.daemon.service
# %{_datadir}/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
# %{_datadir}/polkit-1/actions/com.deepin.filemanager.daemon.policy
%{_datadir}/applications/dde-*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/dbus-1/services/com.deepin.dde.desktop.service
%ifarch aarch64
%{_sysconfdir}/xdg/autostart/dde-file-manager-autostart.desktop
%endif

%files -n deepin-desktop
%defattr(-,root,root,-)
%{_bindir}/dde-desktop

%files -n lib%{_name}%{sover}
%defattr(-,root,root,-)
%{_libdir}/lib%{_name}.so.*

%files -n libdfm-extension%{sover}
%defattr(-,root,root,-)
%{_libdir}/libdfm-extension.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{_name}
%{_includedir}/dfm-extension
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{_name}.so
%{_libdir}/libdfm-extension.so

%files dbus
%defattr(-,root,root,-)
%{_bindir}/deepin-file-dbus-installer
%{_datadir}/%{_name}/dbus.tar.gz

%files polkit
%defattr(-,root,root,-)
%{_bindir}/deepin-file-polkit-installer
%{_datadir}/%{_name}/polkit.tar.gz

%files lang
%defattr(-,root,root,-)
%{_datadir}/dde-desktop
%{_datadir}/dde-disk-mount-plugin

%changelog
