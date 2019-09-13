#
# spec file for package ocaml-uutf
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define _name   uutf
Name:           ocaml-uutf
Version:        1.0.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Non-blocking streaming Unicode codec for OCaml
License:        ISC
Group:          Development/Languages/OCaml
Url:            http://erratique.ch/software/uutf
Source:         http://erratique.ch/software/uutf/releases/uutf-%{version}.tbz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Uutf is a non-blocking streaming codec to decode and encode the UTF-8,
UTF-16, UTF-16LE and UTF-16BE encoding schemes. It can efficiently
work character by character without blocking on IO. Decoders perform
character position tracking and support newline normalization.

Functions are also provided to fold over the characters of UTF encoded
OCaml string values and to directly encode characters in OCaml
Buffer.t values.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n uutf-%{version}

%build
rm -fv setup.ml myocamlbuild.ml META* _* */_* 
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        uutf
Version:     0
Synopsis:    Non-blocking streaming Unicode codec
Authors:     Daniel Bünzli <daniel.buenzl i@erratique.ch>
License:     %{license}
LicenseFile: LICENSE.md
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library uutf
 Path: src
 Install: true
 Modules: Uutf

Document uutf
 Title:                API reference for uutf
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: uutf
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%{oasis_docdir_html}
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
