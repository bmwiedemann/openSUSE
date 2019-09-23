#
# spec file for package kdebase4-workspace
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%{!?_fillupdir: %global _fillupdir /var/adm/fillup-templates}

%define with_multiseat 1

Name:           kdebase4-workspace
Version:        4.11.22
Release:        0
Summary:        The KDE Workspace Components
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Url:            http://www.kde.org/
BuildRequires:  fdupes
BuildRequires:  kde4-filesystem
BuildRequires:  libdbusmenu-qt-devel
BuildRequires:  libkactivities-devel
BuildRequires:  libkde4-devel >= %{_kde_platform_version}
#BuildRequires:  libkdepimlibs4-devel >= %{_kde_platform_version}
BuildRequires:  libpolkit-qt-1-devel
BuildRequires:  libprison-devel
BuildRequires:  libqimageblitz-devel
BuildRequires:  libraw1394-devel
BuildRequires:  pam-devel
BuildRequires:  pciutils-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(libxklavier)
%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
%endif
BuildRequires:  libqjson-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxml2-tools
%if %{with_multiseat}
BuildRequires:  systemd-devel
%endif
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
# SLE12 doesn't provide wayland-egl
%if 0%{?suse_version} > 1230 && 0%{?is_opensuse}
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(wayland-egl)
%endif
Source0:        kde-workspace-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        titlebar_decor.png
Source3:        kwin-cubecap.png
Source4:        sysconfig.displaymanager-kdm
Source5:        kdm
Source6:        kdm-logrotate
Source7:        ksysguardd.service
## KDM patches
# PATCH-FIX-OPENSUSE kdm-cope-with-new-grub.diff -- Don't look for grub-set-default, we won't need it (bnc#771545)
Patch1:         kdm-cope-with-new-grub.diff
# PATCH-FIX-OPENSUSE In O:F since r24
Patch2:         kdm-relaxed-auth.diff
Patch3:         kdm-make_it_cool.diff
# PATCH-FIX-OPENSUSE kdm-sysconfig-values.diff -- Adds syconfig support to KDM
Patch4:         kdm-sysconfig-values.diff
# PATCH-FIX-OPENSUSE kdm-wordbreak.diff -- Wraps the username if it's too long
Patch5:         kdm-wordbreak.diff
# PATCH-FIX-OPENSUSE kdm-remove-duplicated-sessions.diff -- Removes duplicate sessions from KDM session list
Patch6:         kdm-remove-duplicated-sessions.diff
# PATCH-FIX-OPENSUSE kdm-all-users-nopass.diff -- Allows the setting which enables users to login without password
Patch7:         kdm-all-users-nopass.diff
# PATCH-FIX-OPENSUSE kdm-kdmconf.diff -- Cleans up the old kdmrc file
Patch8:         kdm-kdmconf.diff
# PATCH-FIX-OPENSUSE kdm-dont-grab-mouse.diff -- Revert changes in KDM that made it also grab the mouse, which
# prevents xvkbd from working on tablet PCs (bnc#445726)
Patch9:         kdm-dont-grab-mouse.diff
# PATCH-FIX-OPENSUSE kdm-long-xserver-timeout.diff -- Increases the time KDM waits for X to start up (bnc#462478)
Patch10:        kdm-long-xserver-timeout.diff
# PATCH-FIX-OPENSUSE These three patches are workarounds for fingerprint support (bnc#533189)
Patch11:        kdm-fix-generic-greeter.diff
Patch12:        kdm-fix-labelcolors.diff
Patch13:        same-pam-generic-classic.diff
# PATCH-FIX-OPENSUSE kdm_systemd_shutdown.patch Avoid the situation where systemd would kill KDM
# which prevents reboot/shutdown (Fedora Patch)
Patch14:        kdm_systemd_shutdown.patch
# Patch from Fedora to enable plymouth support in KDM.
# Patch is based on the changes within GDM to detect running plymouth
# and issue a quit to the plymouth daemon
Patch15:        kdm_plymouth.patch
# PATCH-FIX-OPENSUSE kdm-filter-out-btrfs-snapshots.patch wbauer@tmo.at -- filter out btrfs snapshot entries from the restart menu
Patch17:        kdm-filter-out-btrfs-snapshots.patch
## Workspace patches
# PATCH-FIX-OPENSUSE startkde.diff -- Injects branded startupconfigkeys to users $KDEHOME, and adds %datadir/kde4/env
# to list of read enviroments
Patch50:        startkde.diff
# PATCH-FIX-OPENSUSE kde4-migrate.diff -- Migrates config from .kde to .kde4
Patch51:        kde4-migrate.diff
# PATCH-FIX-OPENSUSE systemsettings-desktop.diff -- Changes name of System Settings to Configure Desktop
Patch52:        systemsettings-desktop.diff
# PATCH-FIX-OPENSUSE rotate-wacom-pointers.diff -- Adds support to krandrtray that rotates wacom pointers when the display is rotated
Patch53:        rotate-wacom-pointers.diff
# PATCH-FIX-OPENSUSE plasma-branding-defaults-applets.diff -- Brands kickoff, so it uses branded start-here icon, and adds
# several applications to SystemApplications category
Patch54:        plasma-branding-defaults-applets.diff
# PATCH-FIX-OPENSUSE plasma-dashboard-leave.diff -- Makes possible to leave dashboard view with just left-click
Patch55:        plasma-dashboard-leave.diff
# PATCH-FIX-OPENSUSE plasma-kickoff-newly-collapsing.diff -- Adds several features to kickoff, e.g. recently installed category,
# and reduced menu length
Patch56:        plasma-kickoff-newly-collapsing.diff
# PATCH-FIX-OPENSUSE plasma-panel-resize-hint.diff -- Displays pixel size when resizing panel
Patch57:        plasma-panel-resize-hint.diff
# PATCH-FIX-OPENSUSE krunner-no-italics.diff -- Change italic krunner result subtext to be smaller instead of italic (kde#307344)
Patch59:        krunner-no-italics.diff
# PATCH-FIX-OPENSUSE plasma-disable-networkmanager.diff -- Makes it possible to disable it on KDE start depending on sysconfig
Patch60:        plasma-disable-networkmanager.diff
# PATCH-FIX-OPENSUSE opensuse-homepage.diff -- Makes kickoff use openSUSE homepage as default
Patch62:        opensuse-homepage.diff
# PATCH-FIX-OPENSUSE opensuse-kinfocenter.diff (created by Alin M. Elena to have some openSUSE distro info in kinfocenter)
Patch63:        opensuse-kinfocenter.diff
# PATCH-FIX-UPSTREAM klipper.diff -- fix performance issue with Klipper see https://bugs.kde.org/show_bug.cgi?id=238084
Patch64:        klipper.patch
# PATCH-FIX-UPSTREAM kdm-backend-session.patch fix type mismatch in resource handling kde#323436
Patch65:        kdm-backend-session.patch
# PATCH-FIX-OPENSUSE add-calculator-hotkey.patch -- Adds hotkey for Calculator button (bnc#726550)
Patch66:        add-calculator-hotkey.patch
# PATCH-FIX-OPENSUSE Remove the dependencies on strigi
Patch67:        remove_strigi.patch
# Taken from fedora, additional changes resubmitted to fedora
Patch71:        kde-workspace-4.11.0-kdm-logind-multiseat.patch
Patch72:        much-more-plasma-debug.patch
# PATCH-FIX-OPENSUSE systemsettings-desktop-kde4.diff -- Changes name of System Settings to Configure KDE 4 Applications
Patch73:        systemsettings-desktop-kde4.diff
# PATCH-FIX-OPENSUSE gcc6-fixes.diff -- Fix errors reported by GCC6 compiler
Patch74:        gcc6-fixes.diff
# PATCH-FIX-OPENSUSE gcc7-fix.diff boo#1031317 wbauer@tmo.at -- Fix an error reported by the GCC7 compiler
Patch75:        gcc7-fix.diff
# PATCH-FIX-OPENSUSE
Patch76:        skip-qtwebkit-parts.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{name}-liboxygenstyle = %{version}
# Requires /etc/xdg/menus/applications.menu (bnc#754104)
%if !0%{?is_opensuse}
Requires:       desktop-data-SLE
%else
Requires:       desktop-data-openSUSE
%endif
Requires:       kactivities4 >= 4.13.3
Requires:       kde4-kgreeter-plugins = %{version}
%if 0%{?suse_version} <= 1320 && !0%{?is_opensuse}
Requires:       kscreen < 5.3.0
%endif
Requires:       windowmanager
# patch kdm-sysconfig-values.diff requires /var/lib/xdm/authdir/authfiles (bnc#784212)
Requires:       xdm
Requires:       xmessage
Requires:       xprop
# The openSUSE-release package should always be installed, but just to make sure as that kinfocenter needs it
Requires:       %{name}-addons = %{version}
Requires:       %{name}-libs = %{version}
Requires:       distribution-release
Requires:       socat
Recommends:     kdebase4-SuSE
Recommends:     kwin
Recommends:     plasma-addons
Recommends:     plasmoid-quickaccess
Recommends:     %{name}-plasma-calendar
# bnc#845592
Recommends:     kde-gtk-config
Suggests:       kdm
Requires(pre):	permissions
%define debug_package_requires %{name} = %{version}-%{release} kdelibs4-debuginfo
Provides:       kdebase3:/opt/kde3/bin/kicker
#Ktouchpadenabler is now part of workspace
Provides:       ktouchpadenabler = %{version}
Obsoletes:      ktouchpadenabler < %{version}
#KDED Appmenu is now part of workspace
Provides:       kded-appmenu = %{version}
Obsoletes:      kded-appmenu < %{version}
Requires:       appmenu-qt > 0.2.0
Requires:       oxygen-cursors
#Akonadi plasma engine is no longer provided
Obsoletes:      kdebase4-workspace-plasma-engine-akonadi < %{version}
Provides:       kdebase4-workspace-plasma-engine-akonadi = %{version}
%kde4_runtime_requires
# libplasmaclock links to kdepimlibs
# %%kde4_pimlibs_requires
%define _dminitdir %{_kde4_prefix}/lib/X11/displaymanagers

