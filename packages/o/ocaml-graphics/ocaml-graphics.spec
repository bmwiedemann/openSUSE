#
# spec file for package ocaml-graphics
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


Name:           ocaml-graphics
Version:        5.2.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        The OCaml graphics library
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
URL:            https://opam.ocaml.org/packages/graphics/
Source:         %name-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version)  >= 4.09
BuildRequires:  ocaml-dune >= 2.1
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)

%description
The graphics library provides a set of portable drawing
primitives. Drawing takes place in a separate window that is created
when Graphics.open_graph is called.

This library used to be distributed with OCaml up to OCaml 4.08.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xft)
Provides:       ocaml-x11 = %version-%release
Obsoletes:      ocaml-x11 < %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='graphics'
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

