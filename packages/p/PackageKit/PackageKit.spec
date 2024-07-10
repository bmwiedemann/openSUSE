#
# spec file for package PackageKit
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


%if 0%{?sle_version} && 0%{?sle_version} < 160000
%bcond_with offline_updates
%else
%bcond_without offline_updates
%endif

# Only make DNF backend available openSUSE Leap 15.1+
%if 0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550
%bcond_without dnf
%bcond_with cnf
%else
%bcond_with dnf
%bcond_with cnf
%endif

Name:           PackageKit
Version:        1.2.8
Release:        0
Summary:        Simple software installation management software
License:        GPL-2.0-or-later
Group:          System/Daemons
URL:            https://www.freedesktop.org/software/PackageKit
Source0:        %{url}/releases/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/%{name}-%{version}.tar.xz.asc
Source3:        PackageKit.tmpfiles
Source99:       PackageKit.keyring

# PATCH-FEATURE-OPENSUSE PackageKit-systemd-timers.patch bsc#1115410 sckang@suse.com -- Migrate from cron to systemd timers
Patch1:         PackageKit-systemd-timers.patch
# PATCH-FIX-OPENSUSE PackageKit-remove-polkit-rules.patch bsc#1125434 sckang@suse.com -- Remove polkit rules file
Patch2:         PackageKit-remove-polkit-rules.patch
# PATCH-FIX-OPENSUSE PackageKit-dnf-Add-support-for-AppStream-repodata-basenames-use.patch ngompa13@gmail.com -- Band-aid to deal with OBS producing differently named appstream repodata files
Patch3:         PackageKit-dnf-Add-support-for-AppStream-repodata-basenames-use.patch
# PATCH-FIX-UPSTREAM PackageKit-fix-crash-pre-dbus.patch gh#hughsie/PackageKit!436 -- Do not crash when calling pk_dbus_get_uid() before D-Bus is  setup
Patch4:         PackageKit-fix-crash-pre-dbus.patch
# PATCH-FIX-UPSTREAM PackageKit-zypp-disable-upgrade-system-in-sle.patch gh#PackageKit/PackageKit/commit/0fcd820c2 sckang@suse.com -- zypp: Disable upgrade-system support in SLE
Patch7:         PackageKit-zypp-disable-upgrade-system-in-sle.patch
# PATCH-FIX-UPSTREAM PackageKit-fix-pkcon-permission.patch gh#PackageKit/PackageKit/commit/47b7f97bc, bsc#1209138 sckang@suse.com -- trivial: Drop unnecessary x permission
Patch15:        PackageKit-fix-pkcon-permission.patch
# PATCH-FIX-UPSTREAM PackageKit-dynamic-export.patch boo#1213309 dimstar@opensuse.org -- Fix loading modules when built with glib 2.70
Patch16:        PackageKit-dynamic-export.patch

# PATCH-FIX-SLE PackageKit-find-python-3-6.patch alynx.zhou@suse.com -- Build PackageKit with Python 3.6
Patch1001:      PackageKit-find-python-3-6.patch

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
%if %{with dnf}
BuildRequires:  appstream-glib-devel
BuildRequires:  libdnf-devel >= 0.43.1
BuildRequires:  pkgconfig(appstream)
%endif
BuildRequires:  libgudev-1_0-devel
BuildRequires:  libtool
BuildRequires:  meson >= 0.50
BuildRequires:  mozilla-nspr-devel >= 4.8
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel >= 0.98
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  sqlite-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(bash-completion) >= 2.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# We really want a working backend (likely zypp)
Requires:       %{name}-backend
Requires:       %{name}-branding = %{version}
Suggests:       %{name}-backend-zypp
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
BuildRequires:  libzypp-devel >= 17.31.0
Requires:       %{name} = %{version}
Requires:       libzypp >= 17.31.0
Provides:       %{name}-backend = %{version}
Conflicts:      %{name}-backend
Supplements:    (%{name} and libzypp)

