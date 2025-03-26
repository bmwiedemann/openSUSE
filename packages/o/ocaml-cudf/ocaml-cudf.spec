#
# spec file for package ocaml-cudf
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


%bcond_with ocaml_cudf_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_cudf_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif

%define     pkg ocaml-cudf
Name:           %pkg%nsuffix
Version:        0.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml CUDF library
License:        GPL-3.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/cudf
Source0:        %pkg-%version.tar.xz
Patch0:         allow_underscore.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20231101
BuildRequires:  ocamlfind(extlib)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(cudf)
BuildRequires:  ocamlfind(ounit2)
%endif
%description
CUDF (for Common Upgradeability Description Format) is a format for describing upgrade scenarios in package-based Free and Open Source Software distribution. This is reference implementation in Ocaml.

%package devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='cudf'
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
%_bindir/*

%files devel -f %name.files.devel

%endif

%changelog
