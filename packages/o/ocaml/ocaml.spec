#
# spec file for package ocaml
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _lto_cflags %{nil}
%define ocaml_base_version 4.05
#
# This ensures that the find_provides/find_requires calls ocamlobjinfo correctly.
%global __ocaml_requires_opts -c -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte"
%global __ocaml_provides_opts -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte"

Name:           ocaml
Version:        4.05.0
Release:        0
Summary:        OCaml Compiler and Programming Environment
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
Url:            http://www.ocaml.org
Source0:        http://caml.inria.fr/pub/distrib/ocaml-%{ocaml_base_version}/ocaml-%{version}.tar.xz
Source2:        rpmlintrc
Patch1:         ocamldoc-man-th.patch
# FIX-UPSTREAM pass RPM_OPT_FLAGS to build
Patch4:         ocaml-configure-Allow-user-defined-C-compiler-flags.patch
Patch5:         ocaml-3.08.3-gcc4.patch
Patch8:         ocaml-4.05.0-CVE-2018-9838.patch
# FIX-UPSTREAM backport 'AArch64 GOT fixed' - https://github.com/ocaml/ocaml/pull/1330
Patch9:         ocaml-fix_aarch64_build.patch
# This gets ocamlobjinfo to work with .cmxs files
BuildRequires:  binutils-devel
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  ocaml-rpm-macros >= 20191101
Requires:       ocaml(runtime) = %{version}-%{release}
Obsoletes:      ocaml-docs
Provides:       ocaml(compiler) = %{ocaml_base_version}
Provides:       ocaml(ocaml_base_version) = %{ocaml_base_version}
%if %{ocaml_native_compiler}
Requires:       gcc
Provides:       ocaml(ocaml.opt) = %{ocaml_base_version}
%endif

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
Provides:       ocaml(runtime) = %{version}-%{release}

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

%package x11
Summary:        X11 support for OCaml
License:        SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml

%description x11
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains X11 support for OCaml.

%package ocamldoc
Summary:        Documentation generator for OCaml
License:        QPL-1.0
Group:          Development/Languages/OCaml
Requires:       ocaml = %{version}

%description ocamldoc
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains a documentation generator for OCaml.

%package compiler-libs
Summary:        Libraries used internal to the OCaml Compiler
License:        QPL-1.0
Group:          Development/Languages/OCaml
Requires:       ncurses-devel

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
Requires:       ocaml-compiler-libs = %{version}

%description compiler-libs-devel
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains libraries and signature files for developing
applications that use Ocaml.

%prep
: do_opt %{ocaml_native_compiler}
%autosetup -p1

%build
echo %{version} > VERSION
%if %{ocaml_native_compiler}
make_target='world.opt'
%else
make_target='world'
%endif
./configure -bindir %{_bindir} \
            -libdir %{_libdir}/ocaml \
            -no-cplugins \
            -mandir %{_mandir}

make_target+=" -j1"
%make_build ${make_target}
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
%fdupes %{buildroot}
export EXCLUDE_FROM_STRIP="ocamldebug ocamlbrowser"

