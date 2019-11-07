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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           ocaml-rpm-macros
Version:        20191101
Release:        0
Summary:        RPM macros for building OCaml source packages
License:        GPL-2.0-only
Group:          Development/Languages/OCaml
Url:            https://build.opensuse.org/project/show/devel:languages:ocaml
Source1:        ocaml-findlib.rpm.prov_req.attr.sh

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
# map findlib names to rpm Provides/Requires
tag="ocamlfind"
mkdir -vp %{buildroot}%{_rpmconfigdir}/fileattrs
tee %{buildroot}%{_rpmconfigdir}/fileattrs/${tag}.attr <<_EOF_
%__${tag}_provides %%{_rpmconfigdir}/${tag}.sh -prov
%__${tag}_requires %%{_rpmconfigdir}/${tag}.sh -req
%__${tag}_path     ^%%{_libdir}/ocaml/.*/META$|^%%{_libdir}/ocaml/META$
_EOF_
#
tee %{buildroot}%{_rpmconfigdir}/${tag}.sh < %{SOURCE1}

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
	> %%{name}.files.license ;\
	> %%{name}.files.unhandled ;\
	for license in \\\
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
%if 0%{?suse_version} > 1315
	license_macro='license' ;\
%else
	license_macro='doc' ;\
%endif
	  test -f "${license}" && echo "%%%%${license_macro} ${license}" >> '%%{name}.files.license' ;\
	done ;\
	find %%{buildroot}$(ocamlc -where) | sed -ne '\
	s@^%%{buildroot}@@\
	#\
	# for findlib, describing a package\
	/\\/META$/{ b files_devel }\
	# stub ELF library\
	/\\/[^/]\\+\\.so$/{       b files_ldsoconf }\
	# stub ELF library\
	/\\/[^/]\\+\\.so.owner$/{ b files_ldsoconf }\
	# ELF archive with object files\
	/\\/[^/]\\+\\.a$/{     b files_devel }\
	# OCaml legacy source code annotations, produced via -annot\
	/\\/[^/]\\+\\.annot$/{ b files_devel }\
	# OCaml library file with bytecode\
	/\\/[^/]\\+\\.cma$/{   b files_devel }\
	# OCaml compiled header file\
	/\\/[^/]\\+\\.cmi$/{   b files_devel }\
	# OCaml object file with bytecode\
	/\\/[^/]\\+\\.cmo$/{   b files_devel }\
	# OCaml source code annotations, produced via -bin-annot from source files\
	/\\/[^/]\\+\\.cmt$/{   b files_devel }\
	# OCaml source code annotations, produced via -bin-annot from header files\
	/\\/[^/]\\+\\.cmti$/{  b files_devel }\
	# OCaml object file with native code\
	/\\/[^/]\\+\\.cmx$/{   b files_devel }\
	# OCaml library file with native code\
	/\\/[^/]\\+\\.cmxa$/{  b files_devel }\
	# ELF shared library with native code\
	/\\/[^/]\\+\\.cmxs$/{  b files_devel }\
	# Some helper binary\
	/\\/[^/]\\+\\.exe$/{   b files_devel }\
	# C header\
	/\\/[^/]\\+\\.h$/{     b files_devel }\
	#\
	/\\/[^/]\\+\\.js$/{    b files_devel }\
	# OCaml source code, source file\
	/\\/[^/]\\+\\.ml$/{    b files_devel }\
	# OCaml source code, header file\
	/\\/[^/]\\+\\.mli$/{   b files_devel }\
	# ELF object file\
	/\\/[^/]\\+\\.o$/{     b files_devel }\
	#\
	/\\/[^/]\\+\\.sml$/{   b files_devel }\
	#\
	/\\/dune-package$/{    b files_devel }\
	#\
	/\\/opam$/{            b files_devel }\
	#\
	# record unknown paths\
	w %%{name}.files.unhandled\
	d\
	#\
	: files_devel\
	# full path for file\
	w %%{name}.files.devel\
	# tag + dirname\
	s@\\/[^/]\\+$@@\
	: tag_dirname\
	s@^@%%dir @\
	w %%{name}.files.devel\
	# parent directory\
	s@\\/[^/]\\+$@@\
	w %%{name}.files.devel\
	d\
	#\
	: files_ldsoconf\
	# full path for file\
	w %%{name}.files.devel\
	# dirname for ld.so.conf\
	s@\\/[^/]\\+$@@\
	w %%{name}.files.ldsoconf\
	b tag_dirname\
	' ;\
	cat '%%{name}.files.license' >> '%%{name}.files' ; \
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
	echo '%%{version}' | tee VERSION ; \
	dune_for_release= ; \
	: dune_release_pkgs \
	if test -n "${dune_release_pkgs}" ; \
	then \
		echo "${dune_release_pkgs}" > dune_release_pkgs-%%{name}-%%{version}-%%{release} ; \
		dune_for_release="--for-release-of-packages=${dune_release_pkgs}" ; \
	fi ; \
	dune installed-libraries $OCAML_DUNE_INSTALLED_LIBRARIES_ARGS ; \
	dune external-lib-deps \\\
		${dune_for_release} \\\
		'@install' \\\
		$OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS ; \
	dune external-lib-deps \\\
		${dune_for_release} \\\
		'@runtest' \\\
		$OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS ; \
	dune external-lib-deps \\\
		${dune_for_release} \\\
		'@install' '@runtest' \\\
		$OCAML_DUNE_EXTERNAL_LIB_DEPS_ARGS \\\
		| awk '/^-[[:blank:]]/{ printf "BuildRequires:  ocamlfind(%%s)\\n", $2}' | sort -u ; \
	%%{nil}
