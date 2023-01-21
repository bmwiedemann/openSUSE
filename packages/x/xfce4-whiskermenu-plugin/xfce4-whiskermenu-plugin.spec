#
# spec file for package xfce4-whiskermenu-plugin
#
# Copyright (c) 2023 SUSE LLC
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


%define panel_version 4.12.0
%define plugin whiskermenu
Name:           xfce4-whiskermenu-plugin
Version:        2.7.2
Release:        0
Summary:        Alternate Xfce Menu
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/2.7/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exo-2) >= 0.11
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.12
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12
# BuildRequires:  xfce4-dev-tools
Recommends:     %{name}-lang
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
Whisker Menu is an alternate application launcher for Xfce. When
opened, it shows a list of applications marked as favorites.
Installed applications can be browsed by clicking on the category
buttons on the side. Whisker Menu keeps a list of most recent used
applications launched from it.

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
%cmake
%if 0%{?suse_version} <= 1500
make %{?_smp_mflags} VERBOSE=1
%else
%cmake_build
%endif

%install
%cmake_install
%find_lang xfce4-whiskermenu-plugin %{?no_lang_C}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/xfce4-popup-whiskermenu
%{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.whiskermenu.*
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_mandir}/man?/xfce4-popup-whiskermenu.*

%files lang -f xfce4-whiskermenu-plugin.lang

%changelog
