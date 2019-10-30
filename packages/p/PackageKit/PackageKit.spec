#
# spec file for package PackageKit
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


%define BUILD_CNF 0
%if 0%{?sle_version}
%bcond_with offline_updates
%else
%bcond_without offline_updates
%endif
# $ pkcon search file /usr/bin/anjuta
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

Name:           PackageKit
Version:        1.1.12
Release:        0
Summary:        Simple software installation management software
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://www.freedesktop.org/software/PackageKit/
Source0:        %{url}/releases/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/%{name}-%{version}.tar.xz.asc
Source2:        baselibs.conf
Source3:        PackageKit.tmpfiles
Source99:       PackageKit.keyring

# PATCH-FIX-UPSTREAM PackageKit-return-on-transactions-going-backwards.patch gh#hughsie/PackageKit#301, bsc#1038425 sckang@suse.com -- transaction: Return directly when its state is going backwards
Patch1:         PackageKit-return-on-transactions-going-backwards.patch
# PATCH-FIX-UPSTREAM PackageKit-add-mutex-lock-to-protect-backend-priv-eulas.patch gh#hughsie/PackageKit#303, bsc#1038425 sckang@suse.com -- Remove pk_is_thread_default() check in pk_backend_is_eula_valid
Patch2:         PackageKit-add-mutex-lock-to-protect-backend-priv-eulas.patch
# PATCH-FEATURE-OPENSUSE PackageKit-systemd-timers.patch bsc#1115410 sckang@suse.com -- Migrate from cron to systemd timers
Patch3:         PackageKit-systemd-timers.patch
# PATCH-FIX-OPENSUSE PackageKit-remove-polkit-rules.patch bsc#1125434 sckang@suse.com -- Remove polkit rules file
Patch4:         PackageKit-remove-polkit-rules.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-fix-newest-filter.patch bsc#1137019 gh#hughsie/PackageKit#329 sckang@suse.com -- zypp: Emit installed package for newest filter
Patch5:         PackageKit-zypp-fix-newest-filter.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-fix-what-provides-newest-filter.patch bsc#984865, gh#hughsie/PackageKit#335 sckang@suse.com -- zypp: Add support for newest filter in what-provides
Patch6:         PackageKit-zypp-fix-what-provides-newest-filter.patch
# PATCH-FIX-UPSTREAM PackageKit-drop-gtk2.patch gh#/hughsie/PackageKit#333 - Port away from gtk2 dependency
Patch7:         PackageKit-drop-gtk2.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-get-updates-dup-or-up.patch gh#hughsie/PackageKit#343 sckang@suse.com -- zypp: Fix get-updates in Tumbleweed
Patch8:         PackageKit-zypp-get-updates-dup-or-up.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-dont-set-upgrade-mode-on-updating-specific-packages.patch gh#hughsie/PackageKit#345 sckang@suse.com -- zypp: Don't set upgrade mode in update-packages
Patch9:         PackageKit-zypp-dont-set-upgrade-mode-on-updating-specific-packages.patch
Patch10:        zypp-perform-actions-disallowed-by-update-in-upgrade-mode.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-reset-upgrade-mode-when-not-needed.patch gh#hughsie/PackageKit/commit/57e846f0 sckang@suse.com -- zypp: Reset upgrade mode to FALSE when not needed
Patch11:        PackageKit-zypp-reset-upgrade-mode-when-not-needed.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-promt-installing-already-installed-packages.patch gh#hughsie/PackageKit/commit/c45e0f22 sckang@suse.com -- zypp: Promt users when installing already installed packages
Patch12:        PackageKit-zypp-promt-installing-already-installed-packages.patch

BuildRequires:  autoconf-archive
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libarchive-devel
BuildRequires:  libcppunit-devel
BuildRequires:  libgudev-1_0-devel
BuildRequires:  libtool
BuildRequires:  libzypp-devel
BuildRequires:  mozilla-nspr-devel >= 4.8
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel >= 0.98
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  sqlite-devel
BuildRequires:  translation-update-upstream
BuildRequires:  vala
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# We really want a working backend (likely zypp)
Requires:       %{name}-backend
Requires:       %{name}-branding = %{version}
Requires(post): %fillup_prereq
Recommends:     %{name}-lang
%if 0%{suse_version} < 1500
Suggests:       cron
%endif
# doc package only contained the website, and got removed in 0.7.4
Obsoletes:      %{name}-doc < 0.7.4
# gtk+ 2 module was removed in 0.7.0
Obsoletes:      %{name}-gtk-module < 0.7.0
# ruck was removed in 0.6.4, make sure it gets removed
Obsoletes:      ruck <= 0.6.3
# the browser-plugin was dropped with version 1.1.0
Obsoletes:      %{name}-browser-plugin < 1.1.0
%{?systemd_ordering}

%description
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package backend-zypp
Summary:        Zypp backend for the PackageKit installation management software
License:        GPL-2.0-or-later
Group:          System/Daemons
Requires:       %{name} = %{version}
Provides:       %{name}-backend = %{version}

%description backend-zypp
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package gstreamer-plugin
Summary:        GStreamer plugin for the PackageKit installation management software
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name} = %{version}
Supplements:    packageand(%{name}:gstreamer-plugins-base)

