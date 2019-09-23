#
# spec file for package xfce4-pulseaudio-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define panel_version 4.11.0
%define plugin pulseaudio
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.4.2
Release:        0
Summary:        Pulseaudio Volume Control Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-pulseaudio-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.4/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exo-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libpulse-mainloop-glib) >= 0.9.19
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.11.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.11.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.9.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.6.0
# optional requirements
BuildRequires:  pkgconfig(gio-2.0) >= 2.42
BuildRequires:  pkgconfig(keybinder-3.0) >= 0.2.2
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.20
Requires:       pulseaudio
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
Summary:       Translations for package %{name} 
Group:         System/Localization 
Requires:      %{name} = %{version} 
Provides:      %{name}-lang-all = %{version}
Supplements:   %{name} 
# package was renamed in 2019 after Leap 15.1
Obsoletes:     xfce4-panel-plugin-%{plugin}-lang < %{version}-%{release}
Provides:      xfce4-panel-plugin-%{plugin}-lang = %{version}-%{release}
BuildArch:     noarch 

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.la

%find_lang %{name} %{?no_lang_C}

%files
%doc ChangeLog README
%license COPYING
%{_libdir}/xfce4/panel/plugins/libpulseaudio-plugin.so
%{_datadir}/xfce4/panel/plugins/pulseaudio.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/hicolor/*/status/*

%files lang -f %{name}.lang

%changelog
