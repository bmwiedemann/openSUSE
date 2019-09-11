#
# spec file for package xfce4-panel-plugin-netload
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define panel_version 4.12.0
%define plugin_name xfce4-netload-plugin

Name:           xfce4-panel-plugin-netload
Version:        1.3.1
Release:        0
Summary:        Network Load Monitoring Plugin for the Xfce Panel
License:        GPL-2.0+
Group:          System/GUI/XFCE
Url:            http://goodies.xfce.org/projects/panel-plugins/xfce4-netload-plugin
Source0:        http://archive.xfce.org/src/panel-plugins/%{plugin_name}/1.3/%{plugin_name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM xfce4-panel-plugin-netload-fix-array-out-of-bounds.patch bxo#11328 gber@opensuse.org -- Fix an array out of bounds write
Patch0:         xfce4-panel-plugin-netload-fix-array-out-of-bounds.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Netload plugin allows to monitor the netowrk load of a given network
interface.

%lang_package

%prep
%setup -q -n %{plugin_name}-%{version}
%patch0 -p1

%build
%configure --disable-static
make %{_smp_mflags} V=1

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libnetload.la

%find_lang %{plugin_name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/xfce4/panel/plugins/libnetload.so
%{_datadir}/xfce4/panel/plugins/netload.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-netload-plugin.*

%files lang -f %{name}.lang

%changelog
