#
# spec file for package ocaml-swhid_core
#
# Copyright (c) 2025 SUSE LLC
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


Name:           ocaml-swhid_core
Version:        0.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        library to work with swhids
License:        ISC
URL:            https://opam.ocaml.org/packages/swhid_core
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20231101

%description
swhid_core is an OCaml library to with with Software Heritage
persistent identifiers (swhids).

%package        devel
Summary:        Development files for %name
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='swhid_core'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel

%changelog
