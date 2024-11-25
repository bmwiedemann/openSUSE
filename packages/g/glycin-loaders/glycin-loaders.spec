#
# spec file for package glycin-loaders
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


%bcond_without jxl

Name:           glycin-loaders
Version:        1.1.2
Release:        0
Summary:        Sandboxed image rendering
License:        LGPL-2.1-or-later OR MPL-2.0
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst

BuildRequires:  cargo-packaging
BuildRequires:  clang
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig
%if %{with jxl}
BuildRequires:  (pkgconfig(libjxl) >= 0.8.2 with pkgconfig(libjxl) < 0.13.0)
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.12.0
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libheif) >= 1.17.4
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libseccomp) >= 2.5.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(vapigen)

%description
Sandboxed and extendable image decoding.

%package -n libglycin-1-0
Summary:        Shared library for %{name}

%description -n libglycin-1-0
Sandboxed and extendable image decoding.

This package provides the shared library for %{name}

%package -n libglycin-gtk4-1-0
Summary:        Shared library for %{name}

%description -n libglycin-gtk4-1-0
Sandboxed and extendable image decoding.

This package provides the shared library for %{name}

%package -n typelib-1_0-Gly_1
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-Gly_1
Sandboxed and extendable image decoding.

This package provides introspection bindings for %{name}

%package -n typelib-1_0-GlyGtk4_1
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-GlyGtk4_1
Sandboxed and extendable image decoding.

This package provides introspection bindings for %{name}

%package devel
Summary:        Development Files for %{name}
Requires:       libglycin-1-0 = %{version}
Requires:       libglycin-gtk4-1-0 = %{version}
Requires:       typelib-1_0-GlyGtk4_1 = %{version}
Requires:       typelib-1_0-Gly_1 = %{version}

%description devel
Sandboxed and extendable image decoding.

This package provides developments files for %{name}

%prep
%autosetup -p1 -a1

%build
%meson \
	-Dloaders=glycin-heif,glycin-image-rs,glycin-svg%[%{with jxl}?",glycin-jxl":""] \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libglycin-1-0
%ldconfig_scriptlets -n libglycin-gtk4-1-0

%files
%dir %{_libexecdir}/glycin-loaders
%dir %{_libexecdir}/glycin-loaders/1+
%{_libexecdir}/glycin-loaders/1+/glycin-heif
%{_libexecdir}/glycin-loaders/1+/glycin-image-rs
%{_libexecdir}/glycin-loaders/1+/glycin-svg
%dir %{_datadir}/glycin-loaders
%dir %{_datadir}/glycin-loaders/1+
%dir %{_datadir}/glycin-loaders/1+/conf.d
%{_datadir}/glycin-loaders/1+/conf.d/glycin-heif.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-image-rs.conf
%{_datadir}/glycin-loaders/1+/conf.d/glycin-svg.conf
%if %{with jxl}
%{_libexecdir}/glycin-loaders/1+/glycin-jxl
%{_datadir}/glycin-loaders/1+/conf.d/glycin-jxl.conf
%endif

%files -n libglycin-1-0
%{_libdir}/libglycin-1.so.0

%files -n libglycin-gtk4-1-0
%{_libdir}/libglycin-gtk4-1.so.0

%files -n typelib-1_0-Gly_1
%{_libdir}/girepository-1.0/Gly-1.typelib

%files -n typelib-1_0-GlyGtk4_1
%{_libdir}/girepository-1.0/GlyGtk4-1.typelib

%files devel
%dir %{_includedir}/glycin-1
%{_includedir}/glycin-1/glycin.h
%dir %{_includedir}/glycin-gtk4-1
%{_includedir}/glycin-gtk4-1/glycin-gtk4.h
%{_libdir}/libglycin-1.so
%{_libdir}/libglycin-gtk4-1.so
%{_libdir}/pkgconfig/glycin-1.pc
%{_libdir}/pkgconfig/glycin-gtk4-1.pc
%{_datadir}/gir-1.0/Gly-1.gir
%{_datadir}/gir-1.0/GlyGtk4-1.gir
%{_datadir}/vala/vapi/libglycin-1.deps
%{_datadir}/vala/vapi/libglycin-1.vapi
%{_datadir}/vala/vapi/libglycin-gtk4-1.deps
%{_datadir}/vala/vapi/libglycin-gtk4-1.vapi

%changelog