%description
This package contains the basic packages for a K Desktop Environment
workspace.

%package -n kdm-branding-upstream
Summary:        KDE login and display manager - upstream branding
Group:          System/GUI/KDE
Provides:       kdm-branding = %{_kde_branding_version}
Requires(pre):	%fillup_prereq
Supplements:    packageand(kdm:branding-upstream)
Conflicts:      otherproviders(kdm-branding)

%description -n kdm-branding-upstream
This package contains the upstream branding for KDE's display manager
kdm.

%package -n kwin
Summary:        KDE Window Manager
Group:          System/GUI/KDE
Provides:       kde4-kwin
Provides:       windowmanager
%kde4_runtime_requires
Requires:       %{name}-liboxygenstyle >= %{version}
Provides:       kdebase3:/opt/kde3/bin/kwin

%description -n kwin
KWin is the window manager of the K desktop environment.

%package -n kde4-kgreeter-plugins
Summary:        The KDE Greeter Plugin Components
Group:          System/GUI/KDE
Provides:       windowmanager
%kde4_runtime_requires

%description -n kde4-kgreeter-plugins
This package contains the Greeter Plugins that are needed by KDM and
Screensaver unlocking

%package addons
Summary:        The KDE Workspace addons
Group:          System/GUI/KDE
Requires:       %{name}-libs = %{version}
%kde4_runtime_requires

