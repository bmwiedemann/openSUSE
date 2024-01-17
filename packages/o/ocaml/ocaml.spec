#
# spec file for package ocaml
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010 Andrew Psaltis <ampsaltis at gmail dot com>
# Copyright (c) 2011 Andrew Psaltis <ampsaltis at gmail dot com>
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


%define ocaml_base_version 4.14
#
# This ensures that the find_provides/find_requires calls ocamlobjinfo correctly.
# handle built-in ocaml helper from rpm-build, and helper from ocaml-rpm-macros
%global __suseocaml_requires_opts \
	-c \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil
%global __ocaml_requires_opts \
	-c \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil
%global __suseocaml_provides_opts \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil
%global __ocaml_provides_opts \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil

%global  _buildshell /bin/bash
%bcond_with ocaml_testsuite
%bcond_without suse_ocaml_use_rpm_license_macro

Name:           ocaml
Version:        4.14.1
Release:        0
Summary:        OCaml Compiler and Programming Environment
%if %{with suse_ocaml_use_rpm_license_macro}
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
%else
License:        MIT
%endif
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            http://www.ocaml.org
Source0:        %name-%version.tar.xz
Source2:        %name-rpmlintrc
Patch0:         ocaml-configure-Allow-user-defined-C-compiler-flags.patch
BuildRequires:  autoconf >= 2.69
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-rpm-macros >= 20230101
BuildRequires:  pkgconfig
Requires:       ncurses-devel
Requires:       ocaml(runtime) = %version-%release
Obsoletes:      ocaml-docs
Provides:       ocaml(compiler) = %ocaml_base_version
Provides:       ocaml(ocaml_base_version) = %ocaml_base_version
Requires:       %(type -P gcc | xargs readlink -f | xargs rpm -qf --qf '%%{NAME}\n')
Provides:       ocaml(ocaml.opt) = %ocaml_base_version
Obsoletes:      ocaml-seq < %version-%release
Obsoletes:      ocaml-seq-debuginfo < %version-%release
Obsoletes:      ocaml-seq-devel < %version-%release
Provides:       ocaml-seq = %version-%release
Provides:       ocaml-seq-debuginfo = %version-%release
Provides:       ocaml-seq-devel = %version-%release

%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive top level
system, Lex&Yacc tools, a replay debugger, and a comprehensive library.

%package runtime
Summary:        OCaml runtime environment
License:        QPL-1.0
Group:          Development/Languages/OCaml
Provides:       ocaml(runtime) = %version-%release

%description runtime
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains the runtime environment needed to run OCaml
bytecode.

%package source
Summary:        Source code for OCaml libraries
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml

%description source
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains source code for OCaml libraries.

%package ocamldoc
Summary:        Documentation generator for OCaml
License:        QPL-1.0
Group:          Development/Languages/OCaml
Requires:       ocaml = %version

%description ocamldoc
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains a documentation generator for OCaml.

%package compiler-libs
Summary:        Libraries used internal to the OCaml Compiler
License:        QPL-1.0
Group:          Development/Languages/OCaml
Requires:       ocaml = %version-%release

%description compiler-libs
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains several modules used internally by the OCaml
compilers. They are not needed for normal OCaml development, but may
be helpful in the development of certain applications.

%package compiler-libs-devel
Summary:        Libraries used internal to the OCaml Compiler
License:        QPL-1.0
Group:          Development/Languages/OCaml
Requires:       ocaml-compiler-libs = %version-%release

%description compiler-libs-devel
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains libraries and signature files for developing
applications that use Ocaml.

%prep
%setup -q
%patch0 -p1

%build
echo %version > VERSION
export CC='gcc'
export AS='as'
test -x "$(type -P gcc | xargs readlink -f)" && export CC="$_"
test -x "$(type -P as  | xargs readlink -f)" && export AS="$_"
export ASPP="$CC -c"
configure_target=
extra_cflags=()
extra_cflags+=( '-Werror=implicit-function-declaration' )
extra_cflags+=( '-Werror=return-type' )
extra_cflags+=( '-Wno-deprecated-declarations' )
export EXTRA_CFLAGS="${extra_cflags[@]}"
bash -x tools/autogen
%ifarch %arm
: OCaml issue #9431
triple_fault=`/bin/sh build-aux/config.guess`
configure_target="${configure_target} --host=${triple_fault} --build=${triple_fault}"
%endif
# use only the fixed set of built-in CFLAGS
CFLAGS='-pipe'
./configure --help
%configure \
	${configure_target} \
