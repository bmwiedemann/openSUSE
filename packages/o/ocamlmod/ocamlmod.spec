#
# spec file for package ocamlmod
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


Name:           ocamlmod
Version:        0.0.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Generate OCaml modules
License:        LGPL-2.1+
Group:          Development/Languages/OCaml

Url:            http://forge.ocamlcore.org/projects/ocamlmod/
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocamlmod.patch

BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(str)

%description
Generate OCaml modules from source files

%prep
%autosetup -p1

%build
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%{_bindir}/*

%changelog
