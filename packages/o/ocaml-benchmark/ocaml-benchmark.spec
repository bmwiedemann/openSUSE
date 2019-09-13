#
# spec file for package ocaml-benchmark
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ocaml-benchmark
Version:        1.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Benchmarking module for OCaml
License:        LGPL-3.0-or-later WITH OCaml-linking-exception
Group:          Development/Languages/OCaml

URL:            http://ocaml-benchmark.forge.ocamlcore.org/
Source0:        https://github.com/Chris00/ocaml-benchmark/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros

%description
Benchmark provides functions to measure and compare the run-time of functions.
It is inspired by the Perl module of the same name.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{version}


%build
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc


%install
%ocaml_oasis_findlib_install


%files
%defattr(-,root,root,-)
%doc README.md LICENSE.txt
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
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/META

%changelog

