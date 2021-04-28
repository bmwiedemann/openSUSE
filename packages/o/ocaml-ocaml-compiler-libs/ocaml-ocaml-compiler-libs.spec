#
# spec file for package ocaml-ocaml-compiler-libs
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


Name:           ocaml-ocaml-compiler-libs
Version:        0.12.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Compiler libraries repackaged
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/ocaml-compiler-libs
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-ocaml-compiler-libs.patch
BuildRequires:  ocaml(ocaml_base_version) >= 4.04
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(compiler-libs.bytecomp)
BuildRequires:  ocamlfind(compiler-libs.common)
BuildRequires:  ocamlfind(compiler-libs.optcomp)
BuildRequires:  ocamlfind(compiler-libs.toplevel)

%description
This package simply repackage the OCaml compiler libraries so they
don't expose everything at toplevel. For instance Ast_helper is now
Ocaml_common.Ast_helper.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
dune_release_pkgs='ocaml-compiler-libs'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%defattr(-,root,root,-)

%files devel -f %{name}.files.devel
%defattr(-,root,root,-)

%changelog
