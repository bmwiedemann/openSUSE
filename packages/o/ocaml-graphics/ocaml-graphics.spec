#
# spec file for package ocaml-graphics
#
# Copyright (c) 2022 SUSE LLC
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
Version:        5.1.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        The OCaml graphics library
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml/graphics
Source:         %name-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version)  >= 4.09
BuildRequires:  ocaml-dune >= 2.1
BuildRequires:  ocaml-rpm-macros >= 20220409
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  pkgconfig(x11)

%description
The graphics library provides a set of portable drawing
primitives. Drawing takes place in a separate window that is created
when Graphics.open_graph is called.

This library used to be distributed with OCaml up to OCaml 4.08.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
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

