#
# spec file for package ocaml
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define ocaml_base_version 5.5
#
# This ensures that the find_provides/find_requires calls ocamlobjinfo correctly.
# handle built-in ocaml helper from rpm-build, and helper from ocaml-rpm-macros
%global __suseocaml_requires_opts \
	-c \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	-i Dynlink_cmxs_format \
	-i Dynlink_cmo_format \
	%nil
%global __ocaml_requires_opts \
	-c \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	-i Dynlink_cmxs_format \
	-i Dynlink_cmo_format \
	%nil
%global __suseocaml_provides_opts \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil
%global __ocaml_provides_opts \
	-f "%_bindir/env OCAMLLIB=%buildroot%ocaml_standard_library %buildroot%_bindir/ocamlrun %buildroot%_bindir/ocamlobjinfo.byte" \
	%nil

%bcond_with ocaml_testsuite
%bcond_without suse_ocaml_use_rpm_license_macro

Name:           ocaml
Version:        5.5.0
Release:        0
Summary:        OCaml Compiler and Programming Environment
%if %{with suse_ocaml_use_rpm_license_macro}
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
%else
License:        MIT
%endif
ExclusiveArch:  aarch64 ppc64le riscv64 s390x x86_64
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
URL:            http://www.ocaml.org
Source0:        %name-%version.tar.xz
Source2:        %name-rpmlintrc
Patch0:         ocaml-configure-Allow-user-defined-C-compiler-flags.patch
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-rpm-macros >= 20260707
BuildRequires:  pkgconfig
Requires:       ncurses-devel
Requires:       ocaml(runtime) = %version-%release
Obsoletes:      ocaml-docs
Provides:       ocaml(compiler) = %ocaml_base_version
Provides:       ocaml(ocaml_base_version) = %ocaml_base_version
BuildRequires:  pkgconfig(libzstd) >= 1.4
Requires:       pkgconfig(libzstd) >= 1.4
BuildRequires:  gcc-c++
Requires:       gcc
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
%patch -P 0 -p1

%build
sed -i~ '/README.win32.adoc/d' Makefile
diff -u "$_"~ "$_" && exit 1
echo %version > VERSION
export CC='gcc'
export CXX='g++'
export AS='as'
export ASPP="$CC -c"
extra_cflags=()
extra_cflags+=( '-Werror=implicit-function-declaration' )
extra_cflags+=( '-Werror=return-type' )
extra_cflags+=( '-Wno-deprecated-declarations' )
export EXTRA_CFLAGS="${extra_cflags[@]}"
# use only the fixed set of built-in CFLAGS
CFLAGS='-pipe'
./configure --help
%configure \
%if %{with ocaml_testsuite}
	--enable-ocamltest \
%else
	--disable-ocamltest \
%endif
	--enable-native-compiler \
	--libdir=%ocaml_standard_library
