#
# spec file for package ocaml-dose
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ocaml-dose
Version:        5.0.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        An OCaml dependency toolkit
License:        LGPL-3.0-or-later
URL:            https://opam.ocaml.org/packages/dose3
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-cppo
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20200220
BuildRequires:  ocamlfind(bz2)
BuildRequires:  ocamlfind(cudf)
BuildRequires:  ocamlfind(extlib)
BuildRequires:  ocamlfind(minisat)
BuildRequires:  ocamlfind(ocamlgraph)
BuildRequires:  ocamlfind(re.pcre)
BuildRequires:  ocamlfind(zip)

%description
Dose3 is a framework made of several OCaml libraries for managing distribution
packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems (monitoring
package evolutions, correct and complete dependency resolution, repository-wide
uninstallability checks).

%package devel
Summary:        An OCaml dependency toolkit -- Development files
Requires:       %{name} = %{version}

%description devel
This package contains development files for package %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='dose-algo,dose-common'
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
