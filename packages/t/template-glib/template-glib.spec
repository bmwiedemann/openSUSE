#
# spec file for package template-glib
#
# Copyright (c) 2023 SUSE LLC
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


Name:           template-glib
Version:        3.36.1
Release:        0
Summary:        Library for generating text based on a template and user defined state
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://git.gnome.org/browse/template-glib/
Source0:        https://download.gnome.org/sources/template-glib/3.36/%{name}-%{version}.tar.xz

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.51.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%description
Template-GLib is a library for generating text based on a template and
user defined state. Template-GLib does not use a language runtime, so it is
safe to use from any GObject-Introspectable language.

%package -n     libtemplate_glib-1_0-0
Summary:        Library for generating text based on a template and user defined state
# Make the -lang package installable
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libtemplate_glib-1_0-0
Template-GLib is a library for generating text based on a template and
user defined state. Template-GLib does not use a language runtime, so it is
safe to use from any GObject-Introspectable language.

%package -n     typelib-1_0-Template-1_0
Summary:        Introspection bindings for Template-GLib
Group:          System/Libraries

%description -n typelib-1_0-Template-1_0
Template-GLib is a library for generating text based on a template and
user defined state. Template-GLib does not use a language runtime, so it is
safe to use from any GObject-Introspectable language.

Template-GLib allows accessing properties on GObjects as well as call
simple methods via GObject-Introspection.

This package provides the introspection bindings.

%package        devel
Summary:        Development files for Template-GLib
Group:          Development/Languages/C and C++
Requires:       typelib-1_0-Template-1_0 = %{version}

%description    devel
Template-GLib is a library for generating text based on a template and
user defined state. Template-GLib does not use a language runtime, so it is
safe to use from any GObject-Introspectable language.

This package provides the development files.

%lang_package

%prep
%autosetup

%build
%meson \
	-Dtracing=false \
	-Dprofiling=false \
	-Dintrospection=enabled \
	-Dvapi=true \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%post -n libtemplate_glib-1_0-0 -p /sbin/ldconfig
%postun -n libtemplate_glib-1_0-0 -p /sbin/ldconfig

%files -n libtemplate_glib-1_0-0
%license COPYING
%{_libdir}/libtemplate_glib-1.0.so.0*

%files -n typelib-1_0-Template-1_0
%{_libdir}/girepository-1.0/Template-1.0.typelib

%files devel
%doc README.md
%doc %{_datadir}/gtk-doc/html/template-glib/
%dir %{_includedir}/template-glib-1.0
%{_includedir}/template-glib-1.0/*.h
%{_datadir}/gir-1.0/Template-1.0.gir
%{_libdir}/libtemplate_glib-1.0.so
%{_libdir}/pkgconfig/template-glib-1.0.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/template-glib-1.0.deps
%{_datadir}/vala/vapi/template-glib-1.0.vapi

%files lang -f %{name}.lang

%changelog
