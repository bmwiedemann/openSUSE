#
# spec file for package ocaml-gen
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


%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "testsuite"
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif

%define     pkg ocaml-gen
Name:           %{pkg}%{nsuffix}
Version:        0.5.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Simple, efficient iterators for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/gen
Source0:        %{pkg}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
%if 1
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(dune.configurator)
%endif

%if "%{build_flavor}" == "testsuite"
BuildRequires:  ocamlfind(gen)
BuildRequires:  ocamlfind(oUnit)
BuildRequires:  ocamlfind(qcheck)
BuildRequires:  ocamlfind(qtest)
%endif

%description
Iterators for OCaml, both restartable and consumable.
The implementation keeps a good balance between simplicity and performance.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{pkg}-%{version}

%build
dune_release_pkgs='gen'
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
%doc README.md

%files devel -f %{name}.files.devel

%endif

%changelog
