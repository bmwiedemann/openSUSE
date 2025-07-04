#
# spec file for package xfce4-systemload-plugin
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


%define xfce_version 4.16.0
%define plugin systemload
Name:           xfce4-%{plugin}-plugin
Version:        1.4.0
Release:        0
Summary:        System Load Monitoring Plugin for the Xfce Panel
License:        BSD-2-Clause
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-systemload-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.4/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.19.7
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libgtop-2.0) >= 2.32.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.2
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfce_version}
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
Requires:       xfce4-panel >= %{xfce_version}
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Systemload plugin can display the current CPU load, used memory and swap
space as well as the system uptime in the panel.

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
%autosetup

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libsystemload.so
%{_datadir}/xfce4/panel/plugins/systemload.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.systemload.*

%files lang -f %{name}.lang

%changelog
