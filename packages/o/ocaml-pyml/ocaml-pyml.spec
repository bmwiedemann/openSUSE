#
# spec file for package ocaml-pyml
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ocaml-pyml
Version:        20210226
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stdcompat: compatibility module for OCaml standard library 
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/pyml
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  ocaml
#uildRequires:  ocaml-dune
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  ocamlfind(unix)
# make check
BuildRequires:  python > 3.0
%if 0%{?suse_version} > 1315
BuildRequires:  python3-numpy
%else
BuildRequires:  python-numpy
%endif

%description
Stdcompat is a compatibility layer allowing programs to use some recent additions to the OCaml standard library while preserving the ability to be compiled on former versions of OCaml.

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
sed -i~ '
s@^\(HAVE_OCAMLFIND := $(shell \).*@\1 set -x ; \\@
s@2>&1@@g
' Makefile
diff -u "$_"~ "$_" && exit 1
%make_build
%if 0
dune_release_pkgs='pyml'
%ocaml_dune_setup
%ocaml_dune_build
%endif

%install
mkdir -vp '%{buildroot}%{ocaml_standard_library}'
export OCAMLFIND_DESTDIR='%{buildroot}%{ocaml_standard_library}'
export OCAMLFIND_LDCONF='ignore'
%make_install STDCOMPAT="$(ocamlfind query stdcompat)"
%ocaml_create_file_list
%if 0
%ocaml_dune_install
%ocaml_create_file_list
%endif

%check
%if 0
%ocaml_dune_test
%endif

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