%description gstreamer-plugin
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package gtk3-module
Summary:        GTK3 backend for the PackageKit installation management software
License:        GPL-2.0-or-later
Group:          System/Libraries
Recommends:     %{name} = %{version}
Supplements:    packageand(%{name}:gtk3)
%glib2_gsettings_schema_requires

%description gtk3-module
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package devel
Summary:        Header files for development with PackageKit
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libpackagekit-glib2-devel

%description devel
This package contains all necessary include files, libraries,
configuration files and development tools (with manual pages) needed to
compile and link applications using PackageKit.

%package -n libpackagekit-glib2-18
Summary:        GLib integration of PackageKit
License:        LGPL-2.1-or-later
Group:          System/Libraries
Recommends:     %{name}
Conflicts:      %{name} < %{version}
Provides:       libpackagekit-glib12 = %{version}
Obsoletes:      libpackagekit-glib12 < %{version}

%description -n libpackagekit-glib2-18
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package -n typelib-1_0-PackageKitGlib-1_0
Summary:        Introspection bindings for PackageKit's GLib integration
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-PackageKitGlib-1_0
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

This package provides the GObject Introspection bindings for the
PackageKit client library.

%package -n libpackagekit-glib2-devel
Summary:        GLib integration of PackageKit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       libpackagekit-glib2-18 = %{version}
Requires:       typelib-1_0-PackageKitGlib-1_0 = %{version}
Provides:       libpackagekit-glib12-devel = %{version}
Obsoletes:      libpackagekit-glib12-devel < %{version}

%description -n libpackagekit-glib2-devel
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%package branding-upstream
Summary:        Upstream configuration for the PackageKit installation management software
License:        GPL-2.0-or-later
Group:          System/Daemons
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provide configuration files -
#BRAND: /etc/PackageKit/*

%description branding-upstream
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

This package provides the upstream default configuration for PackageKit.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%if !0%{?is_opensuse}
export CFLAGS="%{optflags} -DSLE"
%endif
%configure \
	--disable-static \
	--enable-zypp \
	--enable-gstreamer-plugin \
%if ! %{BUILD_CNF}
	--disable-command-not-found \
%else
	--enable-command-not-found \
%endif
	--enable-systemd \
%if %{with offline_updates}
	--enable-offline-update \
%else
	--disable-offline-update \
%endif
%if 0%{suse_version} >= 1500
	--disable-cron \
%endif
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%if 0%{suse_version} < 1500
# move the cron configuration to a sysconfig template
install -d %{buildroot}%{_fillupdir}
mv %{buildroot}%{_sysconfdir}/sysconfig/packagekit-background %{buildroot}%{_fillupdir}/sysconfig.packagekit-background
%endif
# Prepare for update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/gst-install-plugins-helper %{buildroot}/%{_libexecdir}/gst-install-plugins-helper
# Add rcFOO symlinks
mkdir -p %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcpackagekit
%if  %{with offline_updates}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcpackagekit-offline-update
%endif
# install transactions.db to another directory so that we can use tmpfiles.d to create a link to it under /var/lib/PackageKit
install -m 0644 %{buildroot}%{_localstatedir}/lib/PackageKit/transactions.db %{buildroot}%{_datadir}/PackageKit/transactions.db
rm %{buildroot}%{_localstatedir}/lib/PackageKit/transactions.db
# install PackageKit.conf in tempfiles.d
install -d -m 0755 %{buildroot}%{_prefix}/lib/tmpfiles.d/
install -m 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/tmpfiles.d/%{name}.conf

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%pre
%service_add_pre packagekit.service
%if 0%{suse_version} >= 1500
%service_add_pre packagekit-background.service packagekit-background.timer
%endif
%if %{with offline_updates}
%service_add_pre packagekit-offline-update.service
%endif

%post
%if 0%{suse_version} < 1500
%{fillup_only -n packagekit-background}
%endif
%mime_database_post
%service_add_post packagekit.service
%if 0%{suse_version} >= 1500
%service_add_post packagekit-background.service packagekit-background.timer
%endif
%if %{with offline_updates}
%service_add_post packagekit-offline-update.service
%else
  if [ -L system-update ]; then
    rm system-update
  fi
  if [ -f var/lib/PackageKit/prepared-update ]; then
    rm var/lib/PackageKit/prepared-update
  fi
%endif
%tmpfiles_create %_tmpfilesdir/%{name}.conf

%preun
%service_del_preun packagekit.service
%if 0%{suse_version} >= 1500
%service_del_preun packagekit-background.service packagekit-background.timer
%endif
%if %{with offline_updates}
%service_del_preun packagekit-offline-update.service
%endif

%postun
%mime_database_postun
# Do not restart PackageKit on upgrade - it kills the transaction
export DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun packagekit.service
%if 0%{suse_version} >= 1500
%service_del_postun packagekit-background.service packagekit-background.timer
%endif
%if %{with offline_updates}
%service_del_postun packagekit-offline-update.service
%endif

