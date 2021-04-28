#
# spec file for package ocaml-lablgtk2
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

%bcond_with    ocaml_lablgtk2_gl
%bcond_with    ocaml_lablgtk2_glade
%bcond_with    ocaml_lablgtk2_gnomecanvas
%bcond_with    ocaml_lablgtk2_gtksourceview2
%bcond_with    ocaml_lablgtk2_gtkspell
%bcond_without ocaml_lablgtk2_rsvg
# handle built-in ocaml helper from rpm-build, and helper from ocaml-rpm-macros
%global __suseocaml_requires_opts -i GtkSourceView2_types
%global __ocaml_requires_opts -i GtkSourceView2_types

Name:           ocaml-lablgtk2
Version:        2.18.11
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        An Objective Caml Interface to gtk2+
License:        LGPL-2.1-only
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/lablgtk
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(findlib)
%if %{with ocaml_lablgtk2_gl}
BuildRequires:  ocamlfind(lablgl)
%endif
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(gtk+-2.0)
%if %{with ocaml_lablgtk2_gtksourceview2}
BuildRequires:  pkgconfig(gtksourceview-2.0)
%endif
%if %{with ocaml_lablgtk2_gtkspell}
BuildRequires:  pkgconfig(gtkspell-2.0)
%endif
%if %{with ocaml_lablgtk2_glade}
BuildRequires:  pkgconfig(libglade-2.0)
%endif
%if %{with ocaml_lablgtk2_gnomecanvas}
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
%endif
%if %{with ocaml_lablgtk2_rsvg}
BuildRequires:  pkgconfig(librsvg-2.0)
%endif

Provides:       lablgtk2 = %{version}
Obsoletes:      lablgtk2 < %{version}
Provides:       ocaml-lablgtk = %{version}
Obsoletes:      ocaml-lablgtk < %{version}

%description
LablGTK2 uses the rich type system of Objective Caml 3 to provide a
strongly typed, yet very comfortable, object-oriented interface to
GTK2+. Objective Caml threads are supported, including for the top
level, which allows the interactive use of the library.


%package devel
Summary:        An Objective Caml interface to gtk2+
Group:          Development/Languages/OCaml
Provides:       lablgtk2-devel = %{version}
Obsoletes:      lablgtk2-devel < %{version}
Provides:       ocaml-lablgtk-devel = %{version}
Obsoletes:      ocaml-lablgtk-devel < %{version}
Provides:       lablgtk2:/usr/lib/ocaml/lablgtk2/glib.cmi
Requires:       %{name} = %{version}

%description devel
LablGTK2 uses the rich type system of Objective Caml 3 to provide a
strongly typed, yet very comfortable, object-oriented interface to
GTK2+. Objective Caml threads are supported, including for the top
level, which allows for interactive use of the library.

%prep
%setup -q

%build
chmod a-x README
%configure \
	--without-gl \
	--without-glade \
	--without-gnomecanvas \
	--without-gnomeui \
	--without-gtksourceview \
	--without-gtksourceview2 \
	--without-gtkspell \
	--without-panel \
	--without-quartz \
	--without-rsvg \
	\
%if %{with ocaml_lablgtk2_gl}
	--with-gl \
%endif
%if %{with ocaml_lablgtk2_glade}
	--with-glade \
%endif
%if %{with ocaml_lablgtk2_gnomecanvas}
	--with-gnomecanvas \
%endif
%if %{with ocaml_lablgtk2_gtksourceview2}
	--with-gtksourceview2 \
%endif
%if %{with ocaml_lablgtk2_gtkspell}
	--with-gtkspell \
%endif
%if %{with ocaml_lablgtk2_rsvg}
	--with-rsvg \
%endif
	%{nil}
make world
make opt

%install
%make_install
# Remove ld.conf (part of main OCaml dist).
rm -fv %{buildroot}%{ocaml_standard_library}/ld.conf
#
%ocaml_create_file_list

%files -f %{name}.files
%defattr(-,root,root,-)
%doc README
%{_bindir}/*

%files devel -f %{name}.files.devel
%defattr(-,root,root,-)
%{ocaml_standard_library}/*/propcc
%{ocaml_standard_library}/*/varcc

%changelog
