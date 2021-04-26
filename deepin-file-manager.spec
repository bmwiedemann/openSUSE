#
# spec file for package deepin-file-manager
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _name dde-file-manager
%define sover 5

%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-file-manager
Version:        5.2.0.87
Release:        0
Summary:        Deepin File Manager
License:        GPL-3.0+
URL:            https://github.com/linuxdeepin/dde-file-manager
Source0:        https://github.com/linuxdeepin/dde-file-manager/archive/%{version}/%{_name}-%{version}.tar.gz
Source1:        deepin-file-dbus-installer.in
Source2:        deepin-file-polkit-installer.in
%ifarch %arm aarch64
# PATCH-FIX-UPSTEAM disable-dmr.patch hillwood@opensuse.org - Disable deepin movie plugin in ARM64
Patch0:         disable-dmr.patch
%endif
# PATCH-FIX-UPSTEAM fix-expected-token-errors.patch hillwood@opensuse.org - Fix error for js code
# Patch1:         fix-expected-token-errors.patch
# PATCH-FIX-UPSTEAM fix-return-type-error.patch hillwood@opensuse.org - Fix build error
Patch2:         fix-return-type-error.patch
# PATCH-FIX-UPSTEAM 001-use-Q_GLOBAL_STATIC.patch hillwood@opensuse.org
# use Q_GLOBAL_STATIC to initialize `eventHanlder` and `eventFilter`
# Initialisation of static global object `eventProcessor` requires `eventHanlder`
# and `eventFilter` initialised first. But that's not guaranteed by C++ standard
# and the program may crash. Instead, use Q_GLOBAL_STATIC to initialise the latter
# two objects.
# Patch4:         001-use-Q_GLOBAL_STATIC.patch
Patch4:         002-use-Q_GLOBAL_STATIC.patch
Group:          Productivity/File utilities
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
BuildRequires:  deepin-gettext-tools
BuildRequires:  file-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel 
BuildRequires:  libqt5-linguist
BuildRequires:  libmimetic-devel
BuildRequires:  dtkcore
BuildRequires:  boost-devel
BuildRequires:  libboost_system-devel
BuildRequires:  udisks2-qt5-devel >= 5.0.0
%ifarch %arm aarch64
%else
BuildRequires:  pkgconfig(libdmr)
%endif
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xdg)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(jemalloc)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(disomaster)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(htmlcxx)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  systemd-rpm-macros
Requires:       deepin-shortcut-viewer
Requires:       deepin-terminal
Requires:       file-roller
Requires:       gvfs
Requires:       samba
Requires:       xdg-user-dirs
Requires:       gstreamer-plugins-good
Requires:       glib2-tools
Requires:       libqt5-dxcbplugin
Requires:       libqt5-qdbus
Requires:       qt5integration
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

%package polkit
Summary:        Deepin File polkit profiles
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
AutoReqProv:    Off

%description polkit
This package provides polkit profiles for deepin-file-manager. These profiles
are not adopted by security team. If you need the polkit feature, you should
install them manually or use deepin-polkit-install package.

%package dbus
Summary:        Deepin File DBus profiles
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

sed -i '/#include <QException>/a #include <QPainterPath>' dialogs/dfmtaskwidget.cpp
sed -i '/#include <QTimer>/a #include <QPainterPath>' dde-file-manager-lib/interfaces/dfmglobal.cpp
sed -i '/#include <QPainter>/a #include <QPainterPath>' \
dde-file-manager-lib/interfaces/{dlistitemdelegate,dfmstyleditemdelegate,diconitemdelegate}.cpp dde-file-manager-lib/dialogs/openwithdialog.cpp

find -type f -perm 775 -exec chmod 644 {} \;
sed -i '/target.path/s|$${PREFIX}/lib|$$LIBDIR|' dde-dock-plugins/disk-mount/disk-mount.pro
# sed -i '/deepin-daemon/s|lib|libexec|' dde-zone/mainwindow.h
# sed -i 's|lib/gvfs|libexec|' %{_name}-lib/gvfs/networkmanager.cpp
# sed -i 's|%{_datadir}|%{_libdir}|' dde-sharefiles/appbase.pri