%%ocaml_dune_build \
	dune build \\\
		--verbose \\\
		${dune_for_release} \\\
		%%{?_smp_mflags} \\\
		'@install' \\\
		$OCAML_DUNE_BUILD_INSTALL_ARGS
%%ocaml_dune_install \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune_for_release= ; \
	if test -f dune_release_pkgs-%%{name}-%%{version}-%%{release} ; \
	then \
		read dune_release_pkgs < dune_release_pkgs-%%{name}-%%{version}-%%{release} ; \
		dune_for_release="--for-release-of-packages=${dune_release_pkgs}" ; \
	fi ; \
	dune install \\\
		--verbose \\\
		${dune_for_release} \\\
		%%{?_smp_mflags} \\\
		--prefix=%%{_prefix} \\\
		--libdir=$(ocamlc -where) \\\
		--destdir=%%{buildroot} \\\
		${dune_release_pkgs//,/ } \\\
		$OCAML_DUNE_INSTALL_ARGS ; \
	rm -rfv %%{buildroot}%%{_prefix}/doc ; \
	if test -d %%{buildroot}%%{_prefix}/man ; then \
		mkdir -vp %%{buildroot}%%{_datadir} ; \
		mv -vt %%{buildroot}%%{_datadir} %%{buildroot}%%{_prefix}/man ; \
	fi ;
%%ocaml_dune_test \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune_for_release= ; \
	if test -f dune_release_pkgs-%%{name}-%%{version}-%%{release} ; \
	then \
		read dune_release_pkgs < dune_release_pkgs-%%{name}-%%{version}-%%{release} ; \
		dune_for_release="--for-release-of-packages=${dune_release_pkgs}" ; \
	fi ; \
	if dune runtest \\\
		--verbose \\\
		${dune_for_release} \\\
		$OCAML_DUNE_RUNTEST_ARGS ; \
	then \
		echo "dune runtest succeeded" ; \
	else \
		echo "dune runtest failed" ; \
		if test -n "${dune_test_tolerate_fail}" ; \
		then \
			echo "ignored" ; \
		else \
			echo "aborting" ; \
			exit 1 ; \
		fi ; \
	fi

#
#
_EOF_

%files
%{_rpmmacrodir}/*
%{_rpmconfigdir}/fileattrs
%attr(755,root,root) %{_rpmconfigdir}/*.sh

%changelog
