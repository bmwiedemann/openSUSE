#
# spec file for package ocaml-csexp
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


%bcond_with ocaml_csexp_testsuite
%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "testsuite"
%if %{without ocaml_csexp_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif

%define     pkg ocaml-csexp
Name:           %{pkg}%{nsuffix}
Version:        1.5.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Parsing and printing of S-expressions in Canonical form
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/csexp
Source0:        %{pkg}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409

%if "%{build_flavor}" == "testsuite"
BuildRequires:  ocamlfind(csexp)
BuildRequires:  ocamlfind(ppx_expect)
%endif

%description
This library provides minimal support for Canonical S-expressions. Canonical S-expressions are a binary encoding of S-expressions that is super simple and well suited for communication between programs.

This library only provides a few helpers for simple applications. If you need more advanced support, such as parsing from more fancy input sources, you should consider copying the code of this library given how simple parsing S-expressions in canonical form is.

To avoid a dependency on a particular S-expression library, the only module of this library is parameterised by the type of S-expressions.

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
dune_release_pkgs='csexp'
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
