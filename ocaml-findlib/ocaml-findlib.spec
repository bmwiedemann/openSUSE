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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ocaml-findlib
Version:        1.7.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective CAML package manager and build helper
License:        MIT
Group:          Development/Languages/OCaml

Url:            http://projects.camlcity.org/projects/findlib.html
Source0:        findlib-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
Recommends:     ocaml-findlib-camlp4
#
Requires:       ocaml-compiler-libs
Requires:       ocaml-runtime
#
Provides:       ocamlfind = %{version}

BuildRequires:  gawk
BuildRequires:  m4
BuildRequires:  ncurses-devel
BuildRequires:  ocaml >= 4.02.0
BuildRequires:  ocaml-camlp4-devel >= 4.02.0
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.02.1

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

%description    devel
The ocaml-findlib-devel package contains libraries and signature files
for developing applications that use ocaml-findlib.



%package camlp4
Summary:        Development files for ocaml-findlib
Group:          Development/Languages/OCaml
Requires:       ocaml-camlp4-devel

%description camlp4
The ocaml-findlib-camlp4 contains signature files for developing applications that use camlp4

%prep
%setup -q -n findlib-%{version}

%build
(cd tools/extract_args && make)
tools/extract_args/extract_args -o src/findlib/ocaml_args.ml ocamlc ocamlcp ocamlmktop ocamlopt ocamldep ocamldoc ||:
./configure -config %{_sysconfdir}/ocamlfind.conf \
  -bindir %{_bindir} \
  -sitelib `ocamlc -where` \
  -mandir %{_mandir} \
  -with-toolbox
make all
%if 0%{?ocaml_native_compiler}
make opt
%endif
rm doc/guide-html/TIMESTAMP

%install
make install prefix=$RPM_BUILD_ROOT
rm -rfv $RPM_BUILD_ROOT%{_libdir}/ocaml/ocamlbuild

%files
%defattr(-,root,root,-)
%doc LICENSE doc/README
%config(noreplace) %{_sysconfdir}/ocamlfind.conf
%{_bindir}/*
%{_mandir}/man?/*
#
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/META
#
%exclude %dir %{_libdir}/ocaml/camlp4
%exclude %dir %{_libdir}/ocaml/findlib
%exclude %dir %{_libdir}/ocaml/num-top
%exclude %{_libdir}/ocaml/camlp4/META
%exclude %{_libdir}/ocaml/findlib/META
%exclude %{_libdir}/ocaml/num-top/META
%{_libdir}/ocaml/topfind
%dir %{_libdir}/ocaml/findlib
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc LICENSE doc/README doc/guide-html
%{_libdir}/ocaml/*/Makefile.config
#
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/findlib
%dir %{_libdir}/ocaml/num-top
%{_libdir}/ocaml/findlib/META
%{_libdir}/ocaml/num-top/META
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.mli

%files camlp4
%defattr(-,root,root,-)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/camlp4
%{_libdir}/ocaml/camlp4/META

%changelog
