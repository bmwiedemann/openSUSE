#
# spec file for package xfce4-stopwatch-plugin
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


%bcond_with git
%define panel_version 4.13.0
%define plugin stopwatch

Name:           xfce4-%{plugin}-plugin
Version:        0.4.0
Release:        0
Summary:        A panel plugin to keep track of elapsed time
License:        BSD-2-Clause
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-stopwatch-plugin
Source:         https://archive.xfce.org/src/panel-plugins/%{name}/0.4/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}

%description
A panel plugin to keep track of elapsed time

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
# setting libexecdir = libdir as workaround for bxo#15608
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --disable-static
%else
%configure \
    --disable-static
%endif

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libstopwatch.la

%files
%license COPYING
%doc README.md NEWS AUTHORS
%{_libdir}/xfce4/panel/plugins/libstopwatch.{so,so.0,so.0.0.0}
%{_datadir}/xfce4/panel/plugins/xfce4-stopwatch-plugin.desktop
%{_datadir}/icons/hicolor/*/apps/xfce4-stopwatch-plugin.*

%files lang -f %{name}.lang

%changelog