%description backend-zypp
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.

%if %{with dnf}
%package backend-dnf
Summary:        DNF backend for the PackageKit installation management software
License:        GPL-2.0-or-later
Group:          System/Daemons
Requires:       %{name} = %{version}
Provides:       %{name}-backend = %{version}
Conflicts:      %{name}-backend
Supplements:    (%{name} and dnf-data)
Recommends:     rpm-repos-openSUSE
Suggests:       PackageKit-command-not-found
# Stricter dependency to keep things sane
%requires_ge %(rpm -qf "$(readlink -f %{_libdir}/libdnf.so)")

%description backend-dnf
PackageKit is a system designed to make installing and updating
software on your computer easier.  The primary design goal is to unify
all the software graphical tools used in different distributions, and
use some of the latest technology like PolicyKit to make the process
suck less.
%endif

%if %{with cnf}
%package command-not-found
Summary:        Command Not Found using PackageKit
License:        GPL-2.0-or-later
Group:          System/Daemons
Obsoletes:      command-not-found
Provides:       command-not-found
Conflicts:      command-not-found
# zypp backend lacks full functionality for this to make sense
Conflicts:      %{name}-backend-zypp

%description command-not-found
The improved Command Not Found utility from the PackageKit utilities
suit, making it easier to install the software you need when you
need it.
%endif

%package gstreamer-plugin
Summary:        Install GStreamer codecs using PackageKit
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name} = %{version}
Supplements:    (%{name} and gstreamer-plugins-base)

%description gstreamer-plugin
The PackageKit GStreamer plugin allows any Gstreamer application to install
codecs from configured repositories using PackageKit.

%package gtk3-module
Summary:        Install fonts automatically using PackageKit
License:        GPL-2.0-or-later
Group:          System/Libraries
Recommends:     %{name} = %{version}
Supplements:    (%{name} and gtk3)
%glib2_gsettings_schema_requires

%description gtk3-module
The PackageKit GTK3+ module allows any Pango application to install
fonts from configured repositories using PackageKit.

%package devel
Summary:        Header files for development with PackageKit
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libpackagekit-glib2-devel = %{version}-%{release}

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
Supplements:    (%{name} and branding-upstream)
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
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 7 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%if 0%{?sle_version} && 0%{?sle_version} < 160000
%patch -P 1001 -p1
%endif

%build
%meson \
        -Dgtk_doc=true \
        -Dpython_backend=false \
        -Dpackaging_backend=%{?with_dnf:dnf,}zypp \
        %{?with_dnf:-Ddnf_vendor=opensuse} \
        %{!?with_cnf:-Dbash_command_not_found=false} \
        %{!?with_offline_updates:-Doffline_update=false} \
        -Dcron=false \
        -Dlocal_checkout=false \
        -Ddbus_sys=%{_datadir}/dbus-1/system.d
%meson_build

%install
%meson_install

%if %{with offline_updates}
# enable packagekit-offline-updates.service here for now, till we
# decide how to do it upstream after the meson conversion:
# https://github.com/hughsie/PackageKit/issues/401
# https://bugzilla.redhat.com/show_bug.cgi?id=1833176
mkdir -p %{buildroot}%{_unitdir}/system-update.target.wants/
ln -sf ../packagekit-offline-update.service %{buildroot}%{_unitdir}/system-update.target.wants/packagekit-offline-update.service
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
%service_add_pre packagekit-background.service packagekit-background.timer
%if %{with offline_updates}
%service_add_pre packagekit-offline-update.service
%endif

%post
%mime_database_post
%service_add_post packagekit.service
%service_add_post packagekit-background.service packagekit-background.timer
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
%service_del_preun packagekit-background.service packagekit-background.timer
%if %{with offline_updates}
%service_del_preun packagekit-offline-update.service
%endif

