#
# spec file for package ocaml-checkseum
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


%bcond_with ocaml_checkseum_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without ocaml_checkseum_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
%define nsuffix %nil
%endif

%define     pkg ocaml-checkseum
Name:           %pkg%nsuffix
Version:        0.5.3
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Adler-32, CRC32 and CRC32-C implementation
License:        ISC
URL:            https://opam.ocaml.org/packages/checkseum/
Source0:        %pkg-%version.tar.xz
BuildRequires:  ocaml(ocaml_base_version) >= 4.07
BuildRequires:  ocaml-dune >= 2.6
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  ocamlfind(dune-configurator)
BuildRequires:  ocamlfind(optint)

%if "%build_flavor" == "testsuite"
BuildRequires:  ocamlfind(alcotest)
BuildRequires:  ocamlfind(astring)
BuildRequires:  ocamlfind(bos)
BuildRequires:  ocamlfind(checkseum) = %version
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(fmt)
BuildRequires:  ocamlfind(fpath)
BuildRequires:  ocamlfind(rresult)
%endif

%description
Checkseum is a library to provide implementation of Adler-32, CRC32 and CRC32-C.

%package        devel
Summary:        Development files for %name
Requires:       %name = %version-%release

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1 -n %pkg-%version

%build
dune_release_pkgs='checkseum'
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
