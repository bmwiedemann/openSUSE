#
# spec file for package coccinelle
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


Name:           coccinelle
Version:        1.0.7
Release:        0
Summary:        Semantic patch utility
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            http://coccinelle.lip6.fr/
#Git-Clone:	git://github.com/coccinelle/coccinelle

Source:         http://coccinelle.lip6.fr/distrib/%name-%version.tar.gz
Patch1:         kill-env.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml >= 3.11
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-menhir-devel
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-ocamldoc >= 3.11
BuildRequires:  ocaml-parmap-devel
BuildRequires:  ocaml-pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  ocamlfind(camlp4)
BuildRequires:  pkgconfig(python)
Requires:       python-base

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
rm -fv tools/spgen/source/spgen{,.opt}

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
# "because it is simply not possible to strip ocaml binaries that are built
# with the -custom option."
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %nil
: >debugfiles.list
: >debugsources.list
: >debugsourcefiles.list

%make_install
# Remove coccilib, don't have the deps
rm -Rf "%buildroot/%_libdir/%name"/{commons,globals,ocaml,parsing_c} \
	"%buildroot/%_mandir/man3"/Coccilib*
%fdupes %buildroot/%_prefix

%files
%doc authors.txt bugs.txt changes.txt copyright.txt credits.txt
%license license.txt
%doc readme.txt
%_mandir/man?/*
%_bindir/sp*
%_libdir/%name
%_datadir/bash-completion/

%changelog
