#
# spec file for package thunar-archive-plugin
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


Name:           thunar-archive-plugin
Version:        0.5.3
Release:        0
URL:            https://docs.xfce.org/xfce/thunar/archive
Source0:        https://archive.xfce.org/src/thunar-plugins/%{name}/0.5/%{name}-%{version}.tar.bz2
Summary:        Thunar Plugin Providing Integration with Archive Managers
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  intltool
BuildRequires:  pkgconfig(exo-2) >= 0.10.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(thunarx-3) >= 0.4.0
Requires:       thunar >= 1.7.0
Recommends:     %{name}-lang = %{version}
Provides:       thunar-plugin-archive = %{version}
Obsoletes:      thunar-plugin-archive < %{version}

%description
The Thunar Archive Plugin allows for creating and extracting archive files
through the file context menus in the Thunar file manager using an archive
manager. It provides scripting interface that can be used to adapt it to
different archive managers.

%lang_package

%prep
%autosetup

%build
%configure --disable-static
%make_build

%install
%make_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-archive-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%{_libdir}/thunarx-3/thunar-archive-plugin.so
%{_libexecdir}/thunar-archive-plugin
%{_datadir}/icons/*/*/*/tap-*.png

%files lang -f %{name}.lang

%changelog
