#
# spec file for package ocaml-parmap
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           ocaml-cmdliner
Version:        1.0.4
Release:        0
%{?ocaml_preserve_bytecode}
License:        ISC
Summary:        Declarative definition of command line interfaces for OCaml
Url:            https://github.com/dbuenzli/cmdliner
Group:          Development/Languages/OCaml
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101

%description
Cmdliner is a module for the declarative definition of command line interfaces.

It provides a simple and compositional mechanism to convert command line
arguments to OCaml values and pass them to your functions. The module
automatically handles syntax errors, help messages and UNIX man page
generation. It supports programs with single or multiple commands and respects
most of the POSIX and GNU conventions.

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
dune_release_pkgs='cmdliner'
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
