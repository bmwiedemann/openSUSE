#
# spec file for package ocaml-findlib
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.8.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective CAML package manager and build helper
License:        MIT
Group:          Development/Languages/OCaml

Url:            https://github.com/ocaml/ocamlfind
Source0:        findlib-%{version}.tar.xz
#
Requires:       ocaml-compiler-libs
Requires:       ocaml-runtime
#
Provides:       ocamlfind = %{version}

BuildRequires:  m4
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 20191101

%description
Findlib is a library manager for Objective Caml. It provides a
convention how to store libraries, and a file format ("META") to
describe the properties of libraries. There is also a tool (ocamlfind)
for interpreting the META files, so that it is very easy to use
libraries in programs and scripts.

%package        devel
Summary:        Development files for ocaml-findlib
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Provides:       %{name}-camlp4 = %{version}-%{release}
Obsoletes:      %{name}-camlp4 < %{version}-%{release}

%description    devel
The ocaml-findlib-devel package contains libraries and signature files
for developing applications that use ocaml-findlib.

%prep
%autosetup -p1 -n findlib-%{version}

%build
rm -rfv site-lib-src
(cd tools/extract_args && make)
tools/extract_args/extract_args -o src/findlib/ocaml_args.ml ocamlc ocamlcp ocamlmktop ocamlopt ocamldep ocamldoc ||:
./configure -config %{_libdir}/ocaml/ocamlfind.conf \
  -bindir %{_bindir} \
  -sitelib `ocamlc -where` \
  -mandir %{_mandir} \
  -with-toolbox
make all
%if 0%{?ocaml_native_compiler}
make opt
%endif
rm -fv doc/guide-html/TIMESTAMP

%install
make install prefix=%{buildroot}
rm -rfv %{buildroot}%{_libdir}/ocaml/ocamlbuild
%ocaml_create_file_list

%files -f %{name}.files
%{_libdir}/ocaml/ocamlfind.conf
%{_libdir}/ocaml/topfind
%{_bindir}/*
%{_mandir}/man?/*
#

%files devel -f %{name}.files.devel
%{_libdir}/ocaml/*/Makefile.config

%changelog
