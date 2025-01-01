#
# spec file for package xfce4-mpc-plugin
#
# Copyright (c) 2024 SUSE LLC
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


%define panel_version 4.16.0
%define plugin mpc
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.5.4
Release:        0
Summary:        MPD Client Plugin for the Xfce Panel
License:        ISC
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-mpc-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/0.5/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.60.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libmpd)
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
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
The Mpc plugin is a simple Music Player Daemon client which can control
playback and show the currently playing song.

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

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libmpc.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/xfce4/panel/plugins/libmpc.so
%{_datadir}/xfce4/panel/plugins/xfce4-mpc-plugin.desktop

%files lang -f %{name}.lang

%changelog
