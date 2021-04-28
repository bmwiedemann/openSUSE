#
# spec file for package ocaml-astring
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


Name:           ocaml-astring
Version:        0.8.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Alternative String module for OCaml
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/astring
Source:         %{name}-%{version}.tar.xz
Patch0:         ocaml-astring.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(compiler-libs.toplevel)

%description
Astring exposes an alternative String module for OCaml. This module tries to balance minimality and expressiveness for basic, index-free, string processing and provides types and functions for substrings, string sets and string maps.

Remaining compatible with the OCaml String module is a non-goal. The String module exposed by Astring has exception safe functions, removes deprecated and rarely used functions, alters some signatures and names, adds a few missing functions and fully exploits OCaml's newfound string immutability.

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
dune_release_pkgs='astring'
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
