#
# spec file for package ocaml-parmap
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           ocaml-cmdliner
Version:        1.0.2
Release:        0
%{?ocaml_preserve_bytecode}
License:        ISC
Summary:        Declarative definition of command line interfaces for OCaml
Url:            https://github.com/dbuenzli/cmdliner
Group:          Development/Languages/OCaml
Source:         https://github.com/dbuenzli/cmdliner/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(result)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cmdliner is a module for the declarative definition of command line interfaces.

It provides a simple and compositional mechanism to convert command line
arguments to OCaml values and pass them to your functions. The module
automatically handles syntax errors, help messages and UNIX man page
generation. It supports programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n cmdliner-%{version}

%build
rm -fv setup.ml myocamlbuild.ml META* _* */_* 
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        cmdliner
Version:     0
Synopsis:    Declarative definition of command line interfaces for OCaml
Authors:     Daniel Bünzli <daniel.buenzl i@erratique.ch>
License:     %{license}
LicenseFile: LICENSE
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library cmdliner
 Path: src
 Install: true
 Modules: Cmdliner
 BuildDepends: bytes, result

Document cmdliner
 Title:                API reference for cmdliner
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: cmdliner
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
