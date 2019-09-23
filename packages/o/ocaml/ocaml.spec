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
%define do_opt 0
# This ensures that the find_provides/find_requires calls ocamlobjinfo correctly.
%global __ocaml_requires_opts -c -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte"
%global __ocaml_provides_opts -f "%{buildroot}%{_bindir}/ocamlrun %{buildroot}%{_bindir}/ocamlobjinfo.byte"
# macros to be set in prjconf:
#Macros:
#_with_ocaml_force_enable_ocaml_opt 1
#_with_ocaml_force_disable_ocaml_opt 1
#_with_ocaml_make_testsuite 1
%bcond_with ocaml_force_enable_ocaml_opt
%bcond_with ocaml_force_disable_ocaml_opt
%bcond_with ocaml_make_testsuite
%if %{with ocaml_force_enable_ocaml_opt}
%define do_opt 1
%endif
%if %{without ocaml_force_enable_ocaml_opt}
%ifarch %{arm} aarch64 %{ix86} ppc ppc64 ppc64le s390x x86_64
%define do_opt 1
%endif
%endif
#
%if %{with ocaml_force_disable_ocaml_opt}
%define do_opt 0
%endif
Name:           ocaml
Version:        4.05.0
Release:        0
Summary:        OCaml Compiler and Programming Environment
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml
Url:            http://www.ocaml.org
Source0:        http://caml.inria.fr/pub/distrib/ocaml-%{ocaml_base_version}/ocaml-%{version}.tar.xz
Source1:        ocaml-findlib.rpm.prov_req.attr.sh
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
Requires:       ocaml(runtime) = %{version}-%{release}
Obsoletes:      ocaml-docs
Provides:       ocaml(compiler) = %{version}
Provides:       ocaml(ocaml_base_version) = %{ocaml_base_version}
%if %{do_opt}
Requires:       gcc
Provides:       ocaml(ocaml.opt) = %{version}
%endif

%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package comprises two batch compilers (a fast bytecode compiler
and an optimizing native-code compiler), an interactive top level
system, Lex&Yacc tools, a replay debugger, and a comprehensive library.

%package       rpm-macros
Summary:        RPM macros for building OCaml source packages
License:        QPL-1.0 AND SUSE-LGPL-2.0-with-linking-exception
Group:          Development/Languages/OCaml

%description       rpm-macros
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains a set of helper macros to unify common code used
in ocaml spec files.

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
: do_opt %{do_opt}
%autosetup -p1

%build
%ifarch %{ix86}
# Default OPT flags for these architectures use -fomit-frame-pointer,
# which gets in the way of some of the profiling done within.
OUR_OPT_FLAGS="`echo '%{optflags}' | sed 's/-fomit-frame-pointer//g'`"
%else
OUR_OPT_FLAGS="%{optflags}"
%endif

CFLAGS="$OUR_OPT_FLAGS -DUSE_INTERP_RESULT" \
./configure -bindir %{_bindir} \
            -libdir %{_libdir}/ocaml \
            -no-cplugins \
            -mandir %{_mandir} \
            -x11include %{_includedir} \
            -x11lib %{_libdir}

%if %{do_opt}
# build using native-code compilers (equivalent to `make world opt opt.opt`)
make world.opt \
%else
# build bytecode compiler
make world \
%endif
	BYTECCRPATH= \
	NATIVECCRPATH= \
	MKSHAREDLIBRPATH=

%install
make install \
     DESTDIR=%{buildroot}

if test -f %{buildroot}%{_libdir}/ocaml/libasmrun_pic.a
then
	cp -av \
	--remove-destination \
	%{buildroot}%{_libdir}/ocaml/libasmrun_pic.a \
	%{buildroot}%{_libdir}/ocaml/libasmrun.a
fi

export EXCLUDE_FROM_STRIP="ocamldebug ocamlbrowser"

# Install the compiler libs
install -d %{buildroot}%{_libdir}/ocaml/compiler-libs
cp -a typing/ utils/ parsing/ %{buildroot}%{_libdir}/ocaml/compiler-libs
%fdupes %{buildroot}

# rpmlint ...
chmod -v a+x %{buildroot}%{_libdir}/ocaml/camlheader
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
	\) -type f -exec chmod -v a-x "{}" \;

# install OCaml macros
mkdir -vp %{buildroot}%{_rpmconfigdir}/macros.d
tee %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name} <<'_EOF_'
# get rid of %{_rpmconfigdir}/find-debuginfo.sh
# strip kills the bytecode part of ELF binaries
#
# provide empty _find_debuginfo_dwz_opts
# the .dwz files contains identical contents, which leads to identical
# checksums, which leads to file conflicts due to identical symlinks
%if %{do_opt}
%%ocaml_preserve_bytecode \
	%%{nil}
%%ocaml_native_compiler 1
%%_find_debuginfo_dwz_opts %%{nil}
%%_lto_cflags %%{nil}
%else
%%ocaml_preserve_bytecode \
	%%undefine _build_create_debug \
	%%define __arch_install_post export NO_BRP_STRIP_DEBUG=true \
	%%{nil}
%%_lto_cflags %%{nil}
%%ocaml_native_compiler 0
%endif

