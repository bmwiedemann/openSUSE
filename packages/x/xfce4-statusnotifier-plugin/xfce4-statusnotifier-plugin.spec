#
# spec file for package xfce4-statusnotifier-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 B1 Systems GmbH, Vohburg, Germany.
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
%define plugin statusnotifier
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.2.1
Release:        100
Summary:        Status Notifier Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            http://goodies.xfce.org/projects/panel-plugins/%{name}
Source0:        http://archive.xfce.org/src/panel-plugins/%{name}/0.2/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4) >= 16.04.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.24.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.0
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
This plugin provides a panel area for status notifier items (application indicators).
This technology is a modern alternative to systray.

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
%configure --disable-static
%endif
%make_build

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libstatusnotifier.la

%find_lang %{name} %{name}.lang %{?no_lang_C}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/libstatusnotifier.so
%{_datadir}/xfce4/panel/plugins/%{plugin}.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-%{plugin}-plugin.*

%files lang -f %{name}.lang

%changelog
