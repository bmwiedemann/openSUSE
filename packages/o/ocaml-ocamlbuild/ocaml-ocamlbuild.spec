#
# spec file for package ocaml-ocamlbuild
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ocaml-ocamlbuild
Version:        0.14.2
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Generic build tool for building OCaml library and programs
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/ocamlbuild
Source:         %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-rpm-macros >= 20230101
Requires:       %name-devel = %version

%description
OCamlbuild is a generic build tool, that has built-in rules for
building OCaml library and programs.

OCamlbuild was distributed as part of the OCaml distribution for
OCaml versions between 3.10.0 and 4.02.3. Starting from OCaml
4.03, it is now released separately.

%package        devel
Summary:        Development files for %name
Group:          Development/Languages/OCaml
Requires:       %name = %version

%description    devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%autosetup -p1

%build
tee %name.sh <<'_EOF_'
set -x
exec \
make \
PREFIX=%_prefix \
OCAML_NATIVE_TOOLS=true \
OCAML_NATIVE=true \
"$@"
_EOF_
sh %name.sh -f configure.make
sh %name.sh configure
sh %name.sh %{?_smp_mflags}

%install
sh %name.sh \
install \
DESTDIR=%buildroot %{?_smp_mflags}
%ocaml_create_file_list

%files -f %name.files
%doc Changes
%_bindir/*
%_mandir/man*/*

%files devel -f %name.files.devel

%changelog
