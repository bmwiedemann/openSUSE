#
# spec file for package ocaml-qcheck
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


%bcond_with     ocaml_alcotest

Name:           ocaml-qcheck
Version:        0.17
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        QuickCheck inspired property-based testing for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml

URL:            https://opam.ocaml.org/packages/qcheck
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(unix)
%if %{with ocaml_alcotest}
BuildRequires:  ocamlfind(alcotest)
%endif

%description
This module allows to check invariants (properties of some types) over
randomly generated instances of the type. It provides combinators for
generating instances and printing them.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
dune_release_pkgs='qcheck,qcheck-core,qcheck-ounit'
%if %{with ocaml_alcotest}
dune_release_pkgs="${dune_release_pkgs},qcheck-alcotest"
%endif
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.adoc

%files devel -f %{name}.files.devel

%changelog
