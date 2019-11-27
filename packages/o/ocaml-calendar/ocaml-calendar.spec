#
# spec file for package ocaml-calendar
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


%bcond_with ocaml_do_dune_runtest
Name:           ocaml-calendar
Version:        2.04
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective Caml library for managing dates and times
License:        LGPL-2.0
Group:          Development/Languages/OCaml
Url:            https://github.com/ocaml-community/calendar
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20191101
BuildRequires:  ocamlfind(re)
BuildRequires:  ocamlfind(unix)
%if %{with ocaml_do_dune_runtest}
BuildRequires:  ocamlfind(alcotest)
%endif

%description
Objective Caml library for managing dates and times.

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
sed -i~ '/system date/d' src/dune
diff -u "$_"~ "$_" && exit 1
dune_release_pkgs='calendar'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%if %{with ocaml_do_dune_runtest}
%check
%ocaml_dune_test
%endif

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
