#
# spec file for package ocaml-bos
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


Name:           ocaml-bos
Version:        0.2.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Basic OS interaction for OCaml
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/bos
Source0:        %name-%version.tar.xz
Patch0:         ocaml-bos.patch
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(astring)
BuildRequires:  ocamlfind(compiler-libs)
BuildRequires:  ocamlfind(fmt)
BuildRequires:  ocamlfind(fpath)
BuildRequires:  ocamlfind(logs)
BuildRequires:  ocamlfind(rresult)
BuildRequires:  ocamlfind(unix)

%description
Bos provides support for basic and robust interaction with the operating system 
in OCaml. It has functions to access the process environment, parse command line 
arguments, interact with the file system and run command line programs.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
dune_release_pkgs='bos'
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
