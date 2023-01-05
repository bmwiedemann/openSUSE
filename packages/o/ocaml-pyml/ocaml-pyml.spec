#
# spec file for package ocaml-pyml
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


%bcond_with ocaml_pyml_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_pyml_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-pyml
Name:           %pkg%nsuffix
Version:        20220905
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stdcompat: compatibility module for OCaml standard library
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/pyml
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  ocamlfind(unix)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(pyml)
%if 0%{?suse_version} > 1315
BuildRequires:  python3-numpy
%else
BuildRequires:  python-numpy
%endif
BuildRequires:  which
%endif

%description
Stdcompat is a compatibility layer allowing programs to use some recent additions to the OCaml standard library while preserving the ability to be compiled on former versions of OCaml.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version
Requires:       which

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='pyml'
%ocaml_dune_setup
%if "%build_flavor" == ""
%ocaml_dune_build
%endif

%install
%if "%build_flavor" == ""
%ocaml_dune_install
%ocaml_create_file_list
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
