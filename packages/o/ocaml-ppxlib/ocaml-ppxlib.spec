#
# spec file for package ocaml-ppxlib
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with ocaml_ppxlib_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_ppxlib_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg ocaml-ppxlib
Name:           %pkg%nsuffix
Version:        0.35.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Base library and tools for ppx rewriters
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/ppxlib
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 3.8
BuildRequires:  ocaml-rpm-macros >= 20240909
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(compiler-libs)
BuildRequires:  ocamlfind(ocaml-compiler-libs)
BuildRequires:  ocamlfind(ppx_derivers)
BuildRequires:  ocamlfind(sexplib0)
BuildRequires:  ocamlfind(stdlib-shims)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(cinaps)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(re)
%endif

%description
The ppxlib project provides the basis for the ppx system, which is
currently the officially supported method for meta-programming in
OCaml. It offers a principled way to generate code at compile time in
OCaml projects.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q -n %pkg-%version

%build
dune_release_pkgs='ppxlib,ppxlib-tools'
%ocaml_dune_setup
%if "%build_flavor" == ""
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == ""
%ocaml_dune_install
%ocaml_create_file_list
%endif

%if "%build_flavor" == "testsuite"
%check
%ocaml_dune_test
%endif

%if "%build_flavor" == ""
%files -f %name.files
%defattr(-,root,root,-)
%_bindir/*

%files devel -f %name.files.devel
%defattr(-,root,root,-)

%endif

%changelog
