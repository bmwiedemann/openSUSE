#
# spec file for package ocaml-lablgtk3
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


Name:           ocaml-lablgtk3
Version:        3.1.1
Release:        0
Summary:        Binding to Cairo, a 2D Vector Graphics Library.  
License:        LGPL-3.0-or-later
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/lablgtk3
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  pkg-config
BuildRequires:  ocaml(ocaml_base_version) >= 4.05
BuildRequires:  ocamlfind(cairo2)
BuildRequires:  ocamlfind(camlp5)
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(threads)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.18
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.18
BuildRequires:  pkgconfig(gtkspell3-3.0) >= 3.0.4

%description
This is an OCaml binding for the Cairo library, a 2D graphics library with support for multiple output devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       pkgconfig(gtk+-3.0) >= 3.18
Requires:       pkgconfig(gtksourceview-3.0) >= 3.18
Requires:       pkgconfig(gtkspell3-3.0) >= 3.0.4

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
sed -i~ '/mode promote/d' tools/dune
diff -u "$_"~ "$_" && exit 1
dune_release_pkgs='lablgtk3,lablgtk3-sourceview3,lablgtk3-gtkspell3'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%{_bindir}/*

%files devel -f %{name}.files.devel

%changelog
