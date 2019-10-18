#
# spec file for package ocaml-parmap
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


Name:           ocaml-parmap
Version:        20191002.803edbb
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Multicore architecture exploitation for OCaml programs with minimal modifications
License:        LGPL-2.0-only
Group:          Development/Languages/OCaml
URL:            http://rdicosmo.github.io/parmap/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ocaml
BuildRequires:  ocaml-oasis
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 20191009
BuildRequires:  ocamlfind(bigarray)
BuildRequires:  ocamlfind(graphics)
BuildRequires:  ocamlfind(unix)
BuildRequires:  pkgconfig(x11)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
If you want to use your many cores to accelerate an operation
which happens to be a map, fold or map/fold (map-reduce), just use
Parmap's parmap, parfold and parmapfold primitives in place of the
standard List.map and friends; you can specify the number of
subprocesses to use with the optional parameter ncores, and the
size of granularity of the parallel computation with the optional
parameter chunksize.

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
echo -n > config.h
if grep -w sched_setaffinity /usr/include/sched.h
then
tee -a config.h <<_EOF_
#define HAVE_DECL_SCHED_SETAFFINITY 1
_EOF_
fi
ocaml_version="$(ocamlc -version)"
case "${ocaml_version}" in
  4.03.*|4.04.*|4.05.*)
  echo 'let map_file = Bigarray.Genarray.map_file' >>parmap_compat.ml
  ;;
  *)
  echo 'let map_file = Unix.map_file' >>parmap_compat.ml
  ;;
esac
rm -fv setup.ml myocamlbuild.ml META* _* */_*
# obs service changes every ^Version line ...
sh -c "sed 's/^Version.*/Version: %{version}/' | tee _oasis" <<_EOF_
OASISFormat: 0.4
Name:        parmap
Version:     0
Synopsis:    library to exploit multicore architectures (parallel programming)
Authors:     Marco Danelutto and Roberto Di Cosmo
License:     WTFPL
LicenseFile: LICENSE
Plugins:     META(`oasis version`)
BuildTools:  ocamlbuild

Library parmap
 Path: .
 Install: true
 Modules: Parmap, Parmap_compat
 CSources: bytearray_stubs.c, setcore_stubs.c, config.h
 CCOpt: %{optflags} -I$PWD -Werror -D_GNU_SOURCE

Document parmap
 Title:                API reference for parmap
 Type:                 ocamlbuild
 BuildTools+:          ocamldoc
 InstallDir:           \$htmldir
 Install:              true
 XOCamlbuildPath:      .
 XOCamlbuildLibraries: parmap

Executable "%{name}-mandels"
 Install: true
 Path: example
 MainIs: mandels.ml
 CompiledObject: best
 BuildDepends: parmap, graphics, unix, bigarray
_EOF_
%oasis_setup
%ocaml_oasis_configure --enable-docs
%ocaml_oasis_build
%ocaml_oasis_doc

%install
%ocaml_oasis_findlib_install
%ocaml_create_file_list

%files -f %{name}.files
%doc README.md
%{_bindir}/*

%files devel -f %{name}.files.devel
%{oasis_docdir_html}
