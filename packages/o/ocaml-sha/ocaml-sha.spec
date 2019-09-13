#
# spec file for package ocaml-sha
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

Name:           ocaml-sha
Version:        1.12
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Binding to the SHA cryptographic functions
License:        ISC
Group:          Development/Languages/OCaml

URL:            https://github.com/djs55/ocaml-sha/
Source0:        https://github.com/djs55/ocaml-sha/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocamlfind
BuildRequires:  ocaml-ounit-devel
BuildRequires:  opam-installer
BuildRequires:  ocaml-rpm-macros

%description
A binding for SHA interface code in OCaml. Offering the same interface than
the MD5 digest included in the OCaml standard library.
It's currently providing SHA1, SHA256 and SHA512 hash functions.


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
dune build @install


%install
mkdir -p %{buildroot}%{_libdir}/ocaml
dune install --destdir=%{buildroot}
# These files will be installed using doc and license directives.
rm -r %{buildroot}/usr/doc


%check
dune runtest


%files
%defattr(-,root,root,-)
%doc README CHANGES.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.so
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif


%files devel
%defattr(-,root,root,-)
%doc README CHANGES.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/dune-package


%changelog
