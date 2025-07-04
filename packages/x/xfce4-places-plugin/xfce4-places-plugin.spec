#
# spec file for package xfce4-places-plugin
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
%define plugin places
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.9.0
Release:        0
Summary:        Places Menu Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-places-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.9/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exo-2) >= 4.16.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.50.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4util-1.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfconf-0) >= %{panel_version}
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Places plugin provides a menu with quick access to folders,
documents, and removable media.

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
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
  --enable-maintainer-mode \
  --disable-static
%else
%meson
%endif
%meson_build

%install
%meson_install

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libplaces.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md TODO
%license COPYING
%{_bindir}/xfce4-popup-places
%{_libdir}/xfce4/panel/plugins/libplaces.so
%{_datadir}/xfce4/panel/plugins/places.desktop

%files lang -f %{name}.lang

%changelog
