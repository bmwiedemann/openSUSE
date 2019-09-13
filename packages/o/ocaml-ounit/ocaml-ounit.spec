#
# spec file for package ocaml-ounit
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


Name:           ocaml-ounit
Version:        2.0.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml OUnit test framework
License:        MIT
Group:          Development/Languages/OCaml
Url:            http://ounit.forge.ocamlcore.org/
Source0:        ounit-%{version}.tar.gz
Patch0:         ounit-strict-formats.diff
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OUnit is a unit test framework for OCaml. It allows one to easily
create unit-tests for OCaml code. It is based on HUnit, a unit testing
framework for Haskell. It is similar to JUnit, and other xUnit testing
frameworks.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Development files needed for application based on %{name}.

%prep
%setup -q -n ounit-%{version}
%patch0 -p1

%build
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root,-)
%doc LICENSE.txt
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
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
