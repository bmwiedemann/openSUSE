#
# spec file for package xfce4-panel-plugin-indicator
#
# Copyright (c) 2022 SUSE LLC
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


%define _name   xfce4-indicator-plugin
%define _version 2.4
Name:           xfce4-panel-plugin-indicator
Version:        2.4.1
Release:        0
Summary:        Plugin to display information from applications in the Xfce panel
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://docs.xfce.org/panel-plugins/xfce4-indicator-plugin
Source:         https://archive.xfce.org/src/panel-plugins/%{_name}/%{_version}/%{_name}-%{version}.tar.bz2
# PATCH-FEATURE-OPENSUSE xfce4-indicator-plugin-ayatana-indicator.patch -- Use Ayatana Indicators instead of Ubuntu ones.
Patch0:         xfce4-indicator-plugin-ayatana-indicator.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  xfce4-dev-tools
BuildRequires:  xfce4-panel-devel >= 4.11.0
BuildRequires:  pkgconfig(ayatana-indicator3-0.4) >= 0.6.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(libayatana-ido3-0.4) >= 0.4.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.11.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.9.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.6.0
Requires:       xfce4-panel >= 4.11.0
Provides:       ayatana-indicator-renderer
%lang_package

%description
A small plugin to display information from various applications
consistently in the Xfce panel as described in
Ubuntu's MessagingMenu design specification.

%prep
%autosetup -n %{_name}-%{version} -p1

%build
xdt-autogen
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}

%files
%license COPYING*
%doc AUTHORS NEWS README.md
%{_libdir}/xfce4/panel/plugins/libindicator-plugin.so
%{_datadir}/xfce4/panel/plugins/indicator.desktop
%{_datadir}/icons/hicolor/*/apps/%{_name}.*

%files lang -f %{_name}.lang

%changelog
