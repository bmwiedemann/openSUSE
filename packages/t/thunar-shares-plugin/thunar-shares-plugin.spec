#
# spec file for package thunar-shares-plugin
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


%define thunar_version 4.18

Name:           thunar-shares-plugin
Version:        0.5.0
Release:        0
URL:            https://docs.xfce.org/xfce/thunar/custom-actions
Source0:        https://archive.xfce.org/src/thunar-plugins/%{name}/0.5/%{name}-%{version}.tar.xz
Summary:        Thunar Plugin for Sharing Files Using Samba
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  gettext >= 0.19.8
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libxfconf-0) >= %{thunar_version}
BuildRequires:  pkgconfig(thunarx-3) >= %{thunar_version}
Requires:       samba
Requires:       thunar >= %{thunar_version}
Recommends:     %{name}-lang = %{version}
Provides:       thunar-plugin-shares = %{version}
Obsoletes:      thunar-plugin-shares < %{version}

%description
The Thunar Shares Plugin allows for quickly sharing a directory using Samba
from within Thunar without requiring root access.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-shares-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%{_libdir}/thunarx-3/thunar-shares-plugin.so

%files lang -f %{name}.lang

%changelog
