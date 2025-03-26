#
# spec file for package ocaml-opam-0install-cudf
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


%bcond_with ocaml_opam_0install_cudf_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_opam_0install_cudf_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif

%define     pkg ocaml-opam-0install-cudf
Name:           %pkg%nsuffix
Version:        0.5.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        JSON parsing and pretty-printing library
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/opam-0install-cudf
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20231101
BuildRequires:  ocamlfind(0install-solver)
BuildRequires:  ocamlfind(cudf)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(opam-0install-cudf)
BuildRequires:  ocamlfind(alcotest)
%endif
%description
Yojson is an optimized parsing and printing library for the JSON format. It
addresses a few shortcomings of json-wheel including 2x speedup, polymorphic
variants and optional syntax for tuples and variants.

ydump is a pretty-printing command-line program provided with the yojson
package.

The program atdgen can be used to derive OCaml-JSON serializers and
deserializers from type definitions. 

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
dune_release_pkgs='opam-0install-cudf'
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
%doc README.md

%files devel -f %name.files.devel

%endif

%changelog
