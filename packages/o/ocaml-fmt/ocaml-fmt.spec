#
# spec file for package ocaml-fmt
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


Name:           ocaml-fmt
Version:        0.8.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Format pretty-printer combinators
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/fmt
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-fmt.patch
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocaml(ocaml_base_version) >= 4.05
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(compiler-libs.toplevel)
BuildRequires:  ocamlfind(result)
BuildRequires:  ocamlfind(seq)
BuildRequires:  ocamlfind(stdlib-shims)
BuildRequires:  ocamlfind(unix)

%description
Fmt exposes combinators to devise Format pretty-printing functions.

Fmt depends only on the OCaml standard library. The optional Fmt_tty library that allows to setup formatters for terminal color output depends on the Unix library. The optional Fmt_cli library that provides command line support for Fmt depends on Cmdliner.

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
dune_release_pkgs='fmt'
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
