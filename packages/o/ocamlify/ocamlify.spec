#
# spec file for package ocamlify
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


Name:           ocamlify
Version:        0.0.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Verbatim file inclusion as OCaml code
License:        LGPL-2.1+
Group:          Development/Languages/OCaml

Url:            http://forge.ocamlcore.org/projects/ocamlify/
Source0:        %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(findlib)

%description
OCamlify allows to create OCaml source code by including whole files
into OCaml string or string list. The code generated can be compiled as
a standard OCaml file. It allows embedding external resources as OCaml
code.

%prep
%setup

%build
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%files
%defattr(-,root,root,-)
%doc COPYING.txt
%{_bindir}/*

%changelog
