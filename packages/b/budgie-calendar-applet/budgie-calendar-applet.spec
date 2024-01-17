#
# spec file for package budgie-calendar-applet
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

%define appid com.github.danielpinto8zz6.budgie-calendar-applet
Name:           budgie-calendar-applet
Version:        5.2
Release:        0
Summary:        Calendar applet for Budgie Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/danielpinto8zz6/budgie-calendar-applet
Source:         https://github.com/danielpinto8zz6/budgie-calendar-applet/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(budgie-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A budgie-desktop applet to show hours and when click show a calendar in a popover.

%lang_package

%prep
%setup -q

%build
%meson
%meson_build

%install
export LANG=en_US.UTF-8
%meson_install
mv %{buildroot}%{_datadir}/appdata %{buildroot}%{_datadir}/metainfo
%find_lang %{appid}

%files
%license LICENSE
%doc README.md
%{_libdir}/budgie-desktop/plugins/%{appid}/
%{_datadir}/metainfo/%{appid}.appdata.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

%files lang -f %{appid}.lang

%changelog
