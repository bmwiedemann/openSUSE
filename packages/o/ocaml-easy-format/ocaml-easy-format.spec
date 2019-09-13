#
# spec file for package ocaml-easy-format
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


Name:           ocaml-easy-format
Version:        1.2.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Data pretty printing made easy
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/mjambon/easy-format
Source:         easy-format-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This module offers a high-level and functional interface to the Format module
of the OCaml standard library. It is a pretty-printing facility, i.e. it takes
as input some code represented as a tree and formats this code into the most
visually satisfying result, breaking and indenting lines of code where
appropriate.

Input data must be first modelled and converted into a tree using 3 kinds of
nodes:

    atoms lists labelled nodes

Atoms represent any text that is guaranteed to be printed as-is. Lists can
model any sequence of items such as arrays of data or lists of definitions that
are labelled with something like "int main", "let x =" or "x:".

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Provides:       ocamlfind(easy-format)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -qn easy-format-%{version}

%build
tee _oasis <<_EOF_
OASISFormat: 0.4
Name:        "easy-format"
Version:     %{version}
Synopsis:    Data pretty printing made easy
Authors:     Martin Jambon
LicenseFile: LICENSE
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library "easy-format"
 Path: .
 Modules: Easy_format
 Install: true

Document easy_format
 Title:                "API reference for easy-format"
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: easy-format

Executable lambda_example
 Install: false
 Path: .
 MainIs: lambda_example.ml
 CompiledObject: best
 BuildDepends: easy-format

Executable test_easy_format
 Install: false
 Path: .
 MainIs: test_easy_format.ml
 CompiledObject: best
 BuildDepends: easy-format

Executable simple_example
 Install: false
 Path: .
 MainIs: simple_example.ml
 CompiledObject: best
 BuildDepends: easy-format

Test lambda_example
 Type: Custom (0.0.1)
 Command: \$lambda_example
 Run: true

Test simple_example
 Type: Custom (0.0.1)
 Command: \$simple_example
 Run: true

Test test_easy_format
 Type: Custom (0.0.1)
 Command: \$test_easy_format
 Run: true
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs --enable-tests
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%check
%ocaml_oasis_test

%files
%defattr(-,root,root)
%doc LICENSE README.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc examples/
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