# preserve .cmxs and .so
find %{buildroot} \( \
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
version = "OCaml %{version}"
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
version = "OCaml %{version}"
description="dummy backward-compatibility package for mutable strings"
requires=""
_META_
#
tee compiler-libs <<_META_
# The compiler itself
requires = ""
version = "OCaml %{version}"
description = "compiler-libs support library"
directory= "+compiler-libs"

package "common" (
  requires = "compiler-libs"
  version = "OCaml %{version}"
  description = "Common compiler routines"
  archive(byte) = "ocamlcommon.cma"
  archive(native) = "ocamlcommon.cmxa"
)

package "bytecomp" (
  requires = "compiler-libs.common"
  version = "OCaml %{version}"
  description = "Bytecode compiler"
  archive(byte) = "ocamlbytecomp.cma"
  archive(native) = "ocamlbytecomp.cmxa"
)

package "optcomp" (
  requires = "compiler-libs.common"
  version = "OCaml %{version}"
  description = "Native-code compiler"
  archive(byte) = "ocamloptcomp.cma"
  archive(native) = "ocamloptcomp.cmxa"
  exists_if = "ocamloptcomp.cma"
)

package "toplevel" (
  requires = "compiler-libs.bytecomp"
  version = "OCaml %{version}"
  description = "Toplevel interactions"
  archive(byte) = "ocamltoplevel.cma"
  archive(native) = "ocamltoplevel.cmxa"
)
_META_
#
tee dynlink <<_META_
requires = ""
version = "OCaml %{version}"
description = "Dynamic loading and linking of object files"
directory = "^"
browse_interfaces = " Unit name: Dynlink Unit name: Dynlinkaux "
archive(byte) = "dynlink.cma"
archive(native) = "dynlink.cmxa"
_META_
#
tee graphics <<_META_
# Specifications for the "graphics" library:
requires = ""
version = "OCaml %{version}"
description = "Portable drawing primitives"
directory = "^"
browse_interfaces = " Unit name: Graphics Unit name: GraphicsX11 "
archive(byte) = "graphics.cma"
archive(native) = "graphics.cmxa"
plugin(byte) = "graphics.cma"
plugin(native) = "graphics.cmxs"
_META_
tee num <<_META_
requires = "num.core"
requires(toploop) = "num.core"
version = "OCaml %{version}"
description = "Arbitrary-precision rational arithmetic"
package "core" (
  version = "OCaml %{version}"
  directory = "^"
  browse_interfaces = " Unit name: Arith_flags Unit name: Arith_status Unit name: Big_int Unit name: Int_misc Unit name: Nat Unit name: Num Unit name: Ratio "
  archive(byte) = "nums.cma"
  archive(native) = "nums.cmxa"
  plugin(byte) = "nums.cma"
  plugin(native) = "nums.cmxs"
)
_META_
#
tee ocamldoc <<_META_
requires = "compiler-libs"
version = "OCaml %{version}"
description = "ocamldoc plugin interface"
directory= "^ocamldoc"
_META_
#
tee raw_spacetime <<_META_
requires = ""
description = "Support library for the spacetime profiler"
version = "OCaml %{version}"
directory = "^"
browse_interfaces = ""
archive(byte) = "raw_spacetime_lib.cma"
archive(native) = "raw_spacetime_lib.cmxa"
plugin(byte) = "raw_spacetime_lib.cma"
plugin(native) = "raw_spacetime_lib.cmxs"
_META_
#
tee stdlib <<_META_
requires = ""
description = "Standard library"
version = "OCaml %{version}"
directory = "^"
browse_interfaces = " Unit name: Arg Unit name: Array Unit name: ArrayLabels Unit name: Buffer Unit name: Bytes Unit name: BytesLabels Unit name: Callback Unit name: CamlinternalFormat Unit name: CamlinternalFormatBasics Unit name: CamlinternalLazy Unit name: CamlinternalMod Unit name: CamlinternalOO Unit name: Char Unit name: Complex Unit name: Digest Unit name: Filename Unit name: Format Unit name: Gc Unit name: Genlex Unit name: Hashtbl Unit name: Int32 Unit name: Int64 Unit name: Lazy Unit name: Lexing Unit name: List Unit name: ListLabels Unit name: Map Unit name: Marshal Unit name: MoreLabels Unit name: Nativeint Unit name: Obj Unit name: Oo Unit name: Parsing Unit name: Pervasives Unit name: Printexc Unit name: Printf Unit name: Queue Unit name: Random Unit name: Scanf Unit name: Set Unit name: Sort Unit name: Stack Unit name: StdLabels Unit name: Stream Unit name: String Unit name: StringLabels Unit name: Sys Unit name: Weak "
_META_
#
tee str <<_META_
requires = ""
description = "Regular expressions and string processing"
version = "OCaml %{version}"
directory = "^"
browse_interfaces = " Unit name: Str "
archive(byte) = "str.cma"
archive(native) = "str.cmxa"
plugin(byte) = "str.cma"
plugin(native) = "str.cmxs"
_META_
#
tee threads <<_META_
version = "OCaml %{version}"
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
  version = "OCaml %{version}"
)

