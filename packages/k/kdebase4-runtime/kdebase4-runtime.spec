#
# spec file for package kdebase4-runtime
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define debug_package_requires %{name} = %{version}-%{release} kdelibs4-debuginfo
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %global _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
Name:           kdebase4-runtime
Version:        17.08.3
Release:        0
Summary:        The KDE Runtime Components
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org/
Source0:        kde-runtime-%{version}.tar.xz
Source1:        kde4-essential.menu
Source2:        kde-settings.menu
Source3:        kde-settings.directory
Source4:        KDE-Sys-Log-Out.ogg
Patch1:         kdesu-remember-keep-password.diff
# PATCH-FIX-OPENSUSE
Patch2:         skip-nfs-kioslave.patch
Patch4:         ksuseinstall.diff
Patch5:         kdesu-symbol-lookup-workaround.diff
# PATCH-FIX-OPENSUSE kdesu-add-some-i18n-love.patch -- bnc#852256
Patch7:         kdesu-add-some-i18n-love.patch
# PATCH-FIX-OPENSUSE kde-runtime-glib2-include.patch -- mlin@suse.com
Patch8:         kde-runtime-glib2-include.patch
# PATCH-FIX-OPENSUSE
Patch9:         skip-qtwebkit-parts.patch
BuildRequires:  NetworkManager-devel
BuildRequires:  alsa-devel
BuildRequires:  automoc4
BuildRequires:  fdupes
BuildRequires:  libattica-devel >= 0.1.4
BuildRequires:  libcanberra-devel
BuildRequires:  libexiv2-devel
BuildRequires:  libgcrypt-devel >= 1.5.0
BuildRequires:  libgpgmepp-devel
BuildRequires:  libkactivities-devel >= 4.13.2
BuildRequires:  libkde4-devel
BuildRequires:  libksuseinstall-devel
# NTrack backend is used when ther is no NM or wicd, however it breaks ifup method, for details see https://bugs.kde.org/show_bug.cgi?id=294441#c23
#BuildRequires:  libntrack-qt4-devel
BuildRequires:  libpulse-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  libssh-devel >= 0.6.0
BuildRequires:  libtirpc-devel
BuildRequires:  lzma-devel
BuildRequires:  openslp-devel
BuildRequires:  phonon-devel >= 4.3.80
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libwebp)
#!BuildIgnore:  kdebase4-runtime
Requires:       dbus-1-x11
Requires:       kdelibs4
Requires:       libphonon4
# the oxygen icon theme is used as fallback by KDE4's icon loader and KDE4 applications may depend on it being installed (boo#1022821)
Requires:       oxygen-icon-theme
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions
Requires(post): shared-mime-info
Requires(post): update-alternatives
Requires(postun): shared-mime-info
Requires(postun): update-alternatives
Recommends:     enscript
Recommends:     icoutils
Recommends:     ispell
Recommends:     kdialog
# KDE4 applications invoke khelpcenter, which is now provided by khelpcenter5
Recommends:     khelpcenter5 >= 17.04.1
Suggests:       cagibi
%{kde4_runtime_requires}
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
This package contains all run-time dependencies of KDE applications.

%package -n plasma-theme-oxygen
Summary:        The Oxygen Plasma Theme
Group:          System/GUI/KDE
Provides:       kdebase4-runtime:%{_datadir}/kde4/apps/desktoptheme/oxygen/metadata.desktop

%description -n plasma-theme-oxygen
This package contains the Plasma theme Oxygen.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
This package contains development files and headers needed to
build software using %{name}

%prep
%setup -q -n kde-runtime-%{version}
cp %{SOURCE4} $RPM_BUILD_DIR/kde-runtime-%{version}/knotify/sounds/
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
# Superseded by khelpcenter5
rm -r $RPM_BUILD_DIR/kde-runtime-%{version}/khelpcenter
sed -i"" "/khelpcenter/d" $RPM_BUILD_DIR/kde-runtime-%{version}/doc/CMakeLists.txt
sed -i"" "/documentationnotfound/d" $RPM_BUILD_DIR/kde-runtime-%{version}/doc/CMakeLists.txt
sed -i"" "/glossary/d" $RPM_BUILD_DIR/kde-runtime-%{version}/doc/CMakeLists.txt

