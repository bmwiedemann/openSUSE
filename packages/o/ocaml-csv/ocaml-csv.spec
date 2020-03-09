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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%bcond_with     ocaml_lwt

Name:           ocaml-csv
Version:        2.4
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        OCaml library for reading and writing CSV files
License:        LGPL-2.0+
Group:          Development/Languages/OCaml
Url:            https://github.com/Chris00/ocaml-csv
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20200220
BuildRequires:  ocamlfind(bytes)
BuildRequires:  ocamlfind(str)
BuildRequires:  ocamlfind(unix)
BuildRequires:  ocamlfind(uutf)
%if %{with ocaml_lwt}
BuildRequires:  ocamlfind(lwt)
BuildRequires:  ocamlfind(lwt.unix)
%endif

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
%autosetup -p1

%build
dune_release_pkgs='csv,csvtool'
%if %{with ocaml_lwt}
dune_release_pkgs="${dune_release_pkgs},csv-lwt"
%endif
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
%ocaml_dune_test

%files -f %{name}.files
%{_bindir}/*

%files devel -f %{name}.files.devel

%changelog
