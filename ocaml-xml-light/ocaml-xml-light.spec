#
# spec file for package ocaml-xml-light
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-xml-light
Version:        2.4.20160613.2bc42e8
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Minimal XML parser and printer for OCaml
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            https://github.com/gasche/xml-light
Source0:        xml-light-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n xml-light-%{version}

%build
rm -fv META*
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        xml-light
Version:     %{version}
Synopsis:    Minimal XML parser and printer for OCaml
Authors:     Nicolas Cannasse <ncannasse@motion-twin.com>
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library "xml-light"
 Path: .
 Modules: Xml, Xml_light_types

Document "xml-light"
 Title:                API reference for xml-light
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: xml-light

Executable test
 Install: false
 Path: .
 MainIs: test.ml
 CompiledObject: best
 BuildDepends: xml-light

Test "test"
 Type: Custom (0.0.1)
 Command: \$test < x
 Run: true
_EOF_

%oasis_setup
%ocaml_oasis_configure --enable-docs --enable-tests
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%check
tee x <<EOF
<abc><123/></abc>

EOF
%ocaml_oasis_test

%files
%defattr(-,root,root,-)
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
%{_libdir}/ocaml/*/META

%changelog
