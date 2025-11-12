#
# spec file for package ocaml-ctypes
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_with ocaml_ctypes_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_ctypes_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg ocaml-ctypes
Name:           %pkg%nsuffix
Version:        0.24.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Combinators for binding to C libraries without writing any C
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/ctypes
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 3.9
BuildRequires:  ocaml-rpm-macros >= 20240909
BuildRequires:  ocamlfind(bisect_ppx)
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(integers)
BuildRequires:  pkgconfig(libffi)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(ctypes)
BuildRequires:  ocamlfind(oUnit)
%endif

%description
ctypes is a library for binding to C libraries using pure OCaml. The primary aim is to make writing C extensions as straightforward as possible.

The core of ctypes is a set of combinators for describing the structure of C types -- numeric types, arrays, pointers, structs, unions and functions. You can use these combinators to describe the types of the functions that you want to call, then bind directly to those functions -- all without writing or generating any C!

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
head -n4 dune > $$
mv $$ dune
dune_release_pkgs='ctypes,ctypes-foreign'
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

%files devel -f %name.files.devel
%defattr(-,root,root,-)

%endif

%changelog
