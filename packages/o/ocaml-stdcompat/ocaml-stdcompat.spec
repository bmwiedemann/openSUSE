#
# spec file for package ocaml-stdcompat
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ocaml-stdcompat
Version:        21.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stdcompat: compatibility module for OCaml standard library 
License:        BSD-2-Clause
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
URL:            https://opam.ocaml.org/packages/stdcompat/
Source0:        %name-%version.tar.xz
Source1:        %name-rpmlintrc
Patch0:         5ce5b7819b39c654ef90f890f5f0c71b5d0107fb.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  ocaml(ocaml_base_version) >= 4.11
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-rpm-macros >= 20260707

%description
Stdcompat is a compatibility layer allowing programs to use some recent additions to the OCaml standard library while preserving the ability to be compiled on former versions of OCaml.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
autoreconf -fi
dune_release_pkgs='stdcompat'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
echo '/* dummy %name */' > %buildroot%ocaml_standard_library/${dune_release_pkgs}/stdcompat.h
%ocaml_create_file_list

%files -f %name.files

%files devel -f %name.files.devel

%changelog
