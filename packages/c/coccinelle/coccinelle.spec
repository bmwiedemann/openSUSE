#
# spec file for package coccinelle
#
# Copyright (c) 2022 SUSE LLC
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


Name:           coccinelle
Version:        1.1.1
Release:        0
Summary:        Semantic patch utility
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            http://coccinelle.lip6.fr/
Source0:        %name-%version.tar.xz
Source1:        %name.rpmlintrc
Patch1:         kill-env.diff
ExclusiveArch:  aarch64 ppc64le s390x x86_64 riscv64
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-ocamldoc >= 3.11
BuildRequires:  python-rpm-macros
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(menhir)
BuildRequires:  ocamlfind(parmap)
BuildRequires:  ocamlfind(pcre)
BuildRequires:  ocamlfind(pyml)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  pkgconfig(python3)
Requires:       findutils
Requires:       grep
Requires:       python3-base
Requires:       which

%description
Coccinelle is a program matching and transformation engine which
provides the language SmPL (Semantic Patch Language) for specifying
desired matches and transformations in C code. [It does not recognize
C++.]

Coccinelle performs collateral evolutions in software. Such
evolutions comprise the changes that are needed in client code in
response to evolutions in library APIs, and may include modifications
such as renaming a function, adding a function argument whose value
is somehow context-dependent, and reorganizing a data structure.
Beyond collateral evolutions, Coccinelle is used for finding and
fixing bugs in systems code.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure --with-python=%python_for_executables
# Compiling the generated parser requires an extraordinary amount of stack
%if 0%{?qemu_user_space_build}
export QEMU_STACK_SIZE=$((32768*1024))
%else
ulimit -s 32768
%endif
%make_build -j1 VERBOSE=yes

%install
b="%buildroot"
# "because it is simply not possible to strip ocaml binaries that are built
# with the -custom option."
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %nil
: >debugfiles.list
: >debugsources.list
: >debugsourcefiles.list

%make_install

# Until https://github.com/coccinelle/coccinelle/issues/259 is fixed
for i in spatch spgen; do
	mv -v "$b/%_bindir/$i" "$b/%_bindir/$i.bin"
	cat >"$b/%_bindir/$i" <<-EOF
		#!/bin/bash
		if test -z "\$COCCINELLE_HOME"; then export COCCINELLE_HOME="%_libdir/coccinelle"; fi
		exec %_bindir/$i.bin "\$@"
	EOF
	chmod -v a+x "$b/%_bindir/$i"
done

%fdupes $b/%_prefix

# Python library have been named after directories in the site-packages hierarchy
mkdir -p "$b/%python3_sitelib"
mv "$b/%_libdir/%name/python/coccilib" "$b/%python3_sitelib"
%fdupes $b/%python3_sitelib/coccilib

%files
%doc authors.txt bugs.txt changes.txt copyright.txt credits.txt
%license license.txt
%doc readme.txt
%python3_sitelib/coccilib
%_mandir/man?/*
%_bindir/sp*
%_libdir/%name
%_datadir/bash-completion/

%changelog
