#
# spec file for package xfce4-diskperf-plugin
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


%define panel_version 4.16.0
%define plugin diskperf
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        2.7.1
Release:        0
Summary:        Disk Performance Plugin for the Xfce Panel
License:        BSD-2-Clause
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/panel-plugins/xfce4-diskperf-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/%{name}/2.7/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  gettext >= 0.19.8
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.16.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       xfce4-panel >= %{panel_version}
Recommends:     %{name}-lang = %{version}-%{release}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The DiskPerf plugin displays the disk/partition performance as trasferred data
per second.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}-%{release}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}-%{release}
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

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libdiskperf.so
%{_datadir}/xfce4/panel/plugins/diskperf.desktop

%files lang -f %{name}.lang

%changelog
