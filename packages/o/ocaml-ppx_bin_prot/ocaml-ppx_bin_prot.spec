#
# spec file for package ocaml-ppx_bin_prot
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with ocaml_ppx_bin_prot_testsuite
%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "testsuite"
%if %{without ocaml_ppx_bin_prot_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif

%define     pkg ocaml-ppx_bin_prot
Name:           %{pkg}%{nsuffix}
Version:        0.14.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Generation of bin_prot readers and writers from types
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/ppx_bin_prot
Source0:        %{pkg}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
%if 1
BuildRequires:  ocamlfind(base)
BuildRequires:  ocamlfind(bin_prot)
BuildRequires:  ocamlfind(compiler-libs.common)
BuildRequires:  ocamlfind(ppx_here.expander)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(ppxlib.metaquot)
%endif

%if "%{build_flavor}" == "testsuite"
BuildRequires:  ocamlfind(core)
BuildRequires:  ocamlfind(core_bench)
BuildRequires:  ocamlfind(oUnit)
BuildRequires:  ocamlfind(ppx_bin_prot)
BuildRequires:  ocamlfind(ppx_jane)
%endif

%description
Generation of binary serialization and deserialization functions from type definitions.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n %{pkg}-%{version}

%build
dune_release_pkgs='ppx_bin_prot'
%ocaml_dune_setup
%if "%{build_flavor}" == ""
%ocaml_dune_build
%endif

%install
%if "%{build_flavor}" == ""
%ocaml_dune_install
%ocaml_create_file_list
%endif

%if "%{build_flavor}" == "testsuite"
%check
%ocaml_dune_test
%endif

%if "%{build_flavor}" == ""
%files -f %{name}.files
%defattr(-,root,root,-)

%files devel -f %{name}.files.devel
%defattr(-,root,root,-)

%endif

%changelog
