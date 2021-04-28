#
# spec file for package ocaml-camlbz2
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


Name:           ocaml-camlbz2
Version:        0.7.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml bindings for bz2
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/camlbz2
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-camlbz2.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(stdlib-shims)
BuildRequires:  pkgconfig(bzip2)

%description
OCaml bindings for libbz (AKA, bzip2).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       pkgconfig(bzip2)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='bz2'
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
