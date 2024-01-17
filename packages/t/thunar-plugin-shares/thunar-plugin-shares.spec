#
# spec file for package thunar-plugin-shares
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


%define thunar_version 1.2.0
%define plugin_name thunar-shares-plugin

Name:           thunar-plugin-shares
Version:        0.3.2
Release:        0
URL:            https://docs.xfce.org/xfce/thunar/custom-actions
Source0:        http://archive.xfce.org/src/thunar-plugins/%{plugin_name}/0.3/%{plugin_name}-%{version}.tar.bz2
Summary:        Thunar Plugin for Sharing Files Using Samba
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(thunarx-3) >= 1.0.1
Requires:       samba
Requires:       thunar >= %{thunar_version}
Recommends:     %{name}-lang = %{version}
Provides:       %{plugin_name} = %{version}
Obsoletes:      %{plugin_name} < %{version}

%description
The Thunar Shares Plugin allows for quickly sharing a directory using Samba
from within Thunar without requiring root access.

%lang_package

%prep
%setup -q -n %{plugin_name}-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-shares-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{plugin_name} %{?no_lang_C}

%clean
rm -rf "%{buildroot}"

%files
%{_libdir}/thunarx-3/thunar-shares-plugin.so

%files lang -f %{plugin_name}.lang

%changelog
