#
# spec file for package xfce4-screenshooter
#
# Copyright (c) 2022 SUSE LLC
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


%define panel_version 4.14.0
%define plugin screenshooter
%bcond_with git

Name:           xfce4-screenshooter
Version:        1.10.0
Release:        0
Summary:        Screenshot Tool for the Xfce Desktop
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://goodies.xfce.org/projects/applications/xfce4-screenshooter
Source:         https://archive.xfce.org/src/apps/xfce4-screenshooter/1.10/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(exo-2) >= 0.11.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{panel_version}
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Recommends:     %{name}-lang = %{version}-%{release}
# needs xfhelp4
Requires:       libxfce4ui-tools
Suggests:       xfce4-%{plugin}-plugin
Obsoletes:      xfce4-screenshooter-doc <= 1.8.1
Provides:       xfce4-screenshooter-doc = %{version}

%description
Xfce4 Screenshooter is a tool for taking screenshots, it can capture the entire
screen, the active window or a selected region. Screenshots may be taken with a
user-specified delay and the resulting images can be saved to a PNG file,
copied it to the clipboard, opened with another application, or uploaded to
ZimageZ, a free online image hosting service.

%package -n xfce4-%{plugin}-plugin
Summary:        Screenshot Plugin for the Xfce Panel
Group:          System/GUI/XFCE
Requires:       xfce4-panel >= %{panel_version}
Requires:       xfce4-screenshooter = %{version}-%{release}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description -n xfce4-%{plugin}-plugin
This package contains the xfce4-screenshooter Xfce panel plugin.

%lang_package

%prep
%setup -q

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
