#
# spec file for package ocaml-rpm-macros
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


Name:           ocaml-rpm-macros
Version:        20230101
Release:        0
Summary:        RPM macros for building OCaml source packages
License:        GPL-2.0-only
Group:          Development/Languages/OCaml
BuildRoot:      %_tmppath/%name-%version-build
ExclusiveArch:  %arm aarch64 %ix86 ppc ppc64 ppc64le riscv64 s390x x86_64
URL:            https://build.opensuse.org/project/show/devel:languages:ocaml
Source0:        ocaml-ocaml.rpm.prov_req.attr.sh
Source1:        ocaml-findlib.rpm.prov_req.attr.sh

# Some rpm variants know about license, but can only use them in plain file context
%bcond_without suse_ocaml_use_rpm_license_macro
# Some rpm variants are unable to create proper debuginfo and/or debugsource packages
%bcond_without suse_ocaml_opt_debug_package
# Some rpm variants fail to build even this innocent package...
%define debug_package %nil

%define ocaml_standard_library %_libdir/ocaml

%description
OCaml is a high-level, strongly-typed, functional and object-oriented
programming language from the ML family of languages.

This package contains a set of helper macros to unify common code used
in ocaml spec files.

%prep

%build

%install
> files.fileattrs
if test -d '%_rpmconfigdir/fileattrs'
then
  # Generating dependencies can currently only be done by rpm versions
  # which support "fileattrs", because it is easy to add new hooks.
  mkdir -vp %buildroot%_rpmconfigdir/fileattrs

  # Map ocamlobjinfo output to rpm Provides/Requires
  # This tag name MUST match what ocaml.spec uses internally
  tag="suseocaml"
  file_attr="%_rpmconfigdir/fileattrs/${tag}.attr"
  file_sh="%_rpmconfigdir/${tag}.sh"
  attr_sh="%%_rpmconfigdir/${tag}.sh"
  tee %buildroot${file_sh} < %{SOURCE0}
  tee %buildroot${file_attr} <<_EOF_
%%__${tag}_provides ${attr_sh} --provides
%%__${tag}_requires ${attr_sh} --requires
%%__${tag}_magic    ^(Objective caml|OCaml) .*$
%%__${tag}_path     .(cma|cmi|cmo|cmx|cmxa)$
%%__${tag}_flags    magic_and_path
_EOF_
  echo "${file_attr}" >> files.fileattrs
  echo "%%attr(755,root,root) ${file_sh}"   >> files.fileattrs

  # Map findlib names to rpm Provides/Requires
  tag="suseocamlfind"
  file_attr="%_rpmconfigdir/fileattrs/${tag}.attr"
  file_sh="%_rpmconfigdir/${tag}.sh"
  attr_sh="%%_rpmconfigdir/${tag}.sh"
  tee %buildroot${file_sh} < %{SOURCE1}
  tee %buildroot${file_attr} <<_EOF_
%%__${tag}_provides ${attr_sh} -prov
%%__${tag}_requires ${attr_sh} -req
%%__${tag}_path     ^%ocaml_standard_library/.*/META$|^%ocaml_standard_library/META$
_EOF_
  echo "${file_attr}" >> files.fileattrs
  echo "%%attr(755,root,root) ${file_sh}" >> files.fileattrs
fi
#

# install OCaml macros
mkdir -vp %buildroot%_rpmmacrodir
tee %buildroot%_rpmmacrodir/macros.%name <<'_EOF_'
# Guidelines:
# - Providing applications written in OCaml is the main goal of our packaging.
# - Applications written in OCaml are static binaries.
# - A concept of shared libraries does not exist, beside the Dynlink module
# - All binaries go into the main package, in case they are produced.
# - All modules go into the -devel subpackage
# - Helper applications below %ocaml_standard_library go into the -devel subpackage
# - License files go into the main package.
# - To aid debugging of cmxs files, their debuginfo is preserved by removing the executable bit.
# 
# get rid of %_rpmconfigdir/find-debuginfo.sh
# strip kills the bytecode part of ELF binaries
#
# provide empty _find_debuginfo_dwz_opts
# the .dwz files contains identical contents, which leads to identical
# checksums, which leads to file conflicts due to identical symlinks
%%ocaml_standard_library %ocaml_standard_library
%if %{without suse_ocaml_opt_debug_package}
# Obviously, handling presence or absence of debug information works only when being built in a SUSE system.
%endif
%%ocaml_preserve_bytecode \
%if %{without suse_ocaml_opt_debug_package}
	%%define debug_package %%nil \
	%%define __debug_install_post %%nil \
%endif
	%%define _lto_cflags %%nil \
	%%nil
%%_find_debuginfo_dwz_opts %%nil

