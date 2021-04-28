#
# spec file for package ocaml-ppx_sexp_conv
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


Name:           ocaml-ppx_sexp_conv
Version:        0.14.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        generate S-expression conversion functions
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/ppx_sexp_conv
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocaml(ocaml_base_version) >= 4.04
BuildRequires:  ocamlfind(base)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(ppxlib.metaquot)
BuildRequires:  ocamlfind(sexplib0)

%description
A PPX syntax extension that generates code for converting OCaml types to and from s-expressions.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
dune_release_pkgs='ppx_sexp_conv'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
dune_test_tolerate_fail='dune_test_tolerate_fail ...'
%ocaml_dune_test

%files -f %{name}.files
%defattr(-,root,root,-)

%files devel -f %{name}.files.devel
%defattr(-,root,root,-)

%changelog