%make_build --no-print-directory
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
#
tee seq <<_META_
version = "%version"
description = ""
requires = ""
_META_
#
tee uchar <<_META_
description = "Unicode characters."
version = "%version"
directory = "^"
_META_
#
popd
> 'files.ocaml.META'
for META in META/*
do
	ocamlfind=${META##*/}
	case "${ocamlfind}" in
	graphics)
	files='files.ocaml.META'
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
%ocaml_standard_library/*.cmxa
%ocaml_standard_library/*.cmx
%ocaml_standard_library/*.o
%ocaml_standard_library/*.mli
%ocaml_standard_library/*.ml.in
%ocaml_standard_library/libasmrun-*.so
%ocaml_standard_library/libasmrun_shared.so
%ocaml_standard_library/libcamlrun-*.so
%ocaml_standard_library/libcamlrun_shared.so
%ocaml_standard_library/dynlink/*.a
%ocaml_standard_library/dynlink/*.cmxa
%ocaml_standard_library/dynlink/*.cmx
%ocaml_standard_library/dynlink/*.mli
%ocaml_standard_library/dynlink/META
%ocaml_standard_library/profiling/*.cmx
%ocaml_standard_library/profiling/*.o
%ocaml_standard_library/runtime_events/*.a
%ocaml_standard_library/runtime_events/*.cmxa
%ocaml_standard_library/runtime_events/*.cmx
%ocaml_standard_library/runtime_events/*.mli
%ocaml_standard_library/runtime_events/META
%ocaml_standard_library/stdlib/META
%ocaml_standard_library/str/*.a
%ocaml_standard_library/str/*.cmxa
%ocaml_standard_library/str/*.cmx
%ocaml_standard_library/str/*.mli
%ocaml_standard_library/str/META
%ocaml_standard_library/threads/*.a
%ocaml_standard_library/threads/*.cmxa
%ocaml_standard_library/threads/*.cmx
%ocaml_standard_library/threads/*.mli
%ocaml_standard_library/threads/META
%ocaml_standard_library/unix/*.a
%ocaml_standard_library/unix/*.cmxa
%ocaml_standard_library/unix/*.cmx
%ocaml_standard_library/unix/*.mli
%ocaml_standard_library/unix/META
%ocaml_standard_library/caml
%ocaml_standard_library/Makefile.config
%ocaml_standard_library/expunge
%ocaml_standard_library/ld.conf
%dir %ocaml_standard_library/stublibs
%exclude %_bindir/ocamlrun
%exclude %_bindir/ocamldoc*
%exclude %ocaml_standard_library/ocamldoc

%files runtime
%defattr(-,root,root,-)
%_bindir/ocamlrun
%dir %ocaml_standard_library
%ocaml_standard_library/runtime-launch-info
%ocaml_standard_library/*.cmo
%ocaml_standard_library/*.cmi
%ocaml_standard_library/*.cmt
%ocaml_standard_library/*.cmti
%ocaml_standard_library/*.cma
%ocaml_standard_library/*/*.cmxs
%ocaml_standard_library/stublibs
%dir %ocaml_standard_library/dynlink
%ocaml_standard_library/dynlink/*.cmi
%ocaml_standard_library/dynlink/*.cma
%ocaml_standard_library/dynlink/*.cmti
%dir %ocaml_standard_library/profiling
%ocaml_standard_library/profiling/*.cmi
%ocaml_standard_library/profiling/*.cmo
%ocaml_standard_library/profiling/*.cmt
%ocaml_standard_library/profiling/*.cmti
%dir %ocaml_standard_library/runtime_events
%ocaml_standard_library/runtime_events/*.cmi
%ocaml_standard_library/runtime_events/*.cma
%ocaml_standard_library/runtime_events/*.cmti
%dir %ocaml_standard_library/stdlib
%dir %ocaml_standard_library/str
%ocaml_standard_library/str/*.cmi
%ocaml_standard_library/str/*.cma
%ocaml_standard_library/str/*.cmti
%dir %ocaml_standard_library/threads
%ocaml_standard_library/threads/*.cmi
%ocaml_standard_library/threads/*.cma
%ocaml_standard_library/threads/*.cmti
%dir %ocaml_standard_library/unix
%ocaml_standard_library/unix/*.cmi
%ocaml_standard_library/unix/*.cma
%ocaml_standard_library/unix/*.cmti
%doc Changes
%if %{with suse_ocaml_use_rpm_license_macro}
%license LICENSE
%endif

%files source
%defattr(-,root,root,-)
%ocaml_standard_library/*.ml

%files ocamldoc
%defattr(-,root,root,-)
%_bindir/ocamldoc*
%ocaml_standard_library/ocamldoc

%files compiler-libs
%defattr(-,root,root,-)
%dir %ocaml_standard_library
%ocaml_standard_library/compiler-libs/*.cma
%ocaml_standard_library/compiler-libs/*.cmi
%ocaml_standard_library/compiler-libs/*.cmo
%ocaml_standard_library/compiler-libs/*.cmt
%ocaml_standard_library/compiler-libs/*.cmti

%files compiler-libs-devel
%defattr(-,root,root,-)
%dir %ocaml_standard_library/compiler-libs
%ocaml_standard_library/compiler-libs/*.a
%ocaml_standard_library/compiler-libs/*.cmx
%ocaml_standard_library/compiler-libs/*.cmxa
%ocaml_standard_library/compiler-libs/*.mli
%ocaml_standard_library/compiler-libs/*.o
%ocaml_standard_library/compiler-libs/META

%if %{with ocaml_testsuite}
%check
trap 'exit 0' EXIT
%make_build -C testsuite clean
%make_build -C testsuite all
%endif

%changelog