%if %{with ocaml_testsuite}
	--enable-ocamltest \
%else
	--disable-ocamltest \
%endif
	--enable-native-compiler \
	--libdir=%ocaml_standard_library
%make_build
#
pushd testsuite
tee checker.sh <<'_EOF_'
#!/bin/bash
t=${0%%.*}
if $DIFF -u "${t}.reference" "${t}.result"
then
  exit 0
fi
ls -l "${t}.reference" "${t}.result"
head -n 1234 "${t}.reference" "${t}.result"
_EOF_
chmod -v 555 checker.sh
c=$PWD/checker.sh
for i in `find tests -name "*.reference" -type f`
do
	test -e ${i%%.reference}.checker || ln -sfvbn "$c" ${i%%.reference}.checker
done
popd

%install
%make_install
rm -rfv %buildroot%_datadir/doc/ocaml
%fdupes %buildroot
export EXCLUDE_FROM_STRIP="ocamldebug ocamlbrowser"

# preserve .cmxs and .so
find %buildroot \( \
	-name '*.a' -o \
	-name '*.cma' -o \
	-name '*.cmi' -o \
	-name '*.cmo' -o \
	-name '*.cmt' -o \
	-name '*.cmti' -o \
	-name '*.cmx' -o \
	-name '*.cmxa' -o \
	-name '*.conf' -o \
	-name '*.h' -o \
	-name '*.hva' -o \
	-name '*.ml' -o \
	-name '*.mli' -o \
	-name '*.mll' -o \
	-name '*.mlp' -o \
	-name '*.mly' -o \
	-name '*.o' -o \
	-name '*.sml' \
	\) -type f -exec chmod a-x "{}" \;

mkdir META
pushd "$_"
tee bigarray <<_META_
requires = "unix"
version = "%version"
description = "Large statically allocated arrays"
directory = "^"
browse_interfaces = " Unit name: Bigarray "
archive(byte) = "bigarray.cma"
archive(native) = "bigarray.cmxa"
plugin(byte) = "bigarray.cma"
plugin(native) = "bigarray.cmxs"
linkopts = ""
_META_
#
tee bytes <<_META_
name="bytes"
version = "%version"
description="dummy backward-compatibility package for mutable strings"
requires=""
_META_
#
tee compiler-libs <<_META_
# The compiler itself
requires = ""
version = "%version"
description = "compiler-libs support library"

package "common" (
  requires = "compiler-libs"
  version = "%version"
  description = "Common compiler routines"
  archive(byte) = "ocamlcommon.cma"
  archive(native) = "ocamlcommon.cmxa"
)

package "bytecomp" (
  requires = "compiler-libs.common"
  version = "%version"
  description = "Bytecode compiler"
  archive(byte) = "ocamlbytecomp.cma"
  archive(native) = "ocamlbytecomp.cmxa"
)

package "optcomp" (
  requires = "compiler-libs.common"
  version = "%version"
  description = "Native-code compiler"
  archive(byte) = "ocamloptcomp.cma"
  archive(native) = "ocamloptcomp.cmxa"
  exists_if = "ocamloptcomp.cma"
)

