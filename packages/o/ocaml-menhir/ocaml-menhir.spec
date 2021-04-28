#
# spec file for package ocaml-menhir
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-menhir
Version:        20210310
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        LR(1) parser generator for the OCaml programming language
License:        LGPL-2.0
Group:          Development/Languages/OCaml
Url:            https://opam.ocaml.org/packages/menhir
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  time
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(unix)

%description
LR(1) parser generator

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
dune_release_pkgs='menhir,menhirLib,menhirSdk'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ifarch x86_64
%else
dune_test_tolerate_fail='dune_test_tolerate_fail bitsize'
%endif
%ocaml_dune_test

%files -f %{name}.files
%{_bindir}/*
%{_mandir}/*/*

%files devel -f %{name}.files.devel

%changelog
