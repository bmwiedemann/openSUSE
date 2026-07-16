#
# spec file for package opam-file-format
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


%bcond_with opam_file_format_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without opam_file_format_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg opam-file-format
Name:           %pkg%nsuffix
Version:        2.2.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Parser and printer for the opam file syntax
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
URL:            https://opam.ocaml.org/packages/opam-file-format/
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 3.13
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  ocamlfind(menhir)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(alcotest)
BuildRequires:  ocamlfind(fmt)
BuildRequires:  ocamlfind(opam-file-format) = %version
%endif

%description
This is a parser and a printer for the opam file syntax.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='opam-file-format'
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

%files devel -f %name.files.devel
%endif

%changelog