%build
  %cmake_kde4 -d build -- -DKDE4_ENABLE_FPIE=1
  %make_jobs

%install
  %kde4_makeinstall -C build
  rm -rf %{buildroot}%{_kde4_datadir}/wallpapers
  rm -rf %{buildroot}%{_kde4_iconsdir}/hicolor/index.theme
  rm -rf %{buildroot}%{_kde4_iconsdir}/oxygen
  rm -rf %{buildroot}%{_kde4_mandir}/man8/nepomukser*
  mkdir -p %{buildroot}%{_kde4_sysconfdir}/xdg/menus
  mv %{buildroot}%{_kde4_sysconfdir}/xdg/menus/kde-information.menu %{buildroot}%{_kde4_sysconfdir}/xdg/menus/kde4-information.menu
  mkdir -p %{buildroot}%{_kde4_sysconfdir}/xdg/menus/applications-merged
  install -m 644 %{SOURCE1} %{buildroot}%{_kde4_sysconfdir}/xdg/menus/applications-merged/kde4-essential.menu
  install -m 644 %{SOURCE2} %{buildroot}%{_kde4_sysconfdir}/xdg/menus/kde4-settings.menu
  install -m 644 %{SOURCE3} %{buildroot}%{_kde4_datadir}/desktop-directories/
  mkdir -p %{buildroot}%{_kde4_prefix}/bin
  # create a dummy target for %{_sysconfdir}/alternatives/kdesu
  install -d -m 755 %{buildroot}%{_sysconfdir}/alternatives/
  touch %{buildroot}%{_sysconfdir}/alternatives/kdesu
  chmod +x %{buildroot}%{_sysconfdir}/alternatives/kdesu
  ln -s -f %{_sysconfdir}/alternatives/kdesu %{buildroot}%{_kde4_bindir}/kdesu
  touch %{buildroot}%{_sysconfdir}/alternatives/kdesu.1%{?ext_man}
  mv %{buildroot}%{_kde4_mandir}/man1/kdesu.1 %{buildroot}%{_kde4_mandir}/man1/kdesu-4.1
  ln -s -f %{_sysconfdir}/alternatives/kdesu.1%{?ext_man} %{buildroot}%{_kde4_mandir}/man1/kdesu.1%{?ext_man}
  rm -rf %{buildroot}%{_kde4_includedir}/KDE
  # Conflicts with kuiserver5
  rm %{buildroot}/%{_datadir}/dbus-1/services/org.kde.kuiserver.service
  %suse_update_desktop_file -r knetattach    System Network
  %fdupes -s %{buildroot}
  %kde_post_install

%post
/sbin/ldconfig
%mime_database_post
%set_permissions %{_kde4_libexecdir}/kdesud
%{_sbindir}/update-alternatives \
    --install %{_kde4_bindir}/kdesu kdesu %{_kde4_libexecdir}/kdesu 20 \
    --slave %{_kde4_mandir}/man1/kdesu.1.gz kdesu.1%{?ext_man} %{_kde4_mandir}/man1/kdesu-4.1%{?ext_man}

%postun
/sbin/ldconfig
%mime_database_postun

if [ $1 -eq 0 ]; then
    %{_sbindir}/update-alternatives --remove kdesu \
        %{_kde4_libexecdir}/kdesu
fi

%verifyscript
%verify_permissions -e %{_kde4_bindir}/kcheckpass
%verify_permissions -e %{_kde4_bindir}/kdesud
%verify_permissions -e %{_kde4_libexecdir}/kdesud

%files -n plasma-theme-oxygen
%license COPYING
%{_kde4_appsdir}/desktoptheme/oxygen

%files devel
%{_kde4_includedir}/knotify_export*
%{_kde4_includedir}/knotifyconfig.h
%{_kde4_includedir}/knotifyplugin.h

%files
%license COPYING COPYING.LIB