%postun
%mime_database_postun
# Do not restart PackageKit on upgrade - it kills the transaction
%service_del_postun_without_restart packagekit.service
%service_del_postun_without_restart packagekit-background.service packagekit-background.timer
%if %{with offline_updates}
%service_del_postun_without_restart packagekit-offline-update.service
%endif

%post gstreamer-plugin
update-alternatives --install %{_libexecdir}/gst-install-plugins-helper gst-install-plugins-helper %{_libexecdir}/pk-gstreamer-install 10

%postun gstreamer-plugin
# Note: we don't use "$1 -eq 0", to avoid issues if the package gets renamed
if [ ! -f %{_libexecdir}/pk-gstreamer-install ]; then
  update-alternatives --remove gst-install-plugins-helper %{_libexecdir}/pk-gstreamer-install
fi

%post -n libpackagekit-glib2-18 -p /sbin/ldconfig
%postun -n libpackagekit-glib2-18 -p /sbin/ldconfig

%files lang -f %{name}.lang

%files
%license COPYING
%doc AUTHORS HACKING NEWS README policy/org.freedesktop.packagekit.rules
%dir %{_sysconfdir}/PackageKit
%dir %{_datadir}/PackageKit
%dir %{_datadir}/PackageKit/helpers
%dir %{_libdir}/packagekit-backend
%dir %{_usr}/lib/tmpfiles.d
%{_datadir}/bash-completion/completions/pkcon
%{_datadir}/dbus-1/system.d/org.freedesktop.PackageKit.conf
%{_bindir}/pkcon
%{_bindir}/pkmon
%{_libdir}/packagekit-backend/libpk_backend_dummy.so
%{_libexecdir}/packagekitd
%{_libexecdir}/packagekit-direct
%{_datadir}/dbus-1/interfaces/org.freedesktop.PackageKit.Transaction.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.PackageKit.xml
%{_datadir}/PackageKit/pk-upgrade-distro.sh
%{_datadir}/PackageKit/packagekit-background.sh
%verify(not md5 size mtime) %{_datadir}/PackageKit/transactions.db
%{_datadir}/polkit-1/actions/org.freedesktop.packagekit.policy
%{_datadir}/dbus-1/system-services/*
%{_datadir}/metainfo/org.freedesktop.packagekit.metainfo.xml
%{_unitdir}/packagekit.service
%{_unitdir}/packagekit-background.service
%{_unitdir}/packagekit-background.timer
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

%if %{with dnf}
%files backend-dnf
%{_libdir}/packagekit-backend/libpk_backend_dnf.so
%{_libexecdir}/packagekit-dnf-refresh-repo
%{python3_sitelib}/dnf-plugins/
%endif

%if %{with cnf}
%files command-not-found
%{_sysconfdir}/profile.d/PackageKit.sh
%{_libexecdir}/pk-command-not-found
%config(noreplace) %{_sysconfdir}/PackageKit/CommandNotFound.conf
%endif

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
%dir %{_includedir}/PackageKit
# Test backends are not useful, except for developers
%{_libdir}/packagekit-backend/libpk_backend_test_fail.so
%{_libdir}/packagekit-backend/libpk_backend_test_nop.so
%{_libdir}/packagekit-backend/libpk_backend_test_spawn.so
%{_libdir}/packagekit-backend/libpk_backend_test_succeed.so
%{_libdir}/packagekit-backend/libpk_backend_test_thread.so
%dir %{_datadir}/PackageKit/helpers/test_spawn
%{_datadir}/PackageKit/helpers/test_spawn/search-name.sh

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
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/packagekit-glib2.vapi
%{_datadir}/vala/vapi/packagekit-glib2.deps

%files branding-upstream
%config(noreplace) %{_sysconfdir}/PackageKit/PackageKit.conf
# This file should not be touched by users/admins, so we can replace it
%{_sysconfdir}/PackageKit/Vendor.conf

%changelog
