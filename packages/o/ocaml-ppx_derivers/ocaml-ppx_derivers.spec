#
# spec file for package ocaml-ppx_derivers
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-ppx_derivers
Version:        1.2.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Deriving plugin registry
License:        BSD-3-Clause
Group:          Development/Languages/OCaml

URL:            https://github.com/ocaml-ppx/ppx_derivers
Source0:        https://github.com/ocaml-ppx/ppx_derivers/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros
BuildRequires:  opam-installer

%description
Ppx_derivers is a tiny package whose sole purpose is to allow
ppx_deriving and ppx_type_conv to inter-operate gracefully when
linked as part of the same ocaml-migrate-parsetree driver.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n ppx_derivers-%{version}

%build
dune build @install

%install
mkdir -p %{buildroot}%{_libdir}/ocaml
dune install --destdir=%{buildroot}

# These files will be installed using doc and license directives.
rm -r %{buildroot}/usr/doc

%files
%defattr(-,root,root,-)
%doc README.md CHANGES.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc README.md CHANGES.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti

%changelog
