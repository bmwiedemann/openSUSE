#
# spec file for package xfce4-pulseaudio-plugin
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015 Guido Berhoerster.
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


%define panel_version 4.16.0
%define plugin pulseaudio
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.5.0
Release:        0
Summary:        Pulseaudio Volume Control Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://docs.xfce.org/apps/pulseaudio-plugin/start
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.5/%{name}-%{version}.tar.xz
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.19
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4windowing-0) >= 4.19.6
BuildRequires:  pkgconfig(libxfconf-0) >= %{panel_version}
# optional requirements
BuildRequires:  pkgconfig(keybinder-3.0) >= 0.2.2
BuildRequires:  pkgconfig(libcanberra) >= 0.30
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.20
%if 0%{?sle_version} && 0%{?sle_version} < 150300
Requires:       pulseaudio
%else
Requires:       pulseaudio-daemon
%endif
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
Recommends:     pavucontrol
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
Xfce4-pulseaudio-plugin is a panel plugin for controlling an audio
output volume of the PulseAudio mixer. The volume can be adjusted using
keyboard shortcuts, mouse wheel, a slider in a popup menu, or via
a linked external audio mixer tool.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
Supplements:    %{name}
# package was renamed in 2019 after Leap 15.1
Obsoletes:      xfce4-panel-plugin-%{plugin}-lang < %{version}-%{release}
Provides:       xfce4-panel-plugin-%{plugin}-lang = %{version}-%{release}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.la

%find_lang %{name} %{?no_lang_C}

%files
%doc README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_datadir}/xfce4/panel/plugins/pulseaudio.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/status/*

%files lang -f %{name}.lang

%changelog
