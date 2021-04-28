#
# spec file for package ocaml-mccs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 The openSUSE Project.
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


Name:           ocaml-mccs
Version:        1.1+13
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stripped-down version of mccs with OCaml bindings
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND BSD-3-Clause AND GPL-3.0-only
Group:          Development/Languages/Other
Url:            https://github.com/AltGr/ocaml-mccs
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}.patch
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(cudf)

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem solver
developed at UNS during the European MANCOOSI project.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='mccs'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md

%files devel -f %{name}.files.devel

%changelog