# --- knewstuff sources ---
%{_kde4_configdir}/emoticons.knsrc
%{_kde4_configdir}/icons.knsrc
%{_kde4_configdir}/khotnewstuff.knsrc
%{_kde4_configdir}/khotnewstuff_upload.knsrc

# --- menus ---
%config %{_kde4_sysconfdir}/xdg/menus/applications-merged
%config %{_kde4_sysconfdir}/xdg/menus/kde4-information.menu
%config %{_kde4_sysconfdir}/xdg/menus/kde4-settings.menu

# --- default configurations ---
%{_kde4_configkcfgdir}/jpegcreatorsettings.kcfg

# --- misc configuration ---
%{_kde4_configdir}/kshorturifilterrc

# --- man file manuals ---
%doc %{_kde4_mandir}/man1/kdesu*.1*
%ghost %{_sysconfdir}/alternatives/kdesu.1%{?ext_man}
%doc %{_kde4_mandir}/man1/plasmapkg.1.gz

# --- html manuals ---
%doc %lang(en) %{_kde4_htmldir}/en/kcontrol
%doc %lang(en) %{_kde4_htmldir}/en/kdebugdialog
%doc %lang(en) %{_kde4_htmldir}/en/kdesu
%doc %lang(en) %{_kde4_htmldir}/en/kioslave
%doc %lang(en) %{_kde4_htmldir}/en/knetattach
%doc %lang(en) %{_kde4_htmldir}/en/onlinehelp
%doc %lang(en) %{_kde4_htmldir}/en/fundamentals

# --- thumbnail generators ---
%{_kde4_modulesdir}/comicbookthumbnail.so
%{_kde4_modulesdir}/cursorthumbnail.so
%{_kde4_modulesdir}/djvuthumbnail.so
%{_kde4_modulesdir}/fixhosturifilter.so
%{_kde4_modulesdir}/imagethumbnail.so
%{_kde4_modulesdir}/jpegthumbnail.so
%{_kde4_modulesdir}/svgthumbnail.so
%{_kde4_modulesdir}/textthumbnail.so
%{_kde4_modulesdir}/windowsexethumbnail.so
%{_kde4_modulesdir}/windowsimagethumbnail.so

# --- kcm modules ---
%{_kde4_modulesdir}/kcm_attica.so
%{_kde4_modulesdir}/kcm_cgi.so
%{_kde4_modulesdir}/kcm_componentchooser.so
%{_kde4_modulesdir}/kcm_device_automounter.so
%{_kde4_modulesdir}/kcm_emoticons.so
%{_kde4_modulesdir}/kcm_filetypes.so
%{_kde4_modulesdir}/kcm_icons.so
%{_kde4_modulesdir}/kcm_kded.so
%{_kde4_modulesdir}/kcm_kdnssd.so
%{_kde4_modulesdir}/kcm_knotify.so
%{_kde4_modulesdir}/kcm_locale.so
%{_kde4_modulesdir}/kcm_phonon.so
%{_kde4_modulesdir}/kcmspellchecking.so
%{_kde4_modulesdir}/kcm_trash.so

# --- kded modules ---
%{_kde4_modulesdir}/kded_desktopnotifier.so
%{_kde4_modulesdir}/kded_device_automounter.so
%{_kde4_modulesdir}/kded_kpasswdserver.so
%{_kde4_modulesdir}/kded_ktimezoned.so
%{_kde4_modulesdir}/kded_networkstatus.so
%{_kde4_modulesdir}/kded_networkwatcher.so
%{_kde4_modulesdir}/kded_phononserver.so
%{_kde4_modulesdir}/kded_remotedirnotify.so
%{_kde4_modulesdir}/kded_solidautoeject.so
%{_kde4_modulesdir}/kded_soliduiserver.so

# --- kdeinit modules ---
%{_kde4_libdir}/libkdeinit4_kcmshell4.so
%{_kde4_libdir}/libkdeinit4_kglobalaccel.so
%{_kde4_libdir}/libkdeinit4_kuiserver.so
%{_kde4_libdir}/libkdeinit4_kwalletd.so

