#
# spec file for package ocaml-qcheck
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-qcheck
Version:        0.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        QuickCheck inspired property-based testing for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml

URL:            https://github.com/c-cube/qcheck
Source0:        https://github.com/c-cube/qcheck/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ounit-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind
BuildRequires:  opam-installer

%description
This module allows to check invariants (properties of some types) over
randomly generated instances of the type. It provides combinators for
generating instances and printing them.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n qcheck-%{version}

%build
# do not build alcotest support since it is not packaged yet
dune build @install -p qcheck,qcheck-core,qcheck-ounit

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
dune install --destdir=%{buildroot} qcheck qcheck-core qcheck-ounit

# These files will be installed using doc and license directives.
rm -r %{buildroot}/usr/doc

%files
%defattr(-,root,root,-)
%doc README.adoc CHANGELOG.md
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%dir %{_libdir}/ocaml/*/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/{,*/}*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%dir %{_libdir}/ocaml/*/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/{,*/}*.a
%{_libdir}/ocaml/*/{,*/}*.cmx
%{_libdir}/ocaml/*/{,*/}*.cmxa
%endif
%{_libdir}/ocaml/*/{,*/}*.ml
%{_libdir}/ocaml/*/{,*/}*.mli
%{_libdir}/ocaml/*/{,*/}*.cma
%{_libdir}/ocaml/*/{,*/}*.cmi
%{_libdir}/ocaml/*/{,*/}*.cmt
%{_libdir}/ocaml/*/{,*/}*.cmti
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam

%changelog
