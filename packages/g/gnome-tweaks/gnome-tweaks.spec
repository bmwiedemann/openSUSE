#
# spec file for package gnome-tweaks
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Luis Medinas, Lisbon, Portugal.
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


Name:           gnome-tweaks
Version:        3.34.0
Release:        0
Summary:        A tool to customize advanced GNOME 3 options
License:        GPL-3.0-or-later AND CC0-1.0
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Tweaks
Source0:        https://download.gnome.org/sources/gnome-tweaks/3.34/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-tweaks-fix-titlebar-buttons-left.patch bsc#1162080, glgo#GNOME/gnome-tweaks#245 alynx.zhou@suse.com -- Fix titlebar flicker after setting buttons placement to left
Patch1:         gnome-tweaks-fix-titlebar-buttons-left.patch
# PATCH-FEATURE-UPSTREAM gnome-tweaks-port-libhandy-1.patch -- Port to libhandy-1
Patch2:         gnome-tweaks-port-libhandy-1.patch

BuildRequires:  fdupes
# GI is needed to have typelib() Requires
BuildRequires:  gobject-introspection
# Hicolor is Needed for directory ownership
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
Requires:       gnome-settings-daemon
# Gsettings Schemas are needed from: gnome-shell, g-d-s and mutter
Requires:       gnome-shell >= 3.24
Requires:       gsettings-desktop-schemas >= 3.27.90
Requires:       mutter
Requires:       python3-gobject >= 3.10
Requires:       python3-gobject-Gdk
Requires:       python3-xml
# Gnome-tweak-tool was renamed to gnome-tweaks in 3.27.4
Provides:       gnome-tweak-tool = %{version}
Obsoletes:      gnome-tweak-tool < 3.27.4
Obsoletes:      gnome-tweak-tool-lang < 3.27.4
BuildArch:      noarch

%description
GNOME Tweak Tool is an application for changing the advanced settings
of GNOME 3.

%lang_package

%prep
%autosetup -p1
translation-update-upstream
# Tiny tweak to shut up rpmlint
sed -i 's:Pantheon:X-Pantheon:g' */org.gnome.tweaks.desktop.in
# Tweak to fix python env
sed -i "s|#!%{_bindir}/env python3|#!%{_bindir}/python3|g" gnome-tweak*

%build
%meson
%meson_build

%install
%meson_install
# FIXME Drop traces of buildroot
rm -rf %{buildroot}/%{python3_sitelib}/gtweak/__pycache__/*.pyc
rm -rf %{buildroot}/%{python3_sitelib}/gtweak/tweaks/__pycache__/*.pyc
%fdupes %{buildroot}%{_datadir}/gnome-tweaks/
%fdupes %{buildroot}%{python_sitelib}
%find_lang %{name} %{?no_lang_C}

%files
%license LICENSES/*
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{python3_sitelib}/gtweak/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.tweaks.appdata.xml
%{_datadir}/applications/org.gnome.tweaks.desktop
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.tweak*
%{_libexecdir}/gnome-tweak-tool-lid-inhibitor

%files lang -f %{name}.lang

%changelog
