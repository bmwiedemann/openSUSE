#
# spec file for package xfce4-calculator-plugin
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
%define plugin calculator
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        0.7.0
Release:        100
Summary:        Calculator plugin for the Xfce4 panel
License:        GPL-2.0-only
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-calculator-plugin
Source:         https://archive.xfce.org/src/panel-plugins/%{name}/0.7/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Recommends:     %{name}-lang = %{version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
xfce4-calculator-plugin is a calculator plugin for the Xfce4 panel.

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

%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README
%{_libdir}/xfce4/panel/plugins/libcalculator.la
%{_libdir}/xfce4/panel/plugins/libcalculator.so
%{_datadir}/icons/hicolor/*
%{_datadir}/xfce4/panel/plugins/calculator.desktop

%files lang -f %{name}.lang

%changelog
