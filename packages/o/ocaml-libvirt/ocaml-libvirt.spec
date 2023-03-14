#
# spec file for package ocaml-libvirt
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


Name:           ocaml-libvirt
Version:        0.6.1.7
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml binding for libvirt
License:        LGPL-2.0-or-later
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/libvirt
Source0:        %name-%version.tar.xz
Patch0:         ocaml-libvirt.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  perl
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(unix)
BuildRequires:  pkgconfig(libvirt)

%description
OCaml binding for libvirt.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
Requires:       pkgconfig(libvirt)

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='libvirt'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
dune_test_tolerate_fail='dune_test_tolerate_fail'
%ocaml_dune_test

%files -f %name.files
%_bindir/*

%files devel -f %name.files.devel

%changelog
