#
# spec file for package ocaml-ocamlgraph
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-ocamlgraph
Version:        1.8.8
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Graph library for OCaml
License:        LGPL-2.1
Group:          Development/Languages/OCaml
Url:            http://ocamlgraph.lri.fr
Source:         http://ocamlgraph.lri.fr/download/ocamlgraph-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(lablgl)
BuildRequires:  ocamlfind(lablgtk2)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%global __requires_exclude ocaml\\\(Sig\\\)

%description
OCamlgraph is a graph library for Objective Caml.

%package devel
Summary:        Development files for the OcamlGraph graph library
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
OCamlgraph is a graph library for Objective Caml.

This package contains development files for %{name}.

%prep
%setup -q -n ocamlgraph-%{version}

%build
%configure
make  %{?_smp_mflags}

%install
%makeinstall
find %{buildroot} -ls
find %{buildroot} -name "*o" -print -delete
install -m0644 META %{buildroot}%{_libdir}/ocaml/ocamlgraph

%files
%defattr(-,root,root)
%doc CHANGES COPYING CREDITS FAQ
%license LICENSE
%{_bindir}/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
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
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
