#
# spec file for package kde-gtk-config6
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0
%define rname kde-gtk-config
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kde-gtk-config6
Version:        6.1.0
Release:        0
Summary:        Daemon for GTK2 and GTK3 Applications Appearance Under KDE
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  gsettings-desktop-schemas
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  sassc
BuildRequires:  cmake(KDecoration2) >= %{_plasma6_bugfix}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
# Needed for syncing GTK+ settings
Requires:       gsettings-desktop-schemas
Requires:       xsettingsd
Recommends:     kde-gtk-config6-gtk3
Suggests:       gtk2-metatheme-breeze
Suggests:       gtk3-metatheme-breeze
Supplements:    (plasma6-workspace and libgtk-2_0-0)
Supplements:    (plasma6-workspace and libgtk-3-0)
Provides:       kde-gtk-config5 = %{version}
Obsoletes:      kde-gtk-config5 < %{version}
Obsoletes:      kde-gtk-config5-lang < %{version}
Provides:       kde-gtk-config = %{version}
Obsoletes:      kde-gtk-config < %{version}
# Since Plasma 5.19, the gtk3 settings also apply to gtk2
# and in 5.20 the gtk2 preview got dropped.
Provides:       kde-gtk-config5-gtk2 = %{version}
Obsoletes:      kde-gtk-config5-gtk2 < %{version}

%description
kde-gtk-config is a KDED module which configures GTK2 and GTK3 applications
appearance under KDE.

%package gtk3
Summary:        GTK3 Preview Helper for the GTK Configuration
Requires:       %{name} = %{version}
Provides:       kde-gtk-config5-gtk3 = %{version}
Obsoletes:      kde-gtk-config5-gtk3 < %{version}

%description gtk3
This package contains a helper application that allows previewing
the GTK3 application style from within the application style KCM

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

# E: env-script-interpreter
sed -i 's#/usr/bin/env sh$#/usr/bin/sh#' %{buildroot}%{_kf6_sharedir}/kconf_update/remove_window_decorations_from_gtk_css.sh

%files
%license LICENSES/*
%dir %{_kf6_libdir}/gtk-3.0/
%dir %{_kf6_libdir}/gtk-3.0/modules/
%{_kf6_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_kf6_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_kf6_libdir}/kconf_update_bin/gtk_theme
%{_kf6_libdir}/kconf_update_bin/remove_deprecated_gtk4_option
%{_kf6_plugindir}/kf6/kded/gtkconfig.so
%{_kf6_sharedir}/kcm-gtk-module/
%{_kf6_sharedir}/kconf_update/gtkconfig.upd
%{_kf6_sharedir}/kconf_update/remove_window_decorations_from_gtk_css.sh

%files gtk3
%license LICENSES/*
%dir %{_kf6_sharedir}/themes/Breeze/
%{_kf6_sharedir}/themes/Breeze/window_decorations.css
%{_libexecdir}/gtk3_preview

%changelog
