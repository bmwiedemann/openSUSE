#
# spec file for package xfce4-fsguard-plugin
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


%define panel_version 4.14.0
%define plugin fsguard
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.1.2
Release:        0
Summary:        Filesystem Space Monitoring Plugin for the Xfce Panel
License:        BSD-2-Clause
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-fsguard-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.1/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# uses exo-open
Requires:       exo-tools
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The FSGuard plugin constantly monitors free space of a given mountpoint and
displays it as an icon in the panel.

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

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libfsguard.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libfsguard.so
%{_datadir}/xfce4/panel/plugins/fsguard.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-fsguard-plugin*

%files lang -f %{name}.lang

%changelog
