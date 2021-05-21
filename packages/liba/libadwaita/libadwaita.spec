#
# spec file for package libadwaita
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libadwaita
Version:        1.1.0~20210512
Release:        0
Summary:        Adwaita library for mobile device UIs using GTK/GNOME
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/libadwaita
Source:        %{name}-%{version}.tar.xz
BuildRequires:  vala sassc meson
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%lang_package

%description
The aim of the Adwaita library is to help with developing UI for mobile devices using GTK/GNOME.

%package -n libadwaita-1-0
Summary:        Adwaita library for mobile device UIs using GTK/GNOME
# Make the -lang package installable
Provides:        %{name} = %{version}

%description -n libadwaita-1-0
The aim of the Adwaita library is to help with developing UI for mobile devices using GTK/GNOME.

%package devel
Summary:        Development files for the Adwaita library
Requires:       libadwaita-1-0 = %{version}

%description devel
The aim of the Adwaita library is to help with developing UI for mobile devices using GTK/GNOME.

%prep
%setup -q

%build
%meson \
  -Dexamples=false \
  -Dintrospection=disabled
%meson_build

%install
%meson_install
%find_lang %{name}

%{ldconfig_scriptlets -n libadwaita-1-0}

%files lang -f %{name}.lang

%files -n libadwaita-1-0
%license COPYING
%doc README.md
%{_libdir}/libadwaita-1.so.0

%files devel
%{_includedir}/libadwaita-1/
%{_libdir}/libadwaita-1.so
%{_libdir}/pkgconfig/libadwaita-1.pc














%changelog
