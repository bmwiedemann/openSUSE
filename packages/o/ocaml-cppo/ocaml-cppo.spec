#
# spec file for package ocaml-cppo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 The openSUSE Project.
# Copyright (c) 2015 LISA GmbH, Bingen, Germany.
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


# cppo may use opam-installer but opam requires cppo for its build.
# So here we don't use opam-installer by default.
# Build with "--with-opam" to use opam despite the circular dependency.
%bcond_with opam
Name:           ocaml-cppo
Version:        1.6.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        The C preprocessor written in OCaml
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-community/cppo
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(easy-format)
BuildRequires:  ocamlfind(ocamlbuild)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(unix)
%if %{with opam}
BuildRequires:  opam
%endif

%description
Cppo is an equivalent of the C preprocessor targeted at the OCaml language and
its variants.

The main purpose of cppo is to provide a lightweight tool for simple macro
substitution (#define) and file inclusion (#include) for the occasional case
when this is useful in OCaml. Processing specific sections of files by calling
external programs is also possible via #ext directives.

The implementation of cppo relies on the standard library of OCaml and on the
standard parsing tools Ocamllex and Ocamlyacc, which contribute to the
robustness of cppo across OCaml versions. 

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
dune build @install --profile release

%install
%if %{with opam}
  install -d %{buildroot}%{_libdir}/ocaml
  dune install --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}/ocaml
  rm -r %{buildroot}%{_prefix}/doc
%else
  # By hand, not funny
  cd _build/install/default
  install -d %{buildroot}%{_libdir}/ocaml/cppo{,_ocamlbuild}
  install -m0644 lib/cppo/* %{buildroot}%{_libdir}/ocaml/cppo/
  install -m0644 lib/cppo_ocamlbuild/* %{buildroot}%{_libdir}/ocaml/cppo_ocamlbuild/
  install -d %{buildroot}%{_bindir}
  install -m0755 bin/cppo %{buildroot}%{_bindir}
%endif

%files
%defattr(-,root,root)
%{_bindir}/cppo
%doc LICENSE.md README.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
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
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam

%changelog