# --- kio slaves ---
%{_kde4_modulesdir}/kio_about.so
%{_kde4_modulesdir}/kio_applications.so
%{_kde4_modulesdir}/kio_archive.so
%{_kde4_modulesdir}/kio_bookmarks.so
%{_kde4_modulesdir}/kio_cgi.so
%{_kde4_modulesdir}/kio_desktop.so
%{_kde4_modulesdir}/kio_filter.so
%{_kde4_modulesdir}/kio_finger.so
%{_kde4_modulesdir}/kio_fish.so
%{_kde4_modulesdir}/kio_floppy.so
%{_kde4_modulesdir}/kio_info.so
%{_kde4_modulesdir}/kio_man.so
%{_kde4_modulesdir}/kio_network.so
%{_kde4_modulesdir}/kio_remote.so
%{_kde4_modulesdir}/kio_settings.so
%if 0%{?suse_version} >= 1310
%{_kde4_modulesdir}/kio_sftp.so
%endif
%{_kde4_modulesdir}/kio_smb.so
%{_kde4_modulesdir}/kio_thumbnail.so
%{_kde4_modulesdir}/kio_trash.so

# --- uri filters ---
%{_kde4_modulesdir}/kshorturifilter.so
%{_kde4_modulesdir}/kuriikwsfilter.so
%{_kde4_modulesdir}/kurisearchfilter.so
%{_kde4_modulesdir}/localdomainurifilter.so

# --- rename plugins ---
%{_kde4_modulesdir}/librenaudioplugin.so
%{_kde4_modulesdir}/librenimageplugin.so

# --- kparts ---
%{_kde4_modulesdir}/libkmanpart.so

# --- other ---
%{_kde4_libdir}/attica_kde.so
%{_kde4_libdir}/libknotifyplugin.so
%{_kde4_libdir}/libkwalletbackend.so
%{_kde4_libdir}/libmolletnetwork.so
%{_kde4_modulesdir}/plugins/imageformats/kimg_webp.so
%{_kde4_modulesdir}/plugins/phonon_platform
%{_kde4_modulesdir}/kio_recentdocuments.so
%{_kde4_modulesdir}/kded_recentdocumentsnotifier.so

# --- libexec ---
%verify(not mode) %attr(2755,root,nogroup) %{_kde4_libexecdir}/kdesud
%{_kde4_libexecdir}/kdeeject
%{_kde4_libexecdir}/kdesu
%{_kde4_libexecdir}/kdontchangethehostname
%{_kde4_libexecdir}/kioexec
%{_kde4_libexecdir}/knetattach

# --- apps directories ---
%dir %{_kde4_appsdir}/hardwarenotifications
%dir %{_kde4_appsdir}/kde
%dir %{_kde4_appsdir}/konqueror
%dir %{_kde4_appsdir}/konqueror/dirtree
%dir %{_kde4_appsdir}/konqueror/dirtree/remote

# --- apps ---
%exclude %{_kde4_appsdir}/desktoptheme/oxygen
%{_kde4_appsdir}/cmake
%{_kde4_appsdir}/desktoptheme
%{_kde4_appsdir}/hardwarenotifications/hardwarenotifications.notifyrc
%{_kde4_appsdir}/kcm_componentchooser
%{_kde4_appsdir}/kcmlocale
%{_kde4_appsdir}/kcm_phonon
%{_kde4_appsdir}/kconf_update/devicepreference.upd
%{_kde4_appsdir}/kconf_update/kuriikwsfilter.upd
%{_kde4_appsdir}/kde/kde.notifyrc
%{_kde4_appsdir}/kglobalaccel
%{_kde4_appsdir}/kio_bookmarks
%{_kde4_appsdir}/kio_desktop
%{_kde4_appsdir}/kio_docfilter
%{_kde4_appsdir}/kio_finger
%{_kde4_appsdir}/kio_info
%{_kde4_appsdir}/konqsidebartng
%{_kde4_appsdir}/konqueror/dirtree/remote/smb-network.desktop
%{_kde4_appsdir}/ksmserver
%{_kde4_appsdir}/kwalletd
%{_kde4_appsdir}/libphonon
%{_kde4_appsdir}/phonon
%{_kde4_appsdir}/remoteview

