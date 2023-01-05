#
# spec file for package ocaml-qcheck
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


%bcond_with ocaml_qcheck_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_qcheck_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-qcheck
Name:           %pkg%nsuffix
Version:        0.20
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        QuickCheck inspired property-based testing for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/qcheck
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 2.2
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(ppx_deriving)
BuildRequires:  ocamlfind(unix)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(alcotest)
BuildRequires:  ocamlfind(qcheck)
%endif

%description
This module allows to check invariants (properties of some types) over
randomly generated instances of the type. It provides combinators for
generating instances and printing them.

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
dune_release_pkgs='qcheck,qcheck-core,qcheck-ounit,ppx_deriving_qcheck'
%if "%build_flavor" == "testsuite"
dune_release_pkgs="${dune_release_pkgs},qcheck-alcotest"
%endif
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
%doc README.adoc

%files devel -f %name.files.devel
%endif

%changelog
