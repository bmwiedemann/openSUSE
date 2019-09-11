#
# spec file for package thunar-plugin-archive
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define plugin_name thunar-archive-plugin

Name:           thunar-plugin-archive
Url:            http://users.xfce.org/~benny/projects/thunar-archive-plugin/
Version:        0.4.0
Release:        0
Source0:        http://archive.xfce.org/src/thunar-plugins/thunar-archive-plugin/0.4/%{plugin_name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM thunar-archive-plugin-0.3.0-fix-file-roller-extract-here.patch gber@opensuse.org -- Make file-roller really extract files to the current directory to match the behavior of xarchiver
Patch0:         thunar-archive-plugin-0.3.0-fix-file-roller-extract-here.patch
Summary:        Thunar Plugin Providing Integration with Archive Managers
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  intltool
BuildRequires:  pkgconfig(exo-2) >= 0.10.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(thunarx-3)
Requires:       thunar >= 1.7.0
Recommends:     %{name}-lang = %{version}
Provides:       %{plugin_name} = %{version}
Obsoletes:      %{plugin_name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Thunar Archive Plugin allows for creating and extracting archive files
through the file context menus in the Thunar file manager using an archive
manager. It provides scripting interface that can be used to adapt it to
different archive managers.

%lang_package

%prep
%setup -q -n %{plugin_name}-%{version}
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-archive-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{plugin_name} %{?no_lang_C}

%files
%defattr(-,root,root)
%{_libdir}/thunarx-3/thunar-archive-plugin.so
%{_libexecdir}/thunar-archive-plugin
%{_datadir}/icons/*/*/*/tap-*.png

%files lang -f %{plugin_name}.lang

%changelog
