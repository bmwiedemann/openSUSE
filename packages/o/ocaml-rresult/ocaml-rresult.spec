#
# spec file for package ocaml-rresult
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


Name:           ocaml-rresult
Version:        0.7.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Result value combinators for OCaml
License:        ISC
URL:            https://opam.ocaml.org/packages/rresult
Source0:        %name-%version.tar.xz
Patch0:         ocaml-rresult.patch
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(compiler-libs)
BuildRequires:  ocamlfind(result)

%description
Rresult is an OCaml module for handling computation results and errors in an 
explicit and declarative manner, without resorting to exceptions. It defines 
combinators to operate on the result type available from OCaml 4.03 in the 
standard library.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='rresult'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check 
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel

%changelog
