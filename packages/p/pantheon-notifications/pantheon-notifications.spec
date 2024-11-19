#
# spec file for package pantheon-notifications
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


%define         appid io.elementary.notifications
Name:           pantheon-notifications
Version:        8.0.0
Release:        0
Summary:        Notification Server
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/notifications
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-leap.patch
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1)
Provides:       elementary-notifications = %{version}
Obsoletes:      elementary-notifications < %{version}

%description
A Gtk notification server for Pantheon desktop.

%package        demo
Summary:        Pantheon Notification Server -- Demo binary

%description    demo
A Gtk notification server for Pantheon desktop.

This package contains a small demo app to send notifications.

%prep
%autosetup -N -n notifications-%{version}
%if 0%{?suse_version} <= 1600
%patch -P0 -p1
%endif

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml

%files demo
%{_bindir}/%{appid}.demo
%{_datadir}/applications/%{appid}.demo.desktop

%changelog
