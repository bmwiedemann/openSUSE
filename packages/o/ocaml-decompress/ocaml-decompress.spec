#
# spec file for package ocaml-decompress
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_with ocaml_decompress_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_decompress_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg ocaml-decompress
Name:           %pkg%nsuffix
Version:        1.6.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Implementation of Zlib and GZip
License:        ISC
URL:            https://opam.ocaml.org/packages/decompress/
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.08
BuildRequires:  ocaml-dune >= 2.9
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  ocamlfind(cmdliner)
BuildRequires:  ocamlfind(optint)
BuildRequires:  ocamlfind(checkseum)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(alcotest)
BuildRequires:  ocamlfind(base64)
BuildRequires:  ocamlfind(bstr)
BuildRequires:  ocamlfind(bytesrw)
BuildRequires:  ocamlfind(camlzip)
BuildRequires:  ocamlfind(crowbar)
BuildRequires:  ocamlfind(decompress) = %version
BuildRequires:  ocamlfind(fmt)
%endif

%description
Decompress is an implementation of Zlib and GZip.

It provides a pure non-blocking interface to inflate and deflate data flow.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='decompress'
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
%_bindir/*

%files devel -f %name.files.devel

%endif

%changelog
