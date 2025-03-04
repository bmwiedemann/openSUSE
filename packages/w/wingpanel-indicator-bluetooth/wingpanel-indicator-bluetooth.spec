#
# spec file for package wingpanel-indicator-bluetooth
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


%define         appid io.elementary.desktop.wingpanel.bluetooth
Name:           wingpanel-indicator-bluetooth
Version:        8.0.0
Release:        0
Summary:        Wingpanel Bluetooth Indicator
License:        LGPL-2.1-or-later
URL:            https://github.com/elementary/wingpanel-indicator-bluetooth
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(wingpanel)

%description
A bluetooth indicator for Wingpanel.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang bluetooth-indicator
%fdupes %{buildroot}

%files
%license COPYING
%doc README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libbluetooth.so
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/io.elementary.wingpanel.bluetooth.metainfo.xml

%files lang -f bluetooth-indicator.lang

%changelog
