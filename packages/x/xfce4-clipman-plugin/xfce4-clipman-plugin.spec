#
# spec file
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


%define panel_version 4.14.0
%define plugin clipman
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.6.3
Release:        0
Summary:        Clipboard Manager Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-clipman-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.6/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gdk-x11-3.0) >= 3.22.29
BuildRequires:  pkgconfig(gio-2.0) >= 2.60.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.60.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.29
BuildRequires:  pkgconfig(libqrencode)
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.14.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.14.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.14.0
BuildRequires:  pkgconfig(xproto) >= 7.0.0
BuildRequires:  pkgconfig(xtst) >= 1.0.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Obsoletes:      xfce4-panel-plugin-clipman-doc < 1.2.4
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo
Requires:       xfce4-panel >= %{panel_version}
# uses exo-open
Requires:       exo-tools
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-lang = %{version}

%description
This is a clipboard manager which comes with a plugin for the Xfce Panel. It
stores the X selection (primary and clipboard) contents even after an
application has quit and is able to handle text and image data. Furthermore, it
can be configured to execute arbitrary actions when the selection content
matches specific regular expressions.

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

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libclipman.la
rm -f %{buildroot}%{_libdir}/debug/usr/bin/%{name}-%{version}-0.x86_64.debug

%suse_update_desktop_file xfce4-clipman
%suse_update_desktop_file %{name}-autostart

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_datadir}/xfce4/panel/plugins/xfce4-clipman-plugin.desktop
%{_sysconfdir}/xdg/autostart/xfce4-clipman-plugin-autostart.desktop
%config %{_sysconfdir}/xdg/xfce4/panel/xfce4-clipman-actions.xml
%dir %{_sysconfdir}/xdg/xfce4/panel
%{_libdir}/xfce4/panel/plugins/libclipman.so
%{_bindir}/xfce4-clipman
%{_bindir}/xfce4-clipman-history
%{_bindir}/xfce4-clipman-settings
%{_bindir}/xfce4-popup-clipman
%{_bindir}/xfce4-popup-clipman-actions
%{_datadir}/applications/xfce4-clipman.desktop
%{_datadir}/applications/xfce4-clipman-settings.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/xfce4-clipman.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*

%files lang -f %{name}.lang

%changelog
