#
# spec file for package d-spy
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


%define libname libdspy-1
%define sover 1

Name:           d-spy
Version:        1.10.0
Release:        0
Summary:        A D-Bus explorer for GNOME
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/d-spy
Source:         %{name}-%{version}.tar.xz

# appstream-glib BR disabled until upstream fixes the metadata test
# BuildRequires: appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  c_compiler
BuildRequires:  libxml2-tools
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.68
BuildRequires:  pkgconfig(gtk4) >= 4.6
BuildRequires:  pkgconfig(libadwaita-1) >= 1.0

%description
D-Spy is a simple tool to explore D-Bus connections.

%package        -n %{libname}-%{sover}
Summary:        Shared library for %{name}

%description    -n %{libname}-%{sover}
Shared library for %{name}.

%package        devel
Summary:        Development/header files for %{name}
Requires:       %{libname}-%{sover} = %{version}
Requires:       %{name} = %{version}

%description    devel
Development/header files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%ldconfig_scriptlets -n %{libname}-%{sover}

%files
%license COPYING COPYING.lgpl3
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/metainfo/org.gnome.dspy.appdata.xml
%{_datadir}/applications/org.gnome.dspy.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dspy.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy.devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.dspy.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.dspy-symbolic.svg

%files -n %{libname}-%{sover}
%{_libdir}/%{libname}.so.*

%files devel
%{_includedir}/dspy-%{sover}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/dspy-1.pc

%files lang -f %{name}.lang

%changelog
