#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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
%define plugin cpugraph
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.2.7
Release:        0
Summary:        CPU Graph Plugin for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-cpugraph-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/1.2/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.2
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
The CPU Graph plugin diplays a customizable graph of the CPU load of either
a specific CPU or all CPUs combined.

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

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libcpugraph.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS ChangeLog NEWS README.md
%{!?with_git:%doc AUTHORS NEWS README.md}
%license COPYING
%{_libdir}/xfce4/panel/plugins/libcpugraph.so
%{_datadir}/xfce4/panel/plugins/cpugraph.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.panel.cpugraph.*

%files lang -f %{name}.lang

%changelog
