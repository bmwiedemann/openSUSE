#
# spec file for package ocaml-re
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%bcond_with ocaml_re_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_re_testsuite}
ExclusiveArch:  do-not-build
%else
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
%endif

%define     pkg ocaml-re
Name:           %pkg%nsuffix
Version:        1.14.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Pure OCaml regular expressions
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/re
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.12
BuildRequires:  ocaml-dune >= 3.15
BuildRequires:  ocaml-rpm-macros >= 20240909

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(base)
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(ppx_expect)
BuildRequires:  ocamlfind(re)
%endif

%description
Pure OCaml regular expressions, with support for Perl and POSIX-style strings.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='re'
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
