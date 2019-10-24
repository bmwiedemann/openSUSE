#
# spec file for package ocaml-rope
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


Name:           ocaml-rope
Version:        0.6.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Ropes ("heavyweight strings") for OCaml
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml

URL:            http://rope.forge.ocamlcore.org/
Source0:        https://github.com/Chris00/ocaml-rope/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20190930
BuildRequires:  ocamlfind(benchmark)
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(compiler-libs.toplevel)

%description
Ropes ("heavyweight strings") are a scalable string implementation:
they are designed for efficient operation that involve the string as
a whole. Operations such as concatenation, and substring take time
that is nearly independent of the length of the string. Unlike
strings, ropes are a reasonable representation for very long strings
such as edit buffers or mail messages.


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
%ocaml_dune_test

%files -f %{name}.files
%license LICENSE.md
%doc README.md

%files devel -f %{name}.files.devel

%changelog
