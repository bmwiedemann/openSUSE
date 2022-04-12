#
# spec file for package ocaml-pp
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with ocaml_pp_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_pp_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-pp
Name:           %pkg%nsuffix
Version:        1.1.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Pretty-printing library
License:        MIT
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            https://opam.ocaml.org/packages/pp
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml-dune >= 2.0
BuildRequires:  ocaml-rpm-macros >= 20220409
BuildRequires:  ocaml(ocaml_base_version) >= 4.08

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(pp)
BuildRequires:  ocamlfind(ppx_expect)
%endif

%description
This library provides a lean alternative to the Format 1 module of the OCaml standard library.

Pp uses the same concepts of boxes and break hints, and the final rendering is done to formatter from the Format module.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup -q -n %pkg-%version

%build
dune_release_pkgs='pp'
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
%defattr(-,root,root,-)

%files devel -f %name.files.devel
%defattr(-,root,root,-)

%endif

%changelog
