#
# spec file for package coccinelle
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_with coccinelle_testsuite
%define build_flavor @BUILD_FLAVOR@%nil
%if "%build_flavor" == "testsuite"
%if %{without coccinelle_testsuite}
ExclusiveArch:  do-not-build
%else
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif
%define nsuffix -testsuite
%else
%define nsuffix %nil
ExclusiveArch:  aarch64 ppc64 ppc64le riscv64 s390x x86_64
%endif

%define     pkg coccinelle
%global _buildshell /bin/bash
Name:           %pkg%nsuffix
Version:        1.3.1
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Semantic patch utility
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            http://coccinelle.lip6.fr/
Source0:        %pkg-%version.tar.xz
Source1:        %pkg.rpmlintrc
Patch0:         %pkg.patch
%if "%build_flavor" == ""
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros
BuildRequires:  python-rpm-macros
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
BuildRequires:  ocamlfind(menhir)
BuildRequires:  ocamlfind(parmap)
BuildRequires:  ocamlfind(pcre2)
BuildRequires:  ocamlfind(pyml)
BuildRequires:  ocamlfind(stdcompat)
BuildRequires:  pkgconfig(python3)
Requires:       findutils
Requires:       grep
Requires:       which
%endif

%if "%build_flavor" == "testsuite"
BuildRequires:  %pkg = %version
BuildRequires:  ocaml(ocaml.opt)
BuildRequires:  ocamlfind(findlib)
%endif

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
%setup -q -n %pkg-%version
%patch -P 0 -p1

%build
%if "%build_flavor" == ""
echo '%version' > version
autoreconf -fi
%configure \
	--enable-pcre-syntax \
	--with-python=$(realpath %__python3) \
	%nil
# Compiling the generated parser requires an extraordinary amount of stack
%if 0%{?qemu_user_space_build}
export QEMU_STACK_SIZE=$((32768*1024))
%else
ulimit -s 32768
%endif
%make_build -j1 VERBOSE=yes
%endif

%install
%if "%build_flavor" == ""
%make_install
# no GUI
rm -rfv %buildroot%_datadir/metainfo
mkdir -vp %buildroot%_bindir
cp -p tools/pycocci %buildroot%_bindir/pycocci
chmod -c 755 $_
mkdir -vp %buildroot%_datadir/vim/site
mv -vt $_ editors/vim/{ftdetect,syntax}
# OCaml libraries will have unsatisfied dependencies, unless everything is installed
mv {commons,globals,parsing_*}/*.{cmi,cmx} %buildroot%_libdir/%name/ocaml
# Python library have been named after directories in the site-packages hierarchy
mkdir -p "%buildroot/%python3_sitelib"
mv "%buildroot/%_libdir/%name/python/coccilib" "%buildroot/%python3_sitelib"
%fdupes %buildroot/%_prefix
%?python3_fix_shebang
%endif

%if "%build_flavor" == "testsuite"
%check
spatch --ctestall
# bug#1192695
tee bug1192695.c <<'_EOC_'
#include <stdio.h>
int main(int argc, char *argv[]){return 0;}
_EOC_
tee bug1192695.cocci <<'_EOC_'
@initialize:ocaml@
@@

let ok_function p =
    not (List.mem (List.hd p).current_element ["kmem_getpages";"kmem_freepages"])

// convert the type in selected functions
@@
position p : script:ocaml() { ok_function p };
@@

- struct page@p
+ struct slab
_EOC_
spatch --sp-file bug1192695.cocci --include-headers --no-includes --smpl-spacing bug1192695.c
%endif

%if "%build_flavor" == ""
%files
%doc changes.txt copyright.txt
%license license.txt
%_bindir/*
%_datadir/bash-completion
%_datadir/vim
%_libdir/%name
%_mandir/*/*
%python3_sitelib/coccilib
%endif

%changelog
