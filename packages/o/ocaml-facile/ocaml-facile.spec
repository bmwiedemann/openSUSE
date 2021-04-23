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
Version:        1.1.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml Constraint Programming Library
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            https://github.com/Emmanuel-PLF/facile
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE ocaml-4.patch hrvoje.senjan@gmail.com -- Fixes build with ocaml 4
Patch0:         ocaml-4.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20200220

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
%autosetup -p1

%build
test -f lib/jbuild && dune upgrade --verbose
dune_release_pkgs='facile'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
