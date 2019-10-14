#
# spec file for package ocaml-rpm-macros
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           ocaml-rpm-macros
Version:        20191009
Release:        0
Summary:        RPM macros for building OCaml source packages
License:        GPL-2.0-only
Group:          Development/Languages/OCaml
Url:            https://build.opensuse.org/project/show/devel:languages:ocaml
#
# keep the following macros in sync with ocaml.spec:
%define do_opt 0
# macros to be set in prjconf:
#Macros:
#_with_ocaml_force_enable_ocaml_opt 1
#_with_ocaml_force_disable_ocaml_opt 1
#_with_ocaml_make_testsuite 1
#:Macros
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
#

%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains a set of helper macros to unify common code used
in ocaml spec files.

%prep

%build

%install
# install OCaml macros
mkdir -vp %{buildroot}%{_rpmmacrodir}
tee %{buildroot}%{_rpmmacrodir}/macros.%{name} <<'_EOF_'
# get rid of %{_rpmconfigdir}/find-debuginfo.sh
# strip kills the bytecode part of ELF binaries
#
# provide empty _find_debuginfo_dwz_opts
# the .dwz files contains identical contents, which leads to identical
# checksums, which leads to file conflicts due to identical symlinks
%if %{do_opt}
%%ocaml_preserve_bytecode \
	%%define _lto_cflags %%{nil} \
	%%{nil}
%%ocaml_native_compiler 1
%%_find_debuginfo_dwz_opts %%{nil}
%else
%%ocaml_preserve_bytecode \
	%%undefine _build_create_debug \
	%%define __arch_install_post export NO_BRP_STRIP_DEBUG=true \
	%%define _lto_cflags %%{nil} \
	%%{nil}
%%ocaml_native_compiler 0
%endif

# Create file list for base pkg and base-devel pkg
# Files with known extensions or names are written to 'files' or 'files.devel'
# Other unknown files are shown on stdout
%%ocaml_create_file_list \
	> %%{name}.files ;\
	> %%{name}.files.devel ;\
	> %%{name}.files.ldsoconf ;\
	> %%{name}.files.unhandled ;\
	for i in \\\
	COPYING \\\
	COPYING.txt \\\
	COPYRIGHT \\\
	Copyright \\\
	LICENCE \\\
	LICENSE \\\
	LICENSE.md \\\
	LICENSE.txt \\\
	;\
	do\
	  test -f "$i" && echo "%%%%license $i" >> %%{name}.files ;\
	done ;\
	find %%{buildroot}$(ocamlc -where) | sed -ne '\
	s@^%%{buildroot}@@\
	/\\/\\(META\\|dune-package\\|opam\\)$/{\
	w %%{name}.files.devel\
	s@\\/[^/]\\+$@@\
	s@^@%%dir @\
	w %%{name}.files.devel\
	s@\\/[^/]\\+$@@\
	w %%{name}.files.devel\
	d\
	}\
	/\\/[^/]\\+\\.\\(a\\|annot\\|cmx\\|cmxa\\|cma\\|cmi\\|cmo\\|cmt\\|cmti\\|exe\\|h\\|js\\|ml\\|mli\\|o\\)$/{\
	w %%{name}.files.devel\
	s@\\/[^/]\\+$@@\
	s@^@%%dir @\
	w %%{name}.files.devel\
	s@\\/[^/]\\+$@@\
	w %%{name}.files.devel\
	d\
	}\
	/\\/[^/]\\+\\.\\(so\\|so.owner\\)$/{\
	w %%{name}.files\
	s@\\/[^/]\\+$@@\
	w %%{name}.files.ldsoconf\
	s@^@%%dir @\
	w %%{name}.files\
	s@\\/[^/]\\+$@@\
	w %%{name}.files\
	d\
	}\
	/\\/[^/]\\+\\.\\(cmxs\\)$/{\
	w %%{name}.files\
	s@\\/[^/]\\+$@@\
	s@^@%%dir @\
	w %%{name}.files\
	s@\\/[^/]\\+$@@\
	w %%{name}.files\
	d\
	}\
	w %%{name}.files.unhandled\
	d\
	' ;\
	for i in \\\
	%%{name}.files \\\
	%%{name}.files.devel \\\
	%%{name}.files.ldsoconf \\\
	%%{name}.files.unhandled \\\
	;\
	do\
	  sort -u $i > $$ ;\
	  mv $$ $i ;\
	done ;\
	if test -s %%{name}.files.ldsoconf ;\
	then \
		ldsoconfd='/etc/ld.so.conf.d' ;\
		mkdir -vp "%%{buildroot}${ldsoconfd}" ;\
		tee "%%{buildroot}${ldsoconfd}/%%{name}.conf" < %%{name}.files.ldsoconf ;\
		echo "%config ${ldsoconfd}/%%{name}.conf" >> %%{name}.files ;\
	fi ;\
	head -n 1234 \\\
	%%{name}.files \\\
	%%{name}.files.devel \\\
	%%{name}.files.ldsoconf \\\
	%%{name}.files.unhandled \\\
	;\
	%%{nil}

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
%%ocaml_dune_setup \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune installed-libraries $OCAML_DUNE_INSTALLED_LIBRARIES_ARGS ; \
	dune external-lib-deps @install $OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS ; \
	dune external-lib-deps @runtest $OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS ; \
	%%{nil}
%%ocaml_dune_build \
	dune build --verbose @install $OCAML_DUNE_BUILD_INSTALL_ARGS
%%ocaml_dune_install \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune install --verbose --destdir=%%{buildroot} $OCAML_DUNE_INSTALL_ARGS ; \
	rm -rfv %%{buildroot}%%{_prefix}/doc ; \
	if test -d %%{buildroot}%%{_prefix}/man ; then \
		mkdir -vp %%{buildroot}%%{_datadir} ; \
		mv -vt %%{buildroot}%%{_datadir} %%{buildroot}%%{_prefix}/man ; \
	fi ;
%%ocaml_dune_test \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune runtest --verbose $OCAML_DUNE_RUNTEST_ARGS
#
#
_EOF_

%files
%{_rpmmacrodir}/*

%changelog