%description addons
This package contains the files required to run the KDE4 systemsettings, and aditional
addons useful outside 4.x Plasma. They were split out for co-instability with Plasma5
and to maintain the ability to maintain settings for kdelibs4 based applications.

%package devel
Summary:        The KDE Workspace Components
Group:          Development/Libraries/KDE
Requires:       %{name}-liboxygenstyle = %{version}
Requires:       %{name}-libs = %{version}
Requires:       kwin = %{version}
Requires:       libkde4-devel >= %{_kde_platform_version}
Provides:       plasma-devel = %{_kde_platform_version}
%kde4_runtime_requires

%description devel
This package contains the basic packages for a K Desktop Environment
workspace.

%package -n kdm
Summary:        KDE login and display manager
Group:          System/GUI/KDE
Requires:       kde4-kgreeter-plugins = %{version}
Requires:       kdm-branding = %{_kde_branding_version}
Requires:       logrotate
Requires:       pam-config
Requires:       xorg-x11-server
Provides:       kdebase3-kdm = 3.5.1
Obsoletes:      kdebase3-kdm < 3.5.1
%kde4_runtime_requires

%description -n kdm
This package contains kdm, the login and session manager for KDE.

%package liboxygenstyle
Summary:        The Libraries of the oxygen-style
Group:          System/GUI/KDE
Requires:       %{name}-libs = %{version}
%kde4_runtime_requires

%description liboxygenstyle
This package contains the libraries of the oxygen style.

%package -n krandr
Summary:        KDE Screen management tools
Group:          System/GUI/KDE
%kde4_runtime_requires

%description -n krandr
KDE Screen management tools

%package -n oxygen4-cursors
Summary:        The KDE Workspace Cursors
Group:          System/GUI/KDE
Provides:       oxygen-cursors = %{version}
Obsoletes:      oxygen-cursors4 < %{version}
Provides:       oxygen-cursors4 = %{version}

%description -n oxygen4-cursors
This package contains the default cursor set for a K Desktop Environment
workspace.

%package libs
Summary:        The KDE Workspace Libraries
Group:          System/GUI/KDE
Obsoletes:      libkworkspace4
%kde4_runtime_requires

%description libs
This package contains the KDE Workspace Libraries.

%prep
%setup -q -n kde-workspace-%{version}
## KDM patches
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9 -p0
%patch10
%patch11
%patch12 -p1
%patch13
%patch14 -p1
%patch15 -p1
%patch17 -p1
## Workspace patches
%patch50
%patch51
%patch53
%patch54
%patch55
%patch56 -p1
%patch57
%patch59 -p1
%patch60 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%if %{with_multiseat}
%patch71 -p1
%endif
%patch72 -p1
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
%patch73
%else
%patch52
%endif
%patch74
%patch75 -p1
%patch76 -p1

cp %{SOURCE3} kwin/effects/cube/data/cubecap.png

%build
  EXTRA_FLAGS="-DKDE4_COMMON_PAM_SERVICE=xdm \
	-DSYSCONF_INSTALL_DIR=/etc \
	-DKDE4_ENABLE_FPIE=1"
    %cmake_kde4 -d build -- $EXTRA_FLAGS
    %make_jobs

%install
    cd build
    %kde4_makeinstall
    rm -rf %{buildroot}½{_kde4_modulesdir}/plasma_applet_calendar.so
    install -m 644 %{SOURCE2} %{buildroot}%{_kde4_appsdir}/kwin/
    mkdir -p %{buildroot}%{_fillupdir}/
    install -m 644 %{SOURCE4} %{buildroot}%{_fillupdir}/
    %create_subdir_filelist -d kdm       -v devel
    %create_subdir_filelist -d kwin      -v devel
    %create_subdir_filelist -d systemsettings -v devel
    cd ..
    sed -ri "s,.*%{_kde4_configdir}/kdm/backgroundrc,," filelists/kdm
    sed -ri "s,.*%{_kde4_configdir}/kdm/README,," filelists/kdm
    sed -ri "s,.*(%{_kde4_configdir}/kdm/kdmrc),%config(noreplace) \1," filelists/kdm
    rm -f %{buildroot}/%{_kde4_configdir}/kdm/README
    sed -ri "s,.*%{_kde4_appsdir}/kdm/themes/oxygen.*,," filelists/kdm
    sed -ri "s,.*%{_kde4_appsdir}/kdm/pics.*,," filelists/kdm
    ls -1 %{buildroot}%{_kde4_wallpapersdir}/ | while read wallpaper; \
      do test "$wallpaper" = "Horos" -o ! -d "%{buildroot}%{_kde4_wallpapersdir}/$wallpaper" \
	|| rm -r "%{buildroot}%{_kde4_wallpapersdir}/$wallpaper"; done
    mkdir -p %{buildroot}/etc
    rm -rf %{buildroot}%{_kde4_htmldir}/en/kicker
    pushd $RPM_BUILD_DIR/%buildsubdir/
    cat filelists/devel filelists/systemsettings filelists/kdm filelists/kwin | while read line; do echo "%exclude $line";done >filelists/exclude
    popd
    %suse_update_desktop_file    systemsettings X-SuSE-core
    %suse_update_desktop_file    kmenuedit      Core-Configuration
    %suse_update_desktop_file -r klipper        System TrayIcon
    %suse_update_desktop_file -r krandrtray     System TrayIcon
    mkdir -p  %{buildroot}%{_kde4_sbindir}
    mkdir -p %{buildroot}%{_kde4_sysconfdir}/init.d
    ln -sf rcxdm %{buildroot}%{_kde4_sbindir}/rckdm
    mkdir -p %{buildroot}%{_kde4_sysconfdir}/logrotate.d/
    install -m 644 %{SOURCE6} %{buildroot}%{_kde4_sysconfdir}/logrotate.d/kdm
  # Make it constant so build-compare doesn't complains. If commented postinstall
  # will generate a new one through genkdmconf.
    sed -i 's/^ForgingSeed=[0-9]\+/#ForgingSeed=1111122222/' %{buildroot}%{_kde4_configdir}/kdm/kdmrc
    mkdir -p %{buildroot}%{_dminitdir}/
    cp %{SOURCE5} %{buildroot}%{_dminitdir}/
    mkdir -p %{buildroot}%{_sysconfdir}/alternatives
    touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
    ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_dminitdir}/default-displaymanager

    %fdupes -s %{buildroot}
    %kde_post_install

