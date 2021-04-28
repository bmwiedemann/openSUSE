#
# spec file for package ocaml-stdcompat
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


%define _lto_cflags %{nil}
Name:           ocaml-stdcompat
Version:        15
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Stdcompat: compatibility module for OCaml standard library 
License:        BSD-2-Clause
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/stdcompat
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bash
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocaml-rpm-macros >= 20210409
BuildRequires:  ocaml(ocaml.opt)

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
%make_build -f Makefile.bootstrap
%configure \
	--libdir=%{ocaml_standard_library}
%make_build -j1

%install
%make_install
find %{buildroot} -type f -exec chmod -v 644 '{}' +
%ocaml_create_file_list

%files -f %{name}.files

%files devel -f %{name}.files.devel

%changelog
