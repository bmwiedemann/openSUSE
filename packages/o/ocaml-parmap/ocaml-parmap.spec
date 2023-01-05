#
# spec file for package ocaml-parmap
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


Name:           ocaml-parmap
Version:        1.2.5
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Multicore architecture exploitation for OCaml programs with minimal modifications
License:        LGPL-2.0-only
Group:          Development/Languages/OCaml
URL:            https://opam.ocaml.org/packages/parmap
Source0:        %name-%version.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(dune.configurator)
BuildRequires:  ocamlfind(graphics)
BuildRequires:  ocamlfind(unix)
BuildRequires:  pkgconfig(x11)

%description
If you want to use your many cores to accelerate an operation
which happens to be a map, fold or map/fold (map-reduce), just use
Parmap's parmap, parfold and parmapfold primitives in place of the
standard List.map and friends; you can specify the number of
subprocesses to use with the optional parameter ncores, and the
size of granularity of the parallel computation with the optional
parameter chunksize.

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
sed -i~ '
s@10000000@1000000@
' tests/simplescale.ml
diff -u "$_"~ "$_" && exit 1
dune_release_pkgs='parmap'
%ocaml_dune_setup
%ocaml_dune_build

%install
%ocaml_dune_install
%ocaml_create_file_list

%check
OCAML_DUNE_RUNTEST_ARGS="-j 1"
export nData=$((1000 * 10))
export nProcs=2
%ocaml_dune_test

%files -f %name.files

%files devel -f %name.files.devel

%changelog