%clean
    rm -rf %{buildroot}
    rm -rf filelists

%verifyscript
%verify_permissions -e %{_kde4_libexecdir}/kcheckpass

%post
/sbin/ldconfig
%set_permissions %{_kde4_libexecdir}/kcheckpass

%postun -p /sbin/ldconfig

%post -n kdm
%{_kde4_bindir}/genkdmconf
%{remove_and_set -n displaymanager KDM_SHUTDOWN}
if test -n "$KDM_SHUTDOWN" -a "$KDM_SHUTDOWN" != "no"; then
  if test "$KDM_SHUTDOWN" = "local" ; then
    KDM_SHUTDOWN=all
  fi
  case "$KDM_SHUTDOWN" in
  "auto" | "none" | "root")
    sed -i -e "s/^DISPLAYMANAGER_SHUTDOWN=.*/DISPLAYMANAGER_SHUTDOWN=\"$KDM_SHUTDOWN\"/" %{_kde4_sysconfdir}/sysconfig/displaymanager
    ;;
  esac
fi
/sbin/ldconfig
%{_sbindir}/update-alternatives --install %{_dminitdir}/default-displaymanager \
  default-displaymanager %{_dminitdir}/kdm 15

%postun -n kdm
/sbin/ldconfig
[ -f %{_dminitdir}/kdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_dminitdir}/kdm

%post -n kdm-branding-upstream
%{fillup_only -n displaymanager -s kdm}

%pre
rm -rf %{_kde4_appsdir}/ksmserver/ksmserver.notifyrc/

%post   -n kwin -p /sbin/ldconfig

%postun -n kwin -p /sbin/ldconfig

%post   liboxygenstyle -p /sbin/ldconfig

%postun liboxygenstyle -p /sbin/ldconfig

%post   libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files -n kde4-kgreeter-plugins
%defattr(-,root,root)
%{_kde4_modulesdir}/kgreet_*.so

%files -n kdm -f filelists/kdm
%defattr(-,root,root)
%license COPYING COPYING.DOC
%doc README
%config %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%config %{_kde4_sysconfdir}/logrotate.d/kdm
%dir %{_dminitdir}
%dir %{_kde4_appsdir}/doc
%dir %{_kde4_appsdir}/doc/kdm
%dir %{_kde4_appsdir}/kdm
%dir %{_kde4_configdir}/kdm
%dir %{_kde4_wallpapersdir}
%lang(en) %{_kde4_htmldir}/en/kdm
%{_dminitdir}/kdm
%{_dminitdir}/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_kde4_configdir}/kdm.knsrc
%{_kde4_sbindir}/rckdm

%files -n kdm-branding-upstream
%defattr(-,root,root)
%license COPYING
%config(noreplace) %{_kde4_configdir}/kdm/backgroundrc
%{_kde4_appsdir}/kdm/pics
%{_fillupdir}/sysconfig.displaymanager-kdm

%files -n kwin -f filelists/kwin
%defattr(-,root,root)
%license COPYING COPYING.DOC
%doc README kwin/clients/aurorae/theme-description
%dir %{_kde4_servicesdir}/kwin
%{_kde4_appsdir}/kwin/cubecap.png
%{_kde4_appsdir}/kwin/titlebar_decor.png
%exclude %{_kde4_datadir}/dbus-1/interfaces/org.kde.KWin.xml
%exclude %{_kde4_libdir}/libkdecorations.so*
%exclude %{_kde4_bindir}/oxygen-shadow-demo
%exclude %{_kde4_modulesdir}/kwin3_oxygen.so
%exclude %{_kde4_modulesdir}/kwin_oxygen_config.so
%exclude %{_kde4_appsdir}/kconf_update/oxygen.upd
%exclude %{_kde4_appsdir}/kconf_update/update_oxygen.pl
%exclude %{_kde4_appsdir}/kwin/oxygenclient.desktop
%{_kde4_appsdir}/kwin/default_rules/plasma_desktop_containment.kwinrules

