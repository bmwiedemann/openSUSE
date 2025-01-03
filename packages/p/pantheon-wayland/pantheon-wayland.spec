#
# spec file for package pantheon-wayland
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


%define         sover 1
Name:           pantheon-wayland
Version:        1.0.0
Release:        0
Summary:        Wayland integration library to the Pantheon Desktop
License:        LGPL-3.0-or-later
URL:            https://github.com/elementary/pantheon-wayland
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         fix-version.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(wayland-client)

%description
Pantheon Wayland is an utility library made exclusively for the Pantheon Desktop utilities.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-PantheonWayland-%{sover}_0 = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-PantheonWayland-%{sover}_0
Summary:        Typelib for %{name}

%description -n typelib-1_0-PantheonWayland-%{sover}_0
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license COPYING
%doc README.md
%{_includedir}/%{name}-%{sover}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}-%{sover}.pc
%{_datadir}/gir-1.0/PantheonWayland-%{sover}.gir
%{_datadir}/vala/vapi/%{name}-%{sover}.{deps,vapi}
%dir %{_datadir}/{vala,vala/vapi}

%files -n lib%{name}%{sover}
%license COPYING
%doc README.md
%{_libdir}/lib%{name}.so.*

%files -n typelib-1_0-PantheonWayland-%{sover}_0
%{_libdir}/girepository-1.0/PantheonWayland-%{sover}.typelib

%changelog
