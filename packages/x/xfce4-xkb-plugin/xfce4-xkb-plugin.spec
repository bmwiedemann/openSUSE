#
# spec file for package xfce4-xkb-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%define plugin xkb
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.8.1
Release:        100
Summary:        XKB Layout Switcher Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-xkb-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.8/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE xfce4-xkb-plugin-0.8.0-downgrade-libxklavier-requirement.diff -- xklavier-5.3 is good enough -- seife
Patch0:         xfce4-xkb-plugin-0.8.0-downgrade-libxklavier-requirement.diff
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(garcon-1) >= 0.4.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.1
BuildRequires:  pkgconfig(libxklavier) >= 5.3
BuildRequires:  pkgconfig(pango)
Requires:       xfce4-panel >= %{panel_version}
Requires:       xfce4-settings >= 4.11.0
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The XKB plugin allows to setup and switch between multiple XKB keyboard
layouts.

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

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/*.la
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/libxkb.so
%{_datadir}/xfce4/panel/plugins/xkb.desktop
%dir %{_datadir}/xfce4/xkb
%{_datadir}/xfce4/xkb/*

%files lang -f %{name}.lang

%changelog
