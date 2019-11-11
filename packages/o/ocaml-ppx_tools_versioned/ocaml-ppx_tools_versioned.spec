#
# spec file for package ocaml-ppx_tools_versioned
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


Name:           ocaml-ppx_tools_versioned
Version:        5.2.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Tools for authors of ppx rewriters
License:        MIT
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-ppx/ppx_tools_versioned
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocamlfind(ocaml-migrate-parsetree)

%description
A variant of ppx_tools based on ocaml-migrate-parsetree.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
dune_release_pkgs='ppx_tools_versioned'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md

%files devel -f %{name}.files.devel

%changelog
