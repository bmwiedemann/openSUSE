#
# spec file for package ocaml-bigarray-compat
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


Name:           ocaml-bigarray-compat
Version:        1.0.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Expose Stdlib.Bigarray
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/bigarray-compat
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210407

%description
A library that exposes Stdlib.Bigarray when possible (>= 4.07) but can fallback to Bigarray. The compability bigarray module is exposed under Bigarray_compat.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='bigarray-compat'
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

