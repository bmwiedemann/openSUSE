#
# spec file for package ocaml-cppo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 The openSUSE Project.
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


Name:           ocaml-cppo
Version:        1.6.6
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        The C preprocessor written in OCaml
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-community/cppo
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRequires:  ocamlfind(easy-format)
BuildRequires:  ocamlfind(ocamlbuild)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(unix)

%description
Cppo is an equivalent of the C preprocessor targeted at the OCaml language and
its variants.

The main purpose of cppo is to provide a lightweight tool for simple macro
substitution (#define) and file inclusion (#include) for the occasional case
when this is useful in OCaml. Processing specific sections of files by calling
external programs is also possible via #ext directives.

The implementation of cppo relies on the standard library of OCaml and on the
standard parsing tools Ocamllex and Ocamlyacc, which contribute to the
robustness of cppo across OCaml versions. 

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
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md
%{_bindir}/cppo

%files devel -f %{name}.files.devel

%changelog