# --- protocols ---
%{_kde4_servicesdir}/about.protocol
%{_kde4_servicesdir}/applications.protocol
%{_kde4_servicesdir}/ar.protocol
%{_kde4_servicesdir}/bookmarks.protocol
%{_kde4_servicesdir}/bzip.protocol
%{_kde4_servicesdir}/bzip2.protocol
%{_kde4_servicesdir}/cgi.protocol
%{_kde4_servicesdir}/desktop.protocol
%{_kde4_servicesdir}/finger.protocol
%{_kde4_servicesdir}/fish.protocol
%{_kde4_servicesdir}/floppy.protocol
%{_kde4_servicesdir}/gzip.protocol
%{_kde4_servicesdir}/info.protocol
%{_kde4_servicesdir}/man.protocol
%{_kde4_servicesdir}/network.protocol
%{_kde4_servicesdir}/programs.protocol
%{_kde4_servicesdir}/recentdocuments.protocol
%{_kde4_servicesdir}/remote.protocol
%{_kde4_servicesdir}/settings.protocol
%{_kde4_servicesdir}/smb.protocol
%if 0%{?suse_version} >= 1310
%{_kde4_servicesdir}/sftp.protocol
%endif
%{_kde4_servicesdir}/tar.protocol
%{_kde4_servicesdir}/thumbnail.protocol
%{_kde4_servicesdir}/trash.protocol
%{_kde4_servicesdir}/zip.protocol
%{_kde4_servicesdir}/lzma.protocol
%{_kde4_servicesdir}/xz.protocol

# --- services ---
%{_kde4_servicesdir}/comicbookthumbnail.desktop
%{_kde4_servicesdir}/componentchooser.desktop
%{_kde4_servicesdir}/cursorthumbnail.desktop
%{_kde4_servicesdir}/desktopthumbnail.desktop
%{_kde4_servicesdir}/device_automounter_kcm.desktop
%{_kde4_servicesdir}/directorythumbnail.desktop
%{_kde4_servicesdir}/djvuthumbnail.desktop
%{_kde4_servicesdir}/emoticons.desktop
%{_kde4_servicesdir}/filetypes.desktop
%{_kde4_servicesdir}/fixhosturifilter.desktop
%{_kde4_servicesdir}/htmlthumbnail.desktop
%{_kde4_servicesdir}/icons.desktop
%{_kde4_servicesdir}/imagethumbnail.desktop
%{_kde4_servicesdir}/jpegthumbnail.desktop
%{_kde4_servicesdir}/kcm_attica.desktop
%{_kde4_servicesdir}/kcmcgi.desktop
%{_kde4_servicesdir}/kcmkded.desktop
%{_kde4_servicesdir}/kcm_kdnssd.desktop
%{_kde4_servicesdir}/kcmnotify.desktop
%{_kde4_servicesdir}/kcm_phonon.desktop
%{_kde4_servicesdir}/kcmtrash.desktop
%{_kde4_servicesdir}/kglobalaccel.desktop
%{_kde4_servicesdir}/kmanpart.desktop
%{_kde4_servicesdir}/knotify4.desktop
%{_kde4_servicesdir}/kshorturifilter.desktop
%{_kde4_servicesdir}/kuiserver.desktop
%{_kde4_servicesdir}/kuriikwsfilter.desktop
%{_kde4_servicesdir}/kurisearchfilter.desktop
%{_kde4_servicesdir}/kwalletd.desktop
%{_kde4_servicesdir}/language.desktop
%{_kde4_servicesdir}/localdomainurifilter.desktop
%{_kde4_servicesdir}/qimageioplugins/webp.desktop
%{_kde4_servicesdir}/renaudiodlg.desktop
%{_kde4_servicesdir}/renimagedlg.desktop
%{_kde4_servicesdir}/searchproviders
%{_kde4_servicesdir}/spellchecking.desktop
%{_kde4_servicesdir}/svgthumbnail.desktop
%{_kde4_servicesdir}/textthumbnail.desktop
%{_kde4_servicesdir}/windowsimagethumbnail.desktop
%{_kde4_servicesdir}/windowsexethumbnail.desktop

