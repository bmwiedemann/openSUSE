#
# spec file for package ocaml-logs
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ocaml-logs
Version:        0.6.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Logging infrastructure for OCaml
License:        ISC
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/logs
Source0:        %{name}-%{version}.tar.xz
Patch0:         ocaml-logs.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(compiler-libs.toplevel)
BuildRequires:  ocamlfind(fmt)
BuildRequires:  ocamlfind(result)
BuildRequires:  ocamlfind(threads)

%description
Logs provides a logging infrastructure for OCaml. Logging is performed on sources whose reporting level can be set independently. Log message report is decoupled from logging and is handled by a reporter.

A few optional log reporters are distributed with the base library and the API easily allows to implement your own.

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
dune_release_pkgs='logs'
mv opam ${dune_release_pkgs}.opam
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
