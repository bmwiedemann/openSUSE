#
# spec file for package ocaml-camlzip
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ocaml-camlzip
Version:        1.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml ZIP interface
License:        LGPL-2.1+
Group:          Development/Languages/OCaml
Url:            https://github.com/xavierleroy/camlzip
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This OCaml library provides easy access to compressed files in ZIP
and GZIP format, as well as to Java JAR files. It provides functions
for reading from and writing to compressed files in these formats.

%package devel
Summary:        Devel files for OCaml ZIP
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       pkgconfig(zlib)

%description devel
Development file for the OCaml ZIP interface

%package        test
Summary:        Testcases for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    test
This package contains testcases to verify %{name} functionality.

%prep
%autosetup -p1

%build
tee _oasis <<_EOF_
OASISFormat: 0.4
Name:        zip
Version:     %{version}
Synopsis:    OCaml ZIP interface
Authors:     Xavier.Leroy@inria.fr
LicenseFile: LICENSE
License:     %{license}
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library zip
 Path:            .
 Modules:         Zip, Gzip, Zlib
 BuildDepends:    unix
 CSources:        zlibstubs.c
 CCOpt:           %{optflags} -fPIC `pkg-config --cflags zlib`
 CCLib:           `pkg-config --libs zlib`

Document "zip"
 Title:                API reference for zip
 Type:                 ocamlbuild (0.1.0)
 BuildTools+:          ocamldoc
 Install:              true
 InstallDir:           \$htmldir
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: zip

Executable "%{name}-test-minigzip"
 Install: true
 Path: test
 MainIs: minigzip.ml
 CompiledObject: best
 BuildDepends: zip

Executable "%{name}-test-minigip"
 Install: true
 Path: test
 MainIs: minizip.ml
 CompiledObject: best
 BuildDepends: zip

Executable "%{name}-test-testzlib"
 Install: true
 Path: test
 MainIs: testzlib.ml
 CompiledObject: best
 BuildDepends: zip
_EOF_
oasis setup-clean
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
%ocaml_create_file_list

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files test
%{_bindir}/*

%files -f %{name}.files
%doc Changes

%files devel -f %{name}.files.devel
%{oasis_docdir_html}

%changelog