# Compatibility for quilt setup and old packages
%%ocaml_native_compiler 1
%%suse_ocaml_native_compiler 1

# Create file list for base pkg and base-devel pkg
# Files with known extensions or names are written to 'files' or 'files.devel'
# Other unknown files are shown on stdout
%%ocaml_create_file_list \
	> %%name.files ;\
	> %%name.files.changes ;\
	> %%name.files.devel ;\
	> %%name.files.ldsoconf ;\
	> %%name.files.license ;\
	> %%name.files.unhandled ;\
	for changes in \\\
	CHANGELOG.md \\\
	CHANGES \\\
	CHANGES.md \\\
	CHANGES.txt \\\
	ChangeLog \\\
	Changelog \\\
	;\
	do\
	  test -f "${changes}" && echo "%%%%doc ${changes}" >> '%%name.files.changes' ;\
	done ;\
	for license in \\\
	COPYING \\\
	COPYING.txt \\\
	COPYRIGHT \\\
	COPYRIGHT.txt \\\
	Copyright \\\
	LGPL \\\
	LICENCE \\\
	LICENSE \\\
	LICENSE.md \\\
	LICENSE.txt \\\
	;\
	do\
%if %{with suse_ocaml_use_rpm_license_macro}
	license_macro='license' ;\
%else
	license_macro='doc' ;\
%endif
	  test -f "${license}" && echo "%%%%${license_macro} ${license}" >> '%%name.files.license' ;\
	done ;\
	if test -d %%buildroot%%ocaml_standard_library ;\
	then\
		find %%buildroot%%ocaml_standard_library -name '*.cmxs' -exec chmod -v a-x '{}' + ;\
		find %%buildroot%%ocaml_standard_library ! -type d | awk\\\
		-v "buildroot=%%buildroot"\\\
		-v "ocaml_standard_library=%%ocaml_standard_library"\\\
		-v "out_files_main=%%name.files"\\\
		-v "out_files_devel=%%name.files.devel"\\\
		-v "out_files_ldconf=%%name.files.ldsoconf"\\\
		-v "out_files_unhandled=%%name.files.unhandled"\\\
		-v "ocaml_ldconf=$(ls -1d %%ocaml_standard_library/ld.conf || : ld.conf not found)"\\\
		'\
	BEGIN {\
		nr=0\
		if (ocaml_ldconf != "") {\
			do {\
				r = getline < ocaml_ldconf\
				if (r > 0) {\
					ldconf[nr++]=$0\
				}\
			} while (r > 0)\
		}\
	}\
	function _split (line) {\
		file_path=substr(line, length(buildroot) + 1)\
		m=match(file_path, "/[^/]+$")\
		dirname=substr(file_path, 0, m - 1)\
		basename=substr(file_path, m + 1)\
		if (dirname == ocaml_standard_library) {\
			# do not package above standard_library\
			parent_dir=""\
		} else {\
			m=match(dirname, "/[^/]+$")\
			parent_dir=substr(dirname, 0, m - 1)\
		}\
	}\
	function files_ldconf(line) {\
		_split(line)\
		print file_path >> out_files_devel\
		print "%%dir " dirname >> out_files_devel\
		for (ldconf_dir in ldconf) {\
			if (dirname == ldconf[ldconf_dir]) {\
				# done with this cycle, ocaml ld.conf covers it\
				next\
			}\
		}\
		print dirname >> out_files_ldconf\
		next\
	}\
	function files_devel(line) {\
		_split(line)\
		print file_path >> out_files_devel\
		print "%%dir " dirname >> out_files_devel\
		if (parent_dir != "") {\
			print "%%dir " parent_dir >> out_files_devel\
		}\
		next\
	}\
	function files_main(line) {\
		_split(line)\
		print file_path >> out_files_main\
		print "%%dir " dirname >> out_files_main\
		if (parent_dir != "") {\
			print "%%dir " parent_dir >> out_files_main\
		}\
		next\
	}\
	function files_unhandled(line) {\
		_split(line)\
		print file_path >> out_files_unhandled\
		next\
	}\
	# for findlib, describing a package\
	/\\/META$/{\
		files_devel($0)\
	}\
	# stub ELF library\
	/\\/[^/]+\\.so$/{\
		files_ldconf($0)\
	}\
	# stub ELF library\
	/\\/[^/]+\\.so.owner$/{\
		files_ldconf($0)\
	}\
	# ELF archive with object files\
	/\\/[^/]+\\.a$/{\
		files_devel($0)\
	}\
	# OCaml legacy source code annotations, produced via -annot\
	/\\/[^/]+\\.annot$/{\
		files_devel($0)\
	}\
	# OCaml library file with bytecode\
	/\\/[^/]+\\.cma$/{\
		files_devel($0)\
	}\
	# OCaml compiled header file\
	/\\/[^/]+\\.cmi$/{\
		files_devel($0)\
	}\
	# OCaml object file with bytecode\
	/\\/[^/]+\\.cmo$/{\
		files_devel($0)\
	}\
	# OCaml source code annotations, produced via -bin-annot from source files\
	/\\/[^/]+\\.cmt$/{\
		files_devel($0)\
	}\
	# OCaml source code annotations, produced via -bin-annot from header files\
	/\\/[^/]+\\.cmti$/{\
		 files_devel($0)\
	}\
	# OCaml object file with native code\
	/\\/[^/]+\\.cmx$/{\
		files_devel($0)\
	}\
	# OCaml library file with native code\
	/\\/[^/]+\\.cmxa$/{\
		files_devel($0)\
	}\
	# ELF shared library with native code\
	/\\/[^/]+\\.cmxs$/{\
		files_main($0)\
	}\
	# Some helper binary\
	/\\/[^/]+\\.exe$/{\
		files_devel($0)\
	}\
	# C header\
	/\\/[^/]+\\.h$/{\
		files_devel($0)\
	}\
	#\
	/\\/[^/]+\\.js$/{\
		files_devel($0)\
	}\
	# OCaml source code, source file\
	/\\/[^/]+\\.ml$/{\
		files_devel($0)\
	}\
	# OCaml source code, header file\
	/\\/[^/]+\\.mli$/{\
		files_devel($0)\
	}\
	# ELF object file\
	/\\/[^/]+\\.o$/{\
		files_devel($0)\
	}\
	#\
	/\\/[^/]+\\.sml$/{\
		files_devel($0)\
	}\
	# generated by dune\
	/\\/dune-package$/{\
		files_devel($0)\
	}\
	# generated by dune\
	/\\/opam$/{\
		files_devel($0)\
	}\
	# Some Coq files\
	/\\/[^/]+\\.v$/{\
		files_devel($0)\
	}\
	#\
	# record unknown paths\
	files_unhandled($0)\
	END {\
	;\
	}' ;\
	fi ;\
	cat '%%name.files.changes' >> '%%name.files' ;\
	cat '%%name.files.license' >> '%%name.files' ;\
	if test -s %%name.files.ldsoconf ;\
	then\
		ldsoconfd='/etc/ld.so.conf.d' ;\
		mkdir -vp "%%buildroot${ldsoconfd}" ;\
		tee "%%buildroot${ldsoconfd}/%%name.conf" < %%name.files.ldsoconf ;\
		echo "%config ${ldsoconfd}/%%name.conf" >> %%name.files.devel ;\
	fi ;\
	for i in \\\
	%%name.files \\\
	%%name.files.devel \\\
	%%name.files.ldsoconf \\\
	%%name.files.unhandled \\\
	;\
	do\
	  sort -u $i > $$ ;\
	  mv $$ $i ;\
	done ;\
	%%nil