%post gstreamer-plugin
update-alternatives --install %{_libexecdir}/gst-install-plugins-helper gst-install-plugins-helper %{_libexecdir}/pk-gstreamer-install 10

%postun gstreamer-plugin
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_libexecdir}/pk-gstreamer-install ]; then
  update-alternatives --remove gst-install-plugins-helper %{_libexecdir}/pk-gstreamer-install
fi

%if 0%{?suse_version} < 1330
%post gtk3-module
%glib2_gsettings_schema_post

%postun gtk3-module
%glib2_gsettings_schema_postun
%endif

%post -n libpackagekit-glib2-18 -p /sbin/ldconfig
%postun -n libpackagekit-glib2-18 -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%license COPYING
%doc AUTHORS HACKING NEWS README policy/org.freedesktop.packagekit.rules
%dir %{_sysconfdir}/PackageKit
%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_datadir}/PackageKit/helpers/test_spawn
%dir %{_libdir}/packagekit-backend
%dir %{_usr}/lib/tmpfiles.d
%{_datadir}/bash-completion/completions/pkcon
%if 0%{suse_version} < 1500
%{_sysconfdir}/cron.daily/packagekit-background.cron
%endif
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.PackageKit.conf
%if %{BUILD_CNF}
%{_sysconfdir}/profile.d/PackageKit.sh
%endif
%if 0%{suse_version} < 1500
%{_fillupdir}/sysconfig.packagekit-background
%endif
%{_bindir}/pkcon
%{_bindir}/pkmon
%{_libdir}/packagekit-backend/libpk_backend_dummy.so
%{_libexecdir}/packagekitd
%{_libexecdir}/packagekit-direct
%if %{BUILD_CNF}
%{_libexecdir}/pk-command-not-found
%endif
%{_datadir}/dbus-1/interfaces/org.freedesktop.PackageKit.Transaction.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.PackageKit.xml
%{_datadir}/PackageKit/helpers/test_spawn/search-name.sh
%{_datadir}/PackageKit/pk-upgrade-distro.sh
%if 0%{suse_version} >= 1500
%{_datadir}/PackageKit/packagekit-background.sh
%endif
%verify(not md5 size mtime) %{_datadir}/PackageKit/transactions.db
%{_datadir}/polkit-1/actions/org.freedesktop.packagekit.policy
%{_datadir}/dbus-1/system-services/*
%{_unitdir}/packagekit.service
%if 0%{suse_version} >= 1500
%{_unitdir}/packagekit-background.service
%{_unitdir}/packagekit-background.timer
%endif
%{_sbindir}/rcpackagekit
%{_mandir}/man?/*%{ext_man}
%{_tmpfilesdir}/PackageKit.conf
%if %{with offline_updates}
%{_libexecdir}/pk-offline-update
%{_unitdir}/packagekit-offline-update.service
%dir %{_unitdir}/system-update.target.wants
%{_unitdir}/system-update.target.wants/packagekit-offline-update.service
%{_sbindir}/rcpackagekit-offline-update
%endif
%ghost %dir %{_localstatedir}/lib/PackageKit
%ghost %dir %{_localstatedir}/cache/PackageKit
%ghost %{_localstatedir}/lib/PackageKit/transactions.db

%files backend-zypp
%{_libdir}/packagekit-backend/libpk_backend_zypp.so

%files gstreamer-plugin
%ghost %{_sysconfdir}/alternatives/gst-install-plugins-helper
%{_libexecdir}/gst-install-plugins-helper
%{_libexecdir}/pk-gstreamer-install

%files gtk3-module
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/pk-gtk-module.desktop
%{_libdir}/gtk-3.0/modules/*

%files devel
%doc %{_datadir}/gtk-doc/html/PackageKit
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/packagekit-glib2.vapi
# Test backends are not useful, except for developers
%{_libdir}/packagekit-backend/libpk_backend_test_fail.so
%{_libdir}/packagekit-backend/libpk_backend_test_nop.so
%{_libdir}/packagekit-backend/libpk_backend_test_spawn.so
%{_libdir}/packagekit-backend/libpk_backend_test_succeed.so
%{_libdir}/packagekit-backend/libpk_backend_test_thread.so
%dir %{_includedir}/PackageKit

%files -n libpackagekit-glib2-18
%license lib/packagekit-glib2/COPYING
%{_libdir}/libpackagekit-glib2.so.*

%files -n typelib-1_0-PackageKitGlib-1_0
%{_libdir}/girepository-1.0/PackageKitGlib-1.0.typelib

%files -n libpackagekit-glib2-devel
%{_libdir}/libpackagekit-glib2.so
%{_libdir}/pkgconfig/packagekit-glib2.pc
%dir %{_includedir}/PackageKit
%{_includedir}/PackageKit/packagekit-glib2/
%{_datadir}/gir-1.0/PackageKitGlib-1.0.gir

%files branding-upstream
%if %{BUILD_CNF}
%config(noreplace) %{_sysconfdir}/PackageKit/CommandNotFound.conf
%endif
%config(noreplace) %{_sysconfdir}/PackageKit/PackageKit.conf
# This file should not be touched by users/admins, so we can replace it
%{_sysconfdir}/PackageKit/Vendor.conf

%changelog
