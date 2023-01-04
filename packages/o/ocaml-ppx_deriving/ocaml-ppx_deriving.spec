#
# spec file for package ocaml-ppx_deriving
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


%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-ppx_deriving
Name:           %pkg%nsuffix
Version:        5.2.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Type-driven code generation
License:        MIT
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/ppx_deriving
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
%if 1
BuildRequires:  ocamlfind(cppo)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(ppx_derivers)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(result)
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(ppx_deriving)
%endif

%description
ppx_deriving provides common infrastructure for generating
code based on type definitions, and a set of useful plugins
for common tasks.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='ppx_deriving'
%ocaml_dune_setup
%if "%build_flavor" == ""
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == ""
%ocaml_dune_install
%ocaml_create_file_list
tools='
ppx_deriving
'
d="$(ocamlc -where)/ppx_deriving"
for i in ${tools}
do
echo "${d}/${i}" >> %name.files.devel
done
%endif

%if "%build_flavor" == "testsuite"
%check
%ocaml_dune_test
%endif

%if "%build_flavor" == ""
%files -f %name.files

%files devel -f %name.files.devel

%endif

%changelog
