#
# spec file for package ocaml-bisect_ppx
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


%bcond_with ocaml_bisect_ppx_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_bisect_ppx_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-bisect_ppx
Name:           %pkg%nsuffix
Version:        2.8.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Code coverage for OCaml and Reason
License:        GPL-2.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/bisect_ppx
Source0:        %pkg-%version.tar.xz
Patch0:         %pkg.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20230101
%if 1
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(ppxlib)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(unix)
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  git-core
BuildRequires:  ocamlfind(bisect_ppx)
BuildRequires:  ocamlfind(ocamlformat)
%endif

%description
Bisect_ppx is a code coverage tool for OCaml and Reason. It helps you test thoroughly by showing what's not tested.

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
dune_release_pkgs='bisect_ppx'
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
%doc doc/CHANGES
%_bindir/*

%files devel -f %name.files.devel

%endif

%changelog
