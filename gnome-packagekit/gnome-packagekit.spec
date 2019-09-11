#
# spec file for package gnome-packagekit
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


# Easy switching on/off of systemd integration
%define with_systemd 1
Name:           gnome-packagekit
Version:        3.32.0
Release:        0
Summary:        Applications for the PackageKit API
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://packagekit.org/
Source0:        https://download.gnome.org/sources/gnome-packagekit/3.32/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM gnome-packagekit-displaysize.patch bgo#770640 dimstar@opensuse.org -- Never expand over 90% of the screen size,
Patch0:         gnome-packagekit-displaysize.patch
# PATCH-FEATURE-OPENSUSE -- Only show gnome-packagekit in gnome.
Patch1:         gnome-packagekit-OnlyShowIn.patch
# PATCH-FIX-SLED bnc#881245-update-test-affects-package-manager-should-restart-gpk-update-viewer.patch rlmu@suse.com -- Restart gpk-update-viewer after certain update.
Patch2:         bnc#881245-update-test-affects-package-manager-should-restart-gpk-update-viewer.patch
# PATCH-FIX-UPSTREAM bnc-946886-install-signatures-in-viewer.patch bsc#946886 mgorse@suse.com -- install signatures in gpk-update-viewer if needed
Patch3:         bnc-946886-install-signatures-in-viewer.patch
# PATCH-FIX-SLED bnc#939278-gnome-packagekit-asks-for-reboot-password-too-early.patch rlmu@suse.com -- Fixed asks for passwd too early.
Patch4:         bnc#939278-gnome-packagekit-asks-for-reboot-password-too-early.patch
#PATCH-FIX-UPSTREAM gnome-packagekit-fix-not-responding-after-update.patch bgo#782673, bsc#1036542 sckang@suse.com -- Fix gpk-update-viewer not responding after installing available updates.
Patch5:         gnome-packagekit-fix-not-responding-after-update.patch

BuildRequires:  PackageKit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils-minimal
BuildRequires:  gettext-devel
BuildRequires:  gnome-menus-devel
BuildRequires:  meson >= 0.46.0
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.3
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(packagekit-glib2) >= 0.9.1
Provides:       opensuse-updater-gnome = 0.4.7
Obsoletes:      opensuse-updater-gnome < 0.4.7
Provides:       org.freedesktop.PackageKit.service
%glib2_gsettings_schema_requires
%if %{with_systemd}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(polkit-gobject-1)
%endif

%description
GNOME PackageKit provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages on your system.

%package extras
Summary:        Extra applications for the PackageKit API
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}

%description extras
GNOME PackageKit provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages on your system.

This package contains tools that provide functionality also provided by
YaST Software Management.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file org.gnome.Packages
# gpk-install-local-file is no longer part of gpk, see boo#941862
rm %{buildroot}%{_datadir}/applications/gpk-install-local-file.desktop
#suse_update_desktop_file gpk-install-local-file
%suse_update_desktop_file gpk-log Settings
%suse_update_desktop_file gpk-prefs X-GNOME-SystemSettings
%suse_update_desktop_file org.gnome.PackageUpdater

%files
%license COPYING
%doc AUTHORS
%{_bindir}/gpk-prefs
%{_bindir}/gpk-update-viewer
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.packagekit.gschema.migrate
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.PackageUpdater.appdata.xml
# do not ship dysfunctional handler for x-rpm mime type
#{_datadir}/applications/gpk-install-local-file.desktop
%{_datadir}/applications/gpk-prefs.desktop
%{_datadir}/applications/org.gnome.PackageUpdater.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.packagekit.gschema.xml
%dir %{_datadir}/gnome-packagekit
%{_datadir}/gnome-packagekit/icons/
%{_datadir}/icons/hicolor/*/apps/gpk-*.*
%{_datadir}/icons/hicolor/*/mimetypes/application-*.*
%{_mandir}/man1/gpk-prefs.1%{?ext_man}
%{_mandir}/man1/gpk-update-viewer.1%{?ext_man}

%files lang -f %{name}.lang

%files extras
%{_bindir}/gpk-application
%{_bindir}/gpk-log
%{_datadir}/metainfo/org.gnome.Packages.appdata.xml
%{_datadir}/applications/org.gnome.Packages.desktop
%{_datadir}/applications/gpk-log.desktop
%{_mandir}/man1/gpk-application.1%{?ext_man}
%{_mandir}/man1/gpk-log.1%{?ext_man}

%changelog