package "toplevel" (
  requires = "compiler-libs.bytecomp"
  version = "%version"
  description = "Toplevel interactions"
  archive(byte) = "ocamltoplevel.cma"
  archive(native) = "ocamltoplevel.cmxa"
)
_META_
#
tee dynlink <<_META_
requires = ""
version = "%version"
description = "Dynamic loading and linking of object files"
directory = "^"
browse_interfaces = " Unit name: Dynlink Unit name: Dynlinkaux "
archive(byte) = "dynlink.cma"
archive(native) = "dynlink.cmxa"
_META_
#
tee ocamldoc <<_META_
requires = "compiler-libs"
version = "%version"
description = "ocamldoc plugin interface"
_META_
#
tee raw_spacetime <<_META_
requires = ""
description = "Support library for the spacetime profiler"
version = "%version"
directory = "^"
browse_interfaces = ""
archive(byte) = "raw_spacetime_lib.cma"
archive(native) = "raw_spacetime_lib.cmxa"
plugin(byte) = "raw_spacetime_lib.cma"
plugin(native) = "raw_spacetime_lib.cmxs"
_META_
%if 0
#
# conflicts with ocaml-result.rpm
tee result <<_META_
version = "%version"
description = ""
requires = ""
_META_
%endif
#
tee seq <<_META_
version = "%version"
description = ""
requires = ""
_META_
#
tee stdlib <<_META_
requires = ""
description = "Standard library"
version = "%version"
directory = "^"
browse_interfaces = " Unit name: Arg Unit name: Array Unit name: ArrayLabels Unit name: Buffer Unit name: Bytes Unit name: BytesLabels Unit name: Callback Unit name: CamlinternalFormat Unit name: CamlinternalFormatBasics Unit name: CamlinternalLazy Unit name: CamlinternalMod Unit name: CamlinternalOO Unit name: Char Unit name: Complex Unit name: Digest Unit name: Filename Unit name: Format Unit name: Gc Unit name: Genlex Unit name: Hashtbl Unit name: Int32 Unit name: Int64 Unit name: Lazy Unit name: Lexing Unit name: List Unit name: ListLabels Unit name: Map Unit name: Marshal Unit name: MoreLabels Unit name: Nativeint Unit name: Obj Unit name: Oo Unit name: Parsing Unit name: Pervasives Unit name: Printexc Unit name: Printf Unit name: Queue Unit name: Random Unit name: Scanf Unit name: Set Unit name: Sort Unit name: Stack Unit name: StdLabels Unit name: Stream Unit name: String Unit name: StringLabels Unit name: Sys Unit name: Weak "
_META_
#
tee str <<_META_
requires = ""
description = "Regular expressions and string processing"
version = "%version"
directory = "^"
browse_interfaces = " Unit name: Str "
archive(byte) = "str.cma"
archive(native) = "str.cmxa"
plugin(byte) = "str.cma"
plugin(native) = "str.cmxs"
_META_
#
tee threads <<_META_
version = "%version"
description = "Multi-threading"
requires(mt,mt_vm) = "threads.vm"
requires(mt,mt_posix) = "threads.posix"
directory = "^"
type_of_threads = "posix"
browse_interfaces = " Unit name: Condition Unit name: Event Unit name: Mutex Unit name: Thread Unit name: ThreadUnix "
warning(-mt) = "Linking problems may arise because of the missing -thread or -vmthread switch"
warning(-mt_vm,-mt_posix) = "Linking problems may arise because of the missing -thread or -vmthread switch"
package "vm" (
  # --- Bytecode-only threads:
  requires = "unix"
  directory = "+vmthreads"
  exists_if = "threads.cma"
  archive(byte,mt,mt_vm) = "threads.cma"
  version = "%version"
)

package "posix" (
  # --- POSIX-threads:
  requires = "unix"
  directory = "+threads"
  exists_if = "threads.cma"
  archive(byte,mt,mt_posix) = "threads.cma"
  archive(native,mt,mt_posix) = "threads.cmxa"
  version = "%version"
)
package "none" (
  error = "threading is not supported on this platform"
  version = "%version"
)
_META_
#
tee uchar <<_META_
description = "Unicode characters."
version = "%version"
directory = "^"
_META_
#
tee unix <<_META_
requires = ""
description = "Unix system calls"
version = "%version"
directory = "^"
browse_interfaces = " Unit name: Unix Unit name: UnixLabels "
archive(byte) = "unix.cma"
archive(native) = "unix.cmxa"
archive(byte,mt_vm) = "vmthreads/unix.cma"
plugin(byte) = "unix.cma"
plugin(native) = "unix.cmxs"
plugin(byte,mt_vm) = "vmthreads/unix.cma"
_META_
#
popd
> 'files.ocaml.META'
> 'files.ocamldoc.META'
> 'files.compiler-libs.META'
for META in META/*
do
	ocamlfind=${META##*/}
	case "${ocamlfind}" in
	graphics)
	files='files.ocaml.META'
	;;
	ocamldoc)
	files='files.ocamldoc.META'
	;;
	compiler-libs)
	files='files.compiler-libs.META'
	;;
	*)
	files='files.ocaml.META'
	;;
	esac
	d=%ocaml_standard_library/${ocamlfind}
	f=${d}/META
	mkdir -vp %buildroot${d}
	mv "${META}" %buildroot${f}
	tee -a "${files}" <<_EOF_
