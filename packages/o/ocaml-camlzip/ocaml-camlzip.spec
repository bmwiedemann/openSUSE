#
# spec file for package ocaml-camlzip
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


Name:           ocaml-camlzip
Version:        1.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml ZIP interface
License:        LGPL-2.1-or-later
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/camlzip
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-camlzip.patch
Provides:       ocaml-camlzip-test = %{version}-%{release}
Obsoletes:      ocaml-camlzip-test < %{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(stdlib-shims)
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)

%description
This OCaml library provides easy access to compressed files in ZIP
and GZIP format, as well as to Java JAR files. It provides functions
for reading from and writing to compressed files in these formats.

%package devel
Summary:        Devel files for OCaml ZIP
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       pkgconfig(zlib)

%description devel
Development file for the OCaml ZIP interface

%prep
%autosetup -p1

%build
dune_release_pkgs='zip'
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
