#
# spec file for package ocaml-fileutils
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

%define     pkg ocaml-fileutils
Name:           %pkg%nsuffix
Version:        0.6.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml library for common file and filename operations
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/fileutils
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(seq)
BuildRequires:  ocamlfind(stdlib-shims)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(unix)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(fileutils)
BuildRequires:  ocamlfind(ounit2)
BuildRequires:  ocamlfind(stdlib-shims)
%endif

%description
This library is intended to provide a basic interface to the most
common file and filename operations.  It provides several different
filename functions: reduce, make_absolute, make_relative...  It also
enables you to manipulate real files: cp, mv, rm, touch...

It is separated into two modules: SysUtil and SysPath.  The first one
manipulates real files, the second one is made for manipulating
abstract filenames.

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
dune_release_pkgs='fileutils'
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
