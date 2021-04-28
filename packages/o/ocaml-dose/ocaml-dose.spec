#
# spec file for package ocaml-dose
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


%bcond_with ocaml_dose_testsuite
%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "testsuite"
%if %{without ocaml_dose_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif

%define     pkg ocaml-dose
Name:           %{pkg}%{nsuffix}
Version:        6.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        An OCaml dependency toolkit
License:        LGPL-3.0-or-later
URL:            https://opam.ocaml.org/packages/dose3
Source0:        %{pkg}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20210409
%if 1
BuildRequires:  ocamlfind(base64)
BuildRequires:  ocamlfind(bz2)
BuildRequires:  ocamlfind(cudf)
BuildRequires:  ocamlfind(extlib)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(ocamlgraph)
BuildRequires:  ocamlfind(parmap)
BuildRequires:  ocamlfind(re.pcre)
BuildRequires:  ocamlfind(zip)
%endif

%if "%{build_flavor}" == "testsuite"
BuildRequires:  dctrl-tools
BuildRequires:  dpkg
BuildRequires:  git-core
BuildRequires:  ocamlfind(dose3)
BuildRequires:  ocamlfind(oUnit)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-PyYAML
%endif

%description
Dose3 is a framework made of several OCaml libraries for managing distribution
packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems (monitoring
package evolutions, correct and complete dependency resolution, repository-wide
uninstallability checks).

%package devel
Summary:        An OCaml dependency toolkit -- Development files
Requires:       %{name} = %{version}

%description devel
This package contains development files for package %{name}.

%prep
%autosetup -p1 -n %{pkg}-%{version}

%build
dune_release_pkgs='dose3'
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
git --no-pager config --global user.email 'you@example.com'
git --no-pager config --global user.name  'Your Name'
git --no-pager init .
git --no-pager add .
git --no-pager commit -m '%{version}'
git --no-pager tag '%{version}'
%ocaml_dune_test
%endif

%if "%{build_flavor}" == ""
%files -f %{name}.files
%{_bindir}/*

%files devel -f %{name}.files.devel

%endif

%changelog