package "posix" (
  # --- POSIX-threads:
  requires = "unix"
  directory = "+threads"
  exists_if = "threads.cma"
  archive(byte,mt,mt_posix) = "threads.cma"
  archive(native,mt,mt_posix) = "threads.cmxa"
  version = "OCaml %{version}"
)
package "none" (
  error = "threading is not supported on this platform"
  version = "OCaml %{version}"
)
_META_
#
tee uchar <<_META_
description = "Unicode characters."
version = "OCaml %{version}"
directory = "^"
_META_
#
tee unix <<_META_
requires = ""
description = "Unix system calls"
version = "OCaml %{version}"
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
	*)
	files='files.compiler-libs.META'
	;;
	esac
	d=%{_libdir}/ocaml/${ocamlfind}
	f=${d}/META
	mkdir -vp %{buildroot}${d}
	mv "${META}" %{buildroot}${f}
	tee -a "${files}" <<_EOF_
%%dir ${d}
${f}
_EOF_
done

%files -f files.ocaml.META
%doc Changes
%license LICENSE
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/ocaml/*.a
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/*.cmxs
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.cmx
%{_libdir}/ocaml/*.o
%endif
%{_libdir}/ocaml/*.mli
%{_libdir}/ocaml/libcamlrun_shared.so
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/libasmrun_shared.so
%endif
%{_libdir}/ocaml/vmthreads/*.mli
%{_libdir}/ocaml/vmthreads/*.a
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/threads/*.a
%{_libdir}/ocaml/threads/*.cmxa
%{_libdir}/ocaml/threads/*.cmx
%endif
%{_libdir}/ocaml/caml
%{_libdir}/ocaml/Makefile.config
%{_libdir}/ocaml/VERSION
%{_libdir}/ocaml/extract_crc
%{_libdir}/ocaml/camlheader
%{_libdir}/ocaml/camlheader_ur
%{_libdir}/ocaml/expunge
%{_libdir}/ocaml/ld.conf
%{_libdir}/ocaml/objinfo_helper
%exclude %{_libdir}/ocaml/graphicsX11.mli
%exclude %{_bindir}/ocamlrun
%exclude %{_bindir}/ocamldoc*
%exclude %{_libdir}/ocaml/ocamldoc

%files runtime
%{_bindir}/ocamlrun
%dir %{_libdir}/ocaml
%{_libdir}/ocaml/*.cmo
%{_libdir}/ocaml/*.cmi
%{_libdir}/ocaml/*.cmt
%{_libdir}/ocaml/*.cmti
%{_libdir}/ocaml/*.cma
%{_libdir}/ocaml/stublibs
%dir %{_libdir}/ocaml/vmthreads
%{_libdir}/ocaml/vmthreads/*.cmi
%{_libdir}/ocaml/vmthreads/*.cma
%{_libdir}/ocaml/vmthreads/*.cmti
%dir %{_libdir}/ocaml/threads
%{_libdir}/ocaml/threads/*.cmi
%{_libdir}/ocaml/threads/*.cma
%{_libdir}/ocaml/threads/*.cmti
%exclude %{_libdir}/ocaml/graphicsX11.cmi
%doc Changes
%license LICENSE

%files x11
%{_libdir}/ocaml/graphicsX11.cmi
%{_libdir}/ocaml/graphicsX11.mli

%files source
%{_libdir}/ocaml/*.ml

%files ocamldoc -f files.ocamldoc.META
%{_bindir}/ocamldoc*
%{_libdir}/ocaml/ocamldoc
%doc ocamldoc/Changes.txt

%files compiler-libs -f files.compiler-libs.META
%license LICENSE
%dir %{_libdir}/ocaml

%files compiler-libs-devel
%dir %{_libdir}/ocaml/compiler-libs
%if %{ocaml_native_compiler}
%{_libdir}/ocaml/compiler-libs/*.a
%{_libdir}/ocaml/compiler-libs/*.o
%{_libdir}/ocaml/compiler-libs/*.cmx
%{_libdir}/ocaml/compiler-libs/*.cmxa
%endif
%{_libdir}/ocaml/compiler-libs/*.cma
%{_libdir}/ocaml/compiler-libs/*.cmi
%{_libdir}/ocaml/compiler-libs/*.cmo
%{_libdir}/ocaml/compiler-libs/*.cmt
%{_libdir}/ocaml/compiler-libs/*.cmti
%{_libdir}/ocaml/compiler-libs/*.mli

%if %{with ocaml_make_testsuite}
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
