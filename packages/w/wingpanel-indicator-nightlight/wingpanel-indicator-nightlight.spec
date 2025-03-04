#
# spec file for package wingpanel-indicator-nightlight
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


%define         appid io.elementary.wingpanel.nightlight
Name:           wingpanel-indicator-nightlight
Version:        2.1.3
Release:        0
Summary:        Wingpanel Nightlight Indicator
License:        GPL-2.0-or-later
URL:            https://github.com/elementary/wingpanel-indicator-nightlight
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(wingpanel)

%description
A Wingpanel indicator for Night Light.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%find_lang nightlight-indicator
%fdupes %{buildroot}

%files
%doc COPYING README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libnightlight.so
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files lang -f nightlight-indicator.lang

%changelog
