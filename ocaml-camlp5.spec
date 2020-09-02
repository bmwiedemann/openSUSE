#
# spec file for package ocaml-camlp5
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ocaml-camlp5
Version:        7.12
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Preprocessor-Pretty-Printer for Objective Caml
License:        BSD-3-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/camlp5
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml <= 4.11.1
BuildRequires:  ocaml-rpm-macros >= 20200514
BuildRequires:  ocamlfind(compiler-libs)

%description
Camlp5 is a preprocessor-pretty-printer of OCaml, parsing a source file and printing some result on standard output.

%package devel
Summary:        Development files for ocaml-camlp5
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description devel
Camlp5 is a preprocessor-pretty-printer of OCaml, parsing a source file and printing some result on standard output.

This package contains the development files.

%prep
%setup -q

%build
pushd ocaml_stuff
test -e '4.11.1' || ln -s 4.11.0 "$_"
popd
pushd ocaml_src/lib/versdep
test -e '4.11.1.ml' || ln -s 4.11.0.ml "$_"
popd
./configure \
	--mandir %{_mandir}
make %{?_smp_mflags} out
make %{?_smp_mflags} world
%if 0%{?ocaml_native_compiler}
make %{?_smp_mflags} world.opt
%endif

%install
%make_install
cp -Lavit %{buildroot}%{ocaml_standard_library}/camlp5 etc/META
%ocaml_create_file_list

%files -f %{name}.files
%{_bindir}/*
%{_mandir}/*/*

%files devel -f %{name}.files.devel

%changelog
