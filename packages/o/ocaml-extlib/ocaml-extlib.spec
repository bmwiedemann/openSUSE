#
# spec file for package ocaml-extlib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Andrew Psaltis <ampsaltis at gmail dot com>
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


Name:           ocaml-extlib
Version:        1.7.6
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml ExtLib additions to the standard library
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/ygrek/ocaml-extlib
Source0:        https://github.com/ygrek/ocaml-extlib/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(cppo_ocamlbuild)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ExtLib is a project aiming at providing a complete - yet small -
standard library for the OCaml programming language. The purpose of
this library is to add new functions to OCaml Standard Library
modules, to modify some functions in order to get better performances
or more safety (tail-recursive) but also to provide new modules which
should be useful for the average OCaml programmer.

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
make build doc -j1

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install -j1

%files
%defattr(-,root,root,-)
%doc CHANGES README.md
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc CHANGES README.md src/doc/*
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
