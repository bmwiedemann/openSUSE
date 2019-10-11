#
# spec file for package ocaml-stdlib-shims
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


Name:           ocaml-stdlib-shims
Version:        0.1.0
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Shim to substitute Pervasives with Stdlib before 4.08
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml/stdlib-shims
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191004

%description
Compiling against this library allows replacing uses of Pervasives
with Stdlib before 4.08. For example, one can use Stdlib.compare
instead of Pervasives.compare. It does not, however, provide
the new functions and modules that were added in the Stdlib module.

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
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test || : make check failed

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
