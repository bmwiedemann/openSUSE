#
# spec file for package ocaml-cairo
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ocaml-cairo
Version:        0.6.4
Release:        0
Summary:        Binding to Cairo, a 2D Vector Graphics Library.  
License:        LGPL-3.0-or-later
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/cairo2
Source:         %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  ocamlfind(str)
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)

%description
This is an OCaml binding for the Cairo library, a 2D graphics library with support for multiple output devices.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
Requires:       pkgconfig(cairo)

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='cairo2'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
dune_test_tolerate_fail='dune_test_tolerate_fail issue#19'
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel

%changelog
