#
# spec file for package ocaml-integers
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

Name:           ocaml-integers
Version:        0.4.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Various signed and unsigned integer types for OCaml
License:        MIT
Group:          Development/Languages/OCaml

URL:            https://github.com/ocamllabs/ocaml-integers
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210121

%description
The ocaml-integers library provides a number of 8-, 16-, 32- and 64-bit
signed and unsigned integer types, together with aliases such as long
and size_t whose sizes depend on the host platform.

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
dune_release_pkgs='integers'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%doc README.md CHANGES.md

%files devel -f %{name}.files.devel

%changelog