# setup.ml comes from oasis, but this is here for libs oasis depends on
#
# html goes into a separate, browsable dir
# which is also safe regarding wiping due to %%doc macro usage
%%_oasis_docdir_base %%_datadir/doc/ocaml
%%_oasis_docdir_dvi   %%_oasis_docdir_base/%%name
%%_oasis_docdir_html  %%_oasis_docdir_base/%%name
%%_oasis_docdir_pdf   %%_oasis_docdir_base/%%name
%%_oasis_docdir_ps    %%_oasis_docdir_base/%%name
%%oasis_docdir        %%_oasis_docdir_base/%%name
#
# For now provide a convinience macro which covers also the parent dir
%%oasis_docdir_dvi  %%dir %%_oasis_docdir_base \
%%_oasis_docdir_dvi
%%oasis_docdir_html %%dir %%_oasis_docdir_base \
%%_oasis_docdir_html
%%oasis_docdir_pdf  %%dir %%_oasis_docdir_base \
%%_oasis_docdir_pdf
%%oasis_docdir_ps   %%dir %%_oasis_docdir_base \
%%_oasis_docdir_ps
#
# various macros to unify setup/build/install
%%oasis_setup \
	oasis setup
%%ocaml_oasis_configure \
ocaml setup.ml -configure \\\
	--psdir          %%_oasis_docdir_ps \\\
	--pdfdir         %%_oasis_docdir_pdf \\\
	--dvidir         %%_oasis_docdir_dvi \\\
	--htmldir        %%_oasis_docdir_html \\\
	--docdir         %%oasis_docdir \\\
	--localedir      %%_datadir/locale \\\
	--datadir        %%_datadir \\\
	\\\
	--bindir         %%_bindir \\\
	--mandir         %%_mandir \\\
	--destdir        %%buildroot \\\
	--datarootdir    %%_datadir \\\
	--infodir        %%_infodir \\\
	--libdir         %%_libdir \\\
	--libexecdir     %%_libexecdir \\\
	--localstatedir  %%_localstatedir \\\
	--sbindir        %%_sbindir \\\
	--prefix         %%_prefix \\\
	--sysconfdir     %%_sysconfdir \\\
	--exec-prefix    %%_prefix \\\
	--sharedstatedir %%_sharedstatedir
