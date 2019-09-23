#
# spec file for package ocaml-type-conv
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


Name:           ocaml-type-conv
Version:        113.00.02
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Generate OCaml modules
License:        Apache-2.0
Group:          Development/Languages/OCaml

Url:            https://github.com/janestreet/type_conv
Source0:        type_conv-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(camlp4.extend)
BuildRequires:  ocamlfind(camlp4.quotations)
BuildRequires:  ocamlfind(findlib)

%description
Generate OCaml modules from source files

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.
%prep
%setup -n type_conv-%{version}

%build
rm -fv */*lib _tags
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        %{name}
Version:     0
Synopsis:    type_conv - support library for preprocessor type conversions
Authors:     Jane Street Group, LLC <opensource@janestreet.com>
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library type_conv
  Path:               src
  Modules:            Pa_type_conv
  BuildDepends:       camlp4.quotations, camlp4.extend
  XMETAType:          syntax
  XMETARequires:      camlp4
  XMETADescription:   Syntax extension for type_conv

Document "type_conv"
 Title:                API reference for type_conv
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: type_conv
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root,-)
%doc COPYRIGHT.txt LICENSE-Tywith.txt LICENSE.txt
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
