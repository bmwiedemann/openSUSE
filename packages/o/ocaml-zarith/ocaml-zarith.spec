#
# spec file for package ocaml-zarith
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


Name:           ocaml-zarith
Version:        1.12
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Arbitrary precision integers
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/zarith
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}.patch
BuildRequires:  gmp-devel
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocaml(ocaml_base_version) >= 4.04
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(ocamldoc)
BuildRequires:  ocamlfind(str)

%description
The Zarith library implements arithmetic and logical operations over arbitrary-precision integers and rational numbers.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       gmp-devel

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='zarith'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
