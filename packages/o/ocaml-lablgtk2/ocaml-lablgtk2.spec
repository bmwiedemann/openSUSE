#
# spec file for package ocaml-lablgtk2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Version:        2.18.10
Release:        0
%{?ocaml_preserve_bytecode}
# handle built-in ocaml helper from rpm-build, and helper from ocaml-rpm-macros
%global __suseocaml_requires_opts -i GtkSourceView2_types
%global __ocaml_requires_opts -i GtkSourceView2_types
Name:           ocaml-lablgtk2
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-lablgtk2.ml_table_extension_events.patch
BuildRequires:  gtk2-devel
BuildRequires:  gtksourceview2-devel
BuildRequires:  gtkspell-devel
BuildRequires:  libglade2-devel
BuildRequires:  libgnomecanvas-devel
BuildRequires:  librsvg-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-lablgl-devel
BuildRequires:  ocaml-rpm-macros >= 20200514
BuildRequires:  xorg-x11
BuildRequires:  zlib-devel
Requires:       ocaml
Provides:       lablgtk2 = %{version}
Obsoletes:      lablgtk2 < %{version}
Provides:       ocaml-lablgtk = %{version}
Obsoletes:      ocaml-lablgtk < %{version}
Url:            https://github.com/garrigue/lablgtk
Summary:        An Objective Caml Interface to gtk2+
License:        LGPL-2.1-only
Group:          Development/Languages/OCaml

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
Requires:       gtk2-devel
Requires:       gtksourceview2-devel
Requires:       libgnomecanvas-devel

%description devel
LablGTK2 uses the rich type system of Objective Caml 3 to provide a
strongly typed, yet very comfortable, object-oriented interface to
GTK2+. Objective Caml threads are supported, including for the top
level, which allows for interactive use of the library.

%prep
%autosetup -p1

%build
find -name ".cvsignore" -print -delete
# fix README file executable permissions
chmod a-x README
export CFLAGS="$RPM_OPT_FLAGS"
make configure 
%configure --with-gnomecanvas
make world
%if 0%{?ocaml_native_compiler}
make opt
pushd src
make lablgtk.cmxa
make lablrsvg.cmxa
make gtkInit.cmx
popd
%endif

%install
%makeinstall
# Remove ld.conf (part of main OCaml dist).
rm $RPM_BUILD_ROOT%{ocaml_standard_library}/ld.conf
#
%ocaml_create_file_list

%files -f %{name}.files
%doc CHANGES README
%{_bindir}/*

%files devel -f %{name}.files.devel
%{ocaml_standard_library}/*/propcc
%{ocaml_standard_library}/*/varcc

%changelog
