#
# spec file for package xfce4-dict
#
# Copyright (c) 2020 SUSE LLC
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
Name:           xfce4-dict
Version:        0.8.4
Release:        0
Summary:        Xfce Dictionary Client Application
License:        GPL-2.0-or-later
Group:          Productivity/Office/Dictionary
URL:            https://goodies.xfce.org/projects/applications/xfce4-dict
Source:         https://archive.xfce.org/src/apps/xfce4-dict/0.8/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.10.0
# uses xdg-open
Requires:       xdg-utils
Recommends:     %{name}-lang = %{version}
Suggests:       xfce4-panel-plugin-dict

%description
xfce4-dict allows you to search different kinds of dictionary services for
words or phrases and shows you the result. Currently you can query a Dict
server (RFC 2229), any online dictionary service by opening a web browser or
search for words using the aspell/ispell program.

%package -n xfce4-panel-plugin-dict
Summary:        Dictionary Plugin for the Xfce Panel
Group:          Productivity/Office/Dictionary
Requires:       %{name} = %{version}
Requires:       xfce4-panel >= %{panel_version}

%description -n xfce4-panel-plugin-dict
This package contains the xfce4-dict dictionary plugin for the Xfce panel.

%lang_package

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libxfce4dict.la

%suse_update_desktop_file -r %{name} Office Dictionary GTK

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/xfce4-dict
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man1/xfce4-dict.1*

%files -n xfce4-panel-plugin-dict
%{_libdir}/xfce4/panel/plugins/libxfce4dict.so
%{_datadir}/xfce4/panel/plugins/*.desktop

%files lang -f %{name}.lang

%changelog
