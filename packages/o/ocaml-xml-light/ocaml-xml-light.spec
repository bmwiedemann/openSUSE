#
# spec file for package ocaml-xml-light
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           ocaml-xml-light
Version:        2.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Minimal XML parser and printer for OCaml
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            https://opam.ocaml.org/packages/xml-light
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20230101

%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='xml-light'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel

%changelog
