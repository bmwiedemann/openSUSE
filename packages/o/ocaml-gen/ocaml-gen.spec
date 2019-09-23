#
# spec file for package ocaml-gen
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


Name:           ocaml-gen
Version:        0.5.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Simple, efficient iterators for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml

URL:            https://github.com/c-cube/gen
Source0:        https://github.com/c-cube/gen/archive/%{version}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros
BuildRequires:  opam-installer

%description
Iterators for OCaml, both restartable and consumable.
The implementation keeps a good balance between simplicity and performance.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n gen-%{version}

%build
dune build @install --profile=release

%install
dune install --destdir="%{buildroot}" --verbose

# These files will be installed using the doc and license directives
rm %{buildroot}/usr/doc/gen/{LICENSE,README.md,CHANGELOG.md}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/META

%changelog
