#
# spec file for package ocaml-mccs
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 The openSUSE Project.
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


Name:           ocaml-mccs
Version:        1.1+9
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stripped-down version of mccs with OCaml bindings
License:        LGPL-2.1-only WITH OCaml-LGPL-linking-exception AND BSD-3-Clause AND GPL-3.0-only
Group:          Development/Languages/Other
Url:            https://github.com/AltGr/ocaml-mccs
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  ocaml
BuildRequires:  ocaml-cudf-devel
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros
BuildRequires:  ocamlfind

%description
mccs (which stands for Multi Criteria CUDF Solver) is a CUDF problem solver
developed at UNS during the European MANCOOSI project.

%package devel
Summary:        Development files for %{name}
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description devel
This package contains development files for %{name}.

%prep
%setup -q

%build
dune build @install

%install
install -d %{buildroot}%{_libdir}/ocaml/mccs/glpk/internal

pushd _build/install/default/lib
install -m0644 mccs/{META,dune-package,libmccs*,mccs*} %{buildroot}%{_libdir}/ocaml/mccs
install -m0644 mccs/glpk/internal/*mccs* %{buildroot}%{_libdir}/ocaml/mccs/glpk/internal
install -m0755 stublibs/dllmccs_stubs.so %{buildroot}%{_libdir}/libmccs_stubs.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENCE
%dir %{_libdir}/ocaml/mccs
%{_libdir}/libmccs_stubs.so
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/mccs/*.cmxs
%endif

%files devel
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/mccs/*.a
%{_libdir}/ocaml/mccs/*.cmx
%{_libdir}/ocaml/mccs/*.cmxa
%endif
%{_libdir}/ocaml/mccs/*.cma
%{_libdir}/ocaml/mccs/*.cmi
%{_libdir}/ocaml/mccs/*.cmt
%{_libdir}/ocaml/mccs/*.cmti
%{_libdir}/ocaml/mccs/*.ml
%{_libdir}/ocaml/mccs/*.mli
%{_libdir}/ocaml/mccs/META
%{_libdir}/ocaml/mccs/dune-package
%{_libdir}/ocaml/mccs/glpk/

%changelog