#
%%ocaml_oasis_build \
	ocaml setup.ml -build
%%ocaml_oasis_doc \
	ocaml setup.ml -doc
%%ocaml_oasis_install \
	ocaml setup.ml -install
%%ocaml_oasis_findlib_install \
	export OCAMLFIND_DESTDIR=%%buildroot%%ocaml_standard_library ; \
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
%if 0
	# obviously this works just with a single entry in dune_release_pkgs=
%endif
	if test -n "${dune_release_pkgs}" ; \
	then \
		test -f 'opam' && mv -v 'opam' "${dune_release_pkgs}.opam" ; \
	fi ; \
	echo '%%version' | tee VERSION ; \
	for opam in *.opam \
	do\
		test -f "${opam}" || continue ; \
		sed -i~ '\
		/^version:/d\
		' "${opam}" ; \
		diff -u "$_"~ "$_" || : got version ; \
	done ; \
	if test -f 'dune-project' ; \
	then \
		sed -i~ '\
		/^([[:blank:]]*version[[:blank:]]\\+/d\
		/^([[:blank:]]*lang[[:blank:]]\\+dune[[:blank:]]/a (version %%version)\
		' 'dune-project'; \
		diff -u "$_"~ "$_" || : got version ; \
	fi ; \
	dune_for_release= ; \
	: dune_release_pkgs \
	if test -n "${dune_release_pkgs}" ; \
	then \
		echo "${dune_release_pkgs}" > dune_release_pkgs-%%name-%%version-%%release ; \
		dune_for_release="--for-release-of-packages=${dune_release_pkgs}" ; \
	fi ; \
	%%nil
%%ocaml_dune_build \
	dune --version ; \
	dune installed-libraries $OCAML_DUNE_INSTALLED_LIBRARIES_ARGS ; \
	if test -z "${_smp_mflags}" ;\
	then \
		_smp_mflags='%%{?_smp_mflags}' ;\
		case "$(ocamlc --version)" in \\\
		4.08*) _smp_mflags='-j1' ;;\\\
		4.09*) _smp_mflags='-j1' ;;\\\
		4.10*) _smp_mflags='-j1' ;;\\\
		esac ;\
	fi ;\
	dune build \\\
		--verbose \\\
		${dune_for_release} \\\
		${_smp_mflags} \\\
		'@install' \\\
		$OCAML_DUNE_BUILD_INSTALL_ARGS
%%ocaml_dune_install \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	if test -z "${_smp_mflags}" ;\
	then \
		_smp_mflags='%%{?_smp_mflags}' ;\
		case "$(ocamlc --version)" in \\\
		4.08*) _smp_mflags='-j1' ;;\\\
		4.09*) _smp_mflags='-j1' ;;\\\
		4.10*) _smp_mflags='-j1' ;;\\\
		esac ;\
	fi ;\
	dune_for_release= ;\
	if test -f dune_release_pkgs-%%name-%%version-%%release ; \
	then \
		read dune_release_pkgs < dune_release_pkgs-%%name-%%version-%%release ; \
		dune_for_release="--for-release-of-packages=${dune_release_pkgs}" ; \
	fi ;\
	dune install \\\
		--verbose \\\
		${dune_for_release} \\\
		${_smp_mflags} \\\
		--prefix=%%_prefix \\\
		--libdir=%%ocaml_standard_library \\\
		--destdir=%%buildroot \\\
		${dune_release_pkgs//,/ } \\\
		$OCAML_DUNE_INSTALL_ARGS ;\
	rm -rfv %%buildroot%%_prefix/doc ;\
	if test -d %%buildroot%%_prefix/man ; then \
		mkdir -vp %%buildroot%%_datadir ; \
		mv -vt %%buildroot%%_datadir %%buildroot%%_prefix/man ; \
	fi ;
%%ocaml_dune_test \
%ifarch ppc64 ppc64le
	ulimit -s $((1024 * 64)) ; \
%endif
	dune_for_release= ; \
	if test -f dune_release_pkgs-%%name-%%version-%%release ; \
	then \
		read dune_release_pkgs < dune_release_pkgs-%%name-%%version-%%release ; \
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

%files -f files.fileattrs
%defattr(-,root,root,-)
%_rpmmacrodir/*

%changelog
