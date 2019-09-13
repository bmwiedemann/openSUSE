#
# spec file for package ocaml-csv
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ocaml-csv
Version:        1.7
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml library for reading and writing CSV files
License:        LGPL-2.0+
Group:          Development/Languages/OCaml
Url:            https://github.com/Chris00/ocaml-csv
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.03
BuildRequires:  ocamlfind(bytes)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This OCaml library can read and write CSV files, including all
extensions used by Excel - eg. quotes, newlines, 8 bit characters in
fields, quote-0 etc.

The library comes with a handy command line tool called csvtool for
handling CSV files from shell scripts.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q

%build
rm -fv setup.ml myocamlbuild.ml META* _tags */_* */META*
sed -i '/^Library csv_lwt/,/^$/d' _oasis
%oasis_setup
%ocaml_oasis_configure --enable-docs --disable-tests
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install

%check
%ocaml_oasis_test

%files
%defattr(-,root,root,-)
%doc AUTHORS.txt LICENSE.txt README.txt
%{_bindir}/csvtool
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*

%files devel
%defattr(-,root,root,-)
%doc LICENSE.txt
%{oasis_docdir_html}
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmxs
%endif
%{_libdir}/ocaml/*/*.annot
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmt
%{_libdir}/ocaml/*/*.cmti
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
