#
# spec file for package ocaml-odn
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


Name:           ocaml-odn
Version:        0.0.11
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Store data using OCaml notation
License:        LGPL-2.1+
Group:          Development/Languages/OCaml

Url:            https://github.com/gildor478/ocaml-data-notation
Source0:        ocaml-data-notation-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       ocaml-data-notation
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(camlp4.lib)
BuildRequires:  ocamlfind(camlp4.quotations.o)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(type_conv)

%description
This project uses type-conv to dump OCaml data structure using OCaml
data notation. This kind of data dumping helps to write OCaml code
generator, like OASIS.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Provides:       ocaml-data-notation-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.
%prep
%setup -n ocaml-data-notation-%{version}

%build
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        %{name}
Version:     0
Synopsis:    Store data using OCaml notation
Authors:     Sylvain Le Gall
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library odn
  Path:    src
  Modules: ODN

Library pa_odn
  Path:               src
  Modules:            Pa_odn
  FindlibParent:      odn
  FindlibContainers:  with
  FindlibName:        syntax
  BuildDepends:       type_conv (>= 108.07.01), camlp4.lib, camlp4.quotations.o
  CompiledObject:     byte
  XMETAType:          syntax
  XMETARequires:      type_conv, camlp4, odn
  XMETADescription:   Syntax extension for odn

Library pa_noodn
  Path:               src
  Modules:            Pa_noodn
  FindlibParent:      odn
  FindlibContainers:  without
  FindlibName:        syntax
  BuildDepends:       type_conv, camlp4.lib, camlp4.quotations.o
  CompiledObject:     byte
  XMETAType:          syntax
  XMETARequires:      type_conv, camlp4
  XMETADescription:   Syntax extension that removes 'with odn'

Document "odn"
 Title:                API reference for odn
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: odn
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root,-)
%doc COPYING.txt
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
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/META

%changelog
