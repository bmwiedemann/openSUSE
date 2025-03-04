#
# spec file for package wingpanel-indicator-keyboard
#
# Copyright (c) 2024 SUSE LLC
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


%define         appid io.elementary.wingpanel.keyboard
Name:           wingpanel-indicator-keyboard
Version:        2.4.2
Release:        0
Summary:        Wingpanel Keyboard Indicator
License:        LGPL-2.1-or-later
URL:            https://github.com/elementary/wingpanel-indicator-keyboard
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wingpanel)

%description
A keyboard indicator for Wingpanel.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang keyboard-indicator
%fdupes %{buildroot}

%files
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libkeyboard.so
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f keyboard-indicator.lang

%changelog
