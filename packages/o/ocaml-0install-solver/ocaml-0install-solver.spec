#
# spec file for package ocaml-0install-solver
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


%bcond_with ocaml_0install_solver_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_0install_solver_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif

%define     pkg ocaml-0install-solver
Name:           %pkg%nsuffix
Version:        2.18
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Package dependency solver
License:        LGPL-2.1-or-later
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/0install-solver
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 2.5
BuildRequires:  ocaml-rpm-macros >= 20231101

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(0install-solver)
%endif
%description
A package dependency resolver based on a SAT solver. This was
originally written for the 0install package manager, but is now
generic and is also used as a solver backend for opam. The SAT solver
is based on MiniSat and the application to package management is based
on OPIUM (Optimal Package Install/Uninstall Manager). 0install-solver
uses a (novel?) strategy to find the optimal solution extremely
quickly (even for a SAT-based solver).

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
dune_release_pkgs='0install-solver'
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
