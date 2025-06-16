#
# spec file for package xfce4-sensors-plugin
#
# Copyright (c) 2025 SUSE LLC
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


%define panel_version 4.20.0
%define plugin sensors
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.5.0
Release:        0
Summary:        Hardware Sensor Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-sensors-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.5/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.19.8
BuildRequires:  libXNVCtrl-devel
BuildRequires:  libsensors4-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{panel_version}
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
Recommends:     hddtemp
Recommends:     netcat-openbsd
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Sensors plugin and standalone application allow to monitor various hardware
sensors supported by libsensors.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
# package was renamed in 2019 after Leap 15.1
Obsoletes:      xfce4-panel-plugin-%{plugin}-lang < %{version}-%{release}
Provides:       xfce4-panel-plugin-%{plugin}-lang = %{version}-%{release}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup -p1

%build
# gcc10 workaround
export CFLAGS="%{optflags} -fcommon"

# --enable-netcat actually enables "hddtemp via netcat"
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --disable-static \
    --enable-libsensors=yes \
    --enable-pathchecks=no \
    --enable-hddtemp \
    --with-pathhddtemp=/usr/sbin/hddtemp \
    --enable-netcat \
    --with-pathnetcat=/usr/bin/netcat \
    --enable-sysfsacpi
%else
%meson
%endif
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_libdir}/xfce4/modules/libxfce4sensors.la

%suse_update_desktop_file -r xfce4-sensors X-XFCE System Monitor

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.la

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS NOTES README TODO
%license LICENSE
%{_bindir}/xfce4-sensors
%{_libdir}/xfce4/panel/plugins/libxfce4-sensors-plugin.so
%{_datadir}/icons/hicolor/*/apps/xfce-sensors.*
%{_datadir}/applications/xfce4-sensors.desktop
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.desktop
%{_datadir}/xfce4/panel/plugins/xfce4-sensors-plugin.css
%dir %{_libdir}/xfce4
%doc %{_mandir}/man1/xfce4-sensors.1*

%files lang -f %{name}.lang

%changelog
