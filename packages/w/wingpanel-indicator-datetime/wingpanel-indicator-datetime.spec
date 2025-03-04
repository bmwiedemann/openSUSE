#
# spec file for package wingpanel-indicator-datetime
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


%define         appid io.elementary.desktop.wingpanel.datetime
Name:           wingpanel-indicator-datetime
Version:        2.4.2
Release:        0
Summary:        Wingpanel Date & Time Indicator
License:        GPL-2.0-or-later
URL:            https://github.com/elementary/wingpanel-indicator-datetime
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(wingpanel)

%description
A date and time indicator for Wingpanel.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}
%find_lang datetime-indicator

%files
%license COPYING
%doc README.md
%dir %{_libdir}/wingpanel
%{_libdir}/wingpanel/libdatetime.so
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/metainfo/io.elementary.wingpanel.datetime.metainfo.xml

%files lang -f datetime-indicator.lang

%changelog