%files liboxygenstyle
%defattr(-,root,root)
%license COPYING COPYING.DOC
%doc README
%dir %{_kde4_modulesdir}/plugins/styles
%{_kde4_bindir}/oxygen-demo
%{_kde4_bindir}/oxygen-settings
%{_kde4_bindir}/oxygen-shadow-demo
%{_kde4_libdir}/liboxygenstyle.so.*
%{_kde4_libdir}/liboxygenstyleconfig.so.*
%{_kde4_modulesdir}/kstyle_oxygen_config.so
%{_kde4_modulesdir}/plugins/styles/oxygen.so
%{_kde4_modulesdir}/kwin3_oxygen.so
%{_kde4_modulesdir}/kwin_oxygen_config.so
%dir %{_kde4_appsdir}/kstyle
%dir %{_kde4_appsdir}/kstyle/themes
%{_kde4_appsdir}/kstyle/themes/oxygen.themerc
%dir %{_kde4_appsdir}/kconf_update
%{_kde4_appsdir}/kconf_update/oxygen.upd
%{_kde4_appsdir}/kconf_update/update_oxygen.pl
%dir %{_kde4_appsdir}/kwin
%{_kde4_appsdir}/kwin/oxygenclient.desktop

%files devel -f filelists/devel
%defattr(-,root,root)
%license COPYING COPYING.DOC
%doc README
%{_kde4_appsdir}/cmake
%{_kde4_datadir}/dbus-1/interfaces/
%{_kde4_includedir}/*
%{_kde4_libdir}/cmake/KDE4Workspace/
%{_kde4_libdir}/libkdecorations.so
%{_kde4_libdir}/libkephal.so
%{_kde4_libdir}/libkfontinst.so
%{_kde4_libdir}/libkfontinstui.so
%{_kde4_libdir}/libkscreensaver.so
%{_kde4_libdir}/libksgrd.so
%{_kde4_libdir}/libkworkspace.so
%{_kde4_libdir}/liblsofui.so
%{_kde4_libdir}/liboxygenstyle.so
%{_kde4_libdir}/liboxygenstyleconfig.so
%{_kde4_libdir}/libplasma-geolocation-interface.so
%{_kde4_libdir}/libplasma_applet-system-monitor.so
%{_kde4_libdir}/libplasmaclock.so
%{_kde4_libdir}/libplasmagenericshell.so
%{_kde4_libdir}/libpowerdevilconfigcommonprivate.so
%{_kde4_libdir}/libpowerdevilcore.so
%{_kde4_libdir}/libpowerdevilui.so
%{_kde4_libdir}/libprocesscore.so
%{_kde4_libdir}/libsystemsettingsview.so
%{_kde4_libdir}/libtaskmanager.so
%{_kde4_libdir}/libweather_ion.so
%{_kde4_modulesdir}/plugins/designer/ksysguardlsofwidgets.so

%files addons -f filelists/systemsettings
%defattr(-,root,root)
%license COPYING
%doc README
%{_kde4_modulesdir}/kcm*.so
%{_kde4_modulesdir}/kded_appmenu.so
%{_kde4_modulesdir}/kded_freespacenotifier.so
%{_kde4_modulesdir}/kded_keyboard.so
%{_kde4_modulesdir}/kded_khotkeys.so
%{_kde4_modulesdir}/kded_ktouchpadenabler.so
%{_kde4_modulesdir}/kded_kwrited.so
%{_kde4_modulesdir}/kded_statusnotifierwatcher.so
%{_kde4_modulesdir}/kstyle*.so
%{_kde4_modulesdir}/plugins/styles/
%{_kde4_servicesdir}/style.desktop
%{_kde4_servicesdir}/screensaver.desktop
%{_kde4_servicesdir}/kcm_infosummary.desktop
%{_kde4_servicesdir}/dma.desktop
%{_kde4_servicesdir}/mouse.desktop
%{_kde4_servicesdir}/interrupts.desktop
%{_kde4_servicesdir}/ksplashthememgr.desktop
%{_kde4_servicesdir}/kcm_pci.desktop
%{_kde4_servicesdir}/kcm_keyboard.desktop
%{_kde4_servicesdir}/opengl.desktop
%{_kde4_servicesdir}/autostart.desktop
%{_kde4_servicesdir}/fontinst.desktop
%{_kde4_servicesdir}/ioports.desktop
%{_kde4_servicesdir}/kcmsmserver.desktop
%{_kde4_servicesdir}/nic.desktop
%{_kde4_servicesdir}/joystick.desktop
%{_kde4_servicesdir}/solid-actions.desktop
%{_kde4_servicesdir}/keys.desktop
%{_kde4_servicesdir}/devinfo.desktop
%{_kde4_servicesdir}/workspaceoptions.desktop
%{_kde4_servicesdir}/cursortheme.desktop
%{_kde4_servicesdir}/display.desktop
%{_kde4_servicesdir}/standard_actions.desktop
%{_kde4_servicesdir}/clock.desktop
%{_kde4_servicesdir}/kcmlaunch.desktop
%{_kde4_servicesdir}/scsi.desktop
%{_kde4_servicesdir}/desktoppath.desktop
%{_kde4_servicesdir}/fonts.desktop
%{_kde4_servicesdir}/desktoptheme.desktop
%{_kde4_servicesdir}/xserver.desktop
%{_kde4_servicesdir}/khotkeys.desktop
%{_kde4_servicesdir}/bell.desktop
%{_kde4_servicesdir}/colors.desktop
%{_kde4_servicesdir}/kcmaccess.desktop
%{_kde4_servicesdir}/kcm_memory.desktop
%{_kde4_servicesdir}/kcmview1394.desktop
%{_kde4_servicesdir}/smbstatus.desktop
%dir %{_kde4_servicesdir}/kded
%{_kde4_servicesdir}/kded/appmenu.desktop
%{_kde4_servicesdir}/kded/khotkeys.desktop
%{_kde4_servicesdir}/kded/kwrited.desktop
%{_kde4_servicesdir}/kded/statusnotifierwatcher.desktop
%{_kde4_servicesdir}/kded/freespacenotifier.desktop
%{_kde4_servicesdir}/kded/keyboard.desktop
%{_kde4_servicesdir}/kded/ktouchpadenabler.desktop
%{_kde4_appsdir}/kstyle/
%{_kde4_appsdir}/kcmstyle/
%{_kde4_appsdir}/color-schemes/
%{_kde4_appsdir}/kaccess/
%{_kde4_appsdir}/kcmkeyboard/
%{_kde4_appsdir}/kcmusb/
%{_kde4_appsdir}/kfontview/
%{_kde4_appsdir}/ksplash/
%{_kde4_appsdir}/desktoptheme/
%{_kde4_appsdir}/kcmkeys/
%{_kde4_appsdir}/kcmview1394/
%{_kde4_appsdir}/kdisplay/
%{_kde4_appsdir}/khotkeys/
%{_kde4_appsdir}/konqsidebartng/
%{_kde4_appsdir}/kthememanager/
%{_kde4_appsdir}/freespacenotifier/
%{_kde4_appsdir}/kcminput/
%{_kde4_appsdir}/kcmsolidactions/
%{_kde4_appsdir}/ksmserver/
%{_kde4_appsdir}/kwrited/
%{_kde4_appsdir}/solid/
%dir %{_kde4_configkcfgdir}
%{_kde4_configkcfgdir}/freespacenotifier.kcfg
%dir %{_kde4_configdir}
%config %{_kde4_configdir}/activities.knsrc
%config %{_kde4_configdir}/colorschemes.knsrc
%config %{_kde4_configdir}/kfontinst.knsrc
%config %{_kde4_configdir}/ksplash.knsrc
%config %{_kde4_configdir}/plasma-themes.knsrc
%config %{_kde4_configdir}/wallpaper.knsrc
%config %{_kde4_configdir}/xcursor.knsrc
%exclude %{_kde4_libdir}/libsystemsettingsview.so.*
%exclude %{_kde4_modulesdir}/kcm_kwin*.so
%exclude %{_kde4_modulesdir}/kcm_kdm.so
%exclude %{_kde4_modulesdir}/kcm_randr.so
%exclude %{_kde4_modulesdir}/plugins/styles/oxygen.so
%exclude %{_kde4_modulesdir}/kstyle_oxygen_config.so
%exclude %{_kde4_appsdir}/kstyle/themes/oxygen.themerc

%files -n krandr
%defattr(-,root,root)
%license COPYING
%doc README
%{_kde4_applicationsdir}/krandrtray.desktop
%{_kde4_bindir}/krandrstartup
%{_kde4_bindir}/krandrtray
%{_kde4_modulesdir}/kcm_randr.so
%{_kde4_modulesdir}/kded_randrmonitor.so
%{_kde4_servicesdir}/kded/randrmonitor.desktop
%{_kde4_servicesdir}/randr.desktop

%files -f filelists/exclude
%defattr(-,root,root)
#positives
%license COPYING COPYING.DOC
%doc README
%doc %lang(en) %{_kde4_htmldir}/en/
%attr(-, root, shadow) %{_kde4_libexecdir}/kcheckpass
%config %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.*
%{_kde4_applicationsdir}/
%{_kde4_appsdir}/
%{_kde4_bindir}/*
%{_kde4_configdir}/
%dir %{_kde4_configkcfgdir}
%{_kde4_configkcfgdir}/plasma-shell-desktop.kcfg
%{_kde4_datadir}/autostart/
%{_kde4_datadir}/dbus-1/services/
%{_kde4_datadir}/dbus-1/system-services/
%{_kde4_datadir}/polkit-1/
%{_kde4_iconsdir}/hicolor/*/*/*
%{_kde4_iconsdir}/oxygen/*/*
%{_kde4_libdir}/*.so
%{_kde4_libdir}/*.so.*
%{_kde4_libdir}/kconf_update_bin/
%{_kde4_modulesdir}/
%{_kde4_sharedir}/services/
%{_kde4_sharedir}/servicetypes/
%{_kde4_appsdir}/plasma-desktop/init
%{_kde4_appsdir}/plasma-netbook/init
%{_kde4_appsdir}/plasma/layout-templates

#blacklist
%exclude %{_kde4_appsdir}/kwin/default_rules/plasma_desktop_containment.kwinrules
%exclude %{_kde4_applicationsdir}/krandrtray.desktop
%exclude %{_kde4_appsdir}/cmake
%exclude %{_kde4_appsdir}/doc
%exclude %{_kde4_appsdir}/doc/kdm
%exclude %{_kde4_appsdir}/kstyle
%exclude %{_kde4_appsdir}/kcmstyle
%exclude %{_kde4_appsdir}/kdm
%exclude %{_kde4_appsdir}/kwin/cubecap.png
%exclude %{_kde4_appsdir}/kwin/titlebar_decor.png
%exclude %{_kde4_appsdir}/color-schemes/
%exclude %{_kde4_appsdir}/kaccess/
%exclude %{_kde4_appsdir}/kcmkeyboard/
%exclude %{_kde4_appsdir}/kcmusb/
%exclude %{_kde4_appsdir}/kfontview/
%exclude %{_kde4_appsdir}/ksplash/
%exclude %{_kde4_appsdir}/desktoptheme/
%exclude %{_kde4_appsdir}/kcmkeys/
%exclude %{_kde4_appsdir}/kcmview1394/
%exclude %{_kde4_appsdir}/kdisplay/
%exclude %{_kde4_appsdir}/khotkeys/
%exclude %{_kde4_appsdir}/konqsidebartng/
%exclude %{_kde4_appsdir}/kthememanager/
%exclude %{_kde4_appsdir}/freespacenotifier/
%exclude %{_kde4_appsdir}/kcminput/
%exclude %{_kde4_appsdir}/kcmsolidactions/
%exclude %{_kde4_appsdir}/ksmserver/
%exclude %{_kde4_appsdir}/kwrited/
%exclude %{_kde4_appsdir}/solid/
%exclude %{_kde4_bindir}/krandrstartup
%exclude %{_kde4_bindir}/krandrtray
%exclude %{_kde4_bindir}/oxygen-demo
%exclude %{_kde4_bindir}/oxygen-settings
%exclude %{_kde4_configdir}/kdm
%exclude %{_kde4_configdir}/kdm/backgroundrc
%exclude %{_kde4_configdir}/activities.knsrc
%exclude %{_kde4_configdir}/colorschemes.knsrc
%exclude %{_kde4_configdir}/kfontinst.knsrc
%exclude %{_kde4_configdir}/ksplash.knsrc
%exclude %{_kde4_configdir}/plasma-themes.knsrc
%exclude %{_kde4_configdir}/wallpaper.knsrc
%exclude %{_kde4_configdir}/xcursor.knsrc
%exclude %{_kde4_htmldir}/en/kdm
%exclude %{_kde4_libdir}/libkephal.so
%exclude %{_kde4_libdir}/libkephal.so.*
%exclude %{_kde4_libdir}/libkfontinst.so
%exclude %{_kde4_libdir}/libkfontinst.so.*
%exclude %{_kde4_libdir}/libkfontinstui.so
%exclude %{_kde4_libdir}/libkfontinstui.so.*
%exclude %{_kde4_libdir}/libkscreensaver.so
%exclude %{_kde4_libdir}/libkscreensaver.so.*
%exclude %{_kde4_libdir}/libksgrd.so
%exclude %{_kde4_libdir}/libksgrd.so.*
%exclude %{_kde4_libdir}/libkworkspace.so
%exclude %{_kde4_libdir}/libkworkspace.so.*
%exclude %{_kde4_libdir}/liblsofui.so
%exclude %{_kde4_libdir}/liblsofui.so.*
%exclude %{_kde4_libdir}/liboxygenstyle.*
%exclude %{_kde4_libdir}/liboxygenstyleconfig.so
%exclude %{_kde4_libdir}/liboxygenstyleconfig.so.*
%exclude %{_kde4_libdir}/libplasma-geolocation-interface.so
%exclude %{_kde4_libdir}/libplasma-geolocation-interface.so.*
%exclude %{_kde4_libdir}/libplasma_applet-system-monitor.so
%exclude %{_kde4_libdir}/libplasma_applet-system-monitor.so.*
%exclude %{_kde4_libdir}/libplasmaclock.so
%exclude %{_kde4_libdir}/libplasmaclock.so.*
%exclude %{_kde4_libdir}/libplasmagenericshell.so
%exclude %{_kde4_libdir}/libplasmagenericshell.so.*
%exclude %{_kde4_libdir}/libpowerdevilconfigcommonprivate.so
%exclude %{_kde4_libdir}/libpowerdevilconfigcommonprivate.so.*
%exclude %{_kde4_libdir}/libpowerdevilcore.so
%exclude %{_kde4_libdir}/libpowerdevilcore.so.*
%exclude %{_kde4_libdir}/libpowerdevilui.so
%exclude %{_kde4_libdir}/libpowerdevilui.so.*
%exclude %{_kde4_libdir}/libprocesscore.so
%exclude %{_kde4_libdir}/libprocesscore.so.*
%exclude %{_kde4_libdir}/libsystemsettingsview.so
%exclude %{_kde4_libdir}/libsystemsettingsview.so.*
%exclude %{_kde4_libdir}/libtaskmanager.so
%exclude %{_kde4_libdir}/libtaskmanager.so.*
%exclude %{_kde4_libdir}/libweather_ion.so
%exclude %{_kde4_libdir}/libweather_ion.so.*
%exclude %{_kde4_libdir}/libkhotkeysprivate.so.*
%exclude %{_kde4_modulesdir}/kcm_kdm.so
%exclude %{_kde4_modulesdir}/kcm_randr.so
%exclude %{_kde4_modulesdir}/kcm*.so
%exclude %{_kde4_modulesdir}/kded_appmenu.so
%exclude %{_kde4_modulesdir}/kded_freespacenotifier.so
%exclude %{_kde4_modulesdir}/kded_keyboard.so
%exclude %{_kde4_modulesdir}/kded_khotkeys.so
%exclude %{_kde4_modulesdir}/kded_ktouchpadenabler.so
%exclude %{_kde4_modulesdir}/kded_kwrited.so
%exclude %{_kde4_modulesdir}/kded_statusnotifierwatcher.so
%exclude %{_kde4_modulesdir}/kstyle*.so
%exclude %{_kde4_modulesdir}/kded_randrmonitor.so
%exclude %{_kde4_modulesdir}/kgreet_*.so
%exclude %{_kde4_modulesdir}/kstyle_oxygen_config.so
%exclude %{_kde4_modulesdir}/plugins/designer/ksysguardlsofwidgets.so
%exclude %{_kde4_modulesdir}/plugins/styles
%exclude %{_kde4_modulesdir}/plugins/styles/oxygen.so
%exclude %{_kde4_modulesdir}/plugins/gui_platform
%exclude %{_kde4_modulesdir}/plugins/gui_platform/libkde.so
%exclude %{_kde4_servicesdir}/kded/randrmonitor.desktop
%exclude %{_kde4_servicesdir}/kwin
%exclude %{_kde4_servicesdir}/randr.desktop
%exclude %{_kde4_servicesdir}/style.desktop
%exclude %{_kde4_servicesdir}/screensaver.desktop
%exclude %{_kde4_servicesdir}/kcm_infosummary.desktop
%exclude %{_kde4_servicesdir}/dma.desktop
%exclude %{_kde4_servicesdir}/mouse.desktop
%exclude %{_kde4_servicesdir}/interrupts.desktop
%exclude %{_kde4_servicesdir}/ksplashthememgr.desktop
%exclude %{_kde4_servicesdir}/kcm_pci.desktop
%exclude %{_kde4_servicesdir}/kcm_keyboard.desktop
%exclude %{_kde4_servicesdir}/opengl.desktop
%exclude %{_kde4_servicesdir}/autostart.desktop
%exclude %{_kde4_servicesdir}/fontinst.desktop
%exclude %{_kde4_servicesdir}/ioports.desktop
%exclude %{_kde4_servicesdir}/kcmsmserver.desktop
%exclude %{_kde4_servicesdir}/nic.desktop
%exclude %{_kde4_servicesdir}/joystick.desktop
%exclude %{_kde4_servicesdir}/solid-actions.desktop
%exclude %{_kde4_servicesdir}/keys.desktop
%exclude %{_kde4_servicesdir}/devinfo.desktop
%exclude %{_kde4_servicesdir}/workspaceoptions.desktop
%exclude %{_kde4_servicesdir}/cursortheme.desktop
%exclude %{_kde4_servicesdir}/display.desktop
%exclude %{_kde4_servicesdir}/standard_actions.desktop
%exclude %{_kde4_servicesdir}/clock.desktop
%exclude %{_kde4_servicesdir}/kcmlaunch.desktop
%exclude %{_kde4_servicesdir}/scsi.desktop
%exclude %{_kde4_servicesdir}/desktoppath.desktop
%exclude %{_kde4_servicesdir}/fonts.desktop
%exclude %{_kde4_servicesdir}/desktoptheme.desktop
%exclude %{_kde4_servicesdir}/xserver.desktop
%exclude %{_kde4_servicesdir}/khotkeys.desktop
%exclude %{_kde4_servicesdir}/bell.desktop
%exclude %{_kde4_servicesdir}/colors.desktop
%exclude %{_kde4_servicesdir}/kcmaccess.desktop
%exclude %{_kde4_servicesdir}/kcm_memory.desktop
%exclude %{_kde4_servicesdir}/kcmview1394.desktop
%exclude %{_kde4_servicesdir}/smbstatus.desktop
%exclude %{_kde4_servicesdir}/kded/appmenu.desktop
%exclude %{_kde4_servicesdir}/kded/khotkeys.desktop
%exclude %{_kde4_servicesdir}/kded/kwrited.desktop
%exclude %{_kde4_servicesdir}/kded/statusnotifierwatcher.desktop
%exclude %{_kde4_servicesdir}/kded/freespacenotifier.desktop
%exclude %{_kde4_servicesdir}/kded/keyboard.desktop
%exclude %{_kde4_servicesdir}/kded/ktouchpadenabler.desktop
%exclude %{_kde4_sysconfdir}/dbus-1/system.d/org.kde.kcontrol.kcmkdm.conf
%exclude %{_fillupdir}/sysconfig.displaymanager-kdm

%files -n oxygen4-cursors
%defattr(-,root,root)
%license COPYING
%doc README
%{_kde4_iconsdir}/Oxygen_*/
%{_kde4_iconsdir}/KDE_Classic/

