#
# spec file for package wingpanel-indicator-a11y
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


%define         appid io.elementary.wingpanel.a11y
Name:           wingpanel-indicator-a11y
Version:        1.0.2
Release:        0
License:        GPL-2.0-or-later
Summary:        Wingpanel Accessibility Indicator
URL:            https://github.com/elementary/wingpanel-indicator-a11y
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  vala
BuildRequires:  meson
BuildRequires:  pkgconfig(granite)
BuildRequires:  cmake
BuildRequires:  pkgconfig(wingpanel)

%description
An accessibility indicator for the Pantheon greeter.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang a11y-indicator

%files
%license COPYING
%doc README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/liba11y.so
%{_datadir}/glib-2.0/schemas/io.elementary.desktop.wingpanel.a11y.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f a11y-indicator.lang

%changelog
