#
# spec file for package ocaml-cudf
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


Name:           ocaml-cudf
Version:        0.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ocaml CUDF library
License:        GPL-3.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/cudf
Source0:        %{name}-%{version}.tar.xz
Patch0:         allow_underscore.patch
Patch1:         ocaml-cudf.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(extlib)
BuildRequires:  ocamlfind(stdlib-shims)

%description
CUDF (for Common Upgradeability Description Format) is a format for describing upgrade scenarios in package-based Free and Open Source Software distribution. This is reference implementation in Ocaml.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='cudf'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%{_bindir}/*

%files devel -f %{name}.files.devel

%changelog