%files libs
%defattr(-,root,root)
%license COPYING
%doc README
%{_kde4_libdir}/libkdecorations.so.*
%{_kde4_libdir}/libkephal.so.*
%{_kde4_libdir}/libkfontinst.so.*
%{_kde4_libdir}/libkfontinstui.so.*
%{_kde4_libdir}/libkscreensaver.so.*
%{_kde4_libdir}/libksgrd.so.*
%{_kde4_libdir}/libkworkspace.so.*
%{_kde4_libdir}/liblsofui.so.*
%{_kde4_libdir}/libplasma-geolocation-interface.so.*
%{_kde4_libdir}/libplasma_applet-system-monitor.so.*
%{_kde4_libdir}/libplasmaclock.so.*
%{_kde4_libdir}/libplasmagenericshell.so.*
%{_kde4_libdir}/libpowerdevilconfigcommonprivate.so.*
%{_kde4_libdir}/libpowerdevilcore.so.*
%{_kde4_libdir}/libpowerdevilui.so.*
%{_kde4_libdir}/libprocesscore.so.*
%{_kde4_libdir}/libsystemsettingsview.so.*
%{_kde4_libdir}/libtaskmanager.so.*
%{_kde4_libdir}/libweather_ion.so.*
%{_kde4_libdir}/libkhotkeysprivate.so.*
%{_kde4_modulesdir}/plugins/gui_platform/

%changelog
