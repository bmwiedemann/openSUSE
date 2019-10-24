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
Version:        1.3.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Data pretty printing made easy
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-community/easy-format
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros >= 20190930
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
%autosetup -p1

%build
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test || : make check failed

%files -f %{name}.files
%license LICENSE
%doc README.md

%files devel -f %{name}.files.devel

%changelog