%%dir ${d}
${f}
_EOF_
done

%files -f files.ocaml.META
%defattr(-,root,root,-)
%doc Changes
%if %{with suse_ocaml_use_rpm_license_macro}
%license LICENSE
%endif
%_bindir/*
%_mandir/*/*
%ocaml_standard_library/*.a
%ocaml_standard_library/*.cmxs
%ocaml_standard_library/*.cmxa
%ocaml_standard_library/*.cmx
%ocaml_standard_library/*.o
%ocaml_standard_library/*.mli
%ocaml_standard_library/libcamlrun_shared.so
%ocaml_standard_library/libasmrun_shared.so
%ocaml_standard_library/threads/*.a
%ocaml_standard_library/threads/*.cmxa
%ocaml_standard_library/threads/*.cmx
%ocaml_standard_library/threads/*.mli
%ocaml_standard_library/caml
%ocaml_standard_library/Makefile.config
%ocaml_standard_library/eventlog_metadata
%ocaml_standard_library/camlheader
%ocaml_standard_library/camlheader_ur
%ocaml_standard_library/expunge
%ocaml_standard_library/ld.conf
%ocaml_standard_library/camlheaderd
%ocaml_standard_library/camlheaderi
%exclude %_bindir/ocamlrun
%exclude %_bindir/ocamldoc*
%exclude %ocaml_standard_library/ocamldoc

%files runtime
%defattr(-,root,root,-)
%_bindir/ocamlrun
%dir %ocaml_standard_library
%ocaml_standard_library/*.cmo
%ocaml_standard_library/*.cmi
%ocaml_standard_library/*.cmt
%ocaml_standard_library/*.cmti
%ocaml_standard_library/*.cma
%ocaml_standard_library/stublibs
%dir %ocaml_standard_library/threads
%ocaml_standard_library/threads/*.cmi
%ocaml_standard_library/threads/*.cma
%ocaml_standard_library/threads/*.cmti
%exclude %ocaml_standard_library/topdirs.cmi
%exclude %ocaml_standard_library/topdirs.cmt
%exclude %ocaml_standard_library/topdirs.cmti
%doc Changes
%if %{with suse_ocaml_use_rpm_license_macro}
%license LICENSE
%endif

%files source
%defattr(-,root,root,-)
%ocaml_standard_library/*.ml

%files ocamldoc -f files.ocamldoc.META
%defattr(-,root,root,-)
%_bindir/ocamldoc*
%ocaml_standard_library/ocamldoc
%doc ocamldoc/Changes.txt

%files compiler-libs
%defattr(-,root,root,-)
%dir %ocaml_standard_library
%ocaml_standard_library/topdirs.cmi
%ocaml_standard_library/topdirs.cmt
%ocaml_standard_library/topdirs.cmti
%ocaml_standard_library/compiler-libs/*.cma
%ocaml_standard_library/compiler-libs/*.cmi
%ocaml_standard_library/compiler-libs/*.cmo
%ocaml_standard_library/compiler-libs/*.cmt
%ocaml_standard_library/compiler-libs/*.cmti

%files compiler-libs-devel -f files.compiler-libs.META
%defattr(-,root,root,-)
%dir %ocaml_standard_library/compiler-libs
%ocaml_standard_library/compiler-libs/*.a
%ocaml_standard_library/compiler-libs/*.o
%ocaml_standard_library/compiler-libs/*.cmx
%ocaml_standard_library/compiler-libs/*.cmxa
%ocaml_standard_library/compiler-libs/*.mli

%if %{with ocaml_testsuite}
%check
make %{?_smp_mflags} -C testsuite clean
if make -C testsuite all
then
	: passed
else
	: failed
fi
%endif

%changelog
