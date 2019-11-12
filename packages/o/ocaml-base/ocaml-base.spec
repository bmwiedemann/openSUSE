#
# spec file for package ocaml-base
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-base
Version:        0.12.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Standard library for OCaml
License:        MIT
Group:          Development/Languages/OCaml
Url:            https://github.com/janestreet/base
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.04
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocamlfind(compiler-libs.bytecomp)
BuildRequires:  ocamlfind(compiler-libs.common)
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(sexplib0)
BuildRequires:  ocamlfind(str)

%description
Base is a standard library for OCaml. It provides a standard set of general purpose modules that are well-tested, performant, and fully-portable across any environment that can run OCaml code. Unlike other standard library projects, Base is meant to be used as a wholesale replacement of the standard library distributed with the OCaml compiler. In particular it makes different choices and doesn’t re-export features that are not fully portable such as I/O, which are left to other libraries.

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
dune_release_pkgs='base'
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
