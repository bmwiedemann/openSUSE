#
# spec file for package pantheon-quick-settings
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


%define         appid io.elementary.quick-settings
Name:           pantheon-quick-settings
Version:        1.1.0
Release:        0
Summary:        Access frequently used settings and system actions
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/quick-settings
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/elementary/quick-settings/pull/91.patch#/fix-uint.patch
BuildRequires:  accountsservice-vala
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite) >= 6.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.0
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wingpanel)

%description
%{summary}.

%lang_package

%prep
%autosetup -p1 -n quick-settings-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{appid}
%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_libdir}/wingpanel/libquick-settings.so
%{_datadir}/glib-2.0/schemas/quick-settings.gschema.xml
%{_datadir}/metainfo/%{appid}.metainfo.xml
%dir %{_libdir}/wingpanel

%files lang -f %{appid}.lang

%changelog
