#
# spec file for package ocaml-findlib
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2010-2011 Andrew Psaltis <ampsaltis at gmail dot com>
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


Name:           ocaml-findlib
Version:        1.9.8
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective CAML package manager and build helper
License:        MIT
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
URL:            https://opam.ocaml.org/packages/ocamlfind/
Source0:        %name-%version.tar.xz
#
Requires:       ocaml-compiler-libs
Requires:       ocaml-runtime
#
Provides:       ocamlfind = %version-%release
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 20260707
#

%description
Findlib is a library manager for Objective Caml. It provides a
convention how to store libraries, and a file format ("META") to
describe the properties of libraries. There is also a tool (ocamlfind)
for interpreting the META files, so that it is very easy to use
libraries in programs and scripts.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release
Provides:       %name-camlp4 = %version-%release
Obsoletes:      %name-camlp4 < %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q

%build
rm -rfv site-lib-src
(cd tools/extract_args && make)
tools/extract_args/extract_args -o src/findlib/ocaml_args.ml ocamlc ocamlcp ocamlmktop ocamlopt ocamldep ocamldoc ||:
./configure -config %ocaml_standard_library/ocamlfind.conf \
  -bindir %_bindir \
  -sitelib '%ocaml_standard_library' \
  -mandir %_mandir \
  -with-toolbox
make all
make opt

%install
%make_install
rm -rfv %buildroot%ocaml_standard_library/ocamlbuild
rm -rfv %buildroot%ocaml_standard_library/findlib/Makefile.packages
%ocaml_create_file_list

%files -f %name.files
%ocaml_standard_library/ocamlfind.conf
%ocaml_standard_library/topfind
%_bindir/*
#

%files devel -f %name.files.devel
%ocaml_standard_library/*/Makefile.config

%changelog
