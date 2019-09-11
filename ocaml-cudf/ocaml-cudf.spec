#
# spec file for package ocaml-cudf
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ocaml-cudf
Version:        0.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml CUDF library
License:        GPL-3.0
Group:          Development/Languages/OCaml
Url:            http://www.mancoosi.org/cudf/
Source0:        cudf-%{version}.tar.gz
Patch0:         allow_underscore.patch
BuildRequires:  glib2-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(extlib)
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CUDF (for Common Upgradeability Description Format) is a format for describing upgrade scenarios in package-based Free and Open Source Software distribution. This is reference implementation in Ocaml.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n cudf-%{version}
%patch0 -p1

%build
rm -fv setup.ml myocamlbuild.ml META* _* */_* *.mllib *.odocl
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        %{name}
Version:     %{version}
Synopsis:    Common Upgradeability Description Format
Authors:     facile@recherche.enac.fr
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library cudf
 Install: true
 Path: .
 BuildDepends: extlib
 Modules: \
 Cudf, \
 Cudf_822_lexer, \
 Cudf_822_parser, \
 Cudf_c, \
 Cudf_checker, \
 Cudf_conf, \
 Cudf_parser, \
 Cudf_printer, \
 Cudf_type_lexer, \
 Cudf_type_parser, \
 Cudf_types, \
 Cudf_types_pp

Document "cudf"
 Title:                API reference for cudf
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: cudf

Executable "cudf-check"
 Path: .
 Install: true
 MainIs: main_cudf_check.ml
 BuildDepends: cudf

Executable "cudf-parse-822"
 Path: .
 Install: true
 MainIs: main_cudf_parse_822.ml
 BuildDepends: cudf
_EOF_

%oasis_setup
%ocaml_oasis_configure --enable-docs --enable-tests
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root)
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%{oasis_docdir_html}
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/META


%changelog
