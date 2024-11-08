#
# spec file for package xfce4-weather-plugin
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


%bcond_with git
%define panel_version 4.14.0
%define plugin weather
Name:           xfce4-weather-plugin
Version:        0.11.3
Release:        0
Summary:        Weather Condition Monitoring Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-weather-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.11/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE 0001-relax-json-c-version.patch lower required json-c version to allow building for Leap which only has 0.13, which is enough, though.
Patch1:         0001-relax-json-c-version.patch
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.64.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.64.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.0
BuildRequires:  pkgconfig(upower-glib) >= 0.9.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# uses exo-open
Requires:       exo-tools
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Weather plugin shows short- and long-term weather forecasts.

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
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-maintainer-mode \
  --disable-static
%else
%configure --disable-static
%endif
%make_build

%install
%make_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libweather.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/libweather.so
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.weather.*
%dir %{_datadir}/xfce4/weather
%{_datadir}/xfce4/weather/*
%{_datadir}/xfce4/panel/plugins/weather.desktop

%files lang -f %{name}.lang

%changelog
