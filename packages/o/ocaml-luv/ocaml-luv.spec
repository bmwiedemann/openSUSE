#
# spec file for package ocaml-luv
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with ocaml_luv_testsuite
%define build_flavor @BUILD_FLAVOR@%{nil}
%if "%{build_flavor}" == "testsuite"
%if %{without ocaml_luv_testsuite}
ExclusiveArch:  do-not-build
%endif
%define nsuffix -testsuite
%else
%define nsuffix %{nil}
%endif

%define     pkg ocaml-luv
Name:           %{pkg}%{nsuffix}
Version:        0.5.7
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Binding to libuv cross-platform asynchronous I/O
License:        MIT
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/luv
Source0:        %{pkg}-%{version}.tar.xz
Patch0:         %{pkg}.patch
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(ctypes)
BuildRequires:  ocamlfind(result)
BuildRequires:  pkgconfig(libuv)

%if "%{build_flavor}" == "testsuite"
BuildRequires:  ocamlfind(luv)
BuildRequires:  ocamlfind(alcotest)
%endif

%description
Luv is a binding to libuv, the cross-platform C library that does
asynchronous I/O in Node.js and runs its main loop.

Besides asynchronous I/O, libuv also supports multiprocessing and
multithreading. Multiple event loops can be run in different threads. libuv also
exposes a lot of other functionality, amounting to a full OS API, and an
alternative to the standard module Unix.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}
Requires:       pkgconfig(libuv)

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{pkg}-%{version}

%build
export LUV_USE_SYSTEM_LIBUV=yes
dune_release_pkgs='luv'
%ocaml_dune_setup
%if "%{build_flavor}" == ""
%ocaml_dune_build
%endif

%install
%if "%{build_flavor}" == ""
export LUV_USE_SYSTEM_LIBUV=yes
%ocaml_dune_install
%ocaml_create_file_list
%endif

%if "%{build_flavor}" == "testsuite"
%check
exit 0
export LUV_USE_SYSTEM_LIBUV=yes
%ocaml_dune_test
%endif

%if "%{build_flavor}" == ""
%files -f %{name}.files

%files devel -f %{name}.files.devel

%endif

%changelog
