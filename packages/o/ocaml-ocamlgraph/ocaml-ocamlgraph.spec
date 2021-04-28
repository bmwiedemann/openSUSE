#
# spec file for package ocaml-ocamlgraph
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


Name:           ocaml-ocamlgraph
Version:        2.0.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Graph library for OCaml
License:        LGPL-2.1
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/ocamlgraph
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(stdlib-shims)

%description
OCamlgraph is a graph library for Objective Caml.

%package devel
Summary:        Development files for the OcamlGraph graph library
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
OCamlgraph is a graph library for Objective Caml.

This package contains development files for %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='ocamlgraph'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
