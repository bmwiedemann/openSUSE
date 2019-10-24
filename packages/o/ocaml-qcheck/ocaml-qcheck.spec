#
# spec file for package ocaml-qcheck
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-qcheck
Version:        0.10
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        QuickCheck inspired property-based testing for OCaml
License:        BSD-2-Clause
Group:          Development/Languages/OCaml

URL:            https://github.com/c-cube/qcheck
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20190930
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(oUnit)
BuildRequires:  ocamlfind(unix)

%description
This module allows to check invariants (properties of some types) over
randomly generated instances of the type. It provides combinators for
generating instances and printing them.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%autosetup -p1

%build
# do not build alcotest support since it is not packaged yet
args='--for-release-of-packages=qcheck,qcheck-core,qcheck-ounit'
OCAML_DUNE_INSTALLED_LIBRARIES_ARGS=''
OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS="${args}"
OCAML_DUNE_BUILD_INSTALL_ARGS="${args}"
%ocaml_dune_setup
%ocaml_dune_build

%install
OCAML_DUNE_INSTALL_ARGS='qcheck qcheck-core qcheck-ounit'
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%license LICENSE
%doc README.adoc

%files devel -f %{name}.files.devel

%changelog
