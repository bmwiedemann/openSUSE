#
# spec file for package wingpanel-indicator-power
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


%define         appid io.elementary.desktop.wingpanel.power
Name:           wingpanel-indicator-power
Version:        8.0.2
Release:        0
Summary:        Wingpanel Power Indicator
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/wingpanel-indicator-power
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wingpanel)

%description
A power indicator for Wingpanel.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/locale
%find_lang power-indicator

%files
%license COPYING
%doc README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libpower.so
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/io.elementary.wingpanel.power.metainfo.xml

%files lang -f power-indicator.lang

%changelog
