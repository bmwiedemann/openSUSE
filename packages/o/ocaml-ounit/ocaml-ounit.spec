#
# spec file for package ocaml-ounit
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


%bcond_with     ocaml_lwt

Name:           ocaml-ounit
Version:        2.2.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml OUnit test framework
License:        MIT
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/ounit
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(stdlib-shims)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(threads)
BuildRequires:  ocamlfind(unix)
%if %{with ocaml_lwt}
BuildRequires:  ocamlfind(lwt)
BuildRequires:  ocamlfind(lwt.unix)
%endif

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Development files needed for application based on %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='ounit,ounit2'
%if %{with ocaml_lwt}
dune_release_pkgs="${dune_release_pkgs},ounit-lwt,ounit2-lwt"
%endif
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
mkdir %{buildroot}$(ocamlc -where)/oUnit
cp -avt "$_" src/lib/oUnit/META
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
