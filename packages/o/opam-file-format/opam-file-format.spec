#
# spec file for package opam-file-format
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 The openSUSE Project.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           opam-file-format
Version:        2.0.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Parser and printer for the opam file syntax
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101

%description
This is a parser and a printer for the opam file syntax.

%package devel
Summary:        Development files for the opam file syntax parser
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
This is a parser and a printer for the opam file syntax.

This package contains development files for package %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='opam-file-format'
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
