#
# spec file for package ocaml-result
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   result
Name:           ocaml-result
Version:        1.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Compatibility OCaml Result module
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
Url:            https://github.com/janestreet/result
Source0:        %{url}/archive/%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 4.03

%description
Projects that want to use the new result type defined in OCaml >= 4.03 while
staying compatible with older version of OCaml should use the Result module
defined in this library.

%package devel
Summary:        Development files for the Compatibility OCaml Result module
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Projects that want to use the new result type defined in OCaml >= 4.03 while
staying compatible with older version of OCaml should use the Result module
defined in this library.

This package contains development files for %{name}.

%prep
%setup -q -n %{_name}-%{version}

%build
dune build @install --profile=release

%install
dune install --prefix=%{buildroot}%{_prefix} --libdir=%{buildroot}%{_libdir}/ocaml
rm -r %{buildroot}%{_prefix}/doc

%files
%doc CHANGES.md README.md
%license LICENSE.md
%dir %{_libdir}/ocaml
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.ml
%{_libdir}/ocaml/*/META
%{_libdir}/ocaml/*/dune-package
%{_libdir}/ocaml/*/opam

%changelog