# setup.ml comes from oasis, but this is here for libs oasis depends on
#
# html goes into a separate, browsable dir
# which is also safe regarding wiping due to %%doc macro usage
%%_oasis_docdir_base %%{_datadir}/doc/ocaml
%%_oasis_docdir_dvi   %%{_oasis_docdir_base}/%%{name}
%%_oasis_docdir_html  %%{_oasis_docdir_base}/%%{name}
%%_oasis_docdir_pdf   %%{_oasis_docdir_base}/%%{name}
%%_oasis_docdir_ps    %%{_oasis_docdir_base}/%%{name}
%%oasis_docdir        %%{_oasis_docdir_base}/%%{name}
#
# For now provide a convinience macro which covers also the parent dir
%%oasis_docdir_dvi  %%dir %%{_oasis_docdir_base} \
%%{_oasis_docdir_dvi}
%%oasis_docdir_html %%dir %%{_oasis_docdir_base} \
%%{_oasis_docdir_html}
%%oasis_docdir_pdf  %%dir %%{_oasis_docdir_base} \
%%{_oasis_docdir_pdf}
%%oasis_docdir_ps   %%dir %%{_oasis_docdir_base} \
%%{_oasis_docdir_ps}
#
# various macros to unify setup/build/install
%%oasis_setup \
	oasis setup
%%ocaml_oasis_configure \
ocaml setup.ml -configure \\\
	--psdir          %%{_oasis_docdir_ps} \\\
	--pdfdir         %%{_oasis_docdir_pdf} \\\
	--dvidir         %%{_oasis_docdir_dvi} \\\
	--htmldir        %%{_oasis_docdir_html} \\\
	--docdir         %%{oasis_docdir} \\\
	--localedir      %%{_datadir}/locale \\\
	--datadir        %%{_datadir} \\\
	\\\
	--bindir         %%{_bindir} \\\
	--mandir         %%{_mandir} \\\
	--destdir        %%{buildroot} \\\
	--datarootdir    %%{_datadir} \\\
	--infodir        %%{_infodir} \\\
	--libdir         %%{_libdir} \\\
	--libexecdir     %%{_libexecdir} \\\
	--localstatedir  %%{_localstatedir} \\\
	--sbindir        %%{_sbindir} \\\
	--prefix         %%{_prefix} \\\
	--sysconfdir     %%{_sysconfdir} \\\
	--exec-prefix    %%{_prefix} \\\
	--sharedstatedir %%{_sharedstatedir}
#
%%ocaml_oasis_build \
	ocaml setup.ml -build
%%ocaml_oasis_doc \
	ocaml setup.ml -doc
%%ocaml_oasis_install \
	ocaml setup.ml -install
%%ocaml_oasis_findlib_install \
	export OCAMLFIND_DESTDIR=%%{buildroot}`ocamlc -where` ; \
	export OCAMLFIND_LDCONF=/dev/null ; \
	mkdir -p $OCAMLFIND_DESTDIR ; \
	ocaml setup.ml -install
%%ocaml_oasis_test \
	ocaml setup.ml -test
#
#
_EOF_

tag="ocamlfind"
mkdir -vp %{buildroot}%{_rpmconfigdir}/fileattrs
tee %{buildroot}%{_rpmconfigdir}/fileattrs/${tag}.attr <<_EOF_
%__${tag}_provides %%{_rpmconfigdir}/${tag}.sh -prov
%__${tag}_requires %%{_rpmconfigdir}/${tag}.sh -req
%__${tag}_path     ^%%{_libdir}/ocaml/.*/META$|^%%{_libdir}/ocaml/META$
_EOF_
#
tee %{buildroot}%{_rpmconfigdir}/${tag}.sh < %{SOURCE1}

%files
%doc Changes
%license LICENSE
%{_rpmconfigdir}/fileattrs
%attr(755,root,root) %{_rpmconfigdir}/*.sh
%{_bindir}/*
%{_mandir}/*/*
%{_libdir}/ocaml/*.a
%if %{do_opt}
%{_libdir}/ocaml/*.cmxs
%{_libdir}/ocaml/*.cmxa
%{_libdir}/ocaml/*.cmx
%{_libdir}/ocaml/*.o
%endif
%{_libdir}/ocaml/*.mli
%{_libdir}/ocaml/libcamlrun_shared.so
%if %{do_opt}
%{_libdir}/ocaml/libasmrun_shared.so
%endif
%{_libdir}/ocaml/vmthreads/*.mli
%{_libdir}/ocaml/vmthreads/*.a
%if %{do_opt}
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

%files rpm-macros
%config %{_rpmconfigdir}/macros.d

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

%files ocamldoc
%{_bindir}/ocamldoc*
%{_libdir}/ocaml/ocamldoc
%doc ocamldoc/Changes.txt

%files compiler-libs
%license LICENSE
%{_libdir}/ocaml/compiler-libs
%if %{do_opt}
%exclude %{_libdir}/ocaml/compiler-libs/*.cmx
%exclude %{_libdir}/ocaml/compiler-libs/*.o
%exclude %{_libdir}/ocaml/compiler-libs/*/*.cmx
%exclude %{_libdir}/ocaml/compiler-libs/*/*.o
%endif
%exclude %{_libdir}/ocaml/compiler-libs/*.mli
%exclude %{_libdir}/ocaml/compiler-libs/*/*.mli
%exclude %{_libdir}/ocaml/compiler-libs/*/*.ml

%files compiler-libs-devel
%license LICENSE
%if %{do_opt}
%{_libdir}/ocaml/compiler-libs/*.cmx
%{_libdir}/ocaml/compiler-libs/*.o
%{_libdir}/ocaml/compiler-libs/*/*.cmx
%{_libdir}/ocaml/compiler-libs/*/*.o
%endif
%{_libdir}/ocaml/compiler-libs/*.mli
%{_libdir}/ocaml/compiler-libs/*/*.ml
%{_libdir}/ocaml/compiler-libs/*/*.mli

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