# --- kded services ---
%{_kde4_servicesdir}/kded/desktopnotifier.desktop
%{_kde4_servicesdir}/kded/device_automounter.desktop
%{_kde4_servicesdir}/kded/kpasswdserver.desktop
%{_kde4_servicesdir}/kded/ktimezoned.desktop
%{_kde4_servicesdir}/kded/networkstatus.desktop
%{_kde4_servicesdir}/kded/networkwatcher.desktop
%{_kde4_servicesdir}/kded/phononserver.desktop
%{_kde4_servicesdir}/kded/remotedirnotify.desktop
%{_kde4_servicesdir}/kded/solidautoeject.desktop
%{_kde4_servicesdir}/kded/soliduiserver.desktop
%{_kde4_servicesdir}/kded/recentdocumentsnotifier.desktop

# --- service types ---
%{_kde4_servicetypes}/knotifynotifymethod.desktop
%{_kde4_servicetypes}/phononbackend.desktop
%{_kde4_servicetypes}/searchprovider.desktop
%{_kde4_servicetypes}/thumbcreator.desktop

# --- applications ---
%{_kde4_applicationsdir}/knetattach.desktop

# --- libraries---
%{_kde4_libdir}/libkwalletbackend.so.*
%{_kde4_libdir}/libmolletnetwork.so.*

# --- kconf update---
%{_kde4_libdir}/kconf_update_bin/phonon_devicepreference_update
%{_kde4_libdir}/kconf_update_bin/phonon_deviceuids_update

# --- executables ---
%{_kde4_bindir}/kcmshell4
%{_kde4_bindir}/kde4
%{_kde4_bindir}/kde4-menu
%{_kde4_bindir}/kdebugdialog
%{_kde4_bindir}/kde-cp
%{_kde4_bindir}/kde-mv
%{_kde4_bindir}/kde-open
%{_kde4_bindir}/kdesu
%ghost %{_sysconfdir}/alternatives/kdesu
%{_kde4_bindir}/keditfiletype
%{_kde4_bindir}/kfile4
%{_kde4_bindir}/kglobalaccel
%{_kde4_bindir}/khotnewstuff4
%{_kde4_bindir}/khotnewstuff-upload
%{_kde4_bindir}/kiconfinder
%{_kde4_bindir}/kioclient
%{_kde4_bindir}/kmimetypefinder
%{_kde4_bindir}/knotify4
%{_kde4_bindir}/kquitapp
%{_kde4_bindir}/kreadconfig
%{_kde4_bindir}/kstart
%{_kde4_bindir}/ksvgtopng
%{_kde4_bindir}/ktraderclient
%{_kde4_bindir}/ktrash
%{_kde4_bindir}/kuiserver
%{_kde4_bindir}/kwalletd
%{_kde4_bindir}/kwriteconfig
%{_kde4_bindir}/solid-hardware

# --- dbus interfaces---
%{_kde4_datadir}/dbus-1/interfaces/org.kde.KTimeZoned.xml
%{_kde4_datadir}/dbus-1/interfaces/org.kde.network.kioslavenotifier.xml

# --- dbus services ---
%{_kde4_datadir}/dbus-1/services/org.kde.knotify.service

# --- theme-related files ---
%{_kde4_datadir}/emoticons/
%{_kde4_iconsdir}/default.kde4
%{_kde4_datadir}/sounds/*.ogg
%{_kde4_iconsdir}/hicolor/*/apps/knetattach.*

# --- other ---
%{_kde4_datadir}/desktop-directories
%{_kde4_datadir}/locale/*
%{_kde4_datadir}/mime/packages/network.xml
%{_kde4_datadir}/mime/packages/webp.xml
%{_kde4_appsdir}/kconf_update/kwallet-4.13.upd

%changelog
