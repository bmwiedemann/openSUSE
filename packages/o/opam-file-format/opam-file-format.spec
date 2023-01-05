#
# spec file for package opam-file-format
#
# Copyright (c) 2023 SUSE LLC
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
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg opam-file-format
Name:           %pkg%nsuffix
Version:        2.1.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Parser and printer for the opam file syntax
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(alcotest)
BuildRequires:  ocamlfind(opam-file-format)
%endif

%description
This is a parser and a printer for the opam file syntax.

%package devel
Summary:        Development files for the opam file syntax parser
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description devel
This is a parser and a printer for the opam file syntax.

This package contains development files for package %name.

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