sed -i 's|lrelease|lrelease-qt5|' %{_name}/generate_translations.sh \
%{_name}-*/generate_translations.sh \
dde-desktop/translate_generation.sh

sed -i 's|lupdate|lupdate-qt5|' %{_name}*/update_translations.sh \
dde-desktop/update_translations.sh \
dde-dock-plugins/disk-mount/update_translations.sh

sed -i '/target.path/s|lib|%{_lib}|' dde-dock-plugins/disk-mount/disk-mount.pro

sed -i '/PLUGINDIR/s|view|views|' \
  %{_name}-plugins/pluginPreview/dde-video-preview-plugin/dde-video-preview-plugin.pro

sed -i 's|/lib/systemd/system|/usr/lib/systemd/system|g' \
dde-file-manager-daemon/dde-file-manager-daemon.pro

sed -i 's|qdbus|qdbus-qt5|g' dde-file-manager-lib/tests/dbus/ut_dbussystemInfo_test.cpp

sed -i 's|qdbusxml2cpp|qdbusxml2cpp-qt5|g' dde-file-manager-daemon/dbusservice/help.sh \
dde-file-manager-daemon/dbusservice/vault.sh

sed -i 's|qdbuscpp2xml|qdbuscpp2xml-qt5|g' dde-file-manager-daemon/dbusservice/vault.sh

# --as-needed link option
sed -i '/gtk/s|$| x11|' %{_name}-lib/%{_name}-lib.pro

# sed -i 's/1.8.2/%{version}/g' common/common.pri

%build
%qmake5 \
        PREFIX=%{_prefix} \
        LIBDIR=%{_libdir} \
        QMAKE_LFLAGS= \
        CONFIG+="DISABLE_ANYTHING" \
        IS_PLATFORM_OPENSUSE=YES \
        VERSION=%{version}-%{distribution} \
        filemanager.pro
%make_build

%install
%qmake5_install

install -m0755 %{SOURCE1} %{buildroot}%{_bindir}/deepin-file-dbus-installer
install -m0755 %{SOURCE2} %{buildroot}%{_bindir}/deepin-file-polkit-installer

# Fix values extending the format should start with "X-" rpmlint warnings
sed -i 's/OnlyShowIn=/X-DEEPIN-OnlyShowIn=/g' \
        %{buildroot}%{_datadir}/applications/dde-computer.desktop \
        %{buildroot}%{_datadir}/applications/dde-trash.desktop
        
# Remove zero-length files
rm -rf %{buildroot}%{_datadir}/dde-file-manager/mimetypes/audio.mimetype \
        %{buildroot}%{_datadir}/dde-file-manager/mimetypes/image.mimetype \
        %{buildroot}%{_datadir}/dde-file-manager/templates/newTxt.txt

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
%suse_update_desktop_file -r %{_name} System FileManager
%suse_update_desktop_file -r dde-computer System FileManager
%suse_update_desktop_file -r dde-trash System FileManager

%fdupes %{buildroot}

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

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
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
%exclude %{_datadir}/%{_name}/*.tar.gz
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/deepin/dde-file-manager
%{_datadir}/dbus-1/interfaces/com.deepin.filemanager.filedialog.xml
%{_datadir}/dbus-1/interfaces/com.deepin.filemanager.filedialogmanager.xml
%{_datadir}/dbus-1/services/com.deepin.filemanager.filedialog.service
%{_datadir}/dbus-1/services/org.freedesktop.FileManager.service
# %{_datadir}/dbus-1/system-services/com.deepin.filemanager.daemon.service
# %{_datadir}/polkit-1/actions/com.deepin.pkexec.dde-file-manager.policy
# %{_datadir}/polkit-1/actions/com.deepin.filemanager.daemon.policy
%{_datadir}/applications/dde-*.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/dbus-1/services/com.deepin.dde.desktop.service
%ifarch %arm aarch64
%{_sysconfdir}/xdg/autostart/dde-file-manager-autostart.desktop
%endif

%files -n deepin-desktop
%defattr(-,root,root,-)
%{_bindir}/dde-desktop

%files -n lib%{_name}%{sover}
%defattr(-,root,root,-)
%{_libdir}/lib%{_name}.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{_name}/
%{_libdir}/pkgconfig/%{_name}.pc
%{_libdir}/lib%{_name}.so

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
