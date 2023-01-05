#
# spec file for package ocaml-sedlex
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


Name:           ocaml-sedlex
Version:        3.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Unicode-friendly lexer generator
License:        MIT
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/sedlex
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(gen)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(uchar)

%description
A lexer generator for OCaml, similar to ocamllex, but supporting Unicode.
Contrary to ocamllex, lexer specifications for sedlex are embedded in
regular OCaml source files.


%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='sedlex'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %name.files
%doc README.md

%files devel -f %name.files.devel

%changelog
