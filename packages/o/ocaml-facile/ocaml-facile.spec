#
# spec file for package ocaml-facile
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


Name:           ocaml-facile
Version:        1.1
Release:        0
Summary:        Ocaml Constraint Programming Library
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            http://www.recherche.enac.fr/log/facile/
Source0:        http://www.recherche.enac.fr/log/facile/distrib/facile-%{version}.tar.gz
# PATCH-FIX-OPENSUSE ocaml-4.patch hrvoje.senjan@gmail.com -- Fixes build with ocaml 4
Patch0:         ocaml-4.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FaCiLe is a constraint programming library on integer and integer set
finite domains written in OCaml. It offers all usual facilities to
create and manipulate finite domain variables, arithmetic expressions
and constraints (possibly non-linear), built-in global constraints
(difference, cardinality, sorting etc.) and search and optimization
goals. FaCiLe as well allows you to build easily user-defined
constraints and goals (including recursive ones), making pervasive use
of OCaml higher-order functionals to provide a simple and flexible
interface for the user. As FaCiLe is an OCaml library and not "yet
another language", the user benefits from type inference and strong
typing discipline, high level of abstraction, a modules and objects
system, as well as native code compilation efficiency, garbage
collection and replay debugger, all features of OCaml (among many
others) that allow to prototype and experiment quickly: modeling, data
processing and interface are implemented with the same powerful and
efficient language.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n facile-%{version}
%patch0 -p1

%build
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        %{name}
Version:     %{version}
Synopsis:    Constraint Programming Library
Authors:     facile@recherche.enac.fr
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library facile
 Install: true
 Path: src
 Modules: Facile, \
 Fcl_alldiff, \
 Fcl_arith, \
 Fcl_boolean, \
 Fcl_conjunto, \
 Fcl_cstr, \
 Fcl_data, \
 Fcl_debug, \
 Fcl_domain, \
 Fcl_expr, \
 Fcl_fdArray, \
 Fcl_float, \
 Fcl_gcc, \
 Fcl_genesis, \
 Fcl_goals, \
 Fcl_interval, \
 Fcl_invariant, \
 Fcl_linear, \
 Fcl_misc, \
 Fcl_nonlinear, \
 Fcl_opti, \
 Fcl_reify, \
 Fcl_setDomain, \
 Fcl_sorting, \
 Fcl_stak, \
 Fcl_var
 CompiledObject: best

Document "facile"
 Title:                API reference for facile
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: facile

Executable "%{name}-coins"
 Path: examples
 Install: true
 MainIs: coins.ml
 BuildDepends: facile
Executable "%{name}-golf"
 Path: examples
 Install: true
 MainIs: golf.ml
 BuildDepends: facile
Executable "%{name}-golomb"
 Path: examples
 Install: true
 MainIs: golomb.ml
 BuildDepends: facile
Executable "%{name}-jobshop"
 Path: examples
 Install: true
 MainIs: jobshop.ml
 BuildDepends: facile
Executable "%{name}-magic"
 Path: examples
 Install: true
 MainIs: magic.ml
 BuildDepends: facile
Executable "%{name}-marriage"
 Path: examples
 Install: true
 MainIs: marriage.ml
 BuildDepends: facile
Executable "%{name}-prolog"
 Path: examples
 Install: true
 MainIs: prolog.ml
 BuildDepends: facile
Executable "%{name}-queens"
 Path: examples
 Install: true
 MainIs: queens.ml
 BuildDepends: facile
Executable "%{name}-scheduling"
 Path: examples
 Install: true
 MainIs: scheduling.ml
 BuildDepends: facile
Executable "%{name}-seven_eleven"
 Path: examples
 Install: true
 MainIs: seven_eleven.ml
 BuildDepends: facile
Executable "%{name}-tiles"
 Path: examples
 Install: true
 MainIs: tiles.ml
 BuildDepends: facile
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
%{_libdir}/ocaml/*/META

%changelog
