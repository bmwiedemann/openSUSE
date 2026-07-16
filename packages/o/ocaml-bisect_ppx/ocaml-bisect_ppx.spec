#
# spec file for package ocaml-bisect_ppx
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with ocaml_bisect_ppx_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_bisect_ppx_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg ocaml-bisect_ppx
Name:           %pkg%nsuffix
Version:        2.8.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Code coverage for OCaml and Reason
License:        GPL-2.0-only
URL:            https://opam.ocaml.org/packages/bisect_ppx/
Source0:        %pkg-%version.tar.xz
Patch4480001:   e30265643e77bcf2c9eba7322429c779122106fc.patch
Patch4480003:   f35fdf4bdcb82c308d70f7c9c313a77777f54bdf.patch
Patch4480006:   07bfceec652773de4b140cebc236a15e2429809e.patch
Patch4480007:   4f0cb2a2e1b0b786b6b5f1c94985b201aa012f12.patch
Patch4480009:   2d8dffbbfc0c431a37319d4d9a143836c9ec542e.patch
Patch4480010:   ebb352612bf32d74f26a9318dc668a54872b0cad.patch
Patch4480011:   a0ff8cf6ea06d7f052c8d0fceac92a42d57e7809.patch
Patch4480012:   a64e135a91b6fedbc25c743816b6208f7e5874c4.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 3.0
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(ppxlib) >= 0.36.0

%if "%build_flavor" == "testsuite"
BuildRequires:  git-core
BuildRequires:  ocamlfind(bisect_ppx) = %version
BuildRequires:  ocamlfind(ocamlformat)
%endif

%description
Bisect_ppx is a code coverage tool for OCaml and Reason. It helps you test thoroughly by showing what's not tested.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='bisect_ppx'
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
%doc doc/CHANGES
%_bindir/*

%files devel -f %name.files.devel

%endif

%changelog
