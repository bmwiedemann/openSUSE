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
BuildRequires:  ocaml-rpm-macros

%description
This is a parser and a printer for the opam file syntax.

%package devel
Summary:        Development files for the opam file syntax parser
Group:          Development/Languages/OCaml

%description devel
This is a parser and a printer for the opam file syntax.

This package contains development files for package %{name}.

%prep
%setup -q

%build
%if 0%{?ocaml_native_compiler}
make all
%else
make byte
%endif

%install
export PREFIX=%{_prefix}
export LIBDIR=%{_libdir}/ocaml
%make_install

%files devel
%license LICENSE
%dir %{_libdir}/ocaml/opam-file-format
%{_libdir}/ocaml/opam-file-format/META
%{_libdir}/ocaml/opam-file-format/opam-file-format.cma
%{_libdir}/ocaml/opam-file-format/opamBaseParser.cmi
%{_libdir}/ocaml/opam-file-format/opamBaseParser.cmo
%{_libdir}/ocaml/opam-file-format/opamLexer.cmi
%{_libdir}/ocaml/opam-file-format/opamLexer.cmo
%{_libdir}/ocaml/opam-file-format/opamParser.cmi
%{_libdir}/ocaml/opam-file-format/opamParser.cmo
%{_libdir}/ocaml/opam-file-format/opamParserTypes.cmi
%{_libdir}/ocaml/opam-file-format/opamPrinter.cmi
%{_libdir}/ocaml/opam-file-format/opamPrinter.cmo
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/opam-file-format/opam-file-format.a
%{_libdir}/ocaml/opam-file-format/opam-file-format.cmxa
%{_libdir}/ocaml/opam-file-format/opam-file-format.cmxs
%{_libdir}/ocaml/opam-file-format/opamBaseParser.cmx
%{_libdir}/ocaml/opam-file-format/opamLexer.cmx
%{_libdir}/ocaml/opam-file-format/opamParser.cmx
%{_libdir}/ocaml/opam-file-format/opamPrinter.cmx
%endif

%changelog
