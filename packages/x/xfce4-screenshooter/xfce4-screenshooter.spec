#
# spec file for package xfce4-screenshooter
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2010 Guido Berhoerster.
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


%define xfce_version 4.18.0
%define plugin screenshooter

Name:           xfce4-screenshooter
Version:        1.11.3
Release:        0
Summary:        Screenshot Tool for the Xfce Desktop
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://goodies.xfce.org/projects/applications/xfce4-screenshooter
Source0:        https://archive.xfce.org/src/apps/xfce4-screenshooter/1.11/%{name}-%{version}.tar.xz
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  help2man
BuildRequires:  meson >= 0.56.0
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(exo-2) >= %{xfce_version}
BuildRequires:  pkgconfig(gdk-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.24.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{xfce_version}
BuildRequires:  pkgconfig(libxfconf-0) >= %{xfce_version}
BuildRequires:  pkgconfig(pango) >= 1.44.0
# We only want wayland on TW and Leap 16
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(gdk-wayland-3.0) >= 3.24.0
BuildRequires:  pkgconfig(wayland-client) >= 1.20
BuildRequires:  pkgconfig(wayland-protocols) >= 1.37
BuildRequires:  pkgconfig(wayland-scanner) >= 1.20
%endif
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xext) >= 1.0.0
BuildRequires:  pkgconfig(xfixes) >= 4.0.0
BuildRequires:  pkgconfig(xi) >= 1.7.8
Recommends:     %{name}-lang = %{version}-%{release}
# needs xfhelp4
Requires:       libxfce4ui-tools
Suggests:       xfce4-%{plugin}-plugin
Obsoletes:      xfce4-screenshooter-doc <= 1.8.1
Provides:       xfce4-screenshooter-doc = %{version}
Recommends:     curl
Recommends:     jq
Recommends:     zenity

%description
Xfce4 Screenshooter is a tool for taking screenshots, it can capture the entire
screen, the active window or a selected region. Screenshots may be taken with a
user-specified delay and the resulting images can be saved to a PNG file,
copied it to the clipboard, opened with another application, or uploaded to
ZimageZ, a free online image hosting service.

%package -n xfce4-%{plugin}-plugin
Summary:        Screenshot Plugin for the Xfce Panel
Group:          System/GUI/XFCE
Requires:       xfce4-panel >= %{xfce_version}
Requires:       xfce4-screenshooter = %{version}-%{release}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description -n xfce4-%{plugin}-plugin
This package contains the xfce4-screenshooter Xfce panel plugin.

%lang_package

%prep
%autosetup -p1

%build
# We only want wayland on TW and Leap 16
%if 0%{?sle_version} == 150600 && 0%{?is_opensuse}
%meson \
	-D wayland=disabled \
	%{nil}
%else
%meson
%endif

%meson_build

%install
%meson_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libscreenshooterplugin.la

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%find_lang xfce4-screenshooter %{?no_lang_C}

%suse_update_desktop_file -r xfce4-screenshooter -G 'Screenshot Tool' Utility X-SuSE-DesktopUtility GTK

%fdupes %{buildroot}%{_datadir}

%files
%doc NEWS README.md TODO
%license COPYING
%{_bindir}/xfce4-screenshooter
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/xfce4-screenshooter.desktop
%{_datadir}/metainfo/xfce4-screenshooter.appdata.xml
%{_mandir}/man1/xfce4-screenshooter.1*

%files -n xfce4-%{plugin}-plugin
%{_libdir}/xfce4/panel/plugins/libscreenshooterplugin.so
%{_datadir}/xfce4/panel/plugins/screenshooter.desktop

%files lang -f %{name}.lang

%changelog
