#
# spec file for package ocaml-ppx_tools_versioned
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


Name:           ocaml-ppx_tools_versioned
Version:        5.2.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Tools for authors of ppx rewriters
License:        MIT
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-ppx/ppx_tools_versioned
Source:         https://github.com/ocaml-ppx/ppx_tools_versioned/archive/%{version}/ppx_tools_versioned-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-migrate-parsetree-devel
BuildRequires:  ocaml-result-devel
BuildRequires:  ocaml-rpm-macros
BuildRequires:  opam-installer
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A variant of ppx_tools based on ocaml-migrate-parsetree.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n ppx_tools_versioned-%{version}

%build
dune build @install --profile=release

%install
dune install --destdir="%{buildroot}" --verbose

# These files will be installed using the doc and license directives
rm %{buildroot}/usr/doc/ppx_tools_versioned/{LICENSE,README.md}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%dir %{_libdir}/ocaml/*
%dir %{_libdir}/ocaml/*/metaquot_*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*/*.a
%{_libdir}/ocaml/*/*/*.cmx
%{_libdir}/ocaml/*/*/*.cmxa
%endif
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/opam
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/*/*.cma
%{_libdir}/ocaml/*/*/*.cmi
%{_libdir}/ocaml/*/*/*.cmt
%{_libdir}/ocaml/*/*/*.ml
%{_libdir}/ocaml/*/*/*.exe

%changelog
