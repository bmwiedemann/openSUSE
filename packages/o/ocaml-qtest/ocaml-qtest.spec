#
# spec file for package ocaml-qtest
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


Name:           ocaml-qtest
Version:        2.9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Inline (Unit) Tests for OCaml
License:        GPL-3.0-or-later
Group:          Development/Languages/OCaml

URL:            https://github.com/vincent-hugot/qtest
Source0:        %{name}-%{version}.tar.xz

BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20190930
BuildRequires:  ocamlfind(qcheck)

%description
qtest extracts inline unit tests written using a special syntax in
comments. Those tests are then run using the oUnit framework and the
qcheck library. The possibilities range from trivial tests
to sophisticated random generation of test cases.


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
%license LICENSE
%doc README.adoc
%{_bindir}/*

%files devel -f %{name}.files.devel

%changelog
